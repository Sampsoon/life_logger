from config_utils import user_enter, function_maker

def build_note_function(definition):
    """
    Builds a function that gets the the data for a note from the user.
    Raises an error if the definition is not valid.
    str -> () -> str or error
    """
    return function_maker(user_enter_note, 
                          definition, is_valid_note_definition, 
                          "Not a valid note definition: " + definition)

def is_valid_note_definition(definition):
    """
    Returns true if the note definition is valid.
    str -> bool
    """
    return True

def user_enter_note(definition):
    """
    Gets a note from the user.
    Returns it along with label for the value.
    A note is a str.
    Signature in config: note label
    str -> (label: str, value: str)
    """
    
    question = 'What notes if any do you have for {}?'
    valid = 'A valid response is a anything...I don\'t know how you got here'

    return user_enter(get_note_label, 
                      user_enter_note_response, 
                      get_note_from_response,
                      is_valid_note_response,
                      question,
                      valid,
                      definition)


def get_note_from_response(response):
    """
    Gets the note from a valid note response.
    str -> float
    """
    return response

def is_valid_note_response(response):
    """
    Returns true if a note response is valid.
    str -> bool
    """
    return True

def user_enter_note_response():
    """
    Prompts the user to enter a note response.
    nothing -> str
    """
    return input('>> ')
    
def get_note_label(definition):
    """
    Given a valid note definition, returns its label.
    str -> str
    """
    return definition