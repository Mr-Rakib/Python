try:
    firstValue = int(input("Enter first number: "))
    secondValue = int(input("Enter second number: "))

    value = firstValue/secondValue
    print(value)

except Exception as e:
    print("error:", e)
