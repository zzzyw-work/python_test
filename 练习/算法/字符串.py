"""验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。"""

"""
正则表达式的使用
 
函数	说明
sub(pattern,repl,string)	把字符串中的所有匹配表达式pattern中的地方替换成repl
[^**]	表示不匹配此字符集中的任何一个字符
\u4e00-\u9fa5	汉字的unicode范围
\u0030-\u0039	数字的unicode范围
\u0041-\u005a	大写字母unicode范围
\u0061-\u007a	
小写字母unicode范围

\uAC00-\uD7AF	韩文的unicode范围
\u3040-\u31FF	日文的unicode范围
"""

# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         tmp = re.sub(r"[^A-Z0-9a-z]", '', s).upper()
#         l = len(tmp)
#         if l <= 1 :
#             return(True)
#         for i in range(int(l/2)):
#             if(tmp[i] != tmp[-i-1]):
#                 return(False)
#         return(True)





"""
分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案
先将原字符串分割成左右两个部分，然后不管左边的字符串，将右边的字符串进行递归操作。但是在对右边的字符串
进行递归操作之前,需要验证左边的左边的字符串是回文串，然后将左边的字符串和右边字符串的递归结果，进行组合，返回最后结果。
"""

# class Solution:
#     def partition(self, s) :
#         res = []
#         if s == "":
#             return [[]]
#         if len(s) == 1:
#             return [[s]]
#         strLenth = len(s)
#         for i in range(1,strLenth+1):
#             leftres = s[:i]  # 以aab为例，左字符串分别为a，aa，aab
#             right = s[i:]
#             if self.isPalindrome(leftres):
#                 rightres = self.partition(right)
#                 for i in rightres:
#                     res.append([leftres]+i)
#         return res
#     def isPalindrome(self,s):   # 判断是不是回文数
#         i = 0
#         j = len(s)-1
#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True







"""
单词拆分
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions/xa503c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

dp[i]表示到第i-1个字符时，是否为能被拆分为字典里的单词
状态转移矩阵：
dp[j] = dp[i] and s[i:j+1] in wordDict
"""


# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         n = len(s)
#         dp = [True] + [False] * n
#         print(dp)
#         for i in range(n):
#             if dp[i]:
#                 for j in range(i, n):
#                     if s[i:j+1] in wordDict:
#                         dp[j+1] =True
#         return dp[-1]



"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入:
s = “catsanddog”
wordDict = [“cat”, “cats”, “and”, “sand”, “dog”]
输出:
[
“cats and dog”,
“cat sand dog”
]

示例 2：
输入:
s = “pineapplepenapple”
wordDict = [“apple”, “pen”, “applepen”, “pine”, “pineapple”]
输出:
[
“pine apple pen apple”,
“pineapple pen apple”,
“pine applepen apple”
]
解释: 注意你可以重复使用字典中的单词。
示例 3：
输入:
s = “catsandog”
wordDict = [“cats”, “dog”, “sand”, “and”, “cat”]
输出:
[]
2.
 思路1:
 

先判断能不能拆分，如果能拆分的话，先根据wordDict中的单词长度，从前往后分割，
然后进行匹配，如果匹配上wordDict里的单词，对剩下的进行递归。直到len(s)==0,
说明s都已经匹配完了。由于可能有不同的分割结果，每一个不同的分割结果只需要记录
一次，因此需要对wordDict里的单词长度进行去重。


