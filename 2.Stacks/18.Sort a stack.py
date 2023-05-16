# Given a stack of integers, sort it in ascending order using another temporary stack.

# Examples: 

# Input : [34, 3, 31, 98, 92, 23]
# Output : [3, 23, 31, 34, 92, 98]

# Input : [3, 5, 1, 4, 2, 8]
# Output : [1, 2, 3, 4, 5, 8]
# Sort iteratively
def sort_stack(stack):
    temp_stack = []
    while len(stack) > 0 :
        temp = stack.pop()
        while len(temp_stack) > 0 and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack
print(sort_stack([34, 3, 31, 98, 92, 23]))
print(sort_stack([3, 5, 1, 4, 2, 8]))

# Sort Recursively
def sort(stack):
    if len(stack) == 1:
        return
    temp = stack.pop()
    sort(stack)
    insert(stack,temp)
    return stack

def insert(st,temp):
    if len(st) == 0 or st[-1] < temp:
        st.append(temp )
        return
    val = st.pop()
    insert(st,temp)
    st.append(val)
    return
    

print(sort([34, 3, 31, 98, 92, 23]))
print(sort([3, 5, 1, 4, 2, 8]))
