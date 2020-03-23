# Create an @authenticated decorator that only allows the functino to run if user1 has 'valid' set to True:

user1 = {
    'name' = 'Sorna',
    'valid' = True # changing this will either run or not runthe message_friends function
}

def authenticated(fn):

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)