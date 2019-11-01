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
    - did? ("y" or "n")
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
    value (0,3) Apreseation

// Activity
    did? Meditate
    did? Exercised
    did? Got a Good Nights Sleep
    did? Read
    did? Worked on Side Project
    value (0,3) Ate low carbs
    value (0,3) Amount of Food Eaten
    value (0,3) solsized
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

# A definition is the text following the type that defines the individual attributes of the type.

# Get a value from the user.
# A value is a int from a to b inclusive.
# Signature in config: value (a,b) name
# str -> int
def get_value(definition):
    pass

# Get a time from the user.
# A time is a float.
# Signature in config: time name
# str -> float
def get_time(definition):
    pass

# Gets a did? from the user.
# A did? is a bool.
# Signature in config: did? name
# str -> bool
def get_did?(definition):
    pass

# Gets a note from the user.
# A note is a str.
# Signature in config: note name
# str -> str
def get_note(definition):
    pass

# Gets a key_event from the user.
# A key_event is a str.
# Signature in config: key_event name
# str -> str
def get_key_event(definition):
    pass

# Gets a state_change from the user.
# A state_change in a str.
# Signature in config: state_change name
# str -> str
def get_state_change(definition):
    pass

'''
Plane: will use list of lambda functions to get user input
'''


def main():
    pass