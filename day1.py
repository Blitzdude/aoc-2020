
'''
expense_report takes an list of integer values
as data. It finds two values in that list that
add to 2020 and multiplies them together.
Then it returns the value
'''
from common import read_file_to_list


def expense_report(parameter):
    if (parameter == None):
        raise TypeError("data is empty or not defined")
    if (type(parameter) != list and type(parameter) != str):
        raise TypeError("input value is not a list or string.")
    if (len(parameter) <= 1):
        raise AssertionError("List must have more than 1 value")

    reportData = []
    if (type(parameter) == str):
        reportData = read_file(parameter)
    else:
        reportData = parameter

    # Find Loop through the values in two iterators
    valueFound = -1
    firstValue = -1
    secondValue = -1
    for i in range(0, len(reportData) - 1):
        for j in range(i+1, len(reportData)):
            if reportData[i] + reportData[j] == 2020:
                firstValue = reportData[i]
                secondValue = reportData[j]
                valueFound = firstValue * secondValue
                break
            else:
                continue

    if valueFound > 0:
        print(f"Sum 2020 found with values {firstValue} and {secondValue}.")
        print(f"Final value was {valueFound}")
        return valueFound
    else:
        print("no two values with sum equal to 2020 found.")
        return -1

def expense_report_advanced(parameter):
    if (parameter == None):
        raise TypeError("data is empty or not defined")
    if (type(parameter) != list and type(parameter) != str):
        raise TypeError("input value is not a list or string.")
    if (len(parameter) <= 2):
        raise AssertionError("List must have more than 2 values")

    reportData = []
    if (type(parameter) == str):
        reportData = read_file_to_list(parameter)
    else:
        reportData = parameter

    # Find Loop through the values in two iterators
    values = {"first":-1, "second":-1, "third":-1, "answer":-1}
    for i in range(0, len(reportData)):
        for j in range(i+1, len(reportData)):
            for k in range(j+1, len(reportData)):
                if reportData[i] + reportData[j] + reportData[k] == 2020:
                    values["first"]  = reportData[i]
                    values["second"] = reportData[j]
                    values["third"]  = reportData[k]
                    values["answer"] = values["first"] * values["second"] * values["third"]
                    break
                else:
                    continue

    if values["answer"] > 0:
        print(f"Sum 2020 found with values {values['first']}, {values['second']} and {values['third']}.")
        print(f"Final value was {values['answer']}")
        return values["answer"]
    else:
        print("no three values with sum equal to 2020 found.")
        return 0

if __name__ == "__main__":
    expense_report_advanced("input/day1_input.txt")
    pass