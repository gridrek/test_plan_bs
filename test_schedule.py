from datetime import datetime, timedelta
from schedule import SignalScheduler
from lampSignal import LampSignal
from typing import Tuple


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


def test_schedule():
    scheduler = SignalScheduler()
    before_schedule_time = datetime.now()

    first_entry = scheduler.scheduleOnSignal(10)
    assert len(scheduler.lamp_signals) == 1
    second_entry = scheduler.scheduleOffSignal(15)
    third_entry = scheduler.scheduleOnSignal(5)
    after_schedule_time = datetime.now()

    assert isinstance(scheduler.lamp_signals[0], Tuple)
    assert isinstance(scheduler.lamp_signals[0][0], LampSignal)
    assert isinstance(scheduler.lamp_signals[0][1], datetime)
    scheduled_time = scheduler.lamp_signals[0][1]
    lower_bound = before_schedule_time + timedelta(seconds=10)
    upper_bound = after_schedule_time + timedelta(seconds=10)
    assert lower_bound <= scheduled_time <= upper_bound


test_schedule()
