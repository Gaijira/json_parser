import pytest
import json
import os

@pytest.fixture
def json_file_clearer():
    yield
    with open('app/data.json', 'w') as f:
        json.dump([], f)

@pytest.fixture
def yml_file_remover():
    yield
    os.remove('app/parsed_data.yml')