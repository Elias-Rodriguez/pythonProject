# importing the module
import json

def greet_player():
    player_data = {}
    # Opening JSON file
    with open('player_file.json') as json_file:
        player_data = json.load(json_file)
    print(player_data)
    print('it is nice to meet you,', player_data['name'])

def say_my_name_and_car():
    player_data = {}
    # Opening JSON file
    with open('player_file.json') as json_file:
        player_data = json.load(json_file)

    print('Hello', player_data['name'])
    print('You drive a', player_data['car'])
    print(player_data)

def story():
    player_data = {}
    # Opening JSON file
    with open('player_file.json') as json_file:
        player_data = json.load(json_file)
    print('Hello', player_data['name'])
    print('You drive a', player_data['car'])
    print('You had a good day.')
    print(player_data['dog'], ' kept your bird safe.')


if __name__ == '__main__':
    say_my_name_and_car()
