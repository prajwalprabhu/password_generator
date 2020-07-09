import random 
import tkinter as tk
password=''
alphbets='''qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM123456789'''
def generate(e1):
    global password
    
    required_charecters=int(e1.get())
    password=random.sample(alphbets,required_charecters)
    e2=tk.Entry(root)
    e2.pack()
    e2.insert(0,password)
root=tk.Tk()
root.title("Password Generator")
tk.Label(root,text="Enter the number of characters").pack()
e1=tk.Entry(root)
e1.pack()
tk.Label(root,text="To generate password").pack()
tk.Button(root,text=" click here",command=lambda:generate(e1)).pack()
tk.Label(root,text="Password:").pack()




root.mainloop()
