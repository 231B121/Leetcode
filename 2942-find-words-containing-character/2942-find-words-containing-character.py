class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i, w in enumerate(words):
            if w.count(x):
                res.append(i)
        return res