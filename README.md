| Region | City Name | Languaje                                 | Time    |
| ------ | --------- | ---------------------------------------- | ------- |
| Africa | Angola    | AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms |
|        |           |                                          |         |
|        |           |                                          |         |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
2. De https://restcountries.com/ Obtenga un pais por region apartir de la region optenida del punto 1.
3. De https://restcountries.com/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json
9. La prueba debe ser entregada en un repositorio git.

**Es un plus si:**

- No usa famework
- Entrega Test Unitarios
- Presenta un diseño de su solucion.

Para Correger la aplicacion se debe:

1. Crear un virtualenv en mi caso use pyenv para crear un entorno virtual:

    $ pyenv virtualenv 3.9.5  <nombre_ambiente>

    Luego se activa el entorno virtual:

    $ pyenv activate <nombre_ambiente>

    y posteriormente se correl paso 2, para mayor insformacion consultar la pagina https://realpython.com/intro-to-pyenv/     

2. Instalar las librerias que estan en el archivo de requirements.txt ejecuntado el siguiente comando

   $ pip3 install -r requirements.txt

3. Luego a traves del shell se ingresa a la carpeta principal y se ejecuta el siguiente comando

   $ python3 run.py --run
