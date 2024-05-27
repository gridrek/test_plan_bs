
class Signal():
  def send(status: bool):
    #Sending fake signal
    pass

signal: Signal = Signal()

def on():
  #send on signal
  signal.send(True)
  return True

def off():
  #send off signal
  signal.send(False)
  return True
