from time import sleep

counter = 60


def countdown_time():
    global counter
    while counter > 0:
        sleep(1)
        counter -= 1
        print(counter)
    return counter




