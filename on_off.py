import random

class LampSignal():
  def send(self, status: bool):
    if(status == True):
      print("turn on")
    #Sending fake signal
    radnom_number = random.random()
    if (radnom_number > 0.1):
      print("signal sent")
      return True
    print("signal failed to send")
    return False

class ScheduleSignal():
  lamp_signals: list[LampSignal]

  def scheduleOn():
    pass
  def scheduleOff():
    pass

lamp_signal: LampSignal = LampSignal()

def on() -> bool:
  #send on signal
  return lamp_signal.send(True)

def off():
  #send off signal
  return lamp_signal.send(False)

on()