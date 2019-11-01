import sys


'''
Event types:

    - value (number from 0 to 10)
    - time (number)
    - note (string)
    - keyevent (string)
    - stateChange: (string)
        When my current living state changes. This data will be carried to every new log unless
        specified otherwise

This tracks:
    value energy
    value confidence
    value sociability
    value excitement
    value dread
    value shock
    value melancholy
    value selflove
    value anger
    value self assurance
    value(0 to 3) euphoric happiness
    value clarity of mind
    value stress
    value aggression
    value longing
    value regret
    value creativity
    value contentness
    value thoughtfulness
    value precents
    value disgust


output:
xml

'''