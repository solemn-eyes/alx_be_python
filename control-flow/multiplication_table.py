number = input("Enter a number to see its multiplication table: ")

for i in range(1, 11):
    result = int(number) * i
    print(f"{number} * {i} = {result}")

    