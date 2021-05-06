from lib_serialization.parsers_factory.parser_objects.Parser import Parser
import lib_serialization.parsers.TOML.iuninertoml as craft_toml


class TOMLParser(Parser):
    """
    Parser object for TOML format, which uses craft library.
    """
    
    def dump(self, obj, fp):
        """
        Classic dump to serialize objects and put results.
        """
        simple = self.serializer.serialize_obj(obj)
        return craft_toml.dump(simple, fp)
    
    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        simple = self.serializer.serialize_obj(obj)
        return craft_toml.dumps(simple)

    def load(self, fp):
        """
        Returns parsed object and data from uploaded file.
        """
        raw_input = craft_toml.load(fp)
        return self.serializer.deserialize_obj(raw_input)

    def loads(self, s):
        """
        Returns parsed object and data from uploaded string.
        """
        raw_input = craft_toml.loads(s)
        return self.serializer.deserialize_obj(raw_input)