"""


# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         res = []
#         if len(s) == 0 or not wordDict:
#             return []
#         wordLenList = [len(word) for word in wordDict]
#         wordLenSet = set(wordLenList)
#         if self.judge(s, wordDict):
#             self.dfs(s, wordDict, [], res, wordLenSet)
#         return res
#
#     def judge(self, s, wordDict):  # 先判断能不能分割
#         lenth = len(s)
#         dp = [False for i in range(lenth + 1)]
#         dp[0] = True
#         for i in range(1, lenth + 1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#                     break
#         return dp[-1]
#
#     def dfs(self, s, wordDict, curResult, res, wordLenSet):
#         if len(s) == 0:  # 递归终止条件
#             res.append(" ".join(curResult))
#             return
#         else:
#             for i in wordLenSet:  # 进行回溯
#                 if i <= len(s):
#                     if s[:i] in wordDict:
#                         self.dfs(s[i:], wordDict, curResult + [s[:i]], res, wordLenSet)
#             return


#思路2：
# 递归 + 构建额外字典保存切分结果
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         res = []
#         memo = dict()
#         return self.dfs(s, res, wordDict, memo)
#
#     def dfs(self, s, res, wordDict, memo):
#         # 如果当前单词存在于字典中，直接返回
#         if s in memo:
#             return memo[s]
#         # 当前字符串的为空判断
#         if not s:
#             return [""]
#
#         # 拼接存在于字典中的字符串
#         res = []
#         for word in wordDict:
#             if s[:len(word)] != word:
#                 continue
#             for r in self.dfs(s[len(word):], res, wordDict, memo):
#                 res.append(word + ("" if not r else " " + r))
#         memo[s] = res
#         print(s)
#         print(memo[s])
#         return res


#解法2
"""
先判断能不能拆分，如果能拆分的话，先根据wordDict中的单词长度，从前往后分
割，然后进行匹配，如果匹配上wordDict里的单词，对剩下的进行递归。直
到len(s)==0,说明s都已经匹配完了。由于可能有不同的分割结果，每一个不
同的分割结果只需要记录一次，因此需要对wordDict里的单词长度进行去重。
"""
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         res = []
#         if len(s) == 0 or not wordDict:
#             return []
#         wordLenList = [len(word) for word in wordDict]
#
#         wordLenSet = set(wordLenList)
#         if self.judge(s, wordDict):
#             self.dfs(s, wordDict, [], res, wordLenSet)
#         return res
#
#     def judge(self, s, wordDict):  # 先判断能不能分割
#         lenth = len(s)
#         dp = [False for i in range(lenth + 1)]
#         print(dp)
#         dp[0] = True
#         for i in range(1, lenth + 1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#                     break
#         return dp[-1]
#
#     def dfs(self, s, wordDict, curResult, res, wordLenSet):
#         if len(s) == 0:  # 递归终止条件
#             res.append(" ".join(curResult))
#             return
#         else:
#             for i in wordLenSet:
#                 print(i)
#                 # 进行回溯
#                 if i <= len(s):
#                     if s[:i] in wordDict:
#                         print(s[:i])
#                         self.dfs(s[i:], wordDict, curResult + [s[:i]], res, wordLenSet)
#             return


"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

trie树，即字典树，又称单词查找树或键树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计
和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：最大
限度地减少无谓的字符串比较，查询效率比哈希表高。” 

因为限定都是由a-z小写字母构成，所以这棵树是一棵26叉树。前缀树的构造过程，通过不断插入新的字符串来
丰富这棵26叉树。前缀树的功能很强大，可以做文本词频统计，例如我们在搜索框中的搜索提示，就可以利用前缀
树实现。因此，前缀树基本的操作是字符串的插入insert，搜索search，删除delete，查找前缀startsWith等。
https://blog.csdn.net/weixin_42077402/article/details/98174130
"""


# class Trie(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = {}
#
#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         node = self.root
#         for char in word:
#             node = node.setdefault(char, {})
#             print(node)
#         node["end"] = True
#
#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         node = self.root
#         for char in word:
#             if char not in node:
#                 return False
#             node = node[char]
#             print(node)
#         return "end" in node
#
#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         node = self.root
#         for char in prefix:
#             if char not in node:
#                 return False
#             node = node[char]
#         return True















"""
反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
# class Solution:
#     def reverseString(self, s) :
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         l = len(s)
#         for i in range(int(l/2)):
#             tmpChar = s[i]
#             s[i] = s[-i-1]
#             s[-i-1] = tmpChar
#         return s


"""
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

"""


"""高级做法 
#find（）找到字符第一次出现的索引，rfind（）找到字符最后一次出现的索引，如果
# 这两个值相等且不等于-1说明该字符只出现一次，将所有只出现一次的字母
# 索引放入列表中，返回其中的最小值
"""

# class Solution:
#     def firstUniqChar(self, s):
#         tmp = s
#         tmp = [tmp.find(i) for i in s if tmp.find(i) == tmp.rfind(i) and tmp.find(i) != -1]
#         if tmp:
#             return min(tmp)
#         else:
#             return -1

"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
"""
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(t) != len(s):
#             return False
#         c = set(t)
#         for i in c:
#             if t.count(i) != s.count(i):
#                 return False
#         return True


#用排序方法，但性能不太好
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         return sorted(s)==sorted(t)


