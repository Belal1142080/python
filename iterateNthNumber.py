list = [1, 4, 7, 2, 3, 0, 6]
sum = 0
len = len(list)
while sum < len:
    if sum == 0:
        print(list[sum])
    else:
        print(list[sum]+list[sum-1])
    sum = sum + 1
