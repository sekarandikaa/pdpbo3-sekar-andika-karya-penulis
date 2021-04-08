from Buku import Buku
from Novel import Novel
from tkinter import *
from tkinter.messagebox import askyesno, showinfo, showwarning

Karyaa = []

root = Tk()
root.geometry('250x500')
root.title("Tugas Praktikum DPBO Python")
root.resizable(False, False)
root.configure(bg='#393232')

mainMenu = Frame(root)
formMenu = Frame(root)

mainMenu.configure(bg='#393232')
formMenu.configure(bg='#e48257')

def openForm(frame):
    frame.tkraise()

for frame in (mainMenu, formMenu):
    frame.grid(row = 0, column = 0, sticky = 'nsew')

#Menu About
def aboutClick():
    top = Toplevel()
    top.title("About")
    top.configure(bg='#3a6351')

    frame = LabelFrame(top, text="About", padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    frame.configure(bg='#e48257', fg='#393232')

    lblNama = Label(frame, text="Aplikasi Karya Penulis")
    lblNama.pack()
    lblNama.config(font=("Arial", 20))
    lblNama.configure(bg='#e48257', fg="#393232")

    lblDeskripsi = Label(frame, text="Aplikasi yang memiliki fungsi dan tujuan untuk menyimpan data karya para penulis.")
    lblDeskripsi.pack()
    lblDeskripsi.configure(bg='#e48257', fg='#393232')

    lblPembuat = Label(frame, text="Dibuat oleh : 1903970 | Sekar Andika Putri")
    lblPembuat.pack()
    lblPembuat.configure(bg='#e48257', fg='#393232')

# Menyimpan semua data
def saveData():
    # cek data apakah semua terisi
    if ipPenulis.get() == "" or ipJudul.get() == "" or ipTahun.get() == "" or ipPenghargaan.get() == "":
        showwarning("Warning","Wajib isi semua data")
    else:
        if r1.get() == "Buku":
            Karyaa.append(Buku(ipPenulis.get(), r2.get(), ipJudul.get(), ipTahun.get(), genreDrop.get(), bestSeller.get(), ipPenghargaan.get()))
        else:
            Karyaa.append(Novel(ipPenulis.get(), r2.get(), ipJudul.get(), ipTahun.get(), genreDrop.get(), bestSeller.get(), ipPenghargaan.get()))
        # menampilkan message box data berhasil disimpan
        showinfo("Information","Data berhasil disimpan!")
        # mereset area input
        r1.set(None)
        ipPenulis.delete(0, 'end')
        r2.set(None)
        ipJudul.delete(0, 'end')
        ipTahun.delete(0, 'end')
        genreDrop.set("Fiksi")
        bestSeller.set("Not Best Seller")
        ipPenghargaan.delete(0, 'end')

# Menampilkan semua data
def readData():
    topp = Toplevel()
    topp.title("Semua Data")
    topp.configure(bg='#393232')

    #list table heading
    heading = ["No", "Jenis Karya", "Penulis", "Jenis Kelamin", "Judul", "Tahun Rilis", "Genre", "Penghargaan", "Best Seller"]
    
    for col in range(9):
        label = Label(topp, text="" + heading[col], bg="#3a6351", fg="#f2edd7", padx=3, pady=3)
        label.config(font=('Arial', 12))
        label.grid(row=0, column=col, sticky='nsew', padx=1, pady=1)
        topp.grid_columnconfigure(col, weight=1)

    for index, h in enumerate(Karyaa):
        dataTable = [ "", h.getJenis(), h.getPenulis(), h.getJkPenulis(), h.getJudul(), h.getTahunRilis(), h.getGenre(), h.getJmlPenghargaan(), h.getBestSeller()]
        for column in range(9):
            if column == 0:
                label = Label(topp, text=str(index+1), bg="#f2edd7", fg="#393232", padx=3, pady=3)
            else:
                label = Label(topp, text=" " + dataTable[column], bg="white", fg="black", padx=3, pady=3)
            label.config(font=('Arial', 10))
            label.grid(row=index+1, column=column, sticky='nsew', padx=1, pady=1)
            topp.grid_columnconfigure(column, weight=1)

# Menghapus semua data
def deleteAllData():
    answerDelete = askyesno(title='Exit', message='Anda yakin untuk menghapus semua data?')
    if answerDelete:
        Karyaa.clear()
        showinfo("Information","Semua data berhasil dihapus!")

#Exit program
def confirmQuit():
    answerQuit = askyesno(title='Exit', message='Anda yakin untuk keluar?')
    if answerQuit:
        root.destroy()

# Main Menu
lblFrame = LabelFrame(mainMenu, padx=10, pady=10, relief="flat")
lblFrame.pack(padx=10, pady=10)
lblFrame.configure(bg='#393232', fg='#bfcba8')

lblJudul = Label(lblFrame, text="Karya Penulis")
lblJudul.pack()
lblJudul.config(font=("Arial", 25))
lblJudul.config(bg='#393232', fg="#e48257")

lblDeskripsi = Label(lblFrame, text="Menyimpan data karya para penulis")
lblDeskripsi.pack(pady=20)
lblDeskripsi.configure(bg='#393232', fg='#f2edd7')

btnForm = Button(lblFrame, text="Input Data", width=26, command= lambda: openForm(formMenu), borderwidth=2, relief="flat")
btnForm.pack(pady=3)
btnForm.configure(bg='#3a6351', fg='#f2edd7')

btnLihatData = Button(lblFrame, text="Lihat Semua Data", width=26, command=readData, borderwidth=2, relief="flat")
btnLihatData.pack(pady=3)
btnLihatData.configure(bg='#3a6351', fg='#f2edd7')

btnHapusData = Button(lblFrame, text="Hapus Semua Data", width=26, command=deleteAllData, borderwidth=2, relief="flat")
btnHapusData.pack(pady=3)
btnHapusData.configure(bg='#3a6351', fg='#f2edd7')

btnAbout = Button(lblFrame, text="About", width=26, command=aboutClick, borderwidth=2, relief="flat")
btnAbout.pack(pady=3)
btnAbout.configure(bg='#3a6351', fg='#f2edd7')

btnViewData = Button(lblFrame, text="Exit", width=26, command=confirmQuit, borderwidth=2, relief="flat")
btnViewData.pack(pady=3)
btnViewData.configure(bg='#3a6351', fg='#f2edd7')

lblNamaNIM = Label(lblFrame, text="1903970 | Sekar Andika Putri")
lblNamaNIM.pack(pady=150)
lblNamaNIM.configure(bg='#393232', fg='#f2edd7')

# Area Input
opts = LabelFrame(formMenu, padx=10, pady=10)
opts.pack(padx=10, pady=10)
opts.configure(bg='#393232', fg='#bfcba8')

lblJenis = Label(opts, text="Jenis karya :")
lblJenis.pack(anchor=W)
lblJenis.configure(bg='#393232', fg='#f2edd7')

r1 = StringVar()
r1.set(None)

jenis1 = Radiobutton(opts, text="Buku", variable=r1, value="Buku")
jenis1.pack(anchor=W)
jenis1.configure(bg='#393232', fg='#f2edd7', activebackground='#393232', activeforeground='#f2edd7', selectcolor='#393232')

jenis2 = Radiobutton(opts, text="Novel", variable=r1, value="Novel")
jenis2.pack(anchor=W)
jenis2.configure(bg='#393232', fg='#f2edd7', activebackground='#393232', activeforeground='#f2edd7', selectcolor='#393232')

lblPenulis = Label(opts, text="Nama penulis :")
lblPenulis.pack(anchor=W)
lblPenulis.configure(bg='#393232', fg='#f2edd7')

ipPenulis = Entry(opts, width=30)
ipPenulis.pack()

lblJudul = Label(opts, text="Judul karya :")
lblJudul.pack(anchor=W)
lblJudul.configure(bg='#393232', fg='#f2edd7')

ipJudul = Entry(opts, width=30)
ipJudul.pack()

lblTahun = Label(opts, text="Tahun rilis :")
lblTahun.pack(anchor=W)
lblTahun.configure(bg='#393232', fg='#f2edd7')

ipTahun = Entry(opts, width=30)
ipTahun.pack()

lblPenghargaan = Label(opts, text="Penghargaan :")
lblPenghargaan.pack(anchor=W)
lblPenghargaan.configure(bg='#393232', fg='#f2edd7')

ipPenghargaan = Entry(opts, width=30)
ipPenghargaan.pack()

lblGender = Label(opts, text="Gender :")
lblGender.pack(anchor=W)
lblGender.configure(bg='#393232', fg='#f2edd7')

r2 = StringVar()
r2.set(None)

gender1 = Radiobutton(opts, text="Pria" , value="Pria" , variable=r2)
gender2 = Radiobutton(opts, text="Wanita", value="Wanita", variable=r2)

gender1.pack(anchor=W)
gender2.pack(anchor=W)

gender1.configure(bg='#393232', fg='#f2edd7', activebackground='#393232', activeforeground='#f2edd7', selectcolor='#393232')
gender2.configure(bg='#393232', fg='#f2edd7', activebackground='#393232', activeforeground='#f2edd7', selectcolor='#393232')

bestSeller = StringVar(value="Not Best Seller")

c = Checkbutton(opts, text="Best Seller Product", variable=bestSeller, onvalue="Best Seller", offvalue="Not Best Seller")
c.pack(anchor=W)
c.configure(bg='#393232', fg='#f2edd7', activebackground='#393232', activeforeground='#f2edd7', selectcolor='#393232')

lblGenre = Label(opts, text="Genre :")
lblGenre.pack(anchor=W)
lblGenre.configure(bg='#393232', fg='#f2edd7')

genreDrop = StringVar()
genreDrop.set("Fiksi")

drop = OptionMenu(opts, genreDrop, "Fiksi", "Romantis", "Horror", "Edukasi", "Sains")
drop.config(width=25)
drop.pack(anchor=W)
drop.configure(bg='#393232', fg='#f2edd7', activebackground='#393232', activeforeground='#f2edd7', highlightthickness=0)
drop["menu"].config(bg='#393232', fg='#f2edd7', activebackground='#e48257', activeforeground='#f2edd7')

btnSubmit = Button(opts, text="Submit", width=26, command=saveData, borderwidth=2, relief="flat")
btnSubmit.pack(pady=2)
btnSubmit.configure(bg='#3a6351', fg='#f2edd7')

btnBack = Button(opts, text="Back to Menu", width=26, command= lambda: openForm(mainMenu), borderwidth=2, relief="flat")
btnBack.pack(pady=2)
btnBack.configure(bg='#3a6351', fg='#f2edd7')

mainMenu.tkraise()
root.mainloop()