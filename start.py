import sys
import constants
from life_logger_utils import config_to_functions 

def main():
    """
    Runs the program.
    """

    mock_config = ['value (0,10) stuff', '//hello', 'time Some stuff', 'did_do otherStuff', 'key_event event', 'state_change change', 'note notworthy thing']

    input_functions = config_to_functions(mock_config)
    
    data = []
    
    new_line = '\n'
    
    print(new_line)
    print(constants.LINE)
    print("WELCOME TO LIFE LOGGER")
    print(constants.LINE)
    print()
    
    for func in input_functions:
        data.append(func())
        print('\n----------------------------\n')

main()