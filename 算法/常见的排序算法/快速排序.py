"""
快速排序
算法思想

快速排序由 C. A. R. Hoare 在1962年提出。它的基本思想是：通过一趟排
序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的
所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过
程可以递归进行，以此达到整个数据变成有序序列。
算法步骤

从数列中挑出一个元素，称为"基准"（pivot）。
重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在
基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的
中间位置。这个称为分区（partition）操作。
递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""