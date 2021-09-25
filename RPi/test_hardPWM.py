import time
import core
import RPi.GPIO_DEVEL as GPIO_DEVEL
import pytest

def test_init():
    GPIO_DEVEL.Reset()
    core.setmode(core.BCM)
    foo = core.HardwarePWM(19, 1)
    assert foo is foo

    with pytest.raises(ValueError) as e:
        bar = core.HardwarePWM(666, 1)
    assert "The channel sent is invalid" in str(e.value)

    with pytest.raises(ValueError) as e:
        bar = core.HardwarePWM(-1, 1)
    assert "The channel sent is invalid" in str(e.value)
    
    with pytest.raises(RuntimeError) as e:
        bar = core.HardwarePWM(19, 1)
    assert "object already exists" in str(e.value)

    with pytest.raises(ValueError) as e:
        bar = core.HardwarePWM(18, -1)
        assert bar is bar
    assert "greater than 0.0" in str(e.value)

"""
def test_start_stop():
    GPIO_DEVEL.Reset()
    # core.setmode(core.BCM)

    foo = core.HardwarePWM(18, 100)

    with pytest.raises(ValueError) as e:
        foo.start(-1)
    assert "dutycycle must have a value from 0.0 to 100.0" in str(e.value)

    with pytest.raises(ValueError) as e:
        foo.start(101)
    assert "dutycycle must have a value from 0.0 to 100.0" in str(e.value)

    assert foo.start(50)

    # Can't run start twice but it won't raise an exception
    # with pytest.warns(Warning):
        # assert foo.start(51) is False

    time.sleep(.2)
    foo.stop()

    time.sleep(.2)
    foo.stop()
"""

def test_change_attributes():

    GPIO_DEVEL.Reset()
    # GPIO.setmode(GPIO.BCM)

    foo = core.HardwarePWM(18, 100)

    foo.start(50)
    time.sleep(.2)

    foo.ChangeFrequency(100)
    foo.ChangeDutyCycle(100)

    with pytest.raises(ValueError) as e:
        foo.ChangeFrequency(-666)
    assert "greater than 0.0" in str(e.value)

    with pytest.raises(ValueError) as e:
        foo.ChangeDutyCycle(-666)
    assert "from 0.0 to 100.0" in str(e.value)

    with pytest.raises(ValueError) as e:
        foo.ChangeDutyCycle(666)
    assert "from 0.0 to 100.0" in str(e.value)

    time.sleep(.2)
    foo.stop()
