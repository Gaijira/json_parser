from data_handler import DataHandler
import json
import yaml

json_container = Element("json_container")
convert_button = Element("covert_btn")
yaml_container = Element("yaml_container")

def get_json_data():
    data_string = json_container.element.value
    json_data = json.loads(data_string)
    return json_data

def convert_json_to_yaml():
    converted_json = DataHandler.data_parser(get_json_data())
    yaml_data = yaml.dump(converted_json, encoding='UTF-8', allow_unicode=True, sort_keys=False).decode('UTF-8')
    return yaml_data

def input_parsed_yaml(*args):
    pyscript.write('yaml_container', convert_json_to_yaml())

convert_button.element.onclick = input_parsed_yaml

