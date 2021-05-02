import random

humanTurnScore = 0
computerTurnScore = 0
humanTotalScore = 0
computerTotalScore = 0
turnStart = random.randint(1,2)

while humanTotalScore < 100 and computerTotalScore < 100:
    if turnStart == 1:
        print('Your turn')
        while True:#because a human is playing now i didnt give a parameter
                    #for the loop
            dieRoll = random.randint(1, 6)
            print('You rolled -', dieRoll)
            if dieRoll == 1:
                print('You pigged out!')
                humanTotalScore = humanTotalScore - humanTurnScore
                humanTurnScore = 0
                turnStart = 2
                break

            else:
                humanTurnScore = humanTurnScore + dieRoll
                humanTotalScore = humanTotalScore + dieRoll
                if humanTotalScore > 99:
                    print('Game over, you win!')
                    break
                print('             Your turn score is', humanTurnScore)
                print('             Your total score is', humanTotalScore)
                print('             Computer total score is', computerTotalScore)
                selection = input('Press "r" to roll again, or "h" to hold ')
                #I didnt specify what happens if something other than r or h
                #is pressed, but is seems to continue the loop
                if selection == 'r':
                    continue
                if selection == 'h':
                    turnStart = 2
                    humanTurnScore = 0
                    break

    if turnStart == 2:
        print('Computer turn')
        while computerTurnScore < 20:
            dieRoll = random.randint(1,6)
            print('Computer rolled -', dieRoll)
            if dieRoll == 1:
                print('Computer pigged out!')
                computerTotalScore = computerTotalScore - computerTurnScore
                computerTurnScore = 0
                turnStart = 1
                break
            else:
                computerTurnScore = computerTurnScore + dieRoll
                computerTotalScore = computerTotalScore + dieRoll
                if computerTotalScore > 99:
                    print('Game over, computer wins!')
                    break
                if computerTurnScore > 19:
                    turnStart = 1
                    break                

        print('             Computer turn score is', computerTurnScore)
        print('             Computer total score is', computerTotalScore)
        print('             Your total score is', humanTotalScore)
            
        computerTurnScore = 0 
