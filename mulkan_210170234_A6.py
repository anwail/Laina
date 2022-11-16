from tkinter import *
window=Tk()
# contoh kode

x,y = 12, 18
result = y if x&1==0 else X
print(result)

window.title('kuis')
lbl=Label(window, text="Hasilnya adalah=18", fg='blue', font=("Helvetica", 16))
lbl.place(x=50, y=50)
window.geometry("300x200+10+20")
window.mainloop()