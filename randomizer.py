import random
import logging
import json

USERS_FILENAME = 'users.txt'
LOG_FILENAME = 'randomizer.log'
NUM_WINNERS = 3

emojis = ['😺','🥰','🙃','👻','👍','💪','🤘','👌']

logging.basicConfig(filename=LOG_FILENAME,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def load_file_to_list(filename):
    with open(filename) as f:
        return f.read().splitlines()

def random_emoji():
    random.shuffle(emojis)
    return emojis.pop(0)

if __name__ == "__main__":
    # Loading users from file
    users = load_file_to_list(USERS_FILENAME)
    num_users = len(users)

    logging.info('Loaded {} users'.format(num_users))
    logging.info(json.dumps(users, indent=4))

    print('\n\nНачинаем розыгрыш среди {} участников! 😳'.format(num_users))
    input()
    
    # cycling through the list
    for i in range(1,NUM_WINNERS + 1):

        # Тщательно перемешиваем лист 3 раза :)
        for j in range(0,3):
            random.shuffle(users)

        logging.info('Iteration: {}, elements in array: {}'.format(i, len(users)))
        logging.info('Randomized array')
        logging.info(json.dumps(users,indent=4))

        # Первый элемент листа => победитель
        # Убираем элемент из листа
        winner = users.pop(0)

        logging.info('Winner in iteration {}: {}'.format(i,winner))

        print('{}. {} {}'.format(i,winner,random_emoji()))

        # Ждем пока пользователь нажмёт Enter
        input()
    
    print('Всем спасибо! ❤️')
    input()