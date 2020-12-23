
from common import read_file_to_list

def passwordConfirmation(parameter):
    """
    docstring
    """
    if (parameter == None):
        raise AssertionError("parameter not given")
    if (type(parameter) != str and type(parameter) != list):
        raise TypeError("parameter is not string or list")

    if (type(parameter) == str):
        # read puzzle file
        puzzleData = read_file_to_list(parameter)
    else:
        puzzleData = parameter

    # modify the puzzle data 
    passwords = []
    for line in puzzleData:
        min_max_letter, password = line.split(": ")
        minimun, max_letter = min_max_letter.split("-")
        maximum, letter = max_letter.split(" ", 1)
        passwords.append(Password(int(minimun), int(maximum), letter, password))

    numberOfValidPasswords = 0
    for p in passwords:
        if (p.isValid()):
            numberOfValidPasswords += 1
    
    print(f"number of valid passwords found: {numberOfValidPasswords}")
    return numberOfValidPasswords

class Password:
    """
    Holds information on a single password. password must be
    follow the requirements
    min - number of required letters minimun
    max - maximun number of required letters allowed
    req_letter - the letter required in password
    password - the password itself
    """
    def __init__(self, _min, _max, _req_letter, _password) -> None:
        self.min = _min
        self.max = _max
        self.req_letter = _req_letter
        self.password = _password

    def isValid(self):
        """
        Returns True if password fulfills the requirements
        """
        numRequiredLetters = self.password.count(self.req_letter)
        if (numRequiredLetters >= self.min and numRequiredLetters <= self.max):
            return True
        else:
            return False

if __name__ == "__main__":
    passwordConfirmation("input/day2_input.txt")
    pass