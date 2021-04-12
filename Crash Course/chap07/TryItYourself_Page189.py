#7-8
sandwhich_orders = ['chicken mayo', 'bacon and egg', 'ham, cheese and tomato', 'bacon, egg and cheese', 'dagwood']
finished_sandwhiches = []

while sandwhich_orders:
	current_orders = sandwhich_orders.pop()
	print(f"Making Sandwhich: {current_orders.title()}")
	finished_sandwhiches.append(current_orders)

print("\nThe following sandwhiches were made:")
for finished_sandwhich in finished_sandwhiches:
	print(finished_sandwhich.title())

#7-9
sandwhich_orders = ['chicken mayo', 'bacon and egg', 'ham, cheese and tomato', 'bacon, egg and cheese', 'dagwood', 'pastrami']
finished_sandwhiches = []

while sandwhich_orders:
	current_orders = sandwhich_orders.pop()
	print(f"Making Sandwhich: {current_orders.title()}")
	finished_sandwhiches.append(current_orders)

while 'pastrami' in finished_sandwhiches:
		finished_sandwhiches.remove('pastrami')

print("\nThe following sandwhiches were made:")
for finished_sandwhich in finished_sandwhiches:
	print(finished_sandwhich.title())

#7-10
prompt = "\nWhat would be the first place in the world if you could go there for free?"
message = input(prompt)
print(message)