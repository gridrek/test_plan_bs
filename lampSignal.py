import random


class LampSignal:
    status: bool

    def __init__(self, status: bool) -> None:
        self.status = status

    def send(self):
        if self.status == True:
            print("turn on")
        else:
            print("turn off")
        # Sending fake signal
        radnom_number = random.random()
        if radnom_number > 0.1:
            print("signal sent")
            return True
        print("signal failed to send")
        return False
