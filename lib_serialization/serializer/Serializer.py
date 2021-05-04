from lib_serialization.serializer.serialization.proc_colls import serialize_obj, deserialize_obj


class Serializer:
    """
    Serialization class to represent any object in simple python structures
    """
    def serialize_obj(self, obj:object):
        """
        Returns serialized objects as dictionary.
        """
        return serialize_obj(obj)

    def deserialize_obj(self, obj:dict):
        """
        Returns object from dictionary with data fields of objects.
        """
        return deserialize_obj(obj)
