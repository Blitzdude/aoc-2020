
'''
expense_report takes an list of integer values
as data. It finds two values in that list that
add to 2020 and multiplies them together.
Then it returns the value
'''
def expense_report(reportData):
    if (reportData == None):
        raise TypeError("data is empty or not defined")
    if (type(reportData) != list):
        raise TypeError("input value is not a list")
    if (len(reportData) <= 1):
        raise AssertionError("List must have more than 1 value")

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
        print("Sum 2020 found with values %d and %d.", firstValue, secondValue)
        print("Final value was %d", valueFound)
        return valueFound
    else:
        print("no two values with sum equal to 2020 found.")
        return -1

def read_file(filename):
    print("Reading file %s", filename)
    with open(filename) as fileObject:
        while fileObject:
            pass


if __name__ == "__main__":
    puzzleInput = []
    expense_report([1010, 1010])
    pass