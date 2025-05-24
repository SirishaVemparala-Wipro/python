from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from signup import loginButton
import pymysql

def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching',parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='Sirisha*1234#',database='userdata')
            mycursor = con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror('Error','Username not Found',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password Updated',parent=window)
                window.destroy()

    window=Toplevel()
    window.title("Change Password")

    bgPic=ImageTk.PhotoImage(file='bg.png')
    bgLabel=Label(window,image=bgPic)
    bgLabel.grid()

    heading_label=Label(window,text="RESET PASSWORD",font=('arial',18,'bold'),bg='white',fg='magenta2')
    heading_label.place(x=630,y=120)

    userLabel=Label(window, text='Username', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    userLabel.place(x=620,y=180)
    user_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    user_entry.place(x=620,y=210)
    Frame(window, width=250, height=2, bg='orchid1').place(x=620,y = 232)
    passwordLabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    passwordLabel.place(x=620, y=260)
    newpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    newpass_entry.place(x=620, y=290)
    Frame(window, width=250, height=2, bg='orchid1').place(x=620, y=312)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    confirmpassLabel.place(x=620, y=340)
    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=620, y=370)
    Frame(window, width=250, height=2, bg='orchid1').place(x=620, y=392)

    submitButton = Button(window, text='Submit', font=('Open Sans', 16, 'bold'),
                          bg='magenta2', fg='white', bd=0, cursor='hand2', width=20,activebackground='magenta2',activeforeground='white',command=change_password)
    submitButton.place(x=620, y=430)

    window.mainloop()
def login_user():
    if usernameEntry.get()=='' or passwordEntry.get=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='Sirisha*1234#')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established, please try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login is successful')
def signup_page():
    login_window.destroy()
    from signup import loginButton
def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show="*")
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN', font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=630,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold')
                    ,bd=0,fg='firebrick1')
usernameEntry.place(x=605,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=605,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold')
                    ,bd=0,fg='firebrick1')
passwordEntry.place(x=605,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)
frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=605,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=830,y=255)\

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),
                    fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=735,y=295)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=21,command=login_user)
loginButton.place(x=595,y=350)
orLabel=Label(login_window,text='----------------OR-------------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=595,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=660,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo, bg='white')
googleLabel.place (x=710,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo, bg='white')
twitterLabel.place(x=760,y=440)

signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white',activeforeground='white',activebackground='blue',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

login_window.mainloop()