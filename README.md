# life_logger

## About:
Our memories are inherently biased. It is very common for a few events to alter our perception of our past completely. We can invent memories, extend others, and change the pace of time. This project aims to counteract this by giving one an objective view of their past.

It does this by allowing you to apply data science to your life. With this logger, you can record your life in a structured manner. The data that is recorded is specifiable through a config file. This can consist of both numbers and strings/sudo journal entries. After that, you can run algorithms over your data to find correlations. You can use ML to build a predictive model with your data. In addition, you can use data visualization to analyze your past manually.

## Config Scripting:
The config allows you to specify the data that you are logging. The format consists of lines of data types followed by their names and any configurable parameters. An example can be found the `config.text`.

You can specify comments with `//` and multiline comments with `/* ... */`

### Data types:
* `range`

Asks the user to enter a range of integers between two values. **Format:** `range (a,b) "name"` Where the value must be between a inclusive and be exclusive.

* `time`

Asks the user to enter how long something took in hours as a float. **Format:** `time "name"`

* `did_do`

Asks the user to enter if they did something. **Format:** `did_do "name"`

* `note`

Asks the user to enter any notes for something. **Format:** `notes "name"`

* `key_event`

Asks the user to describe any key events surrounding something. **Format:** `key_event "name"`

* `state_change`

Asks the user if the state changed for anything in their life, if so, it logs it. An example of this could be job status or housing. **Format:** `state_change "name"`

* `floating_point`

Asks the user in enter a floating point value. **Format:** `floating_point "name"`

* `integer`

Asks the user in enter an integer point value. **Format:** `integer "name"`

* `time_stamp_military`

Asks the user in enter a time in millenary time that an event occurred. **Format:** `time_stamp_military "name"`

* `time_stamp_normal`

Asks the user in enter a time in none millenary time that an event occurred. **Format:** `time_stamp_normal "name"`

### Complex Data Types:

* `if_yes`

Asks the user if the the a yes or no response to a question marked by quotes; if the user's answer is yes, it asks the user to log a given value. **Format:** `if_yes "Did you exercise today?" time_stamp_normal exercise` **Note:** you can not nest other complex types in this. For example, `if_yes "Did you exercise today?" if_yes "Did you weight train?" time_stamp_normal exercise` would not work.

## Installation:
1. First download Python 3 and add it to your system paths.
2. Then run `pip install Pandas` in terminal
3. Then clone the repository

## How To Run
* On windows run `run_windows.bat`
* On Unix run `run_unix.sh`
* All saves will be saved to ./saves. 
* There will be a backup saved file created on every run, so no need to worry about making mistakes when logging.
* The config data can be specified in the config.txt

## Code Style:
* The code is written more functionally rather than ood.
* All methods must come with a purpose statement.
* No long methods
* All methods must come with a signature. Example:
`int, int, (str -> str) -> list of str`

 Would mean a method that took in two ints and a method that takes in a string and returns a string. It would return a list of string.

## Structure:
* All saved logged data are saved to `./saves`
* settings/constants are in `constants.py`
* The main method in is `start.py`
* All the data types that can be logged are in `./data_types` These are written as methods that take in user input through I/O and return the data.

### To create a new data type:
* You must make use of the `function_maker` method in `config_utils.py` to build your method.
* When defining the user input method as a perimeter for `function_maker` use `user_enter.py` in `config_utils.py` It is best to look to the code to see how this is done.
* After that you must add your data type to `TYPE_MAP` or `COMPLEX_TYPE_MAP` in `constants.py` with the key as the keyword that will be used to specify this type in the config. Complex types are defined as any type that references the types in `TYPE_MAP`. Unless this is true, you should add your new type to `TYPE_MAP`.


## To do:
* Increase test coverage (yes, I know test driven development is ideal)
* Write data analysis algorithms
* Write machine learning predictive algorithms
