# Runze Fluid Control - Quick Start

## Required Python Packages
Install the following packages before running the code:

```sh
pip install matterlab-pumps
pip install "medusa_sdl[all]"
```

## COM Port Definition
- Set your COM port (e.g., `COM3`, `COM4`) in your script when initializing the pump or valve.
- Example:
  ```python
  com_port = "COM3"  # Change to your actual port
  ```

## Valve Selection
- Select the valve position using the appropriate method from the library (see library docs for details).
- Example:
  ```python
  pump.select_valve(position=1)  # Select valve position 1
  ```

## Draw and Dispense Example
- Drawing and dispensing can be done as follows:
  ```python
  pump.draw(volume=100)      # Draw 100 µL
  pump.dispense(volume=100)  # Dispense 100 µL
  ```

Refer to the official documentation for advanced usage and troubleshooting.
