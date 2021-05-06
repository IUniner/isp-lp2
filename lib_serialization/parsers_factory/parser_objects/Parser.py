from abc import ABC, abstractmethod
from lib_serialization.serializer.Serializer import Serializer


class Parser(ABC):
    """
    Abstract class of a parser, which has all necessary methods to process different data formats.
    """

    def __init__(self):
        self.serializer = Serializer()

    def set_serializer(self, new_serializer: Serializer):
        assert isinstance(new_serializer, Serializer)
        self.serializer = new_serializer

        @abstractmethod
        def dump(self, obj, fp):
            """
            Classic dump to serialize objects and write in the file.
            """
            pass

        @abstractmethod
        def dumps(self, obj):
            """
            Returns string with serialized objects.
            """
            pass

        @abstractmethod
        def load(self, fp):
            """
            Returns parsed object and infos from the file.
            """
            pass

        @abstractmethod
        def loads(self, s):
            """
            Returns string with parsed objects and infos from the target file.
            """
            pass
