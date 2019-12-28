from data_types.did_do import build_did_do_function
from data_types.key_event import build_key_event_function
from data_types.note import build_note_function
from data_types.state_change import build_state_change_function
from data_types.time import build_time_function
from data_types.value import build_value_function

COMMENT_OUT_STRING = '//'

LINE = '------------------------------------------------------'

MULTILINE_COMMENT_START = '/*'

MULTILINE_COMMENT_END = '*/'

DEFAULT_CONFIG_PATH = 'config.txt'

SAVE_DATA_PATH = 'saves\\save.csv'

"""
A map of type names to input functions.
none -> map of str to (str -> anything)
"""
TYPE_MAP = {
        'value' : build_value_function,
        'time' : build_time_function,
        'did_do' : build_did_do_function,
        'note' : build_note_function,
        'key_event' : build_key_event_function,
        'state_change' : build_state_change_function
        }