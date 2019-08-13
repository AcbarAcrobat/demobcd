import yaml
import re
import os
import logging


class Configuration:

    default_config = {
        'protocol'  : 'http',
        'host'      : 'localhost',
        'port'      : '4444',
        'path'      : '/wd/hub'
    }

    def __init__(self):
        self.config_file = 'config.yml'
        with open(self.config_file) as f:
            data = f.read()
        self.config = {**self.default_config,
                       **self._prepare_config(yaml.safe_load(data))}

    def get(self, k):
        return self.config[k]

    def _prepare_config(self, d):
        for k, v in d.items():
            if isinstance(v, dict):
                self._prepare_config(v)
            else:
                if isinstance(v, list):
                    for i, _ in enumerate(v, start=0):
                        if isinstance(_, str):
                            d[k][i] = re.sub(r'%(\w+)%', lambda match: os.environ[match.group(1)], v[i])
                else:
                    if isinstance(v, str):
                        d[k] = re.sub(r'%(\w+)%', lambda match: os.environ[match.group(1)], v)
        return d

