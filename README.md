# Satellite Telemetry Simulator

A Python-based satellite telemetry simulator that generates simulated CubeSat telemetry packets.
![Satellite Telemetry Simulator](assets/satellite-telemetry-banner.png)



## Project Goal

This project simulates basic satellite telemetry data such as battery voltage, current, temperature, altitude, orbital speed, signal strength, and system status.

The goal is to build a clean and progressively more advanced Python portfolio project related to space systems, telemetry, embedded systems, and aerospace software engineering.

The project currently runs in simulation mode, but its structure is prepared for a future hardware telemetry source, such as an Arduino-based sensor node.

## Current Features

- Generates simulated CubeSat telemetry packets
- Uses realistic engineering units
- Displays telemetry data in a readable terminal format
- Generates multiple telemetry packets in sequence
- Adds a transmission delay between packets
- Saves telemetry data to CSV
- Saves telemetry data to JSON
- Detects telemetry warning conditions
- Supports multiple warnings per packet
- Uses a central configuration file for simulation settings and thresholds
- Includes a telemetry source abstraction for future hardware input

## Telemetry Fields

Each telemetry packet includes:

- `timestamp`
- `satellite_id`
- `battery_voltage_v`
- `battery_current_a`
- `temperature_celsius`
- `altitude_km`
- `speed_km_s`
- `signal_strength_dbm`
- `system_status`
- `warnings`

## Warning Conditions

The simulator currently checks the following warning conditions:

| Condition | Threshold | Warning |
|---|---:|---|
| Low battery voltage | `< 7.2 V` | `LOW_BATTERY` |
| High temperature | `> 40.0 °C` | `HIGH_TEMPERATURE` |
| Weak signal | `< -90 dBm` | `WEAK_SIGNAL` |

If one or more warning conditions are detected, the packet status becomes:

```text
WARNING
```

If no warning conditions are detected, the packet status remains:

```text
OK
```

## Example Terminal Output

```text
Satellite Telemetry Packet #1
----------------------------
Timestamp: 2026-07-23T19:35:33
Satellite ID: CUBESAT-001
Battery Voltage: 7.0 V
Battery Current: 0.52 A
Temperature: 1.7 °C
Altitude: 408.66 km
Speed: 7.52 km/s
Signal Strength: -61 dBm
System Status: WARNING
Warnings: LOW_BATTERY
```

## Example CSV Output

```csv
timestamp,satellite_id,battery_voltage_v,battery_current_a,temperature_celsius,altitude_km,speed_km_s,signal_strength_dbm,system_status,warnings
2026-07-23T19:35:33,CUBESAT-001,7.0,0.52,1.7,408.66,7.52,-61,WARNING,LOW_BATTERY
2026-07-23T19:35:34,CUBESAT-001,7.76,0.72,0.6,413.3,7.74,-89,OK,NONE
```

## Example JSON Output

```json
[
    {
        "timestamp": "2026-07-23T19:35:33",
        "satellite_id": "CUBESAT-001",
        "battery_voltage_v": 7.0,
        "battery_current_a": 0.52,
        "temperature_celsius": 1.7,
        "altitude_km": 408.66,
        "speed_km_s": 7.52,
        "signal_strength_dbm": -61,
        "system_status": "WARNING",
        "warnings": [
            "LOW_BATTERY"
        ]
    }
]
```

## Project Structure

```text
satellite-telemetry-simulator/
├── assets/
│   └── satellite-telemetry-banner.png
├── .gitignore
├── README.md
├── config.py
├── logger.py
├── main.py
├── telemetry.py
└── telemetry_source.py
```

## File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Runs the telemetry simulation loop |
| `config.py` | Stores simulation settings, thresholds, and log file names |
| `telemetry.py` | Generates simulated telemetry packets and warning conditions |
| `telemetry_source.py` | Selects the telemetry source, currently simulation mode |
| `logger.py` | Saves telemetry packets to CSV and JSON files |
| `README.md` | Documents the project |
| `assets/` | Stores README images and project media |

## How to Run

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Run the simulator:

```powershell
python main.py
```

The program will generate telemetry packets, display them in the terminal, and create local log files:

```text
telemetry_log.csv
telemetry_log.json
```

These generated log files are ignored by Git.

## Configuration

The main settings are stored in `config.py`:

```python
NUMBER_OF_PACKETS = 5
TRANSMISSION_DELAY_SECONDS = 1

TELEMETRY_SOURCE = "simulation"

SATELLITE_ID = "CUBESAT-001"

LOW_BATTERY_THRESHOLD_V = 7.2
HIGH_TEMPERATURE_THRESHOLD_C = 40.0
WEAK_SIGNAL_THRESHOLD_DBM = -90

CSV_FILE = "telemetry_log.csv"
JSON_FILE = "telemetry_log.json"
```

## Telemetry Source Modes

The project currently supports:

```text
simulation
```

A future hardware mode is planned:

```text
hardware
```

The hardware mode is intended to support real sensor telemetry from an Arduino-based embedded node.

## Roadmap

Planned next steps:

- Improve code organization further
- Add JSON Lines logging option
- Add unit tests
- Add command-line arguments
- Add simple data visualization
- Add Arduino serial telemetry input
- Add a hardware telemetry mode
- Build a small ground-station style dashboard

## Technologies

- Python
- Git
- GitHub
- VS Code
- CSV
- JSON
- Virtual environments

## Project Status

This project is currently in progress.