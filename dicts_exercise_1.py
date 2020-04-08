# We need to receive the basic info of a user
# (first_name, last_name, age, email)
# and save them as keys into a dict call user.
# After receive the data, show the info in the console

user = {}

user['first_name'] = input('Hey bro, cual es tu nombre?: ')
user['last_name'] = input('Como dices que se apellidan tus gfes?: ')
user['age'] = input('Ya alcanzas el timbre?: ')
user['email'] = input('Pásame tu correo para enviarte unas fotos UwU: ')

for key, value in user.items():
    print(f'{key.upper()}: {value}')