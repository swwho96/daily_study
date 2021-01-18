count = 0
Sum = 0
while True:
    n = input("Enter a number: ")
    if n == 'done':
        break
    try:
       n = int(n)
    except ValueError:
        print("Invalid input")
        continue

    count += 1
    Sum += n

print(Sum, count, Sum/count)