def function_1():
    print("This is a message from function 1")


def function_with_params(param1):
    print(str(param1) + " has been passed to this function")


def function_with_return(val):
    temp = val + 5
    return temp


def concat_strings(string1, string2):
    return string1 + " " + string2


def multiply(val1, val2):
    return val1*val2


if __name__ == '__main__':
    function_1()
    function_with_params("Temp value")
    temp = function_with_return(function_with_return(6))
    print(concat_strings("Hello", "World"))
    print(multiply(5,6))