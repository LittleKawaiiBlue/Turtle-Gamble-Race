import turtle
import random
from random import randint
import time
from turtle import Screen, Turtle

wn = turtle.Screen()
wn.bgcolor("forestgreen")
wn.title("Turtle Run")

#Starting line#

employer3 = turtle.Turtle()
stamp_size = 20
square_size = 15
fisrt_line = -506
second_line = -496

employer3.color("chocolate")
employer3.shape("square")
employer3.shapesize(square_size / stamp_size)
employer3.penup()

for u in range(21):
	employer3.setpos(fisrt_line, (149 - (u * square_size)))
	employer3.stamp()
	employer3.setpos(second_line, (149 - (u * square_size)))
	employer3.stamp()

	
employer3.hideturtle()

#Race track#

employer5 = turtle.Turtle()
stamp_size = 1
square_size = 14
race_track = -348

employer5.color("gainsboro")
employer5.shape("square")
employer5.shapesize(square_size / stamp_size)
employer5.penup()

for i in range(53): 
	employer5.setpos((race_track + (i * square_size)), -2)
	employer5.stamp()
	
	
employer8 = turtle.Turtle()
employer8.color("black")
employer8.shape("square")
stamp_size = 2
square_size = 0.5
employer8.shapesize(square_size / stamp_size)
employer8.penup()

for i in range(79):
	employer8.setpos(-486 + (i * square_size * 25), 85)
	employer8.stamp()

for i in range(79):
	employer8.setpos(-486 + (i * square_size * 25), 25)
	employer8.stamp()

for i in range(79):
	employer8.setpos(-486 + (i * square_size * 25), -35)
	employer8.stamp()
	
for i in range(79):
	employer8.setpos(-486 + (i * square_size * 25), -90)
	employer8.stamp()
		
#Finish line#

employer2 = turtle.Turtle()
stamp_size = 20
square_size = 15
finish_line = 498

employer2.color("black")
employer2.shape("square")
employer2.shapesize(square_size / stamp_size)
employer2.penup()

for i in range(11):
	employer2.setpos(finish_line, (149 - (i * square_size * 2)))
	employer2.stamp()
	

for j in range(10):
	employer2.setpos(finish_line + square_size, ((149 - square_size) - (j * square_size * 2)))
	employer2.stamp()
	
employer2.hideturtle()

#Stadium#

colors = ["yellow", "green", "black", "snow", "chocolate", "dark green", "blue", "navy", "hot pink"]
employer7 = turtle.Turtle()
employer7.shape("turtle")
randColor = random.randrange(len(colors))
employer7.color(colors[randColor])
employer7.penup()
employer7.setheading(90)

employer6 = turtle.Turtle()
stamp_size = 1
square_size = 2
employer6.shape("square")
employer6.shapesize(square_size / stamp_size)
employer6.penup()
employer6.speed(0)

#Setting the stands
for i in range(38): 
	employer6.color("saddle brown")
	employer6.setpos(-665 + (i * square_size * 20), -255)
	employer6.stamp()
	
for i in range(38):
	employer6.color("sienna")
	employer6.setpos(-665 + (i * square_size * 20), -295)
	employer6.stamp()
	
for i in range(38):
	employer6.color("peru")
	employer6.setpos(-665 + (i * square_size * 20), -335)
	employer6.stamp()
	
for i in range(38): 
	employer6.color("saddle brown")
	employer6.setpos(-665 + (i * square_size * 20), 259)
	employer6.stamp()
	
for i in range(38): 
	employer6.color("sienna")
	employer6.setpos(-665 + (i * square_size * 20), 299)
	employer6.stamp()
	
for i in range(38): 
	employer6.color("peru")
	employer6.setpos(-665 + (i * square_size * 20), 339)
	employer6.stamp()

#setting the public in the stadium
for i in range(55):
	randColor = random.randrange(len(colors))
	employer7.color(colors[randColor])
	employer7.setpos(-663 + (i * square_size * 13), -257)
	employer7.stamp()
	
for i in range(55):
	randColor = random.randrange(len(colors))
	employer7.color(colors[randColor])
	employer7.setpos(663 - (i * square_size * 13), -297)
	employer7.stamp()
	
for i in range(55):
	randColor = random.randrange(len(colors))
	employer7.color(colors[randColor])
	employer7.setpos(-663 + (i * square_size * 13), -337)
	employer7.stamp()

employer7.setheading(270)

for i in range(55):
	randColor = random.randrange(len(colors))
	employer7.color(colors[randColor])
	employer7.setpos(-663 + (i * square_size * 13), 261)
	employer7.stamp()
	
for i in range(55):
	randColor = random.randrange(len(colors))
	employer7.color(colors[randColor])
	employer7.setpos(663 - (i * square_size * 13), 301)
	employer7.stamp()
	
for i in range(55):
	randColor = random.randrange(len(colors))
	employer7.color(colors[randColor])
	employer7.setpos(-663 + (i * square_size * 13), 341)
	employer7.stamp()
	
#Title#

#####################################
#####################################
#####################################

#Make your bet
print("Green racer: tim \nBlue racer: tess \nRed racer: alex \nHot pink racer: duck \nGold racer: dog \n ")
print("You have 100€") 
print("If you win the game you gain the valour of the gamble you made multiplied by 1.5.\nIf you lose the gamble you lose the valour of the gamble you made. ")

myMoney = 100
	
runnerName = input("Who do you bet for? ")
runners = ["tim", "tess", "alex", "duck", "dog"]

while runnerName not in runners:
    print("There is no runner with that name. ")
    runnerName = input("Who do you bet for? ")


