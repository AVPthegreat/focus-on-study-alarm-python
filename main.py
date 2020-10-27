# STUDY NOTIFICATION SYSTEM


import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "PLEASE FOCUS ON STUDY ANANT ",
            message = "studying will help you to score good marks and get new tech items",
            timeout = 12
        )
        time.sleep(15*15)