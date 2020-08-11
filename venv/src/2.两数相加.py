# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(self, l1, l2):
    p = result = ListNode(-1)
    temp = 0
    while l1 and l2:  # 当l1和l2属于同长度部分
        sum = l1.val + l2.val + temp
        temp = int(sum / 10)
        ptemp = ListNode(sum % 10)
        p.next = ptemp

        p = p.next
        l1 = l1.next
        l2 = l2.next

    temp1 = l1 or l2
    while temp1:  # 当l1和l2属于不同长度部分
        sum = temp1.val + temp
        temp = int(sum / 10)
        ptemp = ListNode(sum % 10)
        p.next = ptemp

        p = p.next
        temp1 = temp1.next
    if temp:
        p.next = ListNode(temp)
    return result.next
