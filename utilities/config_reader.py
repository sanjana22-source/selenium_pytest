import os

import yaml


def get_config():
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, "config", "config.yaml")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        return config


