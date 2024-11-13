class MinHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
    def get_min(self):
        return self.heap[0] if self.heap else None
    def remove_min(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    def heapify_up(self,index):
        parent=(index-1)//2
        if index>0 and self.heap[parent]>self.heap[index]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapify_up(parent)
    def heapify_down(self,index):
        smallest=index
        left=2*index+1
        right=2*index+2
        if left<len(self.heap) and self.heap[smallest]>self.heap[left]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapify_down(smallest)
    def build_heap(self,array):
        self.heap=array[:]
        n=len(self.heap)
        for i in range((n//2)-1,-1,-1):
            self.heapify_down(i)
heap=MinHeap()
heap.build_heap([3,2,1,6,5,4,3,8])
print("Min value:",heap.get_min())
heap.insert(0)
print("Min value after insertion:",heap.get_min())
heap.remove_min()
print("Min value after removal:",heap.get_min())


            


