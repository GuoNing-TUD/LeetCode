#给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.l2 = l2
        self.l1 = l1
        headnode = ListNode(0)
        endnode = headnode
        # print(endnode.val)
        vorendnode=endnode
        while self.l2 or self.l1:
            temp = (self.l1.val if self.l1 else 0) + (self.l2.val if self.l2 else 0)
            # print(temp)
            carry, sum = divmod(temp, 10)  # carry为0或1
            # print(sum,carry)
            endnode.val = endnode.val + sum  # endnode的next还不存在，需要ListNode生成
            if (endnode.val!=10) :
                endnode.next = ListNode(carry)
                #print(carry,endnode.val)
            else:
                endnode.val = 0
                endnode.next = ListNode(1)
                #print(carry,endnode.val)
            self.l1 = self.l1.next if self.l1 else None
            self.l2 = self.l2.next if self.l2 else None
            # print(endnode.val,endnode)
            vorendnode = endnode
            endnode = endnode.next
        if endnode.val == 0:
            vorendnode.next = None
        return headnode

    def generateList(self, l: list):
        self.l = l
        headnode = ListNode(0)
        endnode = headnode
        for node in self.l:
            endnode.next = ListNode(node)
            endnode = endnode.next
        headnode = headnode.next
        return headnode

l1=[0,0,4,1,2]
l2=[9,1,2,3]
s = Solution()  # 实例化
e1 = s.generateList(l1)
e2 = s.generateList(l2)

s.addTwoNumbers(e1, e2)

rel=s.addTwoNumbers(e1, e2)#7,6,8,8,0,2
while rel:
     print(rel.val)
     rel=rel.next
