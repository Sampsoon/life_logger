import sys


'''
Event types:

Will need:
- Config file for things to track
- A way to visualize data
- Some premade analisis using ML and data science algo
- A way to log data in the consol

Data def:
    - value(a,b) (integer from 0 to 10 inclusive)
    - time (number in hours)
    - did_do ("y" or "n")
    - note (string)
    - keyevent (string)
    - stateChange: (string)
        When my current living state changes. This data will be carried to every new log unless
        specified otherwise

My config:
// emotions
    value (0,3) Energy
    value (0,3) Sociability
    value (0,3) Melancholy
    value (0,3) Self Assurance
    value (0,3) Stress
    value (0,3) Aggression
    value (0,3) Longing
    value (0,3) Contentness
    value (0,3) Focus
    value (0,3) Disgust
    value (0,3) Passion For Life
    value (0,3) Appreciation

// Activity
    did_do Meditate
    did_do Exercised
    did_do Got a Good Nights Sleep
    did_do Read
    did_do Worked on Side Project
    value (0,3) Ate low carbs
    value (0,3) Amount of Food Eaten
    value (0,3) socialized
    value (0,3) walked around white lost in thought
    value (0,3) did school work

// Notes
    note things I learned
    note notworthy stuff
    keyevent key events
    sateChange housing
    sateChange school, work, ect...

output:
xml
    
'''

# A definition is the text following space after the type name.

# Get a value from the user.
# A value is a int from a to b inclusive.
# Signature in config: value (a,b) name
# str -> int
def get_value(definition):
    print("value " + definition)

# Get a time from the user.
# A time is a float.
# Signature in config: time name
# str -> float
def get_time(definition):
    print("time " + definition)

# Gets a did? from the user.
# A did_do is a bool.
# Signature in config: did_do name
# str -> bool
def get_did_do(definition):
    print("did do " + definition)

# Gets a note from the user.
# A note is a str.
# Signature in config: note name
# str -> str
def get_note(definition):
    print("get note " + definition)

# Gets a key_event from the user.
# A key_event is a str.
# Signature in config: key_event name
# str -> str
def get_key_event(definition):
    print("key event " + definition)

# Gets a state_change from the user.
# A state_change in a str.
# Signature in config: state_change name
# str -> str
def get_state_change(definition):
    print("state change " + definition)

# Takes in the data for a config and returns a list of functions to call the meet it's criteria.
# list of str -> list of (none -> str)
def config_to_functions(config):
    type_to_input_functions = get_type_map()

    functions = []

    for line in config:
        check_config_line(line)
        line = line.split(" ", 1)

        type = line[0]
        check_type(type)

        definition = line[1]

        # Have to do binding because Python is retarded: https://stackoverflow.com/questions/58667027/string-values-are-passed-in-as-reference-to-a-python-lambda-for-some-reason?noredirect=1#comment103636999_58667027
        functions.append(lambda type = type, definition = definition: type_to_input_functions[type](definition))
    return functions


# Checks that a given type is valid.
# If not, throw an exception.
# str -> none
def check_type(type):
    if type not in get_type_map():
        raise ValueError(type + " is not a valid type")

# Checks that a given line in the config is valid.
# If not, throw an exception.
# str -> none
def check_config_line(line):
    if len(line.split(" ", 1)) == 1:
        raise ValueError("Invalid config line: " + line)

# Returns a map of type names to input functions.
# An input function is a fuc(str) -> str.
# none -> map of str to (str -> str)
def get_type_map():
    return {
        "value" : get_value,
        "time" : get_time,
        "did_do" : get_did_do,
        "note" : get_note,
        "key_event" : get_key_event,
        "state_change" : get_state_change
        }

# Runs the program.
def main():

    mockConfig = ["value (a,b) stuff", "time Some stuff", "did_do otherStuff"]

    input_functions = config_to_functions(mockConfig)

    for func in input_functions:
        func()

main()
