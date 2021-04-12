#3-4
invite = ['lourens', 'sheldon', 'annatjie']
print(f"Dear {invite[0].title()}, you've been invited to my party!\n")
print(f"Dear {invite[1].title()}, you've been invited to my party!\n")
print(f"Dear {invite[2].title()}, you've been invited to my party!\n")

#3-5
invite[2] = "beryl"
print(invite)
print(f"Dear {invite[0].title()}, you've been invited to my party!\n")
print(f"Dear {invite[1].title()}, you've been invited to my party!\n")
print(f"Dear {invite[2].title()}, you've been invited to my party!\n")

#3-6
invite = ['lourens', 'sheldon', 'annatjie']
invite.insert(0, 'beryl')
invite.insert(2, 'jacques')
invite.append('francois')
print(invite)
print(f"Dear {invite[0].title()}, you've been invited to my party!\n")
print(f"Dear {invite[1].title()}, you've been invited to my party!\n")
print(f"Dear {invite[2].title()}, you've been invited to my party!\n")
print(f"Dear {invite[3].title()}, you've been invited to my party!\n")
print(f"Dear {invite[4].title()}, you've been invited to my party!\n")
print(f"Dear {invite[5].title()}, you've been invited to my party!\n")

#3-7
too_many = invite.pop(0)
print(f"\nI am sorry {too_many.title()} you are no longer invited as I am only able to have two guests.")
too_many = invite.pop(1)
print(f"\nI am sorry {too_many.title()} you are no longer invited as I am only able to have two guests.")
too_many = invite.pop(1)
print(f"\nI am sorry {too_many.title()} you are no longer invited as I am only able to have two guests.")
too_many = invite.pop(2)
print(f"\nI am sorry {too_many.title()} you are no longer invited as I am only able to have two guests.")
print(invite)
print(f"Dear {invite[0].title()}, you've been invited to my party!\n")
print(f"Dear {invite[1].title()}, you've been invited to my party!\n")
del invite[0]
del invite[0]
print(invite)