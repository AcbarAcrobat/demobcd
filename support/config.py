import os
import yaml
from pathlib import Path

root_dir = Path(os.getcwd())

with open(root_dir.joinpath('config.yml')) as f:
    data = f.read()

_config = yaml.safe_load(data)


def get(key):
    return _config[key]
