# Stack span problem
# Input: N = 7, price[] = [100 80 60 70 60 75 85]
# Output: 1 1 1 2 1 4 6
# Explanation: Traversing the given input span for 100 will be 1, 80 is smaller than 100 so the span is 1, 60 is smaller than 80 so the span is 1, 70 is greater than 60 so the span is 2 and so on. Hence the output will be 1 1 1 2 1 4 6.

# Input: N = 6, price[] = [10 4 5 90 120 80]
# Output:1 1 2 4 5 1
# Explanation: Traversing the given input span for 10 will be 1, 4 is smaller than 10 so the span will be 1, 5 is greater than 4 so the span will be 2 and so on. Hence, the output will be 1 1 2 4 5 1.
def next_greater_left(arr):
    n = len(arr)
    ans = [-1]*n
    stack = []
    for i in range(n):
        while len(stack) and arr[stack[-1]] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = -1
        if len(stack) > 0:
            ans[i] = stack[-1]
        stack.append(i)
    return ans
def stack_span(price):
    n = len(price)
    output = [-1]*n
    ngl = next_greater_left(price)
    for i in range(n):
        output[i] = i - ngl[i]
        print("i - ngl[i] => ","i = ",i,"ngl[i] = ",ngl[i], i - ngl[i])
    return output

print(stack_span([100,80,60,70,60,75,85]))
print(stack_span([10,4,5,90,120,80]))

