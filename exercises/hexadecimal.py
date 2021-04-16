
def string_to_hex():
    n = int(input("Enter a number: "))

    if n == pow(2, -31):
        raise Exception("Not a valid number.")

    if n == pow(2, 31):
        raise Exception("Not a valid number.")
    return hex(n)


print(string_to_hex())
