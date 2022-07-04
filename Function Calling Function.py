def get_name():
    name=input('What is your Name? ')
    return name

def say_name(name):
    print('Your Name is {}'.format(name))


def get_and_say_name():

    name=get_name()
    say_name(name)

get_and_say_name()
