from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import random



count = 5
root = Tk()
default_password = StringVar()


def random_password_generator():
        symbols = list(r"!@#$%^&*()_+|}{\":?><~`-=\][';l/.s")
        lower = list("abcdefghijklmnopqrstuvwxyz")
        upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        numbers = list("0123456789")
        count = 0 # Length of the password
        cycle = []
        password = ''
        while True:
                if count == 12:
                        break
                else:
                        randomIndex = random.randrange(4)

                        if randomIndex in cycle:
                                pass
                        else:
                                cycle.append(randomIndex)
                                if randomIndex == 0:
                                        password = password + random.choice(symbols)
                                if randomIndex == 1:
                                        password = password + random.choice(lower)
                                if randomIndex == 2:
                                        password = password + random.choice(upper)
                                if randomIndex == 3:
                                        password = password + random.choice(numbers)
                                if len(cycle) == 4:
                                        cycle.clear()
                                count = count + 1
        default_password.set(password)


def display_credentials():
        global vault
        
        listofdata = []
        count = 8

        with open("data.txt","r") as f:
                for line in f:
                        listofdata.append(line[:-1])
                for i in listofdata:
                        
                        name,email,password = i.split(',')
                        dencryptedName = ""
                        dencryptedEmail = ""
                        dencryptedPassword = ""
                        for letter in name:
                                if letter == ' ':
                                        dencryptedName += ' '
                                else:
                                        dencryptedName += chr(ord(letter) - 5)

                        for letter in email:
                                if letter == ' ':
                                        dencryptedEmail += ' '
                                else:
                                        dencryptedEmail += chr(ord(letter) - 5)

                        for letter in password:
                                if letter == ' ':
                                        dencryptedPassword += ' '
                                else:
                                        dencryptedPassword += chr(ord(letter) - 5)


                        Label(vault,text=dencryptedName).grid(row=count,column=0)
                        Label(vault,text=dencryptedEmail).grid(row=count,column=1,columnspan=2)
                        Label(vault,text=dencryptedPassword).grid(row=count,column=3)
                        count += 1
        

def write_credentials_to_file():
        name = account_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        encryptedName = ""
        encryptedEmail = ""
        encryptedPassword = ""
        for letter in name:
            if letter == ' ':
                encryptedName += ' '
            else:
                encryptedName += chr(ord(letter) + 5)

        for letter in email:
            if letter == ' ':
                encryptedEmail += ' '
            else:
                encryptedEmail += chr(ord(letter) + 5)

        for letter in password:
            if letter == ' ':
                encryptedPassword += ' '
            else:
                encryptedPassword += chr(ord(letter) + 5)
        text = encryptedName + "," + encryptedEmail + "," + encryptedPassword + "\n"

        file = open("data.txt",'a')
        file.write(text)
        file.close()
        account_entry.delete(0,'end')
        email_entry.delete(0,'end')
        password_entry.delete(0,'end')
        messagebox.showinfo(title="Info added", message="Sucessfully added")
        display_credentials()


# to check if password is correct or not
def authentication_check():
        global count
        password = authenticaton.get()
        if password == 'a':
                new_window()
        else:
                if count!=0:
                        if count >1:
                                warning = "you have " + str(count) + " tries left"
                        else:
                                warning = "you have " + str(count) + " try left"
                        messagebox.showwarning(title="Try again", message=warning)
                else:
                        messagebox.showerror(title="Password Vault",message="Try limit exceeded")
                        root.destroy()
                count -= 1


# new window if password is correct
def new_window():
        Label(root,text="correct").grid(row=5,column=1)
        global vault
        global account_entry
        global email_entry
        global password_entry
        vault = Toplevel()
        root.withdraw()
        vault.geometry("325x600")
        vault.title("Password Vault")
        vault.resizable(False,False)
        vault_inside = Label(vault,text="Welcome Back")
        vault_inside.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        add_things_label = Label(vault,text="Add new credentials")
        add_things_label.grid(row=1,column=0,columnspan=4,padx=10,pady=10)
        account = Label(vault,text="Account").grid(row=2,column=0)
        account_entry = Entry(vault,width=20)
        account_entry.grid(row = 2 ,column = 1,columnspan=2,padx=10,pady=10)
        email = Label(vault,text="Email ").grid(row=3,column=0)
        email_entry = Entry(vault)
        email_entry.grid(row = 3 ,column = 1,columnspan=2,padx=10,pady=10)
        password = Label(vault,text="Password").grid(row=4,column=0)
        password_entry = Entry(vault,textvariable=default_password)
        password_entry.grid(row = 4 ,column = 1,columnspan=2,padx=10,pady=10)

        random_pwgen = Button(vault,text="Generate password",command=random_password_generator).grid(row=4,column=3)

        add_credentials = Button(vault,text="Add Credentials",command=write_credentials_to_file).grid(row=6,column=1,columnspan=2,pady=5)

        show_name = Label(vault,text='Account').grid(row=7,column=0)
        show_email = Label(vault,text='Email').grid(row=7,column=1,columnspan=2)
        show_password = Label(vault,text='Password').grid(row=7,column=3)
        display_credentials()



root.title("Verification")
root.iconphoto(True,PhotoImage(file='logo.png'))
root.resizable(width=False,height=False)
heading = Label(root,text="Enter the authentication password",justify = CENTER,padx=50,pady=10).grid(row=1,column=1)
authenticaton = Entry(root,width=20,show="*")
authenticaton.grid(row=2,column=1)

submit_button = Button(root,text="Submit",justify = CENTER,command= authentication_check)
submit_button.grid(row=3,column=1,padx=50,pady=20)




root.mainloop()
