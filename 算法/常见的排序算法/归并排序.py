"""
归并排序
算法思想

归并排序是一种递归算法，它持续地将一个列表分成两半。如果列表是空的或者 只有一个元素，
那么根据定义，它就被排序好了（最基本的情况）。如果列表里的元素超过一个，我们就把列表
拆分，然后分别对两个部分调用递归排序。一旦这两个部分被排序好了，然后就可以对这两部分
数列进行归并了。归并是这样一个过程：把两个排序好了的列表结合在一起组合成一个单一的有
序的新列表。有自顶向下（递归法）和自底向上的两种实现方法。
"""