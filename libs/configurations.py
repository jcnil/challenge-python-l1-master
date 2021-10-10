#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml,os


class Configuration():

    config = yaml.load(open('%s/challenge.conf' % os.path.abspath('.')), Loader=yaml.FullLoader)

    # database sqlite
    SQ_HOST = config['sqlite']['host']
    SQ_NAME = config['sqlite']['name']

    #API-REST
    API_ALL = config['api_all']