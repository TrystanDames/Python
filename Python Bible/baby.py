from random import choice

questions = [
	"Why you so big?: ",
	"Why is the sky blue?: ",
	"Why cant I play in fire?: "
]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
	answer = input("Why?: ").strip().lower()

print("Oh... Okay.")
