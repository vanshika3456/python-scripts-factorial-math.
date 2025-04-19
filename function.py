#task1
#Calculate Factorial Using a Function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n=factorial(6)
print("the factorial of6 is:",n)