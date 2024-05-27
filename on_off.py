
class Signal():
  def send(bool: status):
    #Sending fake signal 

signal = Signal()

def on():
  #send on signal
  signal.send(True)

def off():
  #send off signal
  signal.send(False)
