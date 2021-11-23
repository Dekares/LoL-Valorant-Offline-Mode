from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import os,ctypes

tk = Tk()

tk.geometry("600x200")
tk.title("LoL - Valorant Game Offline Mode")
tk['background'] = "#313131"
tk.resizable(False, False)

# LoL sohbet sunucuları
dict_servers = {
    "TR": "172.65.202.166",  # TR
    "EUNE": "172.65.223.136",  # EUNE
    "EUW": "172.65.252.238",  # EUW
    "JP": "172.65.217.212",  # JP
    "KR": "172.65.226.99",  # KR
    "LAN": "172.65.250.49",  # LAN
    "LAS": "172.65.194.233",  # LAS
    "NA": "172.65.244.155",  # NA
    "OCE": "172.65.208.61",  # OCE
    "PBE": "172.65.223.16",  # PBE
    "RU": "172.65.192.156",  # RU
    "BR": "172.65.212.1"  # BR
}

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def online():
    server = servers.get()
    if server == "":
        showinfo(title="Feedback", message=f"You must choose one server!")
    else:
        os.system(f'netsh advfirewall firewall delete rule name="lolchat{server}"')
        showinfo(title="Feedback", message=f"You are online on {server} server")


def offline():
    server = servers.get()
    if server == "":
        showinfo(title="Feedback", message=f"You must choose one server!")
    else:
        os.system(
            f'netsh advfirewall firewall add rule name="lolchat{server}" dir=out remoteip={dict_servers[server]} protocol=TCP action=block')
        showinfo(title="Feedback", message=f"You are offline on {server} server")


myInfoText = Label(tk, text="Press 'Offline!' for offline, press 'Online!' for online.",
                   font="Arial 10", bg="#313131", fg="white")
button_online = Button(tk, text="Online!", font="Arial",
                       command=online, bg="red", fg="white", height=1, width=13)
button_offline = Button(tk, text="Offline!", font="Arial",
                        command=offline, bg="red", fg="white", height=1, width=13)
exitButton = Button(tk, text="Exit", font="Arial",
                    command=tk.destroy, bg="red", fg="white", height=1, width=13)
servers = ttk.Combobox(tk, font="Arial 15", values=list(dict_servers.keys()))

myInfoText.place(x=30, y=110)  # Bilgilendirme yazısı
button_online.place(x=300, y=55)  # Online butonu
button_offline.place(x=450, y=55)  # Offline butonu
exitButton.place(x=400, y=100)  # Çıkış butonu
servers.place(x=30, y=55)  # Sunucuların bulunduğu combobox

if isAdmin():
    tk.mainloop()
else:
    showinfo(title="Feedback", message=f"You should start as administrator!")


