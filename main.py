import json
import yaml


def formatter(item, key, value) -> None:
    """Форматирует значения ключей в зависимости от типа данных, ключей и значений"""
    if type(value) == int and key != 'id':
        item[key] = "positive()"
    elif key == 'id' or type(value) == float:
        item[key] = f'eq({value})'
    elif value is None:
        item[key] = 'empty()'
    elif key == 'created_at' or key == 'updated_at' or key == 'start_at' or key == 'expiration_at':
        item[key] = "date('RFC3339')"
    elif key == 'False':
        item[key] = 'eq(false)'
    elif key == 'True':
        item[key] = 'eq(true)'
    else:
        item[key] = f'eq("{value}")'



def data_maker() -> dict:
    """Считывает массив c объектами из файла data.json, применяет замену по ключам и значениям к данным из файла, 
    значения могут являться вложенными структурами данных."""
    with open("data.json", 'r') as f:
        data = json.load(f)
        for item in data:
            for key, value in item.items():
                if not isinstance(value ,dict) and not isinstance(value, list):
                    formatter(item, key, value)
                elif isinstance(value, dict):
                    for inner_key, inner_value in value.items():
                        formatter(value, inner_key, inner_value)
                elif isinstance(value, list):
                    if any(isinstance(elem, dict) for elem in value):
                        for el in value:
                            if isinstance(el, dict):
                                for inner_key, inner_value in el.items():
                                    if not isinstance(inner_value, dict):
                                        formatter(el, inner_key, inner_value)
                                    elif isinstance(inner_value, dict):
                                        for nested_key, nested_value in inner_value.items():
                                            formatter(inner_value, nested_key, nested_value)
                    elif all(not isinstance(elem, dict) for elem in value):
                        formatter(item, key, value)
    return data


def yaml_data_writer(data):
    """Записывает переданный словарь и парсит в yaml"""
    with open('parsed_data.yml', 'w') as f2:
        yaml.dump(data, f2, encoding='UTF-8', allow_unicode=True, sort_keys=False)


data = data_maker()
yaml_data_writer(data)
