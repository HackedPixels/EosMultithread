from enum import Enum

class States(Enum):
    INFO=0
    WARN=1
    ERROR=2

# TODO: Wrap this in a class
__log__summary = {}

Colors = {
    'INFO': '\x1b[33m[INFO]: ',
    'WARN': '\x1b[34m[WARN]: ',
    'ERROR': '\x1b[31;1m[FAIL]: ',
}

# prepares the dictionary used to store errors and warnings
def __init_log():
    for t in States:
        __log__summary[t.name] = 0

# prints stuff out to the console prefaced by the Color and State
def __log(state=States.INFO, message=""):
    global Colors
    global __log__summary

    if state != States.INFO:
        __log__summary[state.name] += 1

    print("{}{}\x1b[m".format(Colors[state.name], message))

# prints a finishing line
# TODO: fix the bug that Colors also stores the [WARN] string
def __log_summary():
    print("finished with {}{}\x1b[m errors and {}{}\x1b[m warnings" \
        .format(Colors[States.ERROR.name], __log__summary[States.ERROR.name], \
        Colors[States.WARN.name], __log__summary[States.WARN.name]))
