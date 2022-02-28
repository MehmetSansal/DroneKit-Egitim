from dronekit import connect

import Tkinter as tk
import tkMessageBox

top = tk.Tk()

top.geometry("700x350")



def baglan():
   connection_string = "/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_DN068NZI-if00-port0"
   global iha
   iha = connect(connection_string,wait_ready=True,timeout=100,baud=57600)
   tkMessageBox.showinfo( "Baglanti basarili" )


def heading():
   tkMessageBox.showinfo("Bas aciniz: ",iha.heading)

Baglan = tk.Button(top, text ="Baglan", command = baglan)
headgoster = tk.Button(top, text ="Heading Goster", command = heading)


canvas= tk.Canvas(top, width= 200, height= 100, bg="SpringGreen2")
canvas.create_text(100, 50, text="Imam Degilim YKI", fill="black", font=('Helvetica 15 bold'))
canvas.pack()


Baglan.pack()
headgoster.pack()
top.mainloop()



