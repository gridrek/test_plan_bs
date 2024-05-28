from datetime import datetime, timedelta
from lampSignal import LampSignal
from typing import List, Tuple


class SignalScheduler:
    def __init__(self) -> None:
        self.lamp_signals: List[Tuple[LampSignal, datetime]] = []

    def _schedule_signal(
        self, time_in_seconds: int, state: bool
    ) -> Tuple[LampSignal, datetime]:
        signal = LampSignal(state)
        scheduled_time = datetime.now() + timedelta(seconds=time_in_seconds)
        new_entry = (signal, scheduled_time)  # Use standard tuple syntax here

        for index, (_, scheduled_time_existing) in enumerate(self.lamp_signals):
            if new_entry[1] < scheduled_time_existing:
                self.lamp_signals.insert(index, new_entry)
                return new_entry

        self.lamp_signals.append(new_entry)
        return new_entry

    def scheduleOnSignal(self, time_in_seconds: int):
        return self._schedule_signal(time_in_seconds, True)

    def scheduleOffSignal(self, time_in_seconds: int):
        return self._schedule_signal(time_in_seconds, False)
