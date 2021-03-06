class BinarySearch():
    def __init__(self,a,b):
        '''a is the length while b is the step of the list to be created'''
        self.array = range(b,(a*b)+1,b)
        self.length = len(self.array)

    def __getitem__(self,index):
        return self.array[index]

    def search(self, val):
        count = 0
        first = 0
        last = len(self.array) - 1
        
        while True:
            if val == self.array[first]:
                return {'index': first, 'count': count}
            elif val == self.array[last]:
                return {'index': last, 'count':count}

            mid = (first + last)//2
            
            if val == self.array[mid]:
                return {'index':mid, 'count': count}
            
            elif val > self.array[mid]:
                first = mid+1
                
            elif val < self.array[mid]:
                last = mid -1
                
            if first >= last:
                return {'index':-1, 'count':count}

            count += 1