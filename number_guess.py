import random, math
f = 0
num = random.randint(1,100)
tries = 0
print "Guess a number between 0 and 100"
while f == 0:
	# convert to "input" from "raw_input" to work with 3.x
	theGuess = int(input("Your guess: "))
	if theGuess > num:
		tries = tries + 1
		print("Your guess is too high.")
	if theGuess < num:
		tries = tries + 1
		print("Your guess is too low.") 
	if theGuess == num:
		print("Great Job.")
		f = 1
		
		print('You got that in', tries, 'tries.') 
	else:
		print "Try again."

