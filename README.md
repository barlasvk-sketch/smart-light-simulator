# Smart Lighting Simulator

This project is a simple Python script that simulates the logic of a smart lighting system. It runs entirely in the terminal without any physical hardware.

The system's logic is based on two simulated sensors:
1.  **A PIR Motion Sensor:** Detects if someone is in the room.
2.  **An LDR Light Sensor:** Measures the ambient light level in the room.

## The Logic

The script decides whether to turn the light "ON" or "OFF" based on one simple rule:

**IF** `motion is detected` **AND** `the room is dark` **THEN** `turn the light ON`.

In all other cases (no motion, or it's already bright enough), the light will be "OFF".

## How to Run

1.  Make sure you have Python installed.
2.  Clone or download the `smart_light.py` file.
3.  Run the script from your terminal:

```bash
python smart_light.py
