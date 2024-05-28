from on_off import on, off, SignalScheduler, LampSignal
from datetime import datetime
from typing import Tuple

def test_on():
  result = on()
  assert result == True

def test_off():
  result = off()
  assert result == True

def test_schedule_on():
  scheduler = SignalScheduler()

  scheduler.scheduleOnSignal(10)
  assert len(scheduler.lamp_signals) == 1
  assert isinstance(scheduler.lamp_signals[0], tuple)
  assert isinstance(scheduler.lamp_signals[0][0], LampSignal)
  assert isinstance(scheduler.lamp_signals[0][1], datetime)

#test_on()
test_schedule_on()