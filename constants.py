from data_types.did_do import user_enter_did_do
from data_types.key_event import user_enter_key_event
from data_types.note import user_enter_note
from data_types.state_change import user_enter_state_change
from data_types.time import user_enter_time
from data_types.value import user_enter_value

COMMENT_OUT_STRING = "//"
LINE = '----------------------------'

"""
a map of type names to input functions.
none -> map of str to (str -> anything)
"""
TYPE_MAP = {
        'value' : user_enter_value,
        'time' : user_enter_time,
        'did_do' : user_enter_did_do,
        'note' : user_enter_note,
        'key_event' : user_enter_key_event,
        'state_change' : user_enter_state_change
        }