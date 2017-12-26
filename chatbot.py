import random
"""
   Chat Bot 1.0:
   This is a basic chat bot with zero training and with random response
"""

# Greetings and responses
keywords = ['hello', 'hai', 'greetings', 'what\'s up']
responses = ['hey', 'hello', 'what\'s up bro']

def check_for_greeting(message):
	"""If any of the words in the user's input was a greeting, greet in return"""
	for word in message.split():
		if word.lower() in keywords:
			return random.choice(responses)
		else:
			return 'hmmm'



if __name__ == '__main__':
	msg = ''
	user = input('Enter your good name? ')
	print('Start by greeting robot')
	while msg != 'bye':
		msg = input('%s :' % user)
		print('bot: ' + check_for_greeting(msg))


