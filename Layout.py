from tkinter import *
from tkinter import ttk
from Check_words import *
from Others import *
import sv_ttk

def play():  
                              #this function runs once the user hits PLAY in the starting window
    main_label.grid_forget()
    main_button.grid_forget()
    style.configure("my.Troot", background = None)
   #root = ttk.root(root,width= "750p",height="500p",borderwidth=10,relief = "flat",style= 'my.Troot').grid(column = 0, row = 0, columnspan = 16,rowspan = 11) #creating the parent root with 11 rows and 9 columnns
    dic_lab = {}
    #creating labels in variables
    for i in range(6):
        for j in range(5):
            dic_lab["lab" + str(i) + str(j)] = ttk.Label(root,text = "",background="#ffffff",width = 5,justify = "center", borderwidth=3,relief = 'sunken', font = ("Serif",32,'bold'),anchor= "center")
            dic_lab["lab" + str(i) + str(j)].grid(column = j+2,row = i,ipady = 18,pady =6)
    style.configure("my.TButton",height = 10,background = "White", font = ("Comic Sans",25))
    restart = ttk.Button(root,text = "Restart Game",width = 15,style="my.TButton")
    restart.grid(row=0,column=9,columnspan=4,ipadx =4,ipady = 20,rowspan =2)
    exit = ttk.Button(root,text = "Leave Game",width =15,style="my.TButton")
    exit.grid(row=0,column=13,columnspan=4,ipadx =4,ipady=20,rowspan =2)
    dic_alpha = {}
    pad_label = ttk.Label(root,text ="",width =10).grid(row=2,rowspan = 3, column = 7)
    
    style.configure('alpha.TButton', font = ("Calibri", 22), anchor = 'center', background = "#994C00",foreground = 'white',height = 10)
    style.map('my.TButton', background = [('active','pink')])
    style.map('alpha.TButton', background = [('active','yellow')], foreground = [('active','black')])
    for i in range(65,65+26):
        dic_alpha[chr(i)] = ttk.Button(root,text = chr(i),width = 3, style= 'alpha.TButton')
    for i in range(65,65+9):
        dic_alpha[chr(i)].grid(row = 2, column = i-(65-8),padx=3,ipadx = 3)
    for i in range(65+9,65+18):
       dic_alpha[chr(i)].grid(row = 3, column = i-(65+10-9),ipadx = 3,padx =3)
    for i in range(65+18,65+26):
        dic_alpha[chr(i)].grid(row = 4, column = i-(65+18-8),ipadx = 3,padx =3)
    curr_label= [dic_lab["lab00"]]      #the current label where we are typing
    def backspace_func(label):
        label[0]= list(dic_lab.values())[list(dic_lab.values()).index(label[0])-1]
        label[0].configure(text = "")
    backspace = ttk.Button(root,text = "del", width =3, style = "alpha.TButton")
    backspace.grid(row = 4, column = 16, ipadx = 3, padx =3)
    backspace['command'] = lambda : backspace_func(curr_label)
    photo = PhotoImage(file = 'image.png')
    photoimage = photo.subsample(4, 4)
    backspace.configure(image = photoimage)
    submit_button = ttk.Button(root, text = "SUBMIT", width = 20,style = "my.TButton")
    submit_button.grid(row = 5, column = 10, columnspan=6)
    display = ttk.Label(root,text = "Submit your word",font = ("Serif",28,'bold'), width = 25, anchor = "center")
    display.grid(row = 6, column = 9, columnspan= 8)
    for i in range(65,65+26):
        def type_alpha(s = chr(i)):
            curr_label[0].configure(text = s)
            try :
                curr_label[0]= list(dic_lab.values())[list(dic_lab.values()).index(curr_label[0])+1]
            except IndexError:
                pass
        dic_alpha[chr(i)]['command'] = type_alpha
    row_num = [0]
    checking(submit_button,dic_lab,row_num,curr_label,display)
    #dic_alpha["A"].bind('<Key>', keyboard)
    exiting(exit)
    restarting(restart)
    



root = Tk()
root.geometry("1720x1080")
sv_ttk.use_dark_theme()
style = ttk.Style()
style.theme_use('alt') 
style.configure('my.TButton',font = ('Times New Roman',10))
main_label = ttk.Label(root,width =60, justify= 'center',anchor = "center",text = "WELCOME TO THE GAME OF WORDLE", font = ("Calibri", 40))
main_label.grid(ipady= 80,pady = 30,row =0,column = 0,sticky = (N,S,E,W))
main_button = ttk.Button(root,width = 10, text = "PLAY",style = 'my.TButton',command= play)
main_button.grid(ipady =30, row =1, column =0)
root.mainloop()










