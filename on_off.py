import random

class LampSignal():
  def send(self, status: bool):
    if(status == True):
      print("turn on")
    #Sending fake signal
    radnom_number = random.random()
    if (radnom_number > 0.1):
      return True
    return False

lamp_signal: LampSignal = LampSignal()

def on() -> bool:
  #send on signal
  return lamp_signal.send(True)

def off():
  #send off signal
  return lamp_signal.send(False)

on()