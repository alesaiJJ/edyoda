first = 0
second = 1
total = 1
while True:
    if total <=50:
        print(total)
    total = first + second
    first = second
    second = total
