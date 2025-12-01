#Spin the wheel game
bet = 0
print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
print("         Welcome to spin the wheel")
print("                  With bets")
print("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=")
print("There is 5 options on the wheel:")
print("Green doubles your money")
print("Blue loses your money")
print("Yellow 1.5x your money")
print("Red returns your money")
print("Orange loses your money")
ballance = 0
money = False
while money == False:
    deposit = input("Please deposit money to play: £")
    if deposit.isdigit():
        deposit = int(deposit)
        if deposit > 0:
            print("Thank you your balance is currently: £",ballance+deposit)
            money = True
            ballance = deposit + ballance
        else:
            print("Please deposit at least £1.")
    else:
        print("Please enter a numerical amount.")
play = True
while play == True:
    money = False
    while money == False:
        bet = input("Please enter how much you'd like to bet on this spin: £")
        if bet.isdigit():
            bet = int(bet)
            if bet <= ballance:
                print("Thank you, you have just bet: £",bet)
                ballance = ballance - bet
                money = True
            else:
                print("Please bet an amount that is no larger than your balance of: £",ballance)
        else:
            print("Please enter a numerical amount or a an amount above 0.")
    colour = "green"
    import random
    spin = random.randint(1,5)
    if spin == 1:
        outcome = bet*2
    elif spin == 2:
        outcome = bet - bet
        colour = "Blue"
    elif spin == 3:
        outcome = bet*1.5
        colour = "Yellow"
    elif spin == 4:
        outcome = bet
        colour = "Red"
    else:
        outcome = bet - bet
        colour = "Orange"
    start = input("Hit enter to spin the wheel")
    while start != "":
        quit()
    print("It landed on:",colour)
    if outcome == 0:
        print("That means you lost your bet of £",bet)
    if outcome == bet:
        print("You got your money back.")
    if outcome > bet:
        print("You made: £",outcome - bet,"So got £",outcome,"back.")
    print("Your balance is now: £",ballance+outcome)
    ballance = ballance+outcome
    again = input("Would you like to play another round? ").lower()
    if again in ["yes","y","yea"]:
        if ballance >= 1:
            play = True
        else:
            money = False
            while money == False:
                deposit = input("You have run out of money. Please deposit more money to keep playing. £")
                if deposit.isdigit():
                    deposit = int(deposit)
                    if deposit > 0:
                        print("Thank you your balance is currently: £",ballance+deposit)
                        ballance = deposit + ballance     
                        money = True
                    else:
                        print("Please deposit at least £1.")
                else:
                    print("Please enter a numerical amount.")
    else:
        play = False
        print("Thank you for playing")
        print("Your final balance was: £", ballance)
        if ballance > 0:
            withdraw = input("Would you like to withdraw your money? ").lower()
            if withdraw in ["yes","y","please"]:
                print("We have deposited your balance of £",ballance,"into your bank account.")
                ballance = ballance - ballance
                print("Your balance is now: £",ballance)
            else:
                print("That's ok, we will keep your money for next time you play.")
