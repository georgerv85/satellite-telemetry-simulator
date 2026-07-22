import random                   # Χρησιμοποιώ/ εισάγω βιβλιοθήκη random
from datetime import datetime   # Από τη βιβλιοθήκη datetime, φέρε μου το εργαλείο datetime. Απαραίτητο για χρονική σήμανση στο telemetry packet.

def determine_system_status(battery_voltage_v, temperature_celsius, signal_strength_dbm): # Δημιουργώ την συνάρτηση για έλεγχο συγκεκριμένων τιμών

    if battery_voltage_v < 7.2:
        return "LOW_BATTERY"

    if temperature_celsius > 40.0:
        return "HIGH_TEMPERATURE"

    if signal_strength_dbm < -90:
        return "WEAK_SIGNAL"

    return "OK"

def generate_telemetry_packet(): # Ορίζω την συνάρτηση με το αντίστοιχο όνομα. def-> define. : Από την επόμενη γραμμή αρχίζει το σώμα της συνάρτησης
    
    battery_voltage_v = round(random.uniform(7.0, 8.4), 2) # Εδώ, σε κάθε μεταβλητή αποθηκεύω την τιμή που δημιουργείται....
    battery_current_a = round(random.uniform(0.2, 1.2), 2) # μετά γίνεται ο έλεγχγος και...
    temperature_celsius = round(random.uniform(-10.0, 45.0), 1) # μετά να την βάλουμε στο packet
    altitude_km = round(random.uniform(390.0, 420.0), 2)
    speed_km_s = round(random.uniform(7.5, 7.8), 2)
    signal_strength_dbm = random.randint(-95, -55)
    # random.uniform(7.0, 8.4) παράγει τυχαίο δεκαδικό αριθμό από 7.0 μέχρι 8.4. round(..., 2) για να κρατήσουμε μόνο 2 δεκαδικά ψηφία.
    # random.randint(-95, -55) παράγει τυχαίο ακέραιο αριθμό
    
    system_status = determine_system_status(battery_voltage_v, temperature_celsius, signal_strength_dbm) #Καλώ την συνάρτηση (έχω πάρει τις τιμές απο πάνω),γίνεται έλεγχος και το αποτέλεσμα αποθηκεύεται στην μεταβλητή system_status

    packet = {                   # Δημιουργώ μια μεταβλητή packet και μέσα βάζω ένα Dictionary όπου έχω δομή δεδομένων με ζεύγη -> κλειδί : τιμή
        "timestamp": datetime.now().isoformat(timespec="seconds"), # 1. datetime.now() λαμβάνω τρέχουσα ημερ. και ώρα 2. isoformat μετατροπή σε καθαρή μορφή κειμένου 3.timespec="seconds" ακρίβεια έως και δευτερόλεπτα
        "satellite_id": "CUBESAT-001",
        "battery_voltage_v": battery_voltage_v, 
        "battery_current_a": battery_current_a,
        "temperature_celsius": temperature_celsius,
        "altitude_km": altitude_km,
        "speed_km_s": speed_km_s,
        "signal_strength_dbm": signal_strength_dbm, 
        "system_status": system_status
    }
    return packet # Επιστρέφω το packet που έφτιαξα όταν το καλέσω


