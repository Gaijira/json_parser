import json
from typing import Any
import yaml


def data_formatter(item: Any, key: Any, value: Any) -> None:
    """Форматирует значения ключей в зависимости от типа данных, ключей и значений"""
    if type(value) == int and key != 'id':
        item[key] = "positive()"
    elif key == 'id' or type(value) == float:
        item[key] = f'eq({value})'
    elif value is None:
        item[key] = 'empty()'
    elif key == 'created_at' or key == 'updated_at' or key == 'start_at' or key == 'expiration_at':
        item[key] = "date('RFC3339')"
    elif value == 'False':
        item[key] = 'eq(false)'
    elif value == 'True':
        item[key] = 'eq(true)'
    else:
        item[key] = f'eq("{value}")'


def data_maker() -> dict:
    """Считывает массив c объектами из файла data.json, применяет форматирование по ключам и значениям к данным из файла,
    в завсисимости от структуры данных значения, значения могут являться вложенными структурами данных."""
    with open("data.json", 'r') as f:
        data = json.load(f)
        for item in data:
            for key, value in item.items():
                if not isinstance(value ,dict) and not isinstance(value, list):
                    data_formatter(item, key, value)
                elif isinstance(value, dict):
                    for inner_key, inner_value in value.items():
                        if isinstance(inner_value, dict):
                            for nested_key, nested_value in inner_value.items():
                                if isinstance(nested_value, dict):
                                   for key, value in nested_value.items():
                                       data_formatter(nested_value, key, value)
                        else:   
                            data_formatter(value, inner_key, inner_value)
                elif isinstance(value, list):
                    if any(isinstance(elem, dict) for elem in value):
                        for el in value:
                            if isinstance(el, dict):
                                for inner_key, inner_value in el.items():
                                    if not isinstance(inner_value, dict):
                                        data_formatter(el, inner_key, inner_value)
                                    elif isinstance(inner_value, dict):
                                        for nested_key, nested_value in inner_value.items():
                                            data_formatter(inner_value, nested_key, nested_value)
                    elif all(not isinstance(elem, dict) for elem in value):
                        data_formatter(item, key, value)
    return data


def yaml_data_writer(data: dict) -> None:
    """Записывает переданный словарь в yaml формате в parsed_data.yaml"""
    with open('parsed_data.yml', 'w') as f2:
        yaml.dump(data, f2, encoding='UTF-8', allow_unicode=True, sort_keys=False)


data = data_maker()
yaml_data_writer(data)
