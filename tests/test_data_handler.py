import json
from app.data_handler import DataHandler
from app.file_handler import FileHandler
from .test_data_json import test_data
import pytest


class TestDataHandler:

    with open('app/data.json', 'w') as f:
        json.dump(test_data, f)
    test_data = FileHandler().json_data_loader()
    data = DataHandler.data_parser(test_data)

    cases = test_data[0].keys()
    expected = ['eq(1)', "positive()", "eq('['test', 1, True, False, None]')", "eq('string')", 
                        {'key': "eq('value')"}, "eq('[]')", "empty()", "eq(true)", "eq(false)"]

    @pytest.mark.usefixtures('json_file_clearer')
    @pytest.mark.parametrize('given, expected',list(zip(cases, expected)))
    def test_json_formatter(self, given, expected):
        assert self.data[0].get(given) == expected

    cases = [DataHandler, DataHandler.data_formatter, DataHandler.data_filter, DataHandler.data_parser]
    expected = [True, True, True, True]

    @pytest.mark.parametrize('given, expected', list(zip(cases, expected)))
    def test_data_handler_callable(self, given, expected):
        assert callable(given) == expected
    