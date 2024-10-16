# PART 1 编程基础

Python 是一种**简洁但是功能强大的面向对象**的编程语言：自身拥有丰富的第三方库，另外作为一种胶水语言沟通和调用不同功能组件（比如 hive、spark；计算 cuda、C）。可以快速的上手构建项目。

本文对 Python 编程中自身属性出发，为后续理解第三方库功能奠定基础。行文思路先介绍基本数据结构和基础编程操作，引出高阶编程操作，最后使用 Leetcode 编程来详细展示代码基础能力。

快速浏览可以参考：[《菜鸟教程 - 学习 Python3.x 教程》](https://www.runoob.com/python3/python3-tutorial.html)

##  [1基础数据结构](1基础数据结构) 

在顺序存储和链式存储的基础上，Python 中存在的数据结构抽象为

- 不可变数据结构：Number（数字）、String（字符串）、Tuple（元组）
- 可变数据结构：List（列表）、Dict（字典）、Set（集合）
- 高阶的数据结构：树（Tree）、图（Graph）、队列（Collections.deque）、堆（Heapq）
- 高阶的数据对象：Datetime（日期）、Tensor（张量）、Dataframe（数据框）、ndArray（矩阵）

了解基础数据结构的好处：

- 帮助理解复杂抽象数据结构（比如 Numpy.array ,Pandas.dataframe）
-  提升自身的程序代码思维
- 体会到不可言说的 Python 简洁的开发风格

[1.1 基本数据结构](./1基础数据结构/1.1%20基本数据结构.ipynb)
[1.2 复杂数据结构](./1基础数据结构/1.2%20复杂数据结构.ipynb)
[1.3 时间日期操作](./1基础数据结构/1.3%20时间日期操作.ipynb)
[1.4 字符串处理](./1基础数据结构/1.4%20字符串处理.ipynb)
[1.5 常见小技巧](./1基础数据结构/1.5%20常见小技巧.ipynb)


##  [2基础编程操作](2基础编程操作) 

代码构造本身通常设计到和外部系统的交互，包括不同程序的消息管道、文件系统的交互、操作系统的交互等等，这些通常是不太令人喜欢的*代码实现* 环节，而不是创作型的工作，这一步需要了解到的有

- 外部文件的交互和 IO

##  [3高级编程操作](3高级编程操作) 

- 面向对象的编程方法
- 函数式编程的方法

##  [4 程序设计基础](Leetcode_template) 

**算法和数据结构**是构造复杂系统的基础，虽然语言、技术、框架会不断的变化，但是如何快速的理解和实现依靠的还是这些基于冯诺依曼框架的结构。而对于数据科学或者算法工程师来说，编译原理、计算机网络、计算机组成原理可能相关较远，但是其中的代码和程序设计原理是必然需要详细的了解，这也是刷题的核心目的。

那么如何学习数据结构和算法？非常悲剧的是数据结构和算法思想是相互耦合的，数据结构是算法操作的根基，算法思想是完成程序的流程，好的算法会带来新的数据结构，高效的数据结构带来新的算法流程，也就是会出现：数据结构 -> 算法 -> 高阶数据结构 -> 高阶算法的循环。因此在学习的过程中可以不但的更新自己的视野：

1. 基础的数据结构，包括数组、链表、栈、队列等等
2. 基础的算法思想，包括枚举法、分治法、回溯算法、贪心算法、动态规划
3. 高阶的数据结构，包括树、图、堆
4. 新的结构带来新的算法求解体系，此时需要有更深层次的理解，重点在于理解**计算机本质上是利用大规模的枚举方式来解决复杂的算法问题**，无论是数据结构还是程序设计都是为了更好的描述问题、转换问题、使得计算机可以进行求解。

写了这么多发现无从下手，但是十大排序算法其实给出了很多算法思想的思路。

- **遍历的方式**：冒泡排序（Bubble sort）、选择排序（Selection sort）、插入排序（Insertion sort）
- **递归的方式**：归并排序（Merge sort）、快速排序（Quick sort）
- **算法设计创新**：希尔排序（Shell sort）、桶排序（Bucket sort）、基数排序（Radix sort）
- **数据结构创新**：计数排序（Counting sort），堆排序（Heap）

之后再从不同的题目中获取数据结构和算法的灵感。

|                        序号 力扣链接                         |                备注说明                |
| :----------------------------------------------------------: | :------------------------------------: |
| [75 颜色分类](https://leetcode.cn/problems/sort-colors/description/) |    利用快速排序的思想来实现本地完成    |
| [Top K 算法的实现](https://juejin.cn/post/7059395546712604679) | 可以通过魔改快速排序的方式来实现计算， |
| [153 寻找旋转数组的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/submissions/571789997/) |    二分查找，注意二分查找的边界条件    |
| [264 丑数 II](https://leetcode.cn/problems/ugly-number-ii/)  |                                        |
|                                                              |                                        |
|                                                              |                                        |
|                                                              |                                        |
|                                                              |                                        |
|                                                              |                                        |



## 参考资料

 [CS 61A: Structure and Interpretation of Computer Programs](https://cs61a.org/)

[算法通关手册（Leetcode）](https://algo.itcharge.cn/)

[代码随想录](https://programmercarl.com/)

[《Python cookbook 第三版中文》](https://LTAI5tNwHtQGucyrs15ssbvo@chenxia31blog.oss-cn-hangzhou.aliyuncs.com/fileshare/《Python Cookbook》第三版中文v1.0.2.pdf)

[Python编程从入门到深入](https://pythonhowto.readthedocs.io/zh-cn/latest/index.html)