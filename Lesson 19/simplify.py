def refactor(expression):
    symbols = "xy"
    result = ""
    for i in range(len(expression)):
        if expression[i] in symbols:
            result += "*"
        result += expression[i]
    return result
