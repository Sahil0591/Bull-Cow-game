from tkinter import *
import random
import time as t
from tkinter import messagebox
res=[]
def main_window():
    cond = False
    #cond helps to get a random integer above 999


    while cond == False:
        x = 0
        ra = random.randint(1000,9999)
        #integer digits as elements of list
        a = list(map(int, str(ra)))
        for i in range(0, 4):
            cnt = a.count(a[i])
            x = x + cnt
        if (x == 4):
            cond = True
    print(ra)
    window2 = Tk()
    window2.geometry("1536x864")
    window2.configure(bg = "#ffffff")
    window2.title("Bull and Cow")
    labelx = Label(window2, bg="#B6D8FF")
    f = Frame(window2, height=48, width=178, bg="#B6D8FF").place(x=1259, y=561)

    def correction():
        labelq = Label(window2,text = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",fg="#BBFFF3", bg="#BBFFF3").place(x=734,y=774)

    def err():
        labelq = Label(window2,text = "Please enter a four digit number, which is greater than 999 and less than 10000",bg="#BBFFF3").place(x=734,y=774)
        num.clear()
        labelx = Label(window2, text="@@@@", fg="#B6D8FF",bg="#B6D8FF").place(x = 1332, y = 566)

    def checking():
        x = 0
        for i in range(0,4):
            cnt = num.count(num[i])
            #Checking for repeating digits
            x = x + cnt
        if(x == 4):
            c2()
        else:
            labelq = Label(window2,text = "Please enter a unique number, where the digits are non-repeating",bg="#BBFFF3").place(x=734,y=774)
            num.clear()
            labelx = Label(window2, text="@@@@", fg="#B6D8FF",bg="#B6D8FF").place(x = 1332, y = 566)


    cbl = []

    def c2():    
        global res
        global labelx
        count = 0
        cow = 0
        bull = 0
        tc = 0
        tb = 0
        count += 1
        labelx = Label(window2, text="@@@@", fg="#B6D8FF",bg="#B6D8FF").place(x = 1332, y = 566)
            #cond3 is to obtain a unique 4 digit number from the user
        for i in range(0,4):
            
            for j in range(0,4):
                #cow
                if (a[i] == num[i]):
                    tc = tc+1
                    break
                #bull
                elif(a[i] == num[j]):
                    tb = tb+1
                    break
        if tc == 4:
                    print("you win")
                    messagebox.showinfo("CONGRATULATIONS!!!", "You have won the game")        
        s=""
        s = [str(integer) for integer in num]
        a_string = "".join(s)
        #labelx = Label(window2, text=a_string, bg="#B6D8FF").place(x = 1332, y = 566)
        res.append(int(a_string))
        cbl.append([tc,tb,res])
        x_c_init = 851
        y_c_init = 274

        x_b_init = 909
        y_b_init = 274

        x_a_init = 767
        y_a_init = 274
        
        
        for i in cbl:
            labelc = Label(window2,bg="#AFFC94",text=str(i[0])).place(x = x_c_init,y = y_c_init)
            labelb = Label(window2,bg ="#F97373",text=str(i[1])).place(x = x_b_init,y = y_b_init)
            
            labela = Label(window2, bg="#FFFFFF", text=res[count-1]).place(x=x_a_init, y=y_a_init)
            y_a_init+=40
            y_c_init+=40
            y_b_init+=40
            count+=1
            labela = Label(window2, text="Number of attempts : {}".format(count-1),bg="#F8F37D").place(x=1200, y=703)
            if count == 12:
                x_a_init = 975
                x_b_init = 1113
                x_c_init = 1057
                y_a_init,y_b_init,y_c_init = 274,274,274
            elif count == 23:
                labeld = Label(window2,text="You lost, U coundn't figure out the code in 22 tries").place(x=734,y=773)
        #print("Cow = ",tc)
        #print("bull =",tb)
        
        print()
        cow = tc
        
        num.clear()
        
                
    def typx():
        labelx = Label(window2, text="@@@@", fg="#B6D8FF",bg="#B6D8FF").place(x = 1332, y = 566)
        s=""
        s = [str(integer) for integer in num]
        if len(s) < 5:
            a_string = "".join(s)
            labelx = Label(window2, text=a_string,bg="#B6D8FF").place(x = 1332, y = 566)
        else: 
            err()
            
        
    #def create_window():
    num = []
    cow = 0
    bull = 0

    canvas2 = Canvas(
        window2,
        bg = "#ffffff",
        height = 864,
        width = 1536,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas2.place(x = 0, y = 0)
    background_img = PhotoImage(file = f"background1.png")
    background = canvas2.create_image(
        702.0, 523.5,
        image=background_img)
    img0 = PhotoImage(file = f"submit.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [correction() ,checking()] if len(num)==4 and num[0] != 0 else err(),
        relief = "flat")
    b0.place(
        x = 1243, y = 617,
        width = 211,
        height = 65)
    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(0),typx()],
        relief = "flat")
    b1.place(
        x = 1311, y = 471,
        width = 75,
        height = 60)
    img2 = PhotoImage(file = f"img11.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.pop(),typx()],
        relief = "flat")
    b2.place(
        x = 1397, y = 471,
        width = 75,
        height = 60)
    img3 = PhotoImage(file = f"img2.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(1),typx()],
        relief = "flat")
    b3.place(
        x = 1225, y = 245,
        width = 75,
        height = 60)
    img4 = PhotoImage(file = f"img3.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(2),typx()],
        relief = "flat")
    b4.place(
        x = 1311, y = 245,
        width = 75,
        height = 60)
    img5 = PhotoImage(file = f"img4.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(3),typx()],
        relief = "flat")
    b5.place(
        x = 1397, y = 245,
        width = 75,
        height = 60)
    img6 = PhotoImage(file = f"img5.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(4),typx()],
        relief = "flat")
    b6.place(
        x = 1225, y = 320,
        width = 75,
        height = 60)
    img7 = PhotoImage(file = f"img6.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(5),typx()],
        relief = "flat")
    b7.place(
        x = 1311, y = 320,
        width = 75,
        height = 60)
    img8 = PhotoImage(file = f"img7.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(6),typx()],
        relief = "flat")
    b8.place(
        x = 1397, y = 320,
        width = 75,
        height = 60)
    img9 = PhotoImage(file = f"img8.png")
    b9 = Button(
        image = img9,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(7),typx()],
        relief = "flat")
    b9.place(
        x = 1225, y = 395,
        width = 75,
        height = 60)
    img10 = PhotoImage(file = f"img9.png")
    b10 = Button(
        image = img10,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(8),typx()],
        relief = "flat")
    b10.place(
        x = 1311, y = 395,
        width = 75,
        height = 60)
    img11 = PhotoImage(file = f"img10.png")
    b11 = Button(
        image = img11,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [num.append(9),typx()],
        relief = "flat")
    b11.place(
        x = 1397, y = 395,
        width = 75,
        height = 60)
    window2.resizable(True, True)
    window2.mainloop()

