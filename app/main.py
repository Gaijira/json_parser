from file_handler import FileHandler
from data_handler import DataHandler


data = FileHandler().json_data_loader()
DataHandler.data_parser(data)
FileHandler().yaml_data_writer(data)
