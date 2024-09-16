class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size + n >self.capacity:
            raise ValueError("exceeded the capacity")
        self.size+=n


    def withdraw(self, n):
        if n>self.size:
            raise ValueError("Not enough to withdraw")
        self.size-=n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise ValueError("capacity Error")
        self._capacity=capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size>self.capacity:
            raise ValueError("size Error")
        self._size=size

def main():
    jar=Jar()
    print(jar.capacity)
    jar.deposit(2)
    print(jar)
    jar.deposit(2)
    print(jar)
    jar.withdraw(1)
    print(jar)

if __name__=="__main__":
    main()
