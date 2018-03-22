import sys
def greet_users(usernames):

    print('Hello ' + usernames.capitalize()+'!')
usernames= sys.argv[1:]
for i in usernames :
    greet_users(i)


