#Works but is slow. 
class Solution:
    def getLegalNeighbours(self,current,deadends,Visited):
        
        Neighbours = [self.Moves[val] for val in current]
        FinalViableMoves = []
        for idx, moves in enumerate(Neighbours):
            for move in moves:
                currentCopy = current.copy()
                currentCopy[idx] = move
                strVersion = "{}{}{}{}".format(*currentCopy)
                #print(strVersion)
                if strVersion not in deadends and strVersion not in Visited:
                    FinalViableMoves.append(currentCopy.copy())
        return FinalViableMoves 
    
    def openLock(self, deadends, target):
        Current = [0,0,0,0]
        Visited = []
        ToVisit = {0:[Current]}
        Count=0
        self.Moves = {key :[key-1,key+1] for key in range(10)}
        self.Moves[0][0] = 9
        self.Moves[9][1] = 0
        print(self.Moves)
        #Use HashTAble to Store Moves
        Empty = False
        while not Empty:
            
            while len(ToVisit[Count])>0:
                #print(ToVisit)
                Current=ToVisit[Count].pop(0) 
                
                CurrentStr = "{}{}{}{}".format(*Current)
                if CurrentStr==target:
                    return Count
                
                Visited.append(CurrentStr)
                if Count+1 in ToVisit:
                    ToVisit[Count+1].extend(self.getLegalNeighbours(Current,deadends,Visited))
                else:
                    ToVisit[Count+1] = self.getLegalNeighbours(Current,deadends,Visited)
                
            Count+=1
            Empty =all([len(ToVisit[key])==0 for key in ToVisit])
            print(Count)
        return -1
        
blah = Solution()
blah.openLock(["0201","0101","0102","1212","2009","2121","2211"],"0002")
