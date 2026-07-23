import random                   # Χρησιμοποιώ/ εισάγω βιβλιοθήκη random
from datetime import datetime   # Από τη βιβλιοθήκη datetime, φέρε μου το εργαλείο datetime. Απαραίτητο για χρονική σήμανση στο telemetry packet.
from config import SATELLITE_ID, LOW_BATTERY_THRESHOLD_V, HIGH_TEMPERATURE_THRESHOLD_C, WEAK_SIGNAL_THRESHOLD_DBM

def determine_warnings(battery_voltage_v, temperature_celsius, signal_strength_dbm): # Δημιουργώ την συνάρτηση για έλεγχο συγκεκριμένων τιμών
    warnings = [] # Δημιουργώ μια άδεια λίστα απο warnings

    if battery_voltage_v < LOW_BATTERY_THRESHOLD_V:
        warnings.append("LOW_BATTERY") # Με το warnings.append("") προσθέτω ένα στοιχείο συναγερμού κάθε φορά στο τέλος της λίστας.

    if temperature_celsius > HIGH_TEMPERATURE_THRESHOLD_C:
        warnings.append("HIGH_TEMPERATURE")

    if signal_strength_dbm < WEAK_SIGNAL_THRESHOLD_DBM:
        warnings.append("WEAK_SIGNAL")

    return warnings

def generate_telemetry_packet(): # Ορίζω την συνάρτηση με το αντίστοιχο όνομα. def-> define. : 
    
    battery_voltage_v = round(random.uniform(7.0, 8.4), 2) # Εδώ, σε κάθε μεταβλητή αποθηκεύω την τιμή που δημιουργείται....
    battery_current_a = round(random.uniform(0.2, 1.2), 2) # μετά γίνεται ο έλεγχγος και...
    temperature_celsius = round(random.uniform(-10.0, 45.0), 1) # μετά να την βάλουμε στο packet
    altitude_km = round(random.uniform(390.0, 420.0), 2)
    speed_km_s = round(random.uniform(7.5, 7.8), 2)
    signal_strength_dbm = random.randint(-95, -55)
    # random.uniform(7.0, 8.4) παράγει τυχαίο δεκαδικό αριθμό από 7.0 μέχρι 8.4. round(..., 2) για να κρατήσουμε μόνο 2 δεκαδικά ψηφία.
    # random.randint(-95, -55) παράγει τυχαίο ακέραιο αριθμό

    warnings = determine_warnings(battery_voltage_v,temperature_celsius,signal_strength_dbm)

    if warnings:                    # Αν είναι αληθής(έχει έστω και 1 στοιχείο στην λίστα) τότε αποθηκεύει στην μεταβλητή system_status = "WARNING" διαφορετικά είναι άδεια οπότε είναι οκ
        system_status = "WARNING"
    else:
        system_status = "OK"

    packet = {                   # Δημιουργώ μια μεταβλητή packet και μέσα βάζω ένα Dictionary όπου έχω δομή δεδομένων με ζεύγη -> κλειδί : τιμή
        "timestamp": datetime.now().isoformat(timespec="seconds"), # 1. datetime.now() λαμβάνω τρέχουσα ημερ. και ώρα 2. isoformat μετατροπή σε καθαρή μορφή κειμένου 3.timespec="seconds" ακρίβεια έως και δευτερόλεπτα
        "satellite_id": SATELLITE_ID,
        "battery_voltage_v": battery_voltage_v, 
        "battery_current_a": battery_current_a,
        "temperature_celsius": temperature_celsius,
        "altitude_km": altitude_km,
        "speed_km_s": speed_km_s,
        "signal_strength_dbm": signal_strength_dbm, 
        "system_status": system_status,
        "warnings": warnings
    }

    return packet # Επιστρέφω το packet που έφτιαξα όταν το καλέσω


