from on_off import on, off, SignalScheduler, LampSignal
from datetime import datetime, timedelta
from typing import Tuple

def test_on():
  result = on()
  assert result == True

def test_off():
  result = off()
  assert result == True


def test_schedule_on():
  scheduler = SignalScheduler()
  before_schedule_time = datetime.now()

  scheduler.scheduleOnSignal(10)
  after_schedule_time = datetime.now()

  assert len(scheduler.lamp_signals) == 1
  assert isinstance(scheduler.lamp_signals[0], tuple)
  assert isinstance(scheduler.lamp_signals[0][0], LampSignal)
  assert isinstance(scheduler.lamp_signals[0][1], datetime)
  scheduled_time = scheduler.lamp_signals[0][1]
  lower_bound = before_schedule_time + timedelta(seconds=10)
  upper_bound = after_schedule_time + timedelta(seconds=10)
  assert lower_bound <= scheduled_time <= upper_bound


#test_on()
test_schedule_on()