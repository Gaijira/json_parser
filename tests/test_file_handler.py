import pytest
from app.file_handler import FileHandler
from .test_data_json import *
import json
import os
import yaml


class TestFileHandler():

    data = ''

    def test_json_file_exists(self):
        assert os.path.exists('app/data.json')


    def test_json_file_has_empty_array(self):
        with open('app/data.json', 'r') as f:
            self.data = json.load(f)
        assert  self.data == []
    

    @pytest.mark.usefixtures('json_file_clearer')
    def test_json_loader(self):
        with open('app/data.json', 'w') as f:
            json.dump(test_data, f)
        self.data = FileHandler.json_data_loader()
        assert self.data == test_data
    

    def test_yaml_file_creation(self):
        FileHandler.yaml_data_writer(test_data)
        assert os.path.exists('app/parsed_data.yml')


    @pytest.mark.usefixtures('yml_file_remover')
    def test_yam_file_data(self):
        with open('app/parsed_data.yml', 'r') as f:
            self.data = yaml.safe_load(f)
        assert self.data == test_data