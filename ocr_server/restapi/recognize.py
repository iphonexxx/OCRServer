#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import io

CONFIG_PATH = './recognize/config1.yaml'

CONFIG_DATA = {}


def loadConfig():
    global CONFIG_DATA
    f = io.open(CONFIG_PATH, encoding='utf-8')
    CONFIG_DATA = yaml.safe_load(f)
    f.close()

    print(CONFIG_DATA)
    for name in CONFIG_DATA:
        config = CONFIG_DATA[name]

        if 'option' not in config['feature']:
            config['feature']['option'] = {}

        if 'rotate' not in config:
            config['rotate'] = 'perspective'

        if 'validate' not in config:
            config['validate'] = {
                'roi': None
            }

        if 'roi' not in config['validate']:
            config['validate']['roi'] = None

        if 'roi' not in config:
            config['roi'] = {}

    return


def getConfig():
    return CONFIG_DATA

#if __name__ == "__main__":
#    loadConfig() 
