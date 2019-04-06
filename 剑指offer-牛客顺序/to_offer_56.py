# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author: lvxiing
date: 2019/4/4 10:44
'''
"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

"""
解题思路一：将链表元素保存在列表中，然后过滤掉出现次数大于1的值，只保留出现次数为1的值，再将新的列表建成链表的形式。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next
        res = list(filter(lambda x: res.count(x) == 1, res))
        newList = ListNode(0)
        pre = newList
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return newList.next


"""解题思路二：运用链表的操作，确保将重复的节点略过，始终连接不重复的值。"""


class Solution1:
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(-1)
        first.next = pHead
        last = first
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and pHead.val == val:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next
        return first.next


# 测试:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
s = Solution()
print(s.deleteDuplication(node1).val)
print(s.deleteDuplication(node1).next.val)
print(s.deleteDuplication(node1).next.next.val)
print('--------------------------------------')
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
s1 = Solution1()
print(s1.deleteDuplication(node1).val)
print(s1.deleteDuplication(node1).next.val)
print(s1.deleteDuplication(node1).next.next.val)
print('--------------------------------------')

print('=======================================================================')

# 拓展:
"""
题目：
删除链表中的节点(剑指offer-18题)
题一：
在O(1)时间内删除链表节点。给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
解题思路：
我们要删除节点i,先把i的下一个节点j的内容复制到i,然后把i的指针指向节点j的下一个节点。此时再删除节点j,其效果等同于把节点i删除了。
"""


"""此程序还存在问题，删除的结点被删除后不为None！"""


class ListNode1:
    def __init__(self, x):
        self.value = x
        self.next_node = None
class Solution2:
    def delete_node(self,head_node,del_node):
        """
        删除指定节点
        """
        if not (head_node and del_node):
            return None
        # 要删除的节点不是尾节点
        if del_node.next_node:
            del_next_node = del_node.next_node
            del_node.value = del_next_node.value
            del_node.next_node = del_next_node.next_node
            del_next_node.value = None
            del_next_node.next_node = None
        # 链表只要一个节点，删除头节点（也是尾节点）
        elif del_node == head_node:
            head_node.next_node = None
            head_node.value = None
            del_node.next_node = None
            del_node.value = None
        # 链表中有多个节点，删除尾节点
        else:
            node = head_node
            while node.next_node != del_node:
                node = node.next_node
            node.next_node = None
            del_node.next_node = None
            del_node.value = None

        return head_node

# 测试:
node1 = ListNode1(10)
node2 = ListNode1(11)
node3 = ListNode1(13)
node4 = ListNode1(15)
node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

S = Solution2()
# S.delete_node(node1, node3)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print('------------------')
# S.delete_node(node1, node2)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print('------------------')
# S.delete_node(node1, node1)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print('------------------')
# S.delete_node(node1, node1)
# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# print(node1 == None)
# print('------------------')
S.delete_node(node1, node4)
print(node1.value)
print(node2.value)
print(node3.value)
print(node4.value)
print(node4 == None)   # 这里是问题点!
print('------------------')
