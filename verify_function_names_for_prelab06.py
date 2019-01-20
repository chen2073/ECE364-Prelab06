#! /user/local/bin/python3.4

from inspect import getmembers, isfunction

def runCheckAgainstStringFunctions():
    stringFunctions = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
                       'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
                       'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'ljust', 'lower', 'lstrip',
                       'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
                       'rstrip', 'split', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    fileName = "regex_app.py"
    with open(fileName, "r") as cFile:
        lines = cFile.readlines()

    printOut = ""
    functions = set()

    for index, line in enumerate(lines):
        for fn in stringFunctions:
            verb = "." + fn + "("

            if verb in line :
                printOut += '   Fn: "{}()" => Line({:03d}): "{}"\n'.format(fn, index, line.strip())
                functions.add("{}()".format(fn))

    if printOut:
        message = "The file {0} contains one or more string functions that cannot be used.\n".format(fileName)
        message += "Please remove these functions, or you might get 0.\n\n"
        message += "Functions Used: {0}\n\n".format(", ".join(functions))
        message += "Location Details:\n" + printOut
    else:
        message = "The file {0} has been checked, and it does not contain any string functions.".format(fileName)

    print("-------------------------------\n{}\n-------------------------------\n".format(message))
    
# Define desired functions that should be present.
functionNames = ["get_url_parts", "get_query_parameters", "get_special", "get_real_mac", "get_rejected_entries",
                 "get_employees_with_ids", "get_employees_without_ids", "get_employees_with_phones", "get_employees_with_states",
                 "get_complete_entries"]

# Attempt to import the code, and fail otherwise.
try:
    import regex_app as student
except:
    print("-------------------------------")
    print("Unable to find expected file.")
    print("-------------------------------")
    print()
    exit(-1)
else:
    print("-------------------------------")
    print("Code file imported successfully.")
    print("-------------------------------")
    print()

# Verify that file is clean of string functions.
runCheckAgainstStringFunctions()

# Obtain all functions in the code.
presentFunctions = [fnName for fnName, _ in getmembers(student, isfunction)]

# Check whether each function is present or missing, and print out the result.
for fnIndex, fnName in enumerate(functionNames):

    if fnName in presentFunctions:
        print('{:02d}- Function "{}" located.'.format(fnIndex + 1, fnName))
    else:
        print('{:02d}- =======> Unable to locate the function "{}".'.format(fnIndex + 1, fnName))
