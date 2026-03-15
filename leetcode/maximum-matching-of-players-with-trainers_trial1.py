class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()

        p,t=0,0
        count = 0

        while p<len(players) and t<len(trainers):
            if players[p] > trainers[t]:
                t += 1
            else:
                count += 1
                p += 1
                t += 1
        
        return count