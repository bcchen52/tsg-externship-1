from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def basicCalculator(operation, num1, num2):
    result = 0
    match operation:
        case Operation.ADD:
            print(&quot;this workshop sucks&quot;)
            result = num1 + num2
        case Operation.SUBTRACT:
            print(&quot;I hate working at this company&quot;)
            result = num1 - num2
        case Operation.MULTIPLY:
            print(&quot;My boss is the worst&quot;)
            result = num1 * num2
        case Operation.DIVIDE:
            if num2 == 0:
                print(&quot;error: u suck&quot;)
            else:
                result = num1 / num2
    return result


if __name__ == "__main__":
    print(basicCalculator(Operation.DIVIDE, 1, 2))

