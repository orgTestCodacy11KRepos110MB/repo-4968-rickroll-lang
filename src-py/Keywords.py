from helpers import dict_values

# TO-DO: replace all KW* vars by this dict
KW = {
    'print' : 'ijustwannatelluhowimfeeling',
    'if' : 'andifuaskmehowimfeeling',

    'let' : 'give',
    'assign' : 'up',
    'import1' : 'weknowthe',
    'import2' : "andwe'regonnaplayit",
    'def' : 'gonna',
    'return1' : 'whenigivemy',
    'return2' : 'itwillbecompletely',
    'try' : 'thereaintnomistaking',
    'except' : 'iftheyevergetudown',
    'main' : 'takemetourheart',
    'end' : 'saygoodbye',

    'break' : 'desertu',
    'continue' : 'runaround',
    'endless_loop' : 'togetherforeverandnevertopart',
    'while_loop' : 'togetherforeverwith',

    'L_OP' : 'islessthan',
    'G_OP' : 'isgreaterthan',
    'GOE_OP' : 'isgreaterthanorequalto',
    'LOE_OP' : 'islessthanorequalto',
    'is_not_OP' : 'aint',
    'E_OP' : 'is',

    'PY' : 'py:'
}

# Keywords
KW_print        = 'ijustwannatelluhowimfeeling'
KW_if           = 'andifuaskmehowimfeeling'

KW_let          = 'give'
KW_assign       = 'up'
KW_import1      = 'weknowthe'
KW_import2      = "andwe'regonnaplayit"
KW_def          = 'gonna'
KW_return1      = 'whenigivemy'
KW_return2      = 'itwillbecompletely'
KW_try          = 'thereaintnomistaking'
KW_except       = 'iftheyevergetudown'
KW_main         = 'takemetourheart'
KW_end          = 'saygoodbye'

KW_break        = 'desertu'
KW_continue     = 'runaround'
KW_endless_loop = 'togetherforeverandnevertopart'
KW_while_loop   = 'togetherforeverwith'

KW_L_OP = 'islessthan'
KW_G_OP = 'isgreaterthan'
KW_GOE_OP = 'isgreaterthanorequalto'
KW_LOE_OP = 'islessthanorequalto'
KW_is_not_OP = 'aint'
KW_E_OP = 'is'

KW_PY = 'py:'

keywords = dict_values(KW)

INDENT_KW = [
    KW['if'], KW['def'], KW['try'], KW['except'], KW['while_loop'], KW['endless_loop']
]

# Tokens that the interpreter will totally ignore
ignore_tokens = set("~'")

# Characters in numerals
digits = set('0123456789.')

# Separators are used in tokenization
separators = {
    # Don't use `set`, because multi-char `str`s may be added in the future
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

# Operators
operators = {
    '+', '-', '*', '/', '%', '^', '=',
    '[', ']', '(', ')', '{', '}', ',',
    '>', '<', '<=', '>=', '!=', 'is', 'aint'
}
OP_build_in_functions = {'to_string', 'to_int', 'to_float', 'length'}
