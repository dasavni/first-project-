import random 
num=random.randint(1,100)

print ("remaining guesses: 10")
guess=int(input("guess a number 1,100 " ))
count=1

while guess != num and count<11:

    if guess<num:
        print ("your guess is too low")
    elif guess>num:
        print ("your guess is too high")
    print ("remaining guesses: ", 10- count)
    guess=int(input("guess a number 1,100 " ))
    count+=1



if count<11:
    print ("good job you guessed right")
else:
    print ("sorry you ran out of guesses")
        