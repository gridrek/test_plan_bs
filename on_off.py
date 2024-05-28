import random
from datetime import datetime, timedelta
from typing import List, Tuple

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
  

class SignalScheduler:
  def __init__(self) -> None:
    self.lamp_signals: List[Tuple[LampSignal, datetime]] = []

  def scheduleOnSignal(self, time_in_seconds: int):
    signal: LampSignal = LampSignal(True)
    scheduled_time = datetime.now() + timedelta(seconds=time_in_seconds)
    tuple = (signal, scheduled_time)
    if len(self.lamp_signals) == 0:
      self.lamp_signals.append(tuple)
      return
      
    for index, e in enumerate(self.lamp_signals):
      # Check if the scheduled signal is sooner than the current signal in the list
      if tuple[1] < e[1]:
          self.lamp_signals.insert(index, tuple)
          return
    # If not inserted yet, append to the end
    self.lamp_signals.append(tuple)
    
  def scheduleOffSignal(self, time_in_seconds: int):
    signal: LampSignal = LampSignal(False)
    scheduled_time = datetime.now() + timedelta(seconds=time_in_seconds)
    tuple = (signal, scheduled_time)
    if len(self.lamp_signals) == 0:
      self.lamp_signals.append(tuple)
      return
      
    for index, e in enumerate(self.lamp_signals):
      # Check if the scheduled signal is sooner than the current signal in the list
      if tuple[1] < e[1]:
          self.lamp_signals.insert(index, tuple)
          return
    # If not inserted yet, append to the end
    self.lamp_signals.append(tuple)



def on() -> bool:
  signal = LampSignal(True)
  return signal.send()

def off():
  signal = LampSignal(True)
  return signal.send()

signalScheduler = SignalScheduler()
print()
print(f"NOW: {datetime.now()}")
signalScheduler.scheduleOnSignal(20)
signalScheduler.scheduleOnSignal(10)
signalScheduler.scheduleOnSignal(30)
signalScheduler.scheduleOnSignal(5)
signalScheduler.scheduleOffSignal(15)

for signal, scheduled_time in signalScheduler.lamp_signals:
    print(f"LampSignal(status={'on' if signal.status else 'off'}) at {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}")