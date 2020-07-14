import random


response = ''

prompt = "How are you feeling today?"



non_commital_responses = [ 
	# the next few lines are all part of the list
	# we can break commands up onto separate lines that are too long
	'hmmmm, go on...', 
	'tell me more...', 
	'how does that make you feel?']

1st_to_2nd_person = {
	'me': 'you',
	'you': 'me',
	'i': 'you',
}


while response != 'bye':

	ans = input(prompt)

	




