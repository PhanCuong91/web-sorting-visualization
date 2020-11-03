from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import random
from time import sleep

@shared_task(bind=True)
def update_arr():
    arr = []
    for i in range(0, 5):
        arr.append(random.randrange(0, 100))
    sleep(duration)
    print("update arr", arr)
    return arr

@periodic_task(run_every=(crontab(minute='*/1')))
def schedule():
    arr = update_arr
    print("schedule arr", arr)
    return arr
