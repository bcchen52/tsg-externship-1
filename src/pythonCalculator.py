from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def basicCalculator(operation, num1, num2):
    result = 0

    if operation == ADD:
        result = num1 + num2
    elif Operation.SUBTRACT:
        result = num1 - num2
    elif Operation.MULTIPLY:
        result = num1 * num2
    else:
        if num2 == 0:
                print("Can't divide by 0")
        else:
            result = num1 / num2
    return result


if __name__ == "__main__":
    print(basicCalculator(Operation.DIVIDE, 1, 2))

