import os

from project.constants import Constants
from project.resources.utils.generals_utils import GeneralsUtils


class ConfigurationManager():

    __CONFIGURATIONS__ = {}

    @staticmethod
    def get_api_version() -> str:
        try:
            result = ConfigurationManager.get_config(
                Constants.CONFIG_APP_VERSION_KEY)

        except Exception:
            result = "Unknown"

        return result

    @staticmethod
    def get_config(key: str):
        if key in os.environ:
            return os.environ[key]

        if len(ConfigurationManager.__CONFIGURATIONS__) == 0:
            ConfigurationManager.__CONFIGURATIONS__ =\
                 GeneralsUtils.read_file("config.yml", "yaml")["config"]

        configurations = ConfigurationManager.__CONFIGURATIONS__

        if key not in configurations:
            raise KeyError(f"The requested configuration '{key}' " +
                           "does not exist")

        return configurations[key]
