import tkinter as tk            
from tkinter import font  as tkfont
from tkinter import *
from tkinter import messagebox 
import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="1234",
  database="PROJECT"
)
mycursor =mydb.cursor()
city1=""

userna1=""
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self,bg="Navy Blue")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageZero,PageOne,PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven,PageEight,PageNine,PageTen,PageEleven,PageTwelve,PageThirteen,PageFourteen,PageFifteen,PageSixteen,PageSeventeen,PageEighteen):
            page_name = F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label = tk.Label(self, text="RESTAURANT    MANAGEMENT   SYSTEM",width='299',font=('Amigos',40))
        label.pack(side="top", fill="x", pady=30)
    

        button1 = tk.Button(self, text="CUSTOMER",bg="Navy Blue",fg="White",font=('Amigos',30),width=25,relief=FLAT,height=3,
                            command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(self, text="ADMIN",font=('Amigos',30),fg="White",width=25,height=3,bg="Navy Blue",relief=FLAT,
                            command=lambda: controller.show_frame("PageNine"))
        button1.pack(side="left",padx=140,pady=10)
        button2.pack(side="right",padx=140,pady=10)
        
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label = tk.Label(self, text="CUSTOMER",width='299',bg='White',font=('Amigos',40))
        label.pack(side="top", fill="x", pady=30)
        button1 = tk.Button(self, text="LOGIN",width=10,height=3,bg='Navy Blue',fg='White',relief=FLAT,font=('Amigos',25),
                            command=lambda: controller.show_frame("PageThree"))
        button2 = tk.Button(self, text="SIGN UP",width=10,height=3,bg='Navy Blue',fg='White',relief=FLAT,font=('Amigos',25),
                            command=lambda: controller.show_frame("PageZero"))
        button1.place(relx=.3, rely=.5, anchor="c")
        button2.place(relx=.7, rely=.5, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=2,fg="Navy Blue",bg="White",font=('Amigos',15),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.1, rely=.1, anchor="c")
        

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        global userna1
        label5 = tk.Label(self, text="Customer Log In", fg="Navy Blue",bg='White',font=("Amigos",40))
        label5.pack(side="top", fill="x", pady=30)
        label6 = tk.Label(self, text="Username",bg="Navy Blue",fg='White',font=("Amigos",40))
        label6.place(relx=.4, rely=.3, anchor="c")
        a=tk.StringVar()
        userna=tk.StringVar()
        entry1=tk.Entry(self,textvariable=userna,width=25)
        entry1.place(relx=.6, rely=.3, anchor="c")
        label7 = tk.Label(self, text="Password",bg="Navy Blue",fg='White',font=("Amigos",40))
        label7.place(relx=.4, rely=.5, anchor="c")
        password=tk.StringVar()
        entry1=tk.Entry(self,textvariable=password,width=25)
        entry1.place(relx=.6, rely=.5, anchor="c")
        sql = "select cid,password from customer"
        mycursor.execute(sql)
        fdata = mycursor.fetchall()
        
        
            
        def up():
            global userna1
            z=0
            k=0
            m=0
            x=userna.get()
            userna1=x
            y=password.get()
            for i  in fdata:
                if (x,y) in fdata:
                    z=z+1
                    m=x
                if x in i:
                    k=x
            sql = "select * from customer"
            mycursor.execute(sql)
            results = mycursor.fetchall()
            if x == '' or y == '' :
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            elif(k!=x):
                tk.messagebox.showinfo("Warning", "Sign up first")
            elif(m!=x):
                tk.messagebox.showinfo("Warning", "Wrong password")
            else:
                tk.messagebox.showinfo("Success", "logged in" )
                controller.show_frame("PageFour")       
                
        
        
        button1 = tk.Button(self, text="LOGIN",width=10,height=3,fg='White',bg="Navy Blue",font=('Amigos',30),relief=FLAT,
                            command=up)    
        button1.place(relx=.6, rely=.7, anchor="c")
        button3 = tk.Button(self, text="BACK",width=10,height=3,fg='White',bg="Navy Blue",font=('Amigos',30),relief=FLAT,
                            command=lambda: controller.show_frame("PageTwo"))
        button3.place(relx=.4, rely=.7, anchor="c")
    #def user(self):
    #print(self.username)
    #user()


class PageZero(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label5 = tk.Label(self, text="Enter Details", fg="Navy Blue",bg='White',font=("Amigos",40))
        label5.pack(side="top", fill="x", pady=30)
        label1 = tk.Label(self, text="NAME",  bg="Navy Blue",fg='White',font=("Amigos",17))
        label1.place(relx=.4, rely=.3, anchor="c")
        name=tk.StringVar()
        entry1=tk.Entry(self,textvariable=name,width=25,)
        entry1.place(relx=.6, rely=.3, anchor="c")
        label2 = tk.Label(self, text="USERNAME",  bg="Navy Blue",fg='White',font=("Amigos",17))
        label2.place(relx=.4, rely=.4, anchor="c")
        us=tk.StringVar()
        entry1=tk.Entry(self,textvariable=us,width=25,)
        entry1.place(relx=.6, rely=.4, anchor="c")
        label3 = tk.Label(self, text="PASSWORD", bg="Navy Blue",fg='White',font=("Amigos",17))
        label3.place(relx=.4, rely=.5, anchor="c")
        pas=tk.StringVar()
        entry1=tk.Entry(self,textvariable=pas,width=25,)
        entry1.place(relx=.6, rely=.5, anchor="c")
        label4 = tk.Label(self, text="MOBILE NO", bg="Navy Blue",fg='White',font=("Amigos",17))
        label4.place(relx=.4, rely=.6, anchor="c")
        mob=tk.StringVar()
        entry1=tk.Entry(self,textvariable=mob,width=25,)
        entry1.place(relx=.6, rely=.6, anchor="c")
        label5 = tk.Label(self, text="EMAIL",  bg="Navy Blue",fg='White',font=("Amigos",17))
        label5.place(relx=.4, rely=.7, anchor="c")
        email=tk.StringVar()
        entry1=tk.Entry(self,textvariable=email,width=25)
        entry1.place(relx=.6, rely=.7, anchor="c")
        def val():
            a=name.get()
            b=us.get()
            c=pas.get()
            d=mob.get()
            e=email.get()
            print(b,a,d,e,c)
            if a == '' or b == '' or c == '' or d == '' or e == '':
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                sql = "insert into customer values(%s,%s,%s,%s,%s)"
                vl=(b,a,d,e,c)
                mycursor.execute(sql,vl)
                mydb.commit()
                tk.messagebox.showinfo("Success", "account has been created" )
                controller.show_frame("PageTwo")
                


            
        button1 = tk.Button(self, text="CREATE ACC", bg="Navy Blue",fg='White',font=("Amigos",17),relief=FLAT,
                            command=val)
        button1.place(relx=.5, rely=.8, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageTwo"))
        button3.place(relx=.1, rely=.1, anchor="c")


        
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label5 = tk.Label(self, text="Customer", fg="Navy Blue",bg='White',font=("Amigos",40))
        label5.pack(side="top", fill="x", pady=30)
        button1 = tk.Button(self, text="BOOK  RESTAURANT",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=lambda: controller.show_frame("PageFive"))
        
        button2 = tk.Button(self, text="REVIEW  RESTAURANT",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=lambda: controller.show_frame("PageEight"))
        button1.place(relx=.3, rely=.5, anchor="c")
        button2.place(relx=.7, rely=.5, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageThree"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")
        
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        global city1
        label = tk.Label(self, text="Restaurant list",width='299',bg='White',font=('Amigos',40))
        label.pack(side="top", fill="x", pady=30)
        label5 = tk.Label(self, text="select city",width=20,height=3,bg="Navy Blue",fg="White",font=('Amigos',25))
        label5.place(relx=.5, rely=.3, anchor="c")
        v=tk.IntVar()
        Radio1=tk.Radiobutton(self,text="Delhi",padx=20,font=("Amigos",17),bg='White',variable=v,value=1)
        Radio1.place(relx=.4, rely=.5, anchor="c")
        Radio2=tk.Radiobutton(self,text="Vellore",padx=20,font=("Amigos",17),bg='White',variable=v,value=2)
        Radio2.place(relx=.6, rely=.5, anchor="c")
    
        def cc():
            global city1
            ty=v.get()
            if(ty==1):
                city1='Delhi'
            elif(ty==2):
                city1='vellore'
            else:
                city1=''
            
            
            controller.show_frame("PageSix")
        button1 = tk.Button(self, text="Proceed to get list of available restaurant",width=30,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=cc)
        button1.place(relx=.5, rely=.7, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageFour"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")


        
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        global city1
        global userna1
        label5 = tk.Label(self, text="Slot booking", fg="Navy Blue",bg='White',font=("Amigos",40))
        label5.pack(side="top", fill="x", pady=30)
        
        x="Available restaurant"
        label5 = tk.Label(self, text=x, bg="Navy Blue",fg='White',font=("Amigos",25))
        label5.pack(side="top", fill="x", pady=10)

        def xxxx():
            
            sql = "select * from restaurant where city = %s"
            mycursor.execute(sql,(city1,))
            res = mycursor.fetchall()
            
            for rid in res:
                label5 = tk.Label(self, text=rid,bg='Navy Blue',fg='White',font=("Amigos",20))
                label5.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="show",bg='Navy Blue',fg='White',width=3,height=1
                            ,font=('Amigos',25),relief=FLAT,
                            command=xxxx)
        

        button1.place(relx=.5, rely=.4, anchor="c")
        v=tk.IntVar()
        Radio1=tk.Radiobutton(self,text="morning",font=("Amigos",17),bg='White',padx=20,variable=v,value=1)
        Radio1.place(relx=.3,rely=.6, anchor="c")
        Radio2=tk.Radiobutton(self,text="afternoon",font=("Amigos",17),bg='White',padx=20,variable=v,value=2)
        Radio2.place(relx=.5,rely=.6, anchor="c")
        Radio3=tk.Radiobutton(self,text="evening",font=("Amigos",17),bg='White',padx=20,variable=v,value=3)
        Radio3.place(relx=.7,rely=.6, anchor="c")
        label6 = tk.Label(self, text="Date(yyyy-mm-dd)", bg="Navy Blue",fg='White',font=("Amigos",17))
        label6.place(relx=.4,rely=.7, anchor="c")
        abc=tk.StringVar()
        entry1=tk.Entry(self,textvariable=abc,width=40,)
        entry1.place(relx=.6,rely=.7, anchor="c")
        
        
        ab=tk.StringVar()
        label5 = tk.Label(self, text="Enter rid  to confirm booking", bg="Navy Blue",fg='White',font=("Amigos",17))
        label5.place(relx=.4,rely=.8, anchor="c")
        entry1=tk.Entry(self,textvariable=ab,width=25,)
        var1=entry1.get()
        entry1.place(relx=.6,rely=.8, anchor="c")
        sql = "select rid from restaurant"
        mycursor.execute(sql)
        fdata = mycursor.fetchall()
        sql = "select bid from booking"
        mycursor.execute(sql)
        gdata = mycursor.fetchall()
        def val():
            global city1
            
            x=v.get()
            if(x==1):
                z='morning'
            elif(x==2):
                z='afternoon'
            else:
                z='evening'
            b=userna1
            
            c=ab.get()
            d=abc.get()
            e=z
            y=0
            mx=0
            for i in gdata:
                mx=mx+1
            mx=mx+1;
            a=str(mx)
            for i in fdata:
                if c in i:
                    y=c
            print(a,b,c,d,e)
            if a == '' or b == '' or c == '' or d == '' or e == '':
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

            #elif y!=c:
                #tk.messagebox.showinfo("Warning", "Please select from above only")
                
            else:
                sql = "insert into booking values(%s,%s,%s,%s,%s)"
                vl=(a,b,c,d,e)
                mycursor.execute(sql,vl)
                mydb.commit()
                controller.show_frame("PageSeven")

        
        
        button1 = tk.Button(self, text="Book",bg='Navy Blue',fg='White',width=10,height=1
                            ,font=('Amigos',25),relief=FLAT,
                            command=val)
        button1.place(relx=.5, rely=.9, anchor="c")
        
        button3 = tk.Button(self, text="BACK",width=7,height=3,bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageFive"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,bg="White"
                            ,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")
        

class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="Thank you\n Restaurant Booked Successfully :)",bg='Navy Blue',fg='White',font=('Amigos',50))
        label5.place(relx=.5, rely=.5, anchor="c")
        button1 = tk.Button(self, text="main menu",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageFour"))
        button2 = tk.Button(self, text="logout",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))

        button1.place(relx=.1, rely=.1, anchor="c")
        button2.place(relx=.9, rely=.1, anchor="c")


class PageEight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        global userna1
        self.controller = controller
        label5 = tk.Label(self, text="Customer", fg="Navy Blue",bg='White',font=("Amigos",40))
        label5.pack(side="top", fill="x", pady=30)
        label5 = tk.Label(self, text="Restaurant id", width=20,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,)
        label5.place(relx=.4, rely=.4, anchor="c")
        ri=tk.StringVar()
        entry6=tk.Entry(self,textvariable=ri,width=25)
        entry6.place(relx=.6, rely=.4, anchor="c")
        label7 = tk.Label(self, text="Feedback",width=20,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,)
        label7.place(relx=.4, rely=.6, anchor="c")
        fb=tk.StringVar()
        entry8=tk.Entry(self,textvariable=fb,width=25)
        entry8.place(relx=.6, rely=.6, anchor="c")
        sql = "select rid from restaurant"
        mycursor.execute(sql)
        fdata = mycursor.fetchall()
        
        def fb1():
            r7 =ri.get()
            r8 =userna1
            r9 =fb.get()
            y=0;
            for i in fdata:
                if r7  in i:
                    y=r7
            if r7 == '' or r8 == '' or r9 == '' :
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            
            #elif y!=r7:
                #tk.messagebox.showinfo("Warning", "Restaurant not in our database")
                
            else:
                sql = "insert into feedback values(%s,%s,%s)"
                vl=(r8,r7,r9)
                mycursor.execute(sql,vl)
                mydb.commit()
                controller.show_frame("PageEighteen")
        def not1():
            tk.messagebox.showinfo("success", "loggedout")
            
            
        
        
        button2 = tk.Button(self, text="submit",width=10,height=2,bg="Navy Blue",fg="White",font=('Amigos',20),relief=FLAT,
                            command=fb1)
        button2.place(relx=.5, rely=.8, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageFour"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,fg="Navy Blue",bg="White",font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")
        

        
class PageNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label5 = tk.Label(self, text="ADMIN", bg="Navy Blue",fg='White',font=("Amigos",40))
        label5.place(relx=.5, rely=.1, anchor="c")
        label6 = tk.Label(self, text="USER NAME",bg="Navy Blue",fg='White',font=("Amigos",40))
        label6.place(relx=.4, rely=.3, anchor="c")
        a=tk.StringVar()
        entry1=tk.Entry(self,textvariable=a,width=40,)
        entry1.place(relx=.6, rely=.3, anchor="c")
        label7 = tk.Label(self, text="PASSWORD",bg="Navy Blue",fg='White',font=("Amigos",40))
        label7.place(relx=.4, rely=.5, anchor="c")
        b=tk.StringVar()
        entry1=tk.Entry(self,textvariable=b,width=40,)
        entry1.place(relx=.6, rely=.5, anchor="c")
        
        def adminlog():
            x=a.get()
            y=b.get()
            
                
            if x == '' or y == '' :
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                if x!='admin' or y!='admin':
                    tk.messagebox.showinfo("Warning", "Wrong Username or Password")
                else:
                    tk.messagebox.showinfo("Success", "logged in" )
                    controller.show_frame("PageTen")
        button1 = tk.Button(self, text="LOG IN",width=10,height=3,fg='White',bg="Navy Blue",font=('Amigos',30),relief=FLAT,command=adminlog)
        button1.place(relx=.6, rely=.7, anchor="c")
        button3 = tk.Button(self, text="BACK",width=10,height=3,fg='White',bg="Navy Blue",font=('Amigos',30),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.4, rely=.7, anchor="c")

        
class PageTen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        
        button1 = tk.Button(self, text="ADD   RESTAURANT",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25,),relief=FLAT,
                            command=lambda: controller.show_frame("PageEleven"))
        button2 = tk.Button(self, text="REMOVE   RESTAURANT",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=lambda: controller.show_frame("PageThirteen"))
        
        button3 = tk.Button(self, text="VIEW   RESTAURANT",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=lambda:controller.show_frame("PageFifteen"))
        button4 = tk.Button(self, text="VIEW   BOOKING",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=lambda: controller.show_frame("PageSixteen"))
        button5 = tk.Button(self, text="VIEW   REVIEW",width=25,height=3,bg="Navy Blue",fg="White",font=('Amigos',25),relief=FLAT,
                            command=lambda: controller.show_frame("PageSeventeen"))
        button1.place(relx=.35, rely=.4, anchor="c")
        button2.place(relx=.65, rely=.4, anchor="c")
        button3.place(relx=.2, rely=.6, anchor="c")
        button4.place(relx=.5, rely=.6, anchor="c")
        button5.place(relx=.8, rely=.6, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,bg="Navy Blue",fg="White",font=('Amigos',20),relief=FLAT,
                            command=lambda: controller.show_frame("PageNine"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,bg="Navy Blue",fg="White",font=('Amigos',20),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")


class PageEleven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label5 = tk.Label(self, text="Restaurant Details", width='299',font=('Amigos',40))
        label5.pack(side="top", fill="x", pady=30)
        label5 = tk.Label(self, text="Resaurant id",bg='Navy Blue',fg='White',font=('Amigos',30))
        label5.place(relx=.4, rely=.4, anchor="c")
        rid2=tk.StringVar()
        entry2=tk.Entry(self,textvariable=rid2,width=25)
        entry2.place(relx=.6, rely=.4, anchor="c")
        label5 = tk.Label(self, text="Name",bg='Navy Blue',fg='White', font=('Amigos',30))
        label5.place(relx=.4, rely=.5, anchor="c")
        rid3=tk.StringVar()
        entry3=tk.Entry(self,textvariable=rid3,width=25)
        entry3.place(relx=.6, rely=.5, anchor="c")
        label5 = tk.Label(self, text="Contact no",bg='Navy Blue',fg='White',font=('Amigos',30))
        label5.place(relx=.4, rely=.6, anchor="c")
        rid4=tk.StringVar()
        entry4=tk.Entry(self,textvariable=rid4,width=25)
        entry4.place(relx=.6, rely=.6, anchor="c")
        label5 = tk.Label(self, text="City",bg='Navy Blue',fg='White',font=('Amigos',30))
        label5.place(relx=.4, rely=.7, anchor="c")
        rid5=tk.StringVar()
        entry5=tk.Entry(self,textvariable=rid5,width=25)
        entry5.place(relx=.6, rely=.7, anchor="c")
        label5 = tk.Label(self, text="Complete address",bg='Navy Blue',fg='White',font=('Amigos',30)
                          )
        label5.place(relx=.4, rely=.8, anchor="c")
        rid6=tk.StringVar()
        entry6=tk.Entry(self,textvariable=rid6,width=25)
        entry6.place(relx=.6, rely=.8, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")

            
        def add():
            r2 =rid2.get()
            r3 =rid3.get()
            r4 =rid4.get()
            r5 =rid5.get()
            r6 =rid6.get()
            if r2 == '' or r3 == '' or r4 == '' or r5 == '' or r6 == '':
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                sql = "insert into restaurant values(%s,%s,%s,%s,%s)"
                vl=(r2,r3,r6,r4,r5)
                mycursor.execute(sql,vl)
                mydb.commit()
                controller.show_frame("PageTwelve")
        
        button1 = tk.Button(self, text="confirm",bg='Navy Blue',fg='White',width=10,height=1
                            ,font=('Amigos',25),relief=FLAT,
                            command=add)
        button1.place(relx=.5, rely=.9, anchor="c")


class PageTwelve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="Restaurant Succesfully Added",bg='Navy Blue',fg='White',font=('Amigos',50))
        label5.place(relx=.5, rely=.5, anchor="c")
        button1 = tk.Button(self, text="main menu",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button2 = tk.Button(self, text="logout",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))

        button1.place(relx=.1, rely=.1, anchor="c")
        button2.place(relx=.9, rely=.1, anchor="c")


class PageThirteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="Navy Blue")
        self.controller = controller
        label5 = tk.Label(self, text="Remove Restaurant ", width='299',font=('Amigos',40))
        label5.pack(side="top", fill="x", pady=30)
        label6 = tk.Label(self, text="Restaurant id",bg='Navy Blue',fg='White',font=('Amigos',40))
        label6.place(relx=.5, rely=.4, anchor="c")
        rid1=tk.StringVar()
        entry1=tk.Entry(self,textvariable=rid1,width=25)
        sql = "select rid from restaurant"
        mycursor.execute(sql)
        fdata = mycursor.fetchall()
        def greet():
            x =rid1.get()
            y=0;
            for i in fdata:
                if x in i:
                    y=x
            if x == '':
                tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            #elif y!=x:
                #tk.messagebox.showinfo("Warning", "Restaurant not in our database")
                
            else:
                sql = "delete from restaurant where rid= %s"
                mycursor.execute(sql,(x,))
                mydb.commit()
                controller.show_frame("PageFourteen")
        entry1.place(relx=.5, rely=.6, anchor="c")
        button1 = tk.Button(self, text="remove",bg='Navy Blue',relief=FLAT,fg='White',font=('Amigos',30),command=greet)
        button1.place(relx=.5, rely=.8, anchor="c")
        button3 = tk.Button(self, text="BACK",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")

        
    
        
        

class PageFourteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="Restaurant Removed Succesfully",bg='Navy Blue',fg='White',font=('Amigos',50))
        label5.place(relx=.5, rely=.5, anchor="c")
        button1 = tk.Button(self, text="main menu",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button2 = tk.Button(self, text="logout",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))

        button1.place(relx=.1, rely=.1, anchor="c")
        button2.place(relx=.9, rely=.1, anchor="c")

class PageFifteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="View Restaurant ", width='299',font=('Amigos',40))
        label5.pack(side="top", fill="x", pady=30)
        sql = "select * from restaurant"
        mycursor.execute(sql)
        rdata = mycursor.fetchall()
        x="Rid    Name    Address    Mobile_no    City"
        label5 = tk.Label(self, text=x,bg='Navy Blue',fg='White',font=('Harlow Solid Italic',30))
        label5.pack(side="top", fill="x", pady=10)
        y=""
        for rid in rdata:
            #label5 = tk.Label(self, text=y,bg='Navy Blue',fg='White', font=controller.title_font)
            #label5.pack(side="top", fill="x", pady=10)
            label5 = tk.Label(self, text=rid,bg='Navy Blue',fg='White', font=("Amigos",20))
            label5.pack(side="top", fill="x", pady=10)
        
        button3 = tk.Button(self, text="BACK",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")

class PageSixteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="Booking Details ", width='299',font=('Amigos',40))
        label5.pack(side="top", fill="x", pady=30)
        
        button3 = tk.Button(self, text="BACK",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")

        
        sql = "select * from booking"
        mycursor.execute(sql)
        bdata = mycursor.fetchall()
        x="bid   cid   rid   date    slot"
        label5 = tk.Label(self, text=x,bg='Navy Blue',fg='White',font=('Harlow Solid Italic',30))
        label5.pack(side="top", fill="x", pady=10)
        for date in bdata:
            label5 = tk.Label(self, text=date, bg='Navy Blue',fg='White', font=("Amigos",20))
            label5.pack(side="top", fill="x", pady=10)
            
                            
class PageSeventeen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="Reviews ", width='299',font=('Amigos',40))
        label5.pack(side="top", fill="x", pady=30)
        
        button3 = tk.Button(self, text="BACK",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageTen"))
        button3.place(relx=.1, rely=.1, anchor="c")
        button3 = tk.Button(self, text="LOGOUT",width=7,height=3,font=('Amigos',10),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))
        button3.place(relx=.9, rely=.1, anchor="c")
        sql = "select * from feedback"
        mycursor.execute(sql)
        fdata = mycursor.fetchall()
        x="Username rid feedback"
        label5 = tk.Label(self, text=x,bg='Navy Blue',fg='White',font=('Harlow Solid Italic',30))
        label5.pack(side="top", fill="x", pady=10)
        for rid in fdata:
            label5 = tk.Label(self, text=rid, bg='Navy Blue',fg='White', font=("Amigos",20))
            label5.pack(side="top", fill="x", pady=10)
            
            
class PageEighteen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Navy Blue')
        self.controller = controller
        label5 = tk.Label(self, text="Feedback Given Succesfully",bg='Navy Blue',fg='White',font=('Amigos',50))
        label5.place(relx=.5, rely=.5, anchor="c")
        button1 = tk.Button(self, text="main menu",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageFour"))
        button2 = tk.Button(self, text="logout",bg='Navy Blue',fg='White',font=('Amigos',50),relief=FLAT,
                            command=lambda: controller.show_frame("PageOne"))

        button1.place(relx=.1, rely=.1, anchor="c")
        button2.place(relx=.9, rely=.1, anchor="c")

            
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

