def Quidditch(goal1,goal2, snitch):
    score1=goal1*10
    score2=goal2*10
if(snitch==1):
    score1+=30
elif snitch==2:
    score2+=30

print("Team 1 scored",str(score1))
print("Team 2 scored", str(score2))

if score1>score2:
    print("Team 1 won")
elif score2>score1:
    print("Team 2 won")
else:
    print("tie")

def Quarterback(completions,pass_yards,touchdown_passes, interceptions):
    score= 100 * 5completions–0.3 + 0.25*(pass_yards)-3)) + 20*(touchdown_passes) + 2.375 – (25 * (interceptions))/6
    if score>158.3:
        print("The player is a perfect passer")
        print("The player's rating is", str(score))

    def Gymnast(score,execution):
        mx=max(execution)
        mn=min(execution)



