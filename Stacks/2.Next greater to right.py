def NGR1(arr):
    n = len(arr)
    output = [None]*n
    stack = []
    for i in range(n-1,-1,-1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            output[i] = -1
        if stack and stack[-1] > arr[i]:
            output[i] = stack[-1]
        stack.append(arr[i])
    return output

print(NGR1([3,5,7,4,8,9,2,6]))