# # *!Print name 5 times
# count = 0


# def printName(name):
#     global count
#     if count == 5:
#         return
#     print(name)
#     count += 1
#     printName(name)


# printName('Arslan')
# *! Print linearly from 1 to N
# count = 0
# def print1ToN(n):
#     global count
#     if n == 0:
#         return
#     print1ToN(n-1)
#     print(n)
# print1ToN(10)
# *! Print N to 1
# def printNto1(n):
#     print(n)
#     if n == 1:
#         return
#     printNto1(n-1)
# printNto1(10)
# *! Some of first N numbers
def AddFirstNnumbers(n, sum):
    if n == 0:
        return sum
    return AddFirstNnumbers(n-1, sum+n)


print(AddFirstNnumbers(5, 0))

sum = 0


def sumNnumbers(n):
    global sum
    if n == 0:
        return sum
    sum += n
    return sumNnumbers(n-1)


print(sumNnumbers(5))
