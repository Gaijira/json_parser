from typing import Any


class DataHandler():

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


    @classmethod
    def data_filter(cls, item: Any, key: Any, value: Any) -> None:
        """Общий метод сортировки для словарей и массивов"""
        if not isinstance(value, dict) and not isinstance(value, list):
            cls.data_formatter(item, key, value)
        elif isinstance(value, list) and len(value) == 0:
            cls.data_formatter(item, key, value)
        elif isinstance(value, list) and not all(isinstance(el, dict) for el in value) and not all(isinstance(el, list) for el in value):
            cls.data_formatter(item, key, value)
        else:
            cls.data_parser(value)


    @classmethod
    def data_parser(cls, data: dict) -> dict:
        """Рекурсивно проходит по массиву со словарями, форматируя значения словаря в зависимости от типа данных"""
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    for key, value in item.items():
                        cls.data_filter(item, key, value)
        else:
            for key, value in data.items():
                cls.data_filter(data, key, value)
        return data    