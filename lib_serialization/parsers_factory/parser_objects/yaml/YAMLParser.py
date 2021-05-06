from lib_serialization.parsers_factory.parser_objects.Parser import Parser
import lib_serialization.parsers.YAML.iunineryaml as craft_yaml


class YAMLParser(Parser):
    """
    Parser objects for ".yaml" format, which uses craft library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        simple = self.serializer.serialize_obj(obj)
        return craft_yaml.dump(simple, fp)

    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        simple = self.serializer.serialize_obj(obj)
        return craft_yaml.dump(simple)

    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        raw_input = craft_yaml.load(fp)
        return self.serializer.deserialize_obj(raw_input)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        raw_input = craft_yaml.loads(s)
        return self.serializer.deserialize_obj(raw_input)
