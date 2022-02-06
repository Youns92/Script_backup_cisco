from tkinter import *
from tkinter import messagebox
import sys
import time
import os
import cmd
import datetime
import paramiko as paramiko




def run():
    messagebox.showinfo('information', 'En cours...')
    time.sleep(1)
    backup_switch()



# script backup
def backup_switch():
    now = datetime.datetime.now()
    user = username1.get()
    password = password1.get()
    now = datetime.datetime.now()
    enable_password = en_password1.get()
    port = 22
    f0 = open('cisco.txt')
    for ip in f0.readlines():
        ip = ip.strip()
        filename_prefix ='/Users/Administrateur/Documents' + ip
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip,port, user, password, look_for_keys=False)
            pass
        except  paramiko.ssh_exception.NoValidConnectionsError:
            messagebox.showinfo('error', 'Une tentative de connexion a échoué car le parti connecté n’a pas répondu convenablement')
            break
        except paramiko.ssh_exception.AuthenticationException:
            messagebox.showinfo('error', 'Authentication failed.')
            break
        chan = ssh.invoke_shell()
        time.sleep(2)
        chan.send('enable\n')
        chan.send(enable_password +'\n')
        time.sleep(1)
        chan.send('term len 0\n')
        time.sleep(1)
        chan.send('sh run\n')
        time.sleep(20)
        output = chan.recv(999999)
        filename = "%s_%.2i%.2i%i_%.2i%.2i%.2i" % (ip,now.year,now.month,now.day,now.hour,now.minute,now.second)
        f1 = open(filename, 'a')
        f1.write(output.decode("utf-8") )
        messagebox.showinfo('information', 'Backup sauvegarder')
        f1.close()
        ssh.close()
        f0.close()

def cisco():
    fichier = open("cisco.txt", "w")




# Configuration de la fenetre tk
window = Tk()

window.title("Cisco Backup")


window.geometry('720x480')
window.minsize(480, 360)
window.config(background='#3C81AA')

frame = Frame(window, bg='#3C81AA')

#Titre app
lbl = Label(window, text="Cisco Backup", font=("Berlin Sans FB Demi", 30), bg='#3C81AA', fg="black")
lbl.pack()
lbl1 = Label(window, text="", font=("Arial Black", 8), bg='#3C81AA', fg="white")
lbl1.pack()

# champ username
username = Label(window, text="Username:", font=("Arial Black", 10), bg='#3C81AA', fg="black")
username.pack(side=TOP)

username1 = Entry(window, font=("Arial Black", 10), bg='#3C81AA', fg="black")
username1.pack(side=TOP)



#champ password
password = Label(window, text="Password:", font=("Arial Black", 10), bg='#3C81AA', fg="black")
password.pack(side=TOP)

var_texte = StringVar()
password1 = Entry(window,font=("Arial Black", 10), textvariable=var_texte, bg='#3C81AA', fg="black", show="*")
password1.pack(side=TOP)





#enable password
en_password = Label(window, text="Enable Password:", font=("Arial Black", 10), bg='#3C81AA', fg="black", )
en_password.pack(side=TOP)

en_password1 = Entry(window, font=("Arial Black", 10), bg='#3C81AA', fg="black", show="*")
en_password1.pack(side=TOP)



#version produit
version = Label(window, text="Version 1.0", font=("Arial Black", 10), bg='#3C81AA', fg="black")
version.pack(side=TOP)

# boutton Backup
backup = Button(window, text="Backup", command=run)
backup.pack(expand=YES)

# menu barre
menu_bar = Menu(window)
file = Menu(menu_bar, tearoff=0)
file.add_command(label="Nouveau", command=cisco)
file.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file)
window.config(menu=menu_bar)




window.mainloop()

