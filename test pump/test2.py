# pip install medusa_sdl[all]
from time import sleep
from matterlab_pumps import RunzePump

COM_PORT = "COM9"
ADDR = 0
SYRINGE_VOL_L = 1e-3   # liters
NUM_PORTS = 6

pump = RunzePump(
    COM_PORT, ADDR, SYRINGE_VOL_L, NUM_PORTS,
    top_speed_ml=0.30,   # raise if you want speed up to 0.20 mL/s
    timeout=1.0          # a bit more tolerant than the default 0.2 s
)

def retry_on_busy(func, *args, retries=15, delay=0.2, **kwargs):
    # Retry when the device reports BUSY (OSError with 'No Error')
    for _ in range(retries):
        try:
            return func(*args, **kwargs)
        except OSError as e:
            if "No Error" in str(e):
                sleep(delay)
                continue
            raise
    raise TimeoutError("Pump stayed busy too long.")

try:
    # DO NOT manually move the valve first; pass valve_port in the call:
    retry_on_busy(pump.draw,     volume=0.30, valve_port=1, speed=0.05)
    retry_on_busy(pump.dispense, volume=0.30, valve_port=2, speed=0.05)

finally:
    if hasattr(pump, "close"): pump.close()
    elif hasattr(pump, "disconnect"): pump.disconnect()
