import random

class Signal():
  def send(status: bool):
    #Sending fake signal
    radnom_number = random.random()
    if (radnom_number > 0.1):
      return True
    return False

signal: Signal = Signal()

def on():
  #send on signal
  return signal.send(True)

def off():
  #send off signal
  return signal.send(False)
