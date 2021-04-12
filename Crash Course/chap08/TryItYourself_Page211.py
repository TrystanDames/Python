#8-9
def show_messages(message):
	"""Print a simple greeting to each user in the list."""
	for messages in message:
		msg = messages
		print(msg)
greeting = [
	'You are amazing!',
	'You are loved!',
	'You are you not who they say you are!'
]
show_messages(greeting)

#8-10
send_messages = [
	'You are amazing!',
	'You are loved!',
	'You are you not who they say you are!'
]
sent_messages = []

while send_messages:
	current_messages = send_messages.pop()
	print(current_messages)
	sent_messages.append(current_messages)

print("\nThe following messages have been printed:")
for sent_message in sent_messages:
	print(sent_message)
print(send_messages)

#8-11
def send_messages(message):
	"""Print a simple greeting to each user in the list."""
	for messages in message:
		msg = messages
		print(msg)

send_messages = [
	'You are amazing!',
	'You are loved!',
	'You are you not who they say you are!'
]

show_messages(greeting)
print(sent_message)