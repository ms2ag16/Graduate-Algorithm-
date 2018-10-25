""" 
use BFS to go over the all the child node which are only 1 letter different than the current checking word.
To check if the word is only 1 letter different than the next one, 
The idea is to loopong over ascii_lowercase 26 letters, and if it's only 1 different and then we check if it is in the wordList,
if it does in the wordList, we add the nextWord into the queue, increase the count step number and from there to seach for the endWord;
if it not in the wordList, we keep checking other letters in ascii_lowercase.
Since there's no duplicate and we use one word once, so after we add the newWord to queue, we remove it from wordList
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList=set(wordList)
        if endWord not in wordList: return 0
        from collections import deque
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in xrange(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord in wordList:
                            queue.append((newWord, dist+1))
                            wordList.remove(newWord) 
        return 0   
