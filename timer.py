from time import sleep


def countdown_time():
    for t in range(0, 60):
        sleep(1)
        timer = t
    return timer

