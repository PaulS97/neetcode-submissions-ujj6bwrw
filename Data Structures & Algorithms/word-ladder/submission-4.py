class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        all_word = [beginWord] + wordList

        adjList = [[] for i in range(len(all_word))]

        wordlen = len(beginWord)

        for i in range(len(all_word)):
            for j in range(i+1, len(all_word)):
                word1 = all_word[i]
                word2 = all_word[j]
                sim = 0

                for k in range(wordlen):
                    if word1[k] == word2[k]:
                        sim+=1

                if sim + 1 == wordlen:
                    adjList[i].append(j)
                    adjList[j].append(i)

        seen = set()
        next = deque([0])
        steps = 0
        target = -1
        for i, val in enumerate(all_word):
            if val==endWord:
                target = i
                break

        if target==-1:
            return 0
        #print("target:", target)
        #for i in range(len(all_word)):
           # print(adjList[i])

        while(next):
            steps += 1
            #if steps<10:
                #print("steps:", steps)
                #print("next:", next)
            #else:
              #  break
            for i in range(len(next)):
                j = next.popleft()
                seen.add(j)
                if j==target:
                    return steps
                #print("j:", j)
                for connect in adjList[j]:
                    #print(connect)
                    if connect not in seen:
                        next.append(connect)

        return 0



        