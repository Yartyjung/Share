from tkinter import *
import numpy as np

menu_list = np.array(["กระเพราหมูกรอบ","อึ่งอ่างทอด","โจ๊กหมูก้อน","กระเพราหมูกรอบ"])
price_list = np.array([75,200,40,70])
order_list = np.array([0,0,0,0])

def menu1():
    order_list[0] += 1
def menu2():
    order_list[1] += 1
def menu3():
    order_list[2] += 1
def menu4():
    order_list[3] += 1
def checkout():
    root.destroy()
    root2 = Tk()

    root2.geometry("800x800+560+140")
    root2.configure(background="Antiquewhite1")

    la1 = Label(text = "ต.เต้ย & เต๋า โภชนา",font = ("Arial",50), fg="black", bg="turquoise1")
    la1.pack(side=TOP,fill=BOTH)

    la2_1 = Label(text=f"{menu_list[0]} ทั้งหมด {order_list[0]} จาน\n{menu_list[1]} ทั้งหมด {order_list[1]} จาน\n{menu_list[2]} ทั้งหมด {order_list[2]} จาน\n{menu_list[3]} ทั้งหมด {order_list[3]} จาน", font = ("Arial",35), fg="black", bg="orange red")
    la2_1.place(relx = 0.14 , rely=0.2)

    la2_2 = Label(text=f"{price_list[0]}฿ x {order_list[0]}\n{price_list[1]}฿ x {order_list[1]}\n{price_list[2]}฿ x {order_list[2]}\n{price_list[3]}฿ x {order_list[3]}\n รวม : {sum(price_list*order_list)}฿", font = ("Arial",35), fg="black", bg="springgreen2")
    la2_2.place(relx = 0.34 , rely=0.472)

    # btn2_1 = Button(text=f"สั่งใหม่", font = ("Arial",35,"bold"), bg="gray30", fg="black")
    # btn2_1.place(relx = 0.2, rely= 0.52)
    # btn2_2 = Button(text=f" สังต่อ ", font = ("Arial",35,"bold"), bg="gray30", fg="black")
    # btn2_2.place(relx = 0.2, rely= 0.69)

    root2.mainloop()


root = Tk()

root.geometry("800x800+560+140")
root.configure(background="Antiquewhite1")

pic1 = PhotoImage(file="pics/kaprao.png")
pic2 = PhotoImage(file="pics/toad.png")
pic3 = PhotoImage(file="pics/pouridg.png")
pic4 = PhotoImage(file="pics/chicken_rice.png")

la1 = Label(text = "ต.เต้ย & เต๋า โภชนา",font = ("Arial",50), fg="black", bg="turquoise1")
la1.pack(side=TOP,fill=BOTH)

btn1 = Button(text = "กระเพราหมูกรอบ 75฿", image= pic1 , fg="black", bg="OliveDrab1",compound=TOP,font="BOLD",command=menu1)
btn1.place(relx=0.17,rely=0.17)

btn2 = Button(text = "อึ่งอ่างทอด 200฿", image= pic2 , fg="black", bg="OliveDrab1",compound=TOP,font="BOLD",command=menu2)
btn2.place(relx=0.56,rely=0.17)

btn3 = Button(text = "โจ๊กหมูก้อน 40฿", image= pic3 , fg="black", bg="OliveDrab1",compound=TOP,font="BOLD",command=menu3)
btn3.place(relx=0.17,rely=0.5)

btn4 = Button(text = "กระเพราหมูกรอบ 70฿", image= pic4 , fg="black", bg="OliveDrab1",compound=TOP,font="BOLD",command=menu4)
btn4.place(relx=0.56,rely=0.5)

btn5 = Button(text = "เช็กบิล", font=("Arial",25),fg = "black", bg="lightsalmon",command=checkout)
btn5.place(relx=0.425,rely=0.84)

root.mainloop()