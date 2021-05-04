from lib_serialization.serializer.serialization.proc_colls import serialize_obj, deserialize_obj


class Serializer:
    """
    Serialization class to represent any object in simple python data structures.
    """
    @staticmethod
    def serialize_obj(obj: object):
        """
        Returns serialized object as dictionary.
        """
        return serialize_obj(obj)

    @staticmethod
    def deserialize_obj(obj: dict):
        """
        Returns object from dictionary with fields of objects.
        """
        return deserialize_obj(obj)
