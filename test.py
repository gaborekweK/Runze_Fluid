from matterlab_pumps import RunzePump
import inspect

COM_PORT = "COM9"       # Port
ADDR = 0                # DIP/address on the back; 0 is common default
SYRINGE_VOL_L = 1e-3    # 1 mL syringe -> liters here only
NUM_PORTS = 6           # 6-way valve

# init (adjust param names if your installed version differs) 
pump = RunzePump(
    com_port=COM_PORT,
    address=ADDR,
    syringe_volume=SYRINGE_VOL_L,   
    num_valve_port=NUM_PORTS       
)

try:
    pump.draw(volume=0.60, port=1, speed=0.20)     # draw 0.50 mL from valve port 1 at 0.40 mL/s

    pump.dispense(volume=0.60, port=2, speed=0.20)  #  dispense 0.50 mL to valve port 2 at 0.40 mL/s

finally:
    if hasattr(pump, "close"):
        pump.close()
    elif hasattr(pump, "disconnect"):
        pump.disconnect()
