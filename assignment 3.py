def Quidditch(goal,snitch):
    if snitch:
        score_quidditch=goal*10+30
        print("This team scored "+str(score_quidditch))
    else:
        score_quidditch = goal * 10
        print("This team scored " + str(score_quidditch))

def Quarterback(completions,passing_yards,touchdown_passes, interceptions,attempts):
    score= 100 * (5*(completions/attempts - 0.3) + 0.25 * (passing_yards/attempts-3) + 20*(touchdown_passes/attempts) + 2.375 - (25 * interceptions/attempts))/6
    if score>158.3:
        print("The player is a perfect passer")
        print("The player's rating is", str(score))
    else:
        print("The player's rating is", str(score))

def Gymnast(diff,execution):
    print("the total score is " + str(sum(execution)-max(execution)-min(execution)+diff))

def main():
    sport=input("Choose Quarterback, Quidditch, or Gymnast").lower().replace(" ","")
    if sport=="quarterback":
        completions=input("enter completion")
        if completions.isdigit():
            completions=float(completions)
        else:
            print("You did not enter a number. Please try again.")
            main()
        interceptions = input("enter interception")
        if interceptions.isdigit():
            interceptions = float(interceptions)
        else:
            print("You did not enter a number. Please try again.")
            main()
        passing_yards = input("enter passing_yards")
        if passing_yards.isdigit():
            passing_yards = float(passing_yards)
        else:
            print("You did not enter a number. Please try again.")
            main()
        touchdown_passes = input("enter touchdown_passes")
        if touchdown_passes.isdigit():
            touchdown_passes = float(touchdown_passes)
        else:
            print("You did not enter a number. Please try again.")
            main()
        attempts = input("enter attempts")
        if attempts.isdigit():
            attempts = float(attempts)
        else:
            print("You did not enter a number. Please try again.")
            main()
        Quarterback(completions,passing_yards,touchdown_passes,interceptions,attempts)
    if sport=="quidditch":
        goals=input("how many goals did they score?")
        if goals.isdigit():
            goals=float(goals)
        else:
            print("You did not enter a number. Please try again.")
        snitch=input("did they get the snitch? Yes or no?").lower().replace(" ","")
        if snitch=="yes":
            sntich=True
        elif snitch=="no":
            snitch=False
        else:
            print("You did not answer yes or no. Please try again.")
            main()
        Quidditch(goals,sntich)
    if sport=="gymnast":
        execution = []
        difficulty = input("whats the difficulty score?")
        if difficulty.isdigit():
            difficulty = float(difficulty)
        else:
            print("You did not enter a number. Please try again.")
        i = 1
        while i <= 5:
            temp = input("Enter execution score number " + str(i)+" : ")
            if temp.isdigit():
                execution.append(float(temp))
                i=i+1
            else:
                print("you did not enter a digit please try again")
                main()
        Gymnast(difficulty,execution)
    main()

main()
