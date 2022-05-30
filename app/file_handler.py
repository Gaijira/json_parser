import json
import os

import yaml


class FileHandler():

    def yaml_data_writer(data: dict) -> None:
        """Записывает переданный словарь в yaml формате в parsed_data.yaml"""
        root_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(root_dir, 'parsed_data.yml'), 'w') as f2:
            yaml.dump(data, f2, encoding='UTF-8', allow_unicode=True, sort_keys=False)

    def json_data_loader() -> dict:
        """Выгружает данные из файла data.json и возвращает из в формате словаря"""
        root_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(root_dir, 'data.json'), 'r') as f:
            data = json.load(f)
        return data
