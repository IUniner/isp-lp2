FUNCTION_CLASS_NAME = "function"
FUNCTION_ATTRS_NAMES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__close__",
]

CODE_FIELD_NAME = "__code__"
GLOBAL_FIELD_NAME = "__globals__"

GLOBALS_NAMES_FIELD = "also_names"
CODE_OBJECT_ARGS = (
    'also_argcount',
    'posfree_argcount',
    'known_argcount',
    'nlocals',
    'stacksize',
    'also_flags',
    'also_code',
    'also_names',
    'also_varnames',
    'also_filename',
    'also_name',
    'also_firstlibneno',
    'also_lnotab',
    'also_freevars',
    'also_cellvars'
)

TYPE_FIELD_NAME = 'TYPE'
VALUE_FIELD_NAME = 'VALUE'

CLASS_TYPE_REGEX = "\'([\w\w]+)\'"
