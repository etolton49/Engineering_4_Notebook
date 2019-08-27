num1 = int(input("1st number:"))
num2 = int(input("2nd number:"))


def doMath(a,b,c):
    if c == 1:
        return str(a + b)
    if c == 2:
        return str(a - b)
    if c == 3:
        return str(a * b)
    if c == 4:
        return str(round(a / b, 1))
    if c == 5:
        return str(a % b)

print("Sum:\t\t" + doMath(num1, num2, 1))
print("Difference:\t" + doMath(num1, num2, 2))
print("Product:\t" + doMath(num1, num2, 3))
print("Quotient:\t" + doMath(num1, num2, 4))
print("Modulo:\t\t" + doMath(num1, num2, 5))
