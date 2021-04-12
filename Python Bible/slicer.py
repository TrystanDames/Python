#get user email adress
email = input("What is your email adress?: ").strip()

#slice out user name
user = email[:email.index("@")]

#slice domain name
domain = email[email.index("@") + 1 :]

#format message
output = "Your username is {} and your domain name is {}".format(user, domain)
'''
You can also just use:
output = "Your username is {user} and your domain name is {domain}"
'''

#display output message
print(output)