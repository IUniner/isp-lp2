import pytomlpp as toml
from lib_serialization.parsers.TOML.toml_config import *


def replace_values(d: dict, comp_obj=None, replaced_obj=NULL_STRING):
    if type(d) != dict:
        return d
    for name, o in d.items():
        if type(o) == dict:
            replace_values(o, comp_obj, replaced_obj)
        else:
            t = type(o)
            if t == list or t == tuple:
                for i in range(len(o)):
                    if type(o[i]) == dict:
                        replace_values(o, comp_obj, replaced_obj)
                    elif o[i] == comp_obj:
                        o[i] = replaced_obj
            elif o == comp_obj:
                d[name] = replaced_obj


def dumps(d: dict):
    replace_values(d, None, NULL_STRING)
    return toml.dumps(d)


def dump(s, fp):
    replace_values(s, None, NULL_STRING)
    pp = toml.dumps(s)
    fp.write(pp)


def load(fp):
    result = toml.load(fp)
    print(result)
    replace_values(result, NULL_STRING, None)
    return result


def loads(s):
    result = toml.loads(s)
    replace_values(result, NULL_STRING, None)
    return result
