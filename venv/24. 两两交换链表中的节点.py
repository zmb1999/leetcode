# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #新建2个引用指向一个节点，并将这个节点的next指向head，用以记录初始节点
        pre = temp = ListNode()
        pre.next = head
        while temp.next and temp.next.next:
            #分别拿3个引用指向这三个节点
            a = temp.next
            b = temp.next.next
            c = temp.next.next.next
            #然后改变这三个节点之间的指向关系，原本是->a->b->c，改成了->b->a->c
            temp.next = b
            b.next = a
            a.next = c
            #改变次序后，将temp往后传递两位
            temp = temp.next.next
        #最后返回初始节点
        return pre.next
