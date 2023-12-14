class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        result=[[],[]]
        losses=dict()
        for i in matches:
            players.add(i[0])
            players.add(i[1])
        for i in players:
            losses[i]=0 
        for loss in matches:
            losses[loss[1]]+=1
        for key, value in losses.items():
            if value==0 or value==1:
                result[value].append(key)
        result[0].sort()
        result[1].sort()
        return result


    



    
        
        














        # res = [[],[]]
        # player = set()
        # for i in range(len(matches)):
        #     player.add(matches[i][0])
        #     player.add(matches[i][1])
        # number_of_losses = {play : 0 for play in player}
        # for match in matches:
        #     number_of_losses[match[1]] += 1
        # print(number_of_losses)
        # for player,losses in number_of_losses.items():
        #     if losses == 0 or losses == 1:
        #         res[losses].append(player)
        # res[0].sort()
        # res[1].sort()
        # return res
        