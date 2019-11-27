import sys
import constants
from life_logger_utils import config_to_functions, open_file

def main():
    """
    Runs the program.
    """

    mock_config = open_file(constants.CONFIG_PATH)

    input_functions = config_to_functions(mock_config)
    
    data = []
    
    new_line = '\n'
    tab = '\t'
    
    print(new_line)
    print(constants.LINE)
    print(tab + tab + 'WELCOME TO LIFE LOGGER')
    print(constants.LINE)
    print()
    
    for func in input_functions:
        data.append(func())
        print('\n' + constants.LINE + '\n')

main()