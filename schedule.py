from datetime import datetime, timedelta
from lampSignal import LampSignal
from typing import List, Tuple


class SignalScheduler:
	def __init__(self) -> None:
		self.lamp_signals: List[Tuple[LampSignal, datetime]] = []

	def _schedule_signal(self, time_in_seconds: int, state: bool):
		signal = LampSignal(state)
		scheduled_time = datetime.now() + timedelta(seconds=time_in_seconds)
		new_entry = (signal, scheduled_time)
				
		for index, (_, scheduled_time_existing) in enumerate(self.lamp_signals):
			if new_entry[1] < scheduled_time_existing:
				self.lamp_signals.insert(index, new_entry)
				return
				
		self.lamp_signals.append(new_entry)

	def scheduleOnSignal(self, time_in_seconds: int):
		self._schedule_signal(time_in_seconds, True)

	def scheduleOffSignal(self, time_in_seconds: int):
		self._schedule_signal(time_in_seconds, False)


signalScheduler = SignalScheduler()
print()
print(f"NOW: {datetime.now()}")
signalScheduler.scheduleOnSignal(20)
signalScheduler.scheduleOnSignal(10)
signalScheduler.scheduleOnSignal(30)
signalScheduler.scheduleOnSignal(5)
signalScheduler.scheduleOffSignal(15)

for signal, scheduled_time in signalScheduler.lamp_signals:
		print(f"LampSignal(status={'on' if signal.status else 'off'}) at {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}")