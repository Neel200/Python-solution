import tkinter as tk

#Function to update expression in the text entry
def click_button(item):
    current=input_text.get()
    input_text.set(current+str(item))
    
#Function to clear the entry field
def clear_field():
    input_text.set("")
    
#Function to evaluate the expression
def calculate():
    try:
        result=str(eval(input_text.get()))  #Evaluate the expression
        input_text.set(result)
    except Exception as e:
        input_text.set("Error")  #Display error if any exception occurs
        
#Creating the GUI window
root=tk.Tk()
root.title("Simple Calculator")

#Input field for calculator
input_text=tk.StringVar()
input_field=tk.Entry(root,textvariable=input_text,font=('Arial',18),bd=10,insertwidth=4,width=14,borderwidth=4)
input_field.grid(row=0,column=0,columnspan=4)

#Define button layout
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]

#Place buttons in the window
row_val=1
col_val=0
for button in buttons:
    if button=="=":
        tk.Button(root,text=button,width=5,height=3,command=calculate).grid(row=row_val,column=col_val)
    elif button=="C":
        tk.Button(root,text=button,width=5,height=3,command=clear_field).grid(row=row_val,column=col_val)
    else:
        tk.Button(root,text=button,width=5,height=3,command=lambda b=button:click_button(b)).grid(row=row_val,column=col_val)    
    col_val+=1
    if col_val>3:
        col_val=0
        row_val+=1
root.mainloop()
