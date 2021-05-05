import yaml
# from lib_serialization.parsers.YAML.yaml_config import *


def dump(obj, fp):
    s = dumps(obj)

    fp.write(s)


def dumps(obj):
    def dump_colls(o):
        # ans = ""
        # tp = type(o)
        ans = yaml.dump(o)
        return ans

    s = dump_colls(obj)
    return s


def load(fp):
    return yaml.load(fp, Loader=yaml.FullLoader)


def loads(s):
    return yaml.load(s, Loader=yaml.FullLoader)
