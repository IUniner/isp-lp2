from lib_serialization.parsers_factory.parser_objects.Parser import Parser
import lib_serialization.parsers.JSON.iuninerjson as craft_json


class JSONParser(Parser):
    """
    Parser for ".json" format, which uses craft library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put rhe result to file.
        """
        simple = self.serializer.serialize_obj(obj)
        return craft_json.dump(simple, fp)

    def dumps(self, fp):
        """
        Returns parsed object and data from the file.
        """
        raw_object = craft_json.load(fp)
        return self.serializer.deserialize_obj(raw_object)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        raw_object = craft_json.loads(s)
        return self.serializer.deserialize_obj(raw_object)
