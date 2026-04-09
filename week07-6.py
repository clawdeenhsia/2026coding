#week07-6.py
#leetcode 649
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        print(senate, type(senate))
        print(list(senate), type(list(senate)))

        queue = deque(list(senate))
        print(queue,type(queue))

        banR, banD = 0, 0
        R,D = senate.count('R'), senate.count('D')
        while queue:
            now = queue.popleft()
            if now=='R':
                if banR>0:
                    banR -= 1
                    R -= 1
                    continue
                else:
                    banD += 1
                    queue.append(now)
            else:
                if banD>0:
                    banD -= 1
                    D -= 1
                    continue
                else:
                    banR += 1
                    queue.append(now)
            print('R',R,'D',D,list(queue))

            if R==0: return 'Dire'
            if D==0: return 'Radiant'


        queue = deque(list(senate))
        counter = Counter(senate)
        R, D = counter['R'], counter['D']
        banR = banD = 0
