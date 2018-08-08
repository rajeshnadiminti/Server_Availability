import requests
import time
import smtplib
from tkinter import *
from tkinter import messagebox

def clicked():
    global url, s
    s = url.get()
    if len(s) == 0:
        messagebox.showerror('Error..!', 'No Entry. Please Enter Valid Hostname or IP Address')
    else:
        messagebox.showinfo('Hostname','Input Successfull')
        input.destroy()

input = Tk()
Label(input, text="Enter the HostName or IP Address").grid(row=0)
url = Entry(input)
url.grid(row=0, column=1)

Button(input, text='Submit', command=clicked).grid(row=2, column=1)

input.mainloop()


print (s)

def web_site_online(s, timeout=5):

    server = smtplib.SMTP(host='smtp.gmail.com', port=587) #Please make sure to change th Gmail settings to allow the less secure apps
    server.starttls()
    email_id = "Enter your Email ID"
    password = "Enter your Password"
    send_to_email = "Enter the email ID of the person you want to send the Notifications to"
    server.login(email_id, password)

    msg = "Server is Down..!"

    try:
        req = requests.get(s, timeout=timeout)
        # HTTP errors are not raised by default, this statement does that
        req.raise_for_status()
        print("connection successful")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
        server.sendmail(email_id, send_to_email, msg)
        server.quit()
        return False

while True:
    web_site_online()
    time.sleep(30)
