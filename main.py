import json
from typing import Any
import yaml


def data_formatter(item: Any, key: Any, value: Any) -> None:
    """Форматирует значения словаря в зависимости от типа данных, ключей и значений"""
    if type(value) == int and key != 'id':
        item[key] = "positive()"
    elif key == 'id' or type(value) == float:
        item[key] = f'eq({value})'
    elif value is None:
        item[key] = 'empty()'
    elif key == 'created_at' or key == 'updated_at' or key == 'start_at' or key == 'expiration_at' or key == 'published_at':
        item[key] = "date('RFC3339')"
    elif value == False:
        item[key] = 'eq(false)'
    elif value == True:
        item[key] = 'eq(true)'
    elif key == 'description' or key == 'announcement_description':
        item[key] = "regex('(.)')"
    else:
        item[key] = f"eq('{value}')"

def data_sorter(item: Any, key: Any, value: Any) -> None:
    """Общий метод сортировки для словарей и массивов"""
    if not isinstance(value, dict) and not isinstance(value, list):
        data_formatter(item, key, value)
    elif isinstance(value, list) and len(value) == 0:
        data_formatter(item, key, value)
    elif isinstance(value, list) and not all(isinstance(el, dict) for el in value) and not all(isinstance(el, list) for el in value):
        data_formatter(item, key, value)
    else:
        data_parser(value)


def data_parser(data: dict) -> dict:
    """Рекурсивно проходит по массиву со словарями, форматируя значения словаря в зависимости от типа данных"""
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for key, value in item.items():
                    data_sorter(item, key, value)
    else:
        for key, value in data.items():
            data_sorter(data, key, value)
    return data               


def yaml_data_writer(data: dict) -> None:
    """Записывает переданный словарь в yaml формате в parsed_data.yaml"""
    with open('parsed_data.yml', 'w') as f2:
        yaml.dump(data, f2, encoding='UTF-8', allow_unicode=True, sort_keys=False)

def data_loader() -> dict:
    """Выгружает данные из файла data.json и возвращает из в формате словаря"""
    with open("data.json", 'r') as f:
        data = json.load(f)
    return data

data = data_loader()
data_parser(data)
yaml_data_writer(data)
