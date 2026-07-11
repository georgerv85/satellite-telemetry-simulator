from telemetry import generate_telemetry_packet #Από το αρχείο telemetry.py, φέρε μου τη συνάρτηση generate_telemetry_packet

NUMBER_OF_PACKETS = 5 # Ορίζω πόσα telemetry packets χρειάζομαι (Κεφαλαία λόγω χρήσης ως σταθερής τιμής)


for packet_number in range(1, NUMBER_OF_PACKETS + 1):
    telemetry = generate_telemetry_packet() # Εκτελώ την συνάρτηση και την αποθηκεύω στην μεταβλητή telemetry π

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
    print()                                             # Αφήνω κενή γραμμή
# Συνεπώς εμφανίζει για αρχή απλό κείμενο όπως: Battery Voltage: και στην συνέχεια την τιμή της μεταβητής με το ειδικό χαρακτηριστικό στο τέλος
