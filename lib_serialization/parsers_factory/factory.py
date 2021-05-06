from lib_serialization.parsers_factory.parser_objects.json.JSONParser import JSONParser
from lib_serialization.parsers_factory.parser_objects.yaml.YAMLParser import YAMLParser
from lib_serialization.parsers_factory.parser_objects.toml.TOMLParser import TOMLParser


EXTENSIONS = {
    "JSON": "json",
    "YAML": "yaml",
    "TOML": "toml"
}


class ParserFactory(object):
    """
    Factory class with pure patterns of parser_factory , which create parsing object for specified data formats.
    """

    @staticmethod
    def get_parser(target_format: str):
        ft = target_format.lower()
        if ft == EXTENSIONS["JSON"]:
            return JSONParser()
        elif ft == EXTENSIONS["YAML"]:
            return YAMLParser()
        elif ft == EXTENSIONS["TOML"]:
            return TOMLParser()
        else:
            raise ValueError
