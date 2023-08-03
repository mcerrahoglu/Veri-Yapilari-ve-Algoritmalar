from queue import Queue

class MyStack():

    def __init__(self):
        self.elements = Queue()

    def empty(self):
        self.elements.empty()

    def push(self, element):
        self.elements.put(element)

    def top(self):
        return self.elements.queue[-1]

    def pop(self):
        last = self.elements.queue[-1]
        for i in range(self.elements.qsize()):
            deger = self.elements.get()
            if deger != last:
                self.push(deger)

    def yazdir(self):
        print(self.elements.queue)


veri = MyStack()

veri.push(10)
veri.push(20)
veri.push(30)
veri.yazdir()
veri.pop()
veri.yazdir()
