n = int(input("Enter n = "))
if n < 2:
    print("wrong")
else:
    at = 2
    for i in range(2, n + 1):
        ahh = at + 2 * i + 1
        at = ahh
    print("ahh =", ahh)