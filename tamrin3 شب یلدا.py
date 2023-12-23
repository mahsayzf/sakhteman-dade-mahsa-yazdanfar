def dequeue(self,i):
    if self.num==0:
        raise Exception("queue empty")
    
    if i<0 or i>=self.num:
        raise IndexError("index out of bounds")
    index=(self.first+i) % self.max_size
    item=self.Q[index]

    return item