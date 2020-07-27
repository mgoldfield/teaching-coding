from random import random, randint
import string


ans = ''

prompt = "What's on your mind? "

non_commital_responses = [ 
	# the next few lines are all part of the list
	# we can break commands up onto separate lines that are too long
	'hmmmm, go on... ', 
	'tell me more... ', 
	'how does that make you feel? ']

point_of_view = {
	'me': 'you',
	'you': 'me',
	'i': 'you',
	"im": 'you are',
	"my": "your",
	"your": "my",
	"wasnt": "were not",
}

# make a translator to remove punctuation
remove_punctuation = str.maketrans('', '', string.punctuation)


while ans != 'bye':
	ans = input(prompt)

	# 70% of the time do this, 30% of the time do a non-commital response
	# also if it ends in a question makr, do a non-0commital response
	if ans.strip()[-1] == '?' or len(ans.split(' ')) < 3 or random() < .25: 
		prompt = non_commital_responses[randint(0,len(non_commital_responses) - 1)]
	else:

		# take the last sentence of the user's answer
		ans = ans.split('.')
		if len(ans[-1]) > 0:
			ans = ans[-1]
		else:
			ans = ans[-2]


		ans = ans.translate(remove_punctuation) # remove punctuation
		ans = ans.lower() # lowercase everything
		ans = ans.split(' ') # make ans into a list of words

		# map point of view from 1st person to 2nd person and visa versa
		ans = [ point_of_view[w] if w in point_of_view.keys() else w for w in ans ]

		ans = ' '.join(ans) + "? "
		prompt = ans.capitalize()








