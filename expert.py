from tkinter import *
from win10toast import ToastNotifier

def send_notification(msg):
    toaster = ToastNotifier()
    toaster.show_toast("Demo Notification", msg)

root = Tk()
root.geometry("300x300")

msg = Entry(root, width = 30)
msg.place(x = 20, y = 30)

button = Button(root, text = "Send Notification", bg = "brown", fg = "white", command = lambda : send_notification(msg.get()))
button.place(x = 110, y = 200)

root.mainloop()
