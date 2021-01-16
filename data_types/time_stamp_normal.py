from config_utils import user_enter, function_maker
from data_types.time_utils import respones_to_datetime, datatime_to_string
import constants

def build_time_stamp_normal_function(definition):
    """
    Builds a function that gets the data for a time_stamp_normal from the user.
    Raises an error if the definition is not valid.
    str -> (() -> (label: str, value: str)) or error
    """
    return function_maker(user_enter_time_stamp_normal, 
                          definition, is_valid_time_stamp_normal_definition, 
                          "Not a valid time_stamp_normal definition: " + definition)

def is_valid_time_stamp_normal_definition(definition):
    """
    Returns true if the time_stamp_normal definition is valid.
    str -> bool
    """
    return True

def user_enter_time_stamp_normal(definition):
    """
    Get a time_stamp_normal from the user.
    Returns it along with label for the time_stamp_normal.
    A time_stamp_normal is a string representation of a time.
    Signature in config: time_stamp_normal label
    str -> (label: str, time_stamp_normal: str)
    """
    
    question = 'When did you {}?'
    valid = 'A valid response is any AM/PM time in the following respresation: Hours:Munuts Am/PM'

    return user_enter(get_time_stamp_normal_label,
                      user_enter_time_stamp_normal_response,
                      get_time_stamp_normal_from_response,
                      is_valid_time_stamp_normal_response,
                      question,
                      valid,
                      definition)


def get_time_stamp_normal_from_response(response):
    """
    Gets the value from a valid time_stamp_normal response.
    str -> str
    """
    time = respones_to_datetime(response, constants.DATETIME_FORMATE_NORMAL)
    return datatime_to_string(time, constants.DATETIME_FORMATE_NORMAL)
    
def is_valid_time_stamp_normal_response(response):
    """
    Returns true if a time_stamp_normal response is valid.
    str -> bool
    """
    try:
        respones_to_datetime(response, constants.DATETIME_FORMATE_NORMAL)
        return True
    except ValueError:
        return False

def user_enter_time_stamp_normal_response():
    """
    Prompts the user to enter a time_stamp_normal response.
    nothing -> str
    """
    return input('Time: ')
    
def get_time_stamp_normal_label(definition):
    """
    Given a valid time_stamp_normal definition, returns its label.
    str -> str
    """
    return definition