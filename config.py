# Simulation settings
NUMBER_OF_PACKETS = 5               # Έχω 5 telemetry packets . # Ορίζω πόσα telemetry packets χρειάζομαι (Κεφαλαία λόγω χρήσης ως σταθερής τιμής).
TRANSMISSION_DELAY_SECONDS = 1      # Delay 1 sec μεταξύ των packets

# Satellite identification
SATELLITE_ID = "CUBESAT-001"

# Telemetry warning thresholds
LOW_BATTERY_THRESHOLD_V = 7.2
HIGH_TEMPERATURE_THRESHOLD_C = 40.0
WEAK_SIGNAL_THRESHOLD_DBM = -90

# Log files
CSV_FILE = "telemetry_log.csv"    # Στην σταθερά αποθηκεύω το κείμενο "telemetry_log.csv - string -" (όρίζω το όνομα του αρχείου που θα αποθηκεύονται τα telemetry packets.)
JSON_FILE = "telemetry_log.json"  # Αποθηκεύω στην σταθερά το όνομα του αρχείου.