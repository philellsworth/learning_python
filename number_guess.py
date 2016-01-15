import random, math
f = 0
# did IDLE change 'i' to 'f'? or did I just forget doing that?
num = random.randint(1,100)
tries = 0
userName = input("What's your name? ")
print ("Ok", userName, ", guess a number between 0 and 100")
# how to keep it from putting a space after userName?
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
		print("Great job,", userName)# + userName
		f = 1
		
		print('You got that in', tries, 'tries,', userName, ".") 
	else:
		print ("Try again.")

# how to save number of attempts per userName? Save to a spreadsheet?
# Access that spreadsheet to compare averages?
# trying simpler push to github