bet = int(input("How much you bet? "))

while bet < 0 and bet > myMoney:
    if bet < 0:
        print("The bet can't take negative valours! ")
        bet = int(input("How much you bet? "))
    else:
        print("The bet can't be above the money you have! ")
        bet = int(input("How much you bet? "))

print("Your bet is " + str(bet) + "€. ")

time.sleep(1)

#Runners#

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("red")
alex.penup()
alex.setpos(-504, -10)

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.penup()
tess.setpos(-504, 50)

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("dark green")
tim.penup()
tim.setpos(-504, 110)

duck = turtle.Turtle()
duck.shape("turtle")
duck.color("hot pink")
duck.penup()
duck.setpos(-504, -60)

dog = turtle.Turtle()
dog.shape("turtle")
dog.color("gold")
dog.penup()
dog.setpos(-504, -120)

time.sleep(1)

#Time to start
employer4 = turtle.Turtle()

def recurse(n):
	if n >= 0:
		employer4.hideturtle()
		employer4.color("black")
		employer4.speed(0)
		employer4.penup()
		employer4.setpos(-50, -60)
		employer4.write(n, font=("Arial", 100, "bold"))
		employer4.penup()
		time.sleep(1)
		employer4.clear()
		recurse(n-1)
		
employer4.hideturtle()
recurse(3)

#Setting the distance

screen = Screen()
turtles = screen.turtles()

while True:
	for i in turtles:
		alex.forward(randint(5,10))
		tess.forward(randint(5,10))
		tim.forward(randint(5,10))
		duck.forward(randint(5,10))
		dog.forward(randint(5,10))
	
	if alex.xcor() > finish_line:
		print("The winner is Alex! ") 
		winner = "alex"
		break  
	
	if tess.xcor() > finish_line:
		print("The winner is Tess! ")
		winner = "tess" 
		break
	
	if tim.xcor() > finish_line:
		print("The winner is Tim! ") 
		winner = "tim"
		break
	
	if duck.xcor() > finish_line:
		print("The winner is Duck! ") 
		winner = "duck"
		break
	
	if dog.xcor() > finish_line:
		print("The winner is Dog! ") 
		winner = "dog"
		break
	
if winner != runnerName:
	print("You lose the gamble! ")
	myMoney = myMoney - bet
	if myMoney <= 0:
		print("You lose all your money! \nGAME OVER")
		exit()
	if myMoney > 0:
		print("Your corrent money is " + str(myMoney) + "€. ")

if winner == runnerName:
	print("You win the gamble! ")
	myMoney = myMoney + bet * 1.5
	print("Your corrent money is " + str(myMoney) + "€. ")
	
playAgain = input("Do you want to play again? [y/n]")

while playAgain == "y" or playAgain == "yes":
	
	runnerName = input("Who do you bet for? ")
	runners = ["tim", "tess", "alex", "duck", "dog"]
	
	while runnerName not in runners:
		print("There is no runner with that name. ")
		runnerName = input("Who do you bet for? ")
		
	bet = int(input("How much you bet? "))
		
	while bet < 0 and bet > myMoney:
		if bet < 0:
			print("The bet can't take negative valours! ")
			bet = int(input("How much you bet? "))
		else:
			print("The bet can't be above the money you have! ")
			bet = int(input("How much you bet? "))

	print("Your bet is " + str(bet) + "€. ")
	
	#Runners#
	
	alex.setpos(-504, -10)
	tess.setpos(-504, 50)
	tim.setpos(-504, 110)
	duck.setpos(-504, -60)
	dog.setpos(-504, -120)
	time.sleep(1)
	
	#Time to start
	
	employer4 = turtle.Turtle()
	def recurse(n):
		if n >= 0:
			employer4.hideturtle()
			employer4.color("black")
			employer4.speed(0)
			employer4.penup()
			employer4.setpos(-50, -60)
			employer4.write(n, font=("Arial", 100, "bold"))
			employer4.penup()
			time.sleep(1)
			employer4.clear()
			recurse(n-1)
	
	employer4.hideturtle()
	recurse(3)
	
	#Setting the distance
	
	while True:
		for i in turtles:
			alex.forward(randint(5,10))
			tess.forward(randint(5,10))
			tim.forward(randint(5,10))
			duck.forward(randint(5,10))
			dog.forward(randint(5,10))
		
		if alex.xcor() > finish_line:
			print("The winner is Alex! ") 
			winner = "alex"
			break  
		
		if tess.xcor() > finish_line:
			print("The winner is Tess! ")
			winner = "tess" 
			break
			
		if tim.xcor() > finish_line:
			print("The winner is Tim! ") 
			winner = "tim"
			break
			
		if duck.xcor() > finish_line:
			print("The winner is Duck! ") 
			winner = "duck"
			break
			
		if dog.xcor() > finish_line:
			print("The winner is Dog! ") 
			winner = "dog"
			break
			
	if winner != runnerName:
		print("You lose the gamble! ")
		myMoney = myMoney - bet
		if myMoney <= 0:
			print("You lose all your money! \nGAME OVER")
			exit()
		if myMoney > 0:
			print("Your corrent money is " + str(myMoney) + "€. ")
	
	if winner == runnerName:
		print("You win the gamble! ")
		myMoney = myMoney + bet * 1.5
		print("Your corrent money is " + str(myMoney) + "€. ")
	
	playAgain = input("Do you want to play again? [y/n]")
	
if playAgain == "n" or playAgain == "no":
		exit()
		
print("Your money is " + str(myMoney) + "€. ")

turtle.exitonclick()
