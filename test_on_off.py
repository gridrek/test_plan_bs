from on_off import on, off

def test_on():
  result = on()
  assert result == True

def test_off():
  result = off()
  assert result == True
