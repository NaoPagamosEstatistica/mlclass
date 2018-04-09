arr = []
while (True):
    try:
        arr += [int(float(input()))]
    except EOFError as e:
        break
print(arr)

