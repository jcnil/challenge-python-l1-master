 # -*- coding: utf-8 -*-
#!/usr/bin/env python

import argparse,logging,requests,json,time,hashlib
import pandas as pd
from sqlalchemy import *
from libs.configurations import Configuration
from libs.dbcontroller import *


def extract_information():

    controller = SessionController()
    engine = controller.getEngine()
    session = controller.getSession()
    meta = MetaData()
    

    response = requests.get(Configuration.API_ALL).text
 
    record =[]
    start = time.time()
    for aux in json.loads(response):
        try:
            for k,v in enumerate(aux['languages']):
                vals_encryp = hashlib.sha1(str(aux['languages'][v]).encode('utf-8'))
                record.append({'Region':aux['region'],'City Name':aux['capital'][0],'Language':vals_encryp.hexdigest(),'Time':time.time() - start})
        except:
            pass
 
 
    df = pd.DataFrame(data=record)
    result = df.drop_duplicates(['Region'])
    result.reset_index(drop=True, inplace=True)
    table = pd.DataFrame(columns=['Region','City Name','Language','Time'])
    table.to_sql('table_challenge', engine, if_exists='append')
    logging.info("Creando la tabla con la información a partir de un DataFrame")
    time.sleep(3)
    result.to_sql('table_challenge', engine, if_exists='append')
    logging.info("Cargando la Data en la tabla creada")
    time.sleep(3)
    DataTable = Table("table_challenge", meta, autoload_with=engine)
    records = session.execute(select(DataTable)).all()

    data = []
    for i in records:
        data.append(dict(i))
    
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    logging.info("Generando el archivo data.json en la carpeta json")


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%m-%d-%Y %I:%M:%S %p', level=logging.INFO)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--run",
            help="Corre el proceso para crear la tabla en una Base de Datos SQLite",
            action='store_true')
    parser.add_argument("--debug",
            help="Correr en modo DEBUG",
            action='store_true')
    args = parser.parse_args()

    try:
        if args.debug:
            logger.level = logging.DEBUG
        
        if args.run:
            extract_information()
        
    except Exception as e:
        logging.error("Process terminated with error: {}".format(e))
        raise

    return 0

if __name__ == '__main__':
    main()

