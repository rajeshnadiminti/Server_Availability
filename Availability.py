import matplotlib
matplotlib.use('Agg')
import requests
import time
import smtplib
from smtplib import SMTPException
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def clicked():
    global url, s
    s = url.get()
    if len(s) == 0:
        messagebox.showerror('Error..!', 'No Entry. Please Enter Valid Hostname or IP Address')
        input.destroy()
    else:
        messagebox.showinfo('Hostname','Input Successfull')
        input.destroy()

input = tk.Tk()
Label(input, text="Enter the HostName or IP Address").grid(row=0)
url = Entry(input)
url.grid(row=0, column=1)

Button(input, text='Submit', command=clicked).grid(row=2, column=1)

input.mainloop()

def gmail( ):           #Please make sure to change th Gmail settings to allow the less secure apps
    usermail = user_entry.get()
    receivermail=receiver_entry.get()
    server=smtplib.SMTP('smtp.gmail.com:587')
    pass_word=password.get()
    msg = "Server is Down..!"
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(usermail, pass_word  )
    server.sendmail(usermail,receivermail, msg)
    text.insert(1.0, 'message sent')
    root.destroy()
    server.quit()

#Gui interface

root= tk.Tk()
root.title("Gmail Login")
#user mail
user_email = Label(root, text="Enter your Gmail address:  ")
user_email.grid(row=0, column=0)
user_entry = Entry(root, bd =8)
user_entry.grid(row=0, column=1)


#receiver email
receiver_email = Label(root, text="Enter the recipient's email address:")
receiver_email.grid(row=2, column=0)
receiver_entry = Entry(root, bd =8)
receiver_entry.grid(row=2, column=1)

#password widget
Pass = Label(root, text="Enter your Gmail password:  ")
Pass.grid(row=1, column=0)
password= Entry(root, show='*', bd =8)
password.grid(row=1, column=1)

#submit button
submit_mail = Button(root, bd =8, text="Submit", command=gmail).grid(row=3)

root.mainloop()


def web_site_online():

    try:
        req = requests.get(s)
        # HTTP errors are not raised by default, this statement does that
        req.raise_for_status()
        print("connection successful")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
        gmail()
        return False

while True:
    web_site_online()
    time.sleep(30)
