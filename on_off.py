import random
from datetime import datetime, timedelta

class LampSignal():
  status: bool

  def __init__(self, status: bool) -> None:
    self.status = status

  def send(self):
    if(self.status == True):
      print("turn on")
    else:
      print("turn off")
    #Sending fake signal
    radnom_number = random.random()
    if (radnom_number > 0.1):
      print("signal sent")
      return True
    print("signal failed to send")
    return False
  

class SignalScheduler():

  def __init__(self) -> None:
    self.lamp_signals: list[(LampSignal, datetime)] = []
    pass

  def scheduleOnSignal(self, time_in_seconds: int):
    signal: LampSignal = LampSignal(True)
    now = datetime.now()
    scheduled_time = now + timedelta(seconds=time_in_seconds)
    print(len(self.lamp_signals))
    if len(self.lamp_signals) == 0:
      print("w")
      self.lamp_signals.append((signal, scheduled_time))
      return
    for index, e in enumerate(self.lamp_signals, start=1):
        



  def scheduleOffSignal(self, time_in_seconds: int):
    signal: LampSignal = LampSignal(False)



def on() -> bool:
  signal = LampSignal(True)
  return signal.send()

def off():
  signal = LampSignal(True)
  return signal.send()

signalScheduler = SignalScheduler()
signalScheduler.scheduleOnSignal(20)
print()
signalScheduler.scheduleOnSignal(10)
print()
signalScheduler.scheduleOnSignal(30)