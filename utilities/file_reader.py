import json
import os
from turtle import pd

import yaml


def get_config():
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, "config", "config.yaml")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        return config

def read_json_file(file):
    with open(file, "r") as f:
        return json.load(f)


def read_csv_file(file):
    with open(file, "r") as f:
        return f.read()

