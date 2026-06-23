# Maximum Number of Words Found in Sentences
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        test = []
        for x in range(len(sentences)):
            test.append(len(sentences[x].split(" ")))
        return max(test)
