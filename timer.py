from time import sleep


def countdown_time():
    counter = 60

    while counter > 0:
        sleep(1)
        counter -= 1
        print(counter)
    return counter


countdown_time()



