import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Drink Water! It has been an hour!",
            timeout=10,
        )
        time.sleep(1)