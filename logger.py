import csv #Εισάγω την βιβλιοθήκη csv. Την χρησιμοποιώ για να γράφω ή να διαβάζω csv αρχεία.
import json # Εισάγω την βιβλιοθήκη json.
import os #Εισάγω την βιβλιοθήκη os. Την χρησιμοποιώ για να ελέγξω αν υπάρχει ήδη το αρχείο telemetry_log.csv.
from config import CSV_FILE, JSON_FILE

def save_telemetry_to_csv(telemetry): # Δημιουργώ την συνάρτηση που δέχεται ως είσοδο ένα telemetry packet
    file_exists = os.path.isfile(CSV_FILE) # Εδώ ελέγχω αν υπάρχει ήδη το αρχείο telemetry_log.csv. Boolean έλεγχος.

    telemetry_for_csv = telemetry.copy() # Δημιουργώ αντίγραφω του telemetry packet επειδή δεν θέλω να αλλάξω το αρχικό telemetry για να μετατρέψω την λίστα warnings σε απλό κείμενο.

    if telemetry_for_csv["warnings"]: # Αν υπάρχουν warnings στην λίστα 

        telemetry_for_csv["warnings"] = ";".join(telemetry_for_csv["warnings"]) # Η λίστα μετατρέπεται σε κείμενο
    else:
        telemetry_for_csv["warnings"] = "NONE"

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file: # Εδώ ανοίγω το αρχείο CSV with open(....) as file: mode="a". Αν δεν υπάρχει το δημιουργώ, Αν υπάρχει γράφω στο τέλος του. άνοιξε το αρχείο και πρόσθεσε νέες γραμμές στο τέλος. newline="" βοηθά ώστε να μην εμφανίζονται κενές γραμμές ανάμεσα στις εγγραφές στο CSV. encoding="utf-8" ορίζει κωδικοποίηση κειμένου. with κλείνει αυτόματα το αρχείο όταν τελειώσουμε
        writer = csv.DictWriter(file, fieldnames=telemetry_for_csv.keys()) # Δημιουργώ writer που ξέρει να γράφει dictionaries σε CSV. fieldnames=telemetry.keys() οι στήλες του CSV θα είναι τα keys του dictionary.

        if not file_exists: #Αν το αρχείο δεν υπήρχε πριν, τότε γράφουμε πρώτα τα headers. Αν το αρχείο υπάρχει ήδη, δεν ξαναγράφουμε headers, για να μην επαναλαμβάνονται μέσα στο αρχείο.
            writer.writeheader() 

        
        writer.writerow(telemetry_for_csv) #Γράφω ένα telemetry packet ως νέα γραμμή στο CSV.

def save_telemetry_to_json(telemetry):  # Δημιουργώ μια συνάρτηση που δέχεται ως είσοδο 1 telemetry packet και το αποθηκεύει σε JSON αρχείο.

    if os.path.isfile(JSON_FILE):       # έλεγχος αν υπάρχει ήδη το αρχείο, γιατί δεν θέλω να σβήσω τα προηγούμενα.

        with open(JSON_FILE, mode="r", encoding="utf-8") as file: # Αν υπάρχει το αρχείο το ανοίγουμε σε read mode "mode = "r" .

            telemetry_data = json.load(file) #  Διαβάζει το περιεχόμενο του json αρχείου και το μετατρέπει σε Python object. To telemetry_data θα είναι λίστα απο dictionaries.
    else:
        telemetry_data = [] # Αν δέν υπάρχει το αρχείο ξεκινάω με άδεια λίστα.

    telemetry_data.append(telemetry) # Προσθέτω νέο telemetry_packet στην λίστα

    with open(JSON_FILE, mode="w", encoding="utf-8") as file: # Ανοίγω το αρχείο σε write mode --mode="w"
        json.dump(telemetry_data, file, indent=4) # Γράφω την λίστα telemetry_data στο αρχείο ως JSON. To indent=4 δημιουργεί εσοχές στο αρχείο JSON.