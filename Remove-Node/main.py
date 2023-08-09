class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def removeNthFromEnd(self):
        print(self.val)

    def yazdir(self):
        temp = head
        list = []
        while temp != None:
            print(temp.val)
            list.append(temp.val)
            temp = temp.next
        print(list)

    def elemanEkle(self, eklenecekVeri):
        eklenecekDugum = ListNode(eklenecekVeri)
        eklenecekDugum.next = None
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = eklenecekDugum

    def elemanCikar(self, veri):
        temp = head

    def fonc(self, n):
        sayac = 0
        temp = head

        if temp.next == None:
            return None

        while temp != None:

            temp = temp.next
            sayac = sayac + 1
        temp = head

        if sayac - n == 0:
            temp = head.next
            list = []
            while temp != None:
                list.append(temp.val)
                temp = temp.next
            return print(list)

        for num in range(sayac-n):
            print("num", num)
            temp = temp.next

        if temp.next != None:
            temp.next = temp.next.next
        temp = head
        return self.yazdir()
"""
leetcode solution

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sayac = 0
        temp = head
        if temp.next == None: 
            return None 
        while temp != None:
            temp = temp.next
            sayac = sayac + 1
        temp = head
        if sayac - n == 0:
            temp = head.next
            while temp != None:   
                return temp
        for num in range(sayac-n-1):           
            temp = temp.next
        temp.next = temp.next.next
        temp = head
        return temp
        
"""

head = ListNode(1)
head.elemanEkle(2)
head.elemanEkle(3)
head.elemanEkle(4)
head.elemanEkle(5)

head.fonc(3)
