from datetime import datetime, timedelta
from src.schedule import SignalScheduler
from src.lampSignal import LampSignal
from typing import Tuple
import pytest


def test_schedule():
    scheduler = SignalScheduler()
    before_schedule_time = datetime.now()

    entry = scheduler.scheduleOnSignal(10)  # schedule in seconds into the future
    assert len(scheduler.lamp_signals) == 1
    after_schedule_time = datetime.now()

    assert isinstance(entry[0], LampSignal)
    assert isinstance(entry[1], datetime)
    scheduled_time = entry[1]
    lower_bound = before_schedule_time + timedelta(seconds=10)
    upper_bound = after_schedule_time + timedelta(seconds=10)
    assert lower_bound <= scheduled_time <= upper_bound
