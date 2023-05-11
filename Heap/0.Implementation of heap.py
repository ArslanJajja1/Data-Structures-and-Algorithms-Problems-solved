# Implement heap


# Start at index 1 ,  for maths to work
# Left child =>  2*i
# Right child => 2*i+1
# Parent => i//2
# All these properties will work because we have a complete binary tree

class Heap:
    def __init__(self) -> None:
        self.heap = [0]
    def push(self,val):
        self.heap.append(val)
        i = len(self.heap)-1

        # Percolate up
        while self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            i = i//2
    # TC : O(LOGN)
    # SC : O(1)
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        while i*2 < len(self.heap):
            if (2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i]>self.heap[2*i+1]):
                temp = self.heap[2*i+1]
                self.heap[2*i+1] = self.heap[i]
                self.heap[i] = temp
            elif self.heap[i] > self.heap[2*i]:
                temp = self.heap[2*i]
                self.heap[2*i] = self.heap[i]
                self.heap[i] = temp
            else:
                break
        return res
    # TC : O(LOGN)
    # SC : O(1)

    def heapify(self,arr):
        arr.append(arr[0])
        self.heap = arr
        curr = (len(self.heap)-1)//2
        while curr > 0:
            i = curr
            while 2*i < len(self.heap):
                if (2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]):
                    temp = self.heap[2*i+1]
                    self.heap[2*i+1] = self.heap[i]
                    self.heap[i] = temp
                    i = 2*i+1
                elif self.heap[i] > self.heap[2*i]:
                    temp = self.heap[2*i]
                    self.heap[2*i] = self.heap[i]
                    self.heap[i] = temp
                    i = 2*i
                else:
                    break
            curr -= 1
    # TC : O(N)
    # SC : O(1)




