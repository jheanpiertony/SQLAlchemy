import base64
import json
import os
import yaml

from project.constants import Constants


class GeneralsUtils:

    global_data = {}

    @staticmethod
    def decode(data):
        return base64.b64decode(data).decode('utf-8')

    @staticmethod
    def get_global_data(key):
        if not GeneralsUtils.validate_string(key):
            raise TypeError("The 'key' is not in the correct format")

        if key not in GeneralsUtils.global_data:
            return None

        return GeneralsUtils.global_data[key]

    @staticmethod
    def read_file(path, output_type="json"):
        read_file_output_types_allowed = Constants.READ_FILE_OUTPUT_TYPES

        if not GeneralsUtils.validate_string(path):
            raise TypeError("The 'path' is not in the correct format")

        if not os.path.isfile(path):
            raise FileNotFoundError("The requested file does not exist")

        if output_type not in read_file_output_types_allowed:
            raise ValueError("The configured value is not correct")

        with open(path, "r") as text_file:
            if output_type == "json":
                result = json.load(text_file)

            elif output_type == "yaml":
                result = yaml.safe_load(text_file)

        return result

    @staticmethod
    def set_global_data(key, value):
        if not GeneralsUtils.validate_string(key):
            raise TypeError("The 'key' is not in the correct format")

        GeneralsUtils.global_data[key] = value

    @staticmethod
    def validate_string(value):
        if not isinstance(value, str):
            return False

        if str.strip(value) == "":
            return False

        return True
