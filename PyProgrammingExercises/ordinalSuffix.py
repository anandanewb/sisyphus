def ordinalSuffix(aNum):
    num_str = str(aNum)
    remainder2digit = aNum % 100
    remainder1digit = aNum % 10
    if remainder2digit in (11, 12, 13):
        return f"{num_str}th"
    elif (remainder1digit == 1 ):
        return f"{num_str}st"
    elif (remainder1digit == 2):
        return f"{num_str}nd"
    elif (remainder1digit == 3):
        return f"{num_str}rd"
    else:
        return f"{num_str}th"
    


print(ordinalSuffix(1))  # Output: 1st
print(ordinalSuffix(2))  # Output: 2nd
print(ordinalSuffix(3))  # Output: 3rd
print(ordinalSuffix(4))  # Output: 4th
print(ordinalSuffix(11))  # Output: 11th
print(ordinalSuffix(12))  # Output: 12th
print(ordinalSuffix(13))  # Output: 13th
print(ordinalSuffix(121))  # Output: 21st
print(ordinalSuffix(122))  # Output: 22nd
print(ordinalSuffix(123))  # Output: 23rd
print(ordinalSuffix(124))  # Output: 23rd