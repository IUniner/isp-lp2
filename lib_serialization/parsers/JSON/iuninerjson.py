# import re

from lib_serialization.parsers.JSON.json_config import *
from lib_serialization.parsers.JSON.exceptions import *


def dump(obj, fp):
    s = dumps(obj)

    fp.write(s)


def dumps(obj):
    def dump_colls(colls_obj):
        ans = ""
        tp = type(colls_obj)
        if tp == dict:
            ans += OBJECT_START
            for name, o in colls_obj.items():
                ans += f"\"{name}\": "
                ans += dump_obj(o)
                if list(colls_obj.keys())[-1] != name:
                    ans += FIELDS_SEPARATOR + " "
            ans += OBJECT_END
        elif tp == list or tp == tuple:
            ans += ARRAY_START
            for i in range(len(colls_obj)):
                ans += dump_obj(colls_obj[i])
                if i != len(colls_obj) - 1:
                    ans += FIELDS_SEPARATOR + " "
            ans += ARRAY_END
        return ans

    def dump_obj(o):
        string = ""
        tp = type(o)
        if tp == bool:
            if o:
                string += JSON_TRUE
            else:
                string += JSON_FALSE
        elif o is None:
            string += JSON_NONE
        elif isinstance(o, (int, bytes, float, colls)):
            string += str(o)
        elif tp != str:
            string += dump_colls(o)
        else:
            string += "\"" + str(o).replace("\n", " ") + "\""

        return string

    s = dump_colls(obj)
    return s


def load(fp):
    if fp.encoding != FILE_ENCODING:
        raise ValueError
    s = fp.read()
    return loads(s)


def loads(s):
    assert isinstance(s, str)
    ind = 0

    def parse_colls(s, index=-1):
        assert (isinstance(s, str) or isinstance(index, int))
        nonlocal ind
        ind = index + 1
        ans = {}
        field_name = ""
        value = ""
        is_field = True
        is_value = False
        value_quotes = False
        quotes = False
        while ind < len(s):
            if not quotes and s[ind].isspace():
                ind += 1
                continue
            if s[ind] == '\"' or s[ind] == '\'':
                if is_field and not quotes:
                    if len(field_name) != 0:
                        raise WrongJSONException()
                    quotes = True
                elif is_field and quotes:
                    if s[ind - 1] == '\\':
                        field_name += s[ind]
                    else:
                        quotes = False
                elif is_value and not quotes:
                    if len(value) != 0:
                        raise Exception
                    else:
                        quotes = value_quotes = True
                elif is_value and quotes:
                    if s[ind - 1] == '\\':
                        value += s[ind]
                    quotes = False
            elif not quotes:
                if s[ind] == FIELDS_VALUE_SEPARATOR:
                    is_field = not is_field
                    is_value = not is_value
                elif s[ind] == FIELDS_SEPARATOR and is_value:
                    if not value_quotes and isinstance(value, str):
                        value = try_parse(value)
                    ans[field_name] = value
                    field_name = ""
                    value = ""
                    value_quotes = False
                    is_field = True
                    is_value = False
                elif s[ind] == '.' and is_value:
                    if not s[ind + 1].isdigit() or '.' in value:
                        raise WrongJSONException()
                    value += s[ind]
                elif s[ind] == OBJECT_START:
                    if len(value) != 0:
                        raise WrongJSONException()
                    ans[field_name] = parse_colls(s, ind)
                    field_name = ""
                    value_quotes = False
                    is_field = True
                    is_value = False
                elif s[ind] == OBJECT_END:
                    if field_name != "":
                        if not value_quotes and isinstance(value, str):
                            value = try_parse(value)

                        ans[field_name] = value
                    ind += 1
                    break
                elif is_value:
                    value += s[ind]
            elif is_field:
                field_name += s[ind]
            elif is_value:
                value += s[ind]
            ind += 1
        return ans

    def parse_array(s, index=-1):
        assert (isinstance(s, str) or isinstance(index, int))

        nonlocal ind
        ind = index + 1
        ans = []
        value = ""
        quotes = False
        value_quotes = False
        while ind < len(s):
            if not quotes and s[ind].isspace():
                ind += 1
                continue
            if s[ind] == '\"' or s[ind] == '\'':
                if not quotes:
                    if len(value) != 0:
                        raise WrongJSONException()
                    quotes = True
                    value_quotes = True
                elif quotes:
                    quotes = False
            elif not quotes:
                if s[ind] == '.':
                    if not s[ind + 1].isdigit() or '.' in value:
                        raise WrongJSONException()
                    value += s[ind]
                elif s[ind] == FIELDS_SEPARATOR:
                    if not value_quotes and isinstance(value, str):
                        value = try_parse(value)
                    ans.append(value)
                    value = ""
                    value_quotes = False
                elif s[ind] == OBJECT_START:
                    value = parse_colls(s, ind + 1)
                elif s[ind] == ARRAY_END:
                    if value == "":
                        return ans
                    if not value_quotes and isinstance(value, str):
                        value = try_parse(value)
                    ans.append(value)
                    break
                else:
                    value += s[ind]
            else:
                value += s[ind]
            ind += 1

        return ans

    def try_parse(value):
        val = ""

        if value == JSON_FALSE or value == PYTHON_FALSE:
            val = False
        elif value == JSON_TRUE or value == PYTHON_TRUE:
            val = True
        elif value == JSON_NONE or value == PYTHON_NONE:
            val = None
        else:
            try:
                val = int(value)
            except ValueError:
                try:
                    val = float(value)
                except ValueError:
                    return val

        return val

    ans = parse_colls(s)

    return ans['']
