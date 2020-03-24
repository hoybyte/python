# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:

user1 = {
    'name' : 'Sorna',
    'valid' : True # changing this will either run or not runthe message_friends function
}

user2 = {
    'name' : 'Dwight',
    'valid' : False
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print(f'You are not authorized!')
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
message_friends(user2)
