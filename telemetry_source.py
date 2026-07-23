from config import TELEMETRY_SOURCE
from telemetry import generate_telemetry_packet

def get_telemetry_packet():  # Συνάρτηση η οποία λαμβάνει δεδομένα (telemetry packets) sim or real. 

    if TELEMETRY_SOURCE == "simulation":
        return generate_telemetry_packet() #Καλώ την συνάρτηση και δημιουργώ τα δεδομένα του telemetry packet
    
    if TELEMETRY_SOURCE == "hardware":
        raise NotImplementedError("Hardware telemetry input is not implemented yet.") #Placeholder. Έχω προβλέψει hardware mode αλλά δεν έχει υλοποιηθεί ακόμη.Stby Arduino
    
    raise ValueError(f"Unknown telemetry source: {TELEMETRY_SOURCE}") # Αυτό το χρησιμοποιώ για προστασία, αν στο config εισαχθεί κάτι διαφορετικό να εμφανίσει μήνυμα λάθους.