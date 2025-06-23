import os
import webbrowser
from tkinter import Tk, Button
# esplora dispositivi
def explore_device():
    """Esplora questo PC"""
    DEVICE_MOUNT_POINT_ONE = "C:\\"
    if os.path.exists(DEVICE_MOUNT_POINT_ONE):
       os.startfile(DEVICE_MOUNT_POINT_ONE)  # Su Windows, apre il percorso nel file explorer
def open_shell():
    """Apre la shell nel browser predefinito."""
    webbrowser.open("index.html")  # Modifica con l'URL corretto della tua shell

def explore_iso():
    """Esplora il contenuto della ISO montata, se esiste."""
    ISO_MOUNT_POINT = "F:\\"  # Modifica con il percorso della tua ISO montata
    if os.path.exists(ISO_MOUNT_POINT):
       os.startfile(ISO_MOUNT_POINT)  # Su Windows, apre il percorso nel file explorer
def change_iso():
    ISO_MOUNT_POINT = "F:\\"  # Ridichiaro un punto di mount per cambiare ISO
    if os.path.exists(ISO_MOUNT_POINT):
         NEW_ISO_MOUNT_POINT = "G:\\"  # Modifica con il percorso della tua ISO montata
    if os.path.exists(NEW_ISO_MOUNT_POINT):
       os.startfile(NEW_ISO_MOUNT_POINT)
       NEXT_MOUNT_POINT = "H:\\"
    if os.path.exists(NEW_ISO_MOUNT_POINT):
        os.startfile(NEW_ISO_MOUNT_POINT)
        FIRST_NEXT_MOUNT_POINT= "I:\\"
    if os.path.exists(FIRST_NEXT_MOUNT_POINT):
       os.startfile(FIRST_NEXT_MOUNT_POINT)
       SECOND_NEXT_MOUNT_POINT= "J:\\"
    if os.path.exists(SECOND_NEXT_MOUNT_POINT):
       os.startfile(SECOND_NEXT_MOUNT_POINT)
def open_file_explorer():
    """Apre Esplora File."""
    os.startfile(os.path.expanduser("~"))  # Apre la home directory dell'utente

# Creazione della finestra principale
root = Tk()
root.title("Utility App")
root.geometry("300x150")

# Bottoni
btn_shell = Button(root, text="Esplora dischi", command=explore_device, width=25)
btn_shell.pack(pady=10)
btn_shell = Button(root, text="Apri Shell", command=open_shell, width=25)
btn_shell.pack(pady=10)

btn_iso = Button(root, text="Esplora ISO", command=explore_iso, width=25)
btn_iso.pack(pady=10)
btn_iso = Button(root, text="Cambia ISO", command=change_iso, width=25)
btn_iso.pack(pady=10)
btn_explorer = Button(root, text="Apri Esplora File", command=open_file_explorer, width=25)
btn_explorer.pack(pady=10)

# Avvio della GUI
root.mainloop()
