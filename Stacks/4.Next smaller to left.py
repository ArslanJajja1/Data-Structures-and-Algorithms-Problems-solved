def NSL(arr):
    n = len(arr)
    output = [-1]*n
    stack = []
    for i in range(n):
        while len(stack) and stack[-1] > arr[i]:
            stack.pop()
        if len(stack) == 0:
            output[i] = -1
        if len(stack) > 0:
            output[i] = stack[-1]
        stack.append(arr[i])
    return output
print(NSL([3,5,7,4,8,9,2,6]))