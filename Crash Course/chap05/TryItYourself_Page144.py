# #5-8
# available_users = ['admin', 'trystan', 'hannah', 'kyle', 'malaki', 'lourens']
# people_users =  ['trystan', 'hannah', 'kyle', 'malaki', 'lourens']
# for people_user in people_users:
# 	print(f"Hi there welcome back {people_user.title()} thank you for logging back in!")
# if 'admin' in available_users:
# 	print(f"Hi {available_users[0].title()}, would you like to see the status report for this comuter?")

# #5-9
# available_users = ['']
# if '' in available_users:
# 	print(f"We need to find some user!")

# #5-10
# current_users = ['trystan', 'hannah', 'kyle', 'malkai', 'lourens']
# new_users = ['scott', 'rob', 'trystan', 'malose', 'hannah']
# for new_user in new_users:
# 	if new_user in current_users:
# 		print("This username is already used please use a different one.")
# 	else:
# 		print("This username is available.")

#5-11
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nums in num:
	if nums == 1:
		print(f"{nums}st")
	elif nums == 2:
		print(f"{nums}nd")
	elif nums == 3:
		print(f"{nums}rd")
	else:
		print(f"{nums}th")