import json
import os

import yaml


class FileHandler():
    
    root_dir = os.path.dirname(os.path.abspath(__file__))

    def yaml_data_writer(self, data: dict) -> None:
        """Записывает переданный словарь в yaml формате в parsed_data.yaml"""
        with open(os.path.join(self.root_dir, 'parsed_data.yml'), 'w') as f2:
            yaml.dump(data, f2, encoding='UTF-8', allow_unicode=True, sort_keys=False)

    def json_data_loader(self) -> dict:
        """Выгружает данные из файла data.json и возвращает из в формате словаря"""
        with open(os.path.join(self.root_dir, 'data.json'), 'r') as f:
            data = json.load(f)
        return data
