#

'''
Dense Ranking
In dense ranking, items that compare equally receive the same ranking number, and the next item(s) 
receive the immediately following ranking number. Equivalently, each item's ranking number is 1 plus
the number of items ranked above it that are distinct with respect to the ranking order.

Thus if A ranks ahead of B and C (which compare equal) which are both ranked ahead of D, then A gets
ranking number 1 ("first"), B gets ranking number 2 ("joint second"), C also gets ranking number 2
("joint second") and D gets ranking number 3 ("Third")
'''

#Algorithm 
# 1. create the variable ranked_count and players and take input
# 2. take input of ranked_score and player_score 
# 3. call the funtion Leaguetableby passing ranked_score and player_score as parameters
        # 3.1 sort the ranked score in reverse order and store those values in Scores
        # 3.2 Iterate through the players scores 
        # 3.3 traverse until the score in player_score is greater than the last element and sorted scores are not empty
                # remove the element from scores
        # 3.3 add rank to the players_score list by adding the len(scores) + 1
        # 3.4 return the player_ranks
# 4. print the ranks 

def LeagueTable(ranked_score, player_score):
    # get the unique ranks sorted descending
    scores = sorted(list(set(ranked_score)), reverse=True)
    player_ranks = []
    for score in player_score:
        while scores and score >= scores[-1]:
            scores.pop()
        player_ranks.append(len(scores) + 1)

    return player_ranks

if __name__ == '__main__':
    
    ranked_count = int(input().strip())

    ranked_score= list(map(int, input().rstrip().split()))

    players = int(input().strip())

    player_score = list(map(int, input().rstrip().split()))

    result = LeagueTable(ranked_score, player_score)

    print('\n'.join(map(str, result)))

