# Input
num = int(input("Enter a number greater than or equal to 10: "))

if num >= 10:
    _set = set()        # empty set
    while num != 0:
        _set.add(num%10)
        num = int(num/10)
    print("Set: ", _set)
else:
    print("Oops! Number is less than 10")