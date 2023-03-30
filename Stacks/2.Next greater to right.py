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

def NGR2(arr):
    n = len(arr)
    output = [-1]*n
    stack = []
    for i in range(0,n*2-1):
        while stack and arr[stack[-1]] < arr[i%n]:
            output[stack.pop()] = arr[i%n]
        stack.append(i%n)
    return output

print(NGR2([3,5,7,4,8,9,2,6]))