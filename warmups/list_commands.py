N = int(input())
arr = []

for _ in range(N):
    parts = input().split()

    if parts[0] == "append":
        arr.append(int(parts[1]))

    elif parts[0] == "insert":
        arr.insert(int(parts[1]), int(parts[2]))

    elif parts[0] == "remove":
        arr.remove(int(parts[1]))

    elif parts[0] == "pop":
        arr.pop()

    elif parts[0] == "sort":
        arr.sort()

    elif parts[0] == "reverse":
        arr.reverse()

    elif parts[0] == "print":
        print(arr)
