import random


money = 100
#Write your game of chance functions here

def coin_flip(bet,call,money):
    result = random.randint(0,1)
    if money<=0:
        raise Exception("Sorry, you do not have enough money to play")
    if (call=="Tail") and (result==0):
        print("You won " + str(bet) + " dollars" )
    elif (call=="Head") and (result==1):   
        print("You won " + str(bet) + " dollars")
    else:
        if money <= bet:
            raise Exception("Sorry, you lost all your money")
        bet=-bet
        print("You lost " + str(bet) + " dollars")
    money+=bet
    print("You currently have " + str(money) + " dollars")
    return money

def Cho_Han(bet,call,money):
    if money<=0:
        raise Exception("Sorry, you do not have enough money to play")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    result = die1 + die2
    if(result%2==0 and call=="Even") or (result % 2 ==1 and call == "odd"):
        print("Die 1 is: " + str(die1) + ", and Die 2 is: " + str(die2) + ". You won "+ str(bet) + " dollars.")
    else:
        if money <= bet:
            raise Exception("Sorry, you lost all your money")
        print("Die 1 is: " + str(die1) + ", and Die 2 is: " + str(die2) + ". You lost "+ str(bet) + " dollars.") 
        bet=0-bet
    money+=bet
    print("You currently have " + str(money) + " dollars")
    return money
    

money=coin_flip(10,"Tail",money)
money=Cho_Han(30,"Even",money)


#Call your game of chance functions here
