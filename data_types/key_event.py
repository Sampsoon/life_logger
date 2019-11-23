from life_logger_utils import user_enter, function_maker
import data_types.did_do as bool_lib

def build_key_event_function(definition):
    """
    Builds a function that gets the the data for a key event from the user.
    Raises an error if the definition is not valid.
    str -> () -> int or error
    """
    return function_maker(user_enter_key_event, 
                          definition, is_valid_key_event_definition, 
                          "Not a valid key event definition: " + definition)

def is_valid_key_event_definition(definition):
    """
    Returns true if the key event definition is valid.
    str -> bool
    """
    return True

def user_enter_key_event(definition):
    """
    Gets a key_event from the user.
    Returns it along with label for the value.
    A key_event is a str.
    Signature in config: key_event label
    str -> (label: str, value: str)
    """
    
    update_question = 'Have any important events occurred consurning {}?'
    valid_update_respones = 'A valid response is eather "y" for True or "n" for False.'
    
    update = user_enter(get_key_event_label, 
                      bool_lib.user_enter_boolean_response, 
                      bool_lib.get_bool_from_response,
                      bool_lib.is_valid_boolean_response,
                      update_question,
                      valid_update_respones,
                      definition)
    
    # If the user enters "yes"
    if not update[1]:
        return (update[0], '')
    
    question = 'Enter your event(s)?'
    valid = 'A valid response is a any text.'

    return user_enter(get_key_event_label, 
                      user_enter_key_event_response, 
                      get_key_event_from_response,
                      is_valid_key_event_response,
                      question,
                      valid,
                      definition)

def get_key_event_label(definition):
    """
    Given a valid key event definition, returns its label.
    str -> str
    """
    return definition

def user_enter_key_event_response():
    """
    Prompts the user to enter a key event response.
    nothing -> str
    """
    return input('>> ')

def get_key_event_from_response(response):
    """
    Gets the key event from a valid key event response.
    str -> float
    """
    return response

def is_valid_key_event_response(response):
    """
    Returns true if a key event response is valid.
    str -> bool
    """
    return len(response) > 0