from config_utils import user_enter, function_maker
import data_types.did_do as bool_lib


def build_state_change_function(definition):
    """
    Builds a function that gets the the data for a state change from the user.
    Raises an error if the definition is not valid.
    str -> () -> str or error
    """
    return function_maker(user_enter_state_change, 
                          definition, is_valid_state_change_definition, 
                          "Not a time state change change definition: " + definition)

def is_valid_state_change_definition(definition):
    """
    Returns true if the state change definition is valid.
    str -> bool
    """
    return True

def user_enter_state_change(definition):
    """
    Gets a state_change from the user.
    Returns it along with label for the value.
    A state_change is a str.
    Signature in config: state_change label
    str -> (label: str, value: str)
    """
    update_question = 'Have any important events occurred consurning {}?'
    valid_update_respones = 'A valid response is eather "y" for True or "n" for False.'
    
    update = user_enter(get_state_change_label, 
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

    return user_enter(get_state_change_label, 
                      user_enter_state_change_response, 
                      get_state_change_from_response,
                      is_valid_state_change_response,
                      question,
                      valid,
                      definition)

def get_state_change_label(definition):
    """
    Given a valid key event definition, returns its label.
    str -> str
    """
    return definition

def user_enter_state_change_response():
    """
    Prompts the user to enter a key event response.
    nothing -> str
    """
    return input('>> ')

def get_state_change_from_response(response):
    """
    Gets the key event from a valid key event response.
    str -> float
    """
    return response

def is_valid_state_change_response(response):
    """
    Returns true if a key event response is valid.
    str -> bool
    """
    return len(response) > 0
