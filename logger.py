import csv #Εισάγω την βιβλιοθήκη csv. Την χρησιμοποιώ για να γράφω ή να διαβάζω csv αρχεία.
import os #Εισάγω την βιβλιοθήκη os. Την χρησιμοποιώ για να ελέγξω αν υπάρχει ήδη το αρχείο telemetry_log.csv.

CSV_FILE = "telemetry_log.csv" # Στην σταθερά όρίζω το όνομα του αρχείου που θα αποθηκεύονται τα telemetry packets.

def save_telemetry_to_csv(telemetry): # Δημιουργώ την συνάρτηση που δέχεται ως είσοδο ένα telemetry packet
    file_exists = os.path.isfile(CSV_FILE) # Εδώ ελέγχω αν υπάρχει ήδη το αρχείο telemetry_log.csv. Boolean έλεγχος.

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file: # Εδώ ανοίγω το αρχείο CSV with open(....) as file: mode="a" άνοιξε το αρχείο και πρόσθεσε νέες γραμμές στο τέλος. newline="" βοηθά ώστε να μην εμφανίζονται κενές γραμμές ανάμεσα στις εγγραφές στο CSV. encoding="utf-8" ορίζει κωδικοποίηση κειμένου. with κλείνει αυτόματα το αρχείο όταν τελειώσουμε
        writer = csv.DictWriter(file, fieldnames=telemetry.keys()) # Δημιουργώ writer που ξέρει να γράφει dictionaries σε CSV. fieldnames=telemetry.keys() οι στήλες του CSV θα είναι τα keys του dictionary.

        if not file_exists: #Αν το αρχείο δεν υπήρχε πριν, τότε γράφουμε πρώτα τα headers. Αν το αρχείο υπάρχει ήδη, δεν ξαναγράφουμε headers, για να μην επαναλαμβάνονται μέσα στο αρχείο.
            writer.writeheader() 

            writer.writerow(telemetry) #Γράφω ένα telemetry packet ως νέα γραμμή στο CSV.