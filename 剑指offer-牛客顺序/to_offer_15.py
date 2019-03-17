# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'输入一个链表，反转链表后，输出新链表的表头。'
"""解题思路：注意反转时出现断裂现象，定义3个指针，分别指向当前遍历到的节点pNode、它的前一个节点pPrev及后一个节点pNext。"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        preversedhead = None # 反转后的头结点
        pNode = pHead   # 当前结点
        pPre = None     # 当前结点的前一个结点
        while pNode:
            pNext = pNode.next  # 当前结点的后一个结点
            if not pNext:
                preversedhead = pNode
            pNode.next = pPre
            pPre = pNode
            pNode = pNext
        return preversedhead


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead): # 更简洁的写法
        # write code here
        pNode = pHead   # 当前结点
        pPre = None     # 当前结点的前一个结点
        while pNode:
            pNext = pNode.next  # 当前结点的后一个结点,保存一下
            pNode.next = pPre
            pPre = pNode
            pNode = pNext
        return pPre


# 注意关于链表问题的常见注意点的思考：
# 1、如果输入的头结点是NULL，或者整个链表只有一个结点的时候
# 2、链表断裂的考虑
    """
# 递归的方法其实是非常巧的，它利用递归走到链表的末端，然后再更新每一个node的next 值 ，实现链表的反转。而newhead 的值没有发生改变，为该链表的最后一个结点，所以，反转后，我们可以得到新链表的head.
    def ReverseList(self, pHead):  # 方法三：递归实现！
        # 如果链表为空或者链表中只有一个元素
        if not pHead or not pHead.next:
            return pHead
        else:
            # 先反转后面的链表，走到链表的末端结点
            pReversedHead = self.ReverseList(pHead.next)
            # 再将当前节点设置为后面节点的后续节点  3->4 变成 3<-4
            pHead.next.next = pHead
            pHead.next = None
            return pReversedHead
    """
# 参考链接
"""
链接：https://www.nowcoder.com/questionTerminal/75e878df47f24fdc9dc3e400ec6058ca
来源：牛客网

public class Solution {
    public ListNode ReverseList(ListNode head) {
       
        if(head==null)
            return null;
        //head为当前节点，如果当前节点为空的话，那就什么也不做，直接返回null；
        ListNode pre = null;
        ListNode next = null;
        //当前节点是head，pre为当前节点的前一节点，next为当前节点的下一节点
        //需要pre和next的目的是让当前节点从pre->head->next1->next2变成pre<-head next1->next2
        //即pre让节点可以反转所指方向，但反转之后如果不用next节点保存next1节点的话，此单链表就此断开了
        //所以需要用到pre和next两个节点
        //1->2->3->4->5
        //1<-2<-3 4->5
        while(head!=null){
            //做循环，如果当前节点不为空的话，始终执行此循环，此循环的目的就是让当前节点从指向next到指向pre
            //如此就可以做到反转链表的效果
            //先用next保存head的下一个节点的信息，保证单链表不会因为失去head节点的原next节点而就此断裂
            next = head.next;
            //保存完next，就可以让head从指向next变成指向pre了，代码如下
            head.next = pre;
            //head指向pre后，就继续依次反转下一个节点
            //让pre，head，next依次向后移动一个节点，继续下一次的指针反转
            pre = head;
            head = next;
        }
        //如果head为null的时候，pre就为最后一个节点了，但是链表已经反转完毕，pre就是反转后链表的第一个节点
        //直接输出pre就是我们想要得到的反转后的链表
        return pre;
    }
"""