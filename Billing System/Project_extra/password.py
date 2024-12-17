from tkinter import *
w5=Tk()
#w5 = Toplevel()
w5.title("Enter your Password")
w5.geometry("400x200")
w5.configure(bg="#2d9290")

cartframe=Frame(w5,bd=5,relief=GROOVE)
cartframe.place(x=50,y=45,width=300,height=60)

cartlabel=Label(cartframe,text="Enter cart number: " ,font=("Times New Roman",15))
cartlabel.place(x=5,y=12)

enpass= Entry(cartframe,font=("Times New Roman",15),bd=5,relief=GROOVE,bg="#2d9290")
enpass.place(x=180,y=8,width=90)

cartbtn=Button(w5,text="Enter" , font=("Times New Roman",15),bd=5,relief=GROOVE)
cartbtn.place(x=150,y=130,width=100)
w5.mainloop()