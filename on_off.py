from lampSignal import LampSignal

def on() -> bool:
	signal = LampSignal(True)
	return signal.send()

def off():
	signal = LampSignal(True)
	return signal.send()
