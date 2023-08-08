def function():
    inp = float(input("Float value?"))
    print(inp)

def function_WithArgument(i):
    return i

def function_WithMoreArgument(j,k,l):
    result = j + k + l
    return result

def function_condition():
    for x in range(10):
        print(x)

function()
print(function_WithArgument(5))
print(function_WithMoreArgument(1,2,3))
function_condition()
