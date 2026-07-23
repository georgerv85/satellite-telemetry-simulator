import time # Φέρνουμε στην Python την βιβλιοθήκη time
from telemetry import generate_telemetry_packet #Από το αρχείο telemetry.py, φέρε μου τη συνάρτηση generate_telemetry_packet
from logger import save_telemetry_to_csv, save_telemetry_to_json
from config import NUMBER_OF_PACKETS, TRANSMISSION_DELAY_SECONDS


for packet_number in range(1, NUMBER_OF_PACKETS + 1): #με NUMBER_OF_PACKETS = 5, γίνεται ουσιαστικά: range(1, 6) Στην Python το range(1, 6) δίνει: 1, 2, 3, 4, 5
    telemetry = generate_telemetry_packet() # Εκτελώ την συνάρτηση και την αποθηκεύω στην μεταβλητή telemetry

    save_telemetry_to_csv(telemetry)
    save_telemetry_to_json(telemetry)

    print(f"Satellite Telemetry Packet #{packet_number}")
    print("--------------------------")
    print(f"Timestamp: {telemetry['timestamp']}") # Το f πριν από τα εισαγωγικά επιτρέπει να βάλουμε μεταβλητές ή εκφράσεις μέσα στο κείμενο με {telemetry['timestamp']}. 2. telemetry['timestamp'] παίρνω συγκεκριμένη τιμή απο το Dictionary
    print(f"Satellite ID: {telemetry['satellite_id']}")
    print(f"Battery Voltage: {telemetry['battery_voltage_v']} V") # Λόγω του f θα εμφανίσει μετά την τιμή της μεταβλητής battery_voltage_v και στο τέλος το χαρακτηριστικό V.
    print(f"Battery Current: {telemetry['battery_current_a']} A")
    print(f"Temperature: {telemetry['temperature_celsius']} °C")
    print(f"Altitude: {telemetry['altitude_km']} km")
    print(f"Speed: {telemetry['speed_km_s']} km/s")
    print(f"Signal Strength: {telemetry['signal_strength_dbm']} dBm")
    print(f"System Status: {telemetry['system_status']}")
    # Συνεπώς εμφανίζει για αρχή απλό κείμενο όπως: Battery Voltage: και στην συνέχεια την τιμή της μεταβητής με το ειδικό χαρακτηριστικό στο τέλος


    if telemetry["warnings"]:
        print(f"Warnings: {', '.join(telemetry['warnings'])}") # Το join() ενώνει τα στοιχεία της λίστας με το κείμενο που το δίνουμε
    else:
        print("Warnings: None")

    print()                                             # Αφήνω κενή γραμμή.

    time.sleep(TRANSMISSION_DELAY_SECONDS)
