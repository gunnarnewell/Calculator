"""
Main python script to Calculator program. Will initialize the UI and basically
just be the program

UI from tkinter. I used a tutorial here: https://realpython.com/python-gui-tkinter/

Going to have 0 - 9, +,-,/,=,C,bck, '.',(,),^ so that is 20 buttons... 6x4

so ^ was being really funky, and I'd rather not deal with it

_ _ _|C|bck
7|8|9|(|)
4|5|6|x|/
1|2|3|-|+
0|.|= =|+

Gunnar J. Newell
"""

def main():
  """
  This is just a big UI setup
  """
  #------------------------------------- Functions
  def add(text):
    """
    This will add to the display, and be the go to function of most buttons.
    We'll want to add in conditions for what buttons go.
    """
    orig = dispb["text"]
    new = orig + text
    ops = ["+","-","*","/"]
    # conditions
    # length 21
    if len(new) > 21:
      dispb["text"] = orig
      return 0
      
    # one calc at a time
    if len(orig) > 0:
      if (orig[-1] in ops) & (text in ops):
        dispb["text"] = orig
        return 0

    dispb["text"] = new
    return 0
    
  def clear():
    dispb["text"] = ""
    return 0
    
  def backspace():
    dispb["text"] = dispb["text"][:len(dispb["text"])-1]
    return 0
    
  def equals():
    try:
      dispb["text"] = str(eval(dispb["text"]))
    except:
      dispb["text"]="ERROR, clear display"
    
  #------------------------------------- UI
  
  # title and start
  calc = tk.Tk()
  calc.title("Calculator")
  # size
  calc.geometry("255x235")
  #calc.columnconfigure(range(3), weight=1, minsize=50)
  #calc.rowconfigure(range(1,4), weight=1, minsize=48)
  
  # Icon
  calc.iconbitmap('Icon.ico')#'Icon.ico')
  
  
  calcarea = tk.Frame(master=calc)
  calcarea.pack(padx=5, pady=10)
  
  # display box
  disp = tk.Frame(
    master = calcarea
  )
  disp.grid(row = 0, column = 0, columnspan = 3)
  dispb = tk.Label(
    master = disp,
    text = '',
    fg = 'black',
    bg = 'white',
    borderwidth = 1,
    relief = 'solid',
    height = 2,
    width = 19
  )
  dispb.pack()
  
  # number buttons
  num1 = tk.Frame(
    master=calcarea
  )
  num1.grid(row = 3, column = 0)
  num1b = tk.Button(
    master = num1,
    text = 1,
    width = 5,
    height = 2,
    command = lambda: add("1")
  ).pack()
      # the pack is what adds it to the UI
  # two    
  num2 = tk.Frame(
    master=calcarea
  )
  num2.grid(row = 3, column = 1)
  num2b = tk.Button(
    master = num2,
    text = "2",
    width = 5,
    height = 2,
    command = lambda: add("2")
  ).pack()
  
  # three    
  num3 = tk.Frame(
    master=calcarea
  )
  num3.grid(row = 3, column = 2)
  num3b = tk.Button(
    master = num3,
    text = "3",
    width = 5,
    height = 2,
    command = lambda: add("3")
  ).pack()
  
  # four    
  num4 = tk.Frame(
    master=calcarea
  )
  num4.grid(row = 2, column = 0)
  num4b = tk.Button(
    master = num4,
    text = "4",
    width = 5,
    height = 2,
    command = lambda: add("4")
  ).pack()
  
  # five    
  num5 = tk.Frame(
    master=calcarea
  )
  num5.grid(row = 2, column = 1)
  num5b = tk.Button(
    master = num5,
    text = "5",
    width = 5,
    height = 2,
    command = lambda: add("5")
  ).pack()
  
  # six    
  num6 = tk.Frame(
    master=calcarea
  )
  num6.grid(row = 2, column = 2)
  num6b = tk.Button(
    master = num6,
    text = "6",
    width = 5,
    height = 2,
    command = lambda: add("6")
  ).pack()
  
  # seven    
  num7 = tk.Frame(
    master=calcarea
  )
  num7.grid(row = 1, column = 0)
  num7b = tk.Button(
    master = num7,
    text = "7",
    width = 5,
    height = 2,
    command = lambda: add("7")
  ).pack()
  
  # eight    
  num8 = tk.Frame(
    master=calcarea
  )
  num8.grid(row = 1, column = 1)
  num8b = tk.Button(
    master = num8,
    text = "8",
    width = 5,
    height = 2,
    command = lambda: add("8")
  ).pack()
  
  # nine    
  num9 = tk.Frame(
    master=calcarea
  )
  num9.grid(row = 1, column = 2)
  num9b = tk.Button(
    master = num9,
    text = "9",
    width = 5,
    height = 2,
    command = lambda: add("9")
  ).pack()
  
  # zero
  num0 = tk.Frame(
    master = calcarea
  )
  num0.grid(row = 4, column = 0)
  num0b = tk.Button(
    master = num0,
    text = 0,
    width = 5,
    height = 2,
    command = lambda: add("0")
  ).pack()
  
  # period
  dot = tk.Frame(
    master = calcarea
  )
  dot.grid(row = 4, column = 1)
  dotb = tk.Button(
    master = dot,
    text = ".",
    width = 5,
    height = 2,
    command = lambda: add(".")
  ).pack()
  
  # equal sign
  eq = tk.Frame(
    master = calcarea
  )
  eq.grid(row = 4, column = 2, columnspan = 2)
  eqb = tk.Button(
    master = eq,
    text = "=",
    width = 11,
    height = 2,
    command = equals
  ).pack()
  
  # plus sign
  plus = tk.Frame(
    master = calcarea
  )
  plus.grid(row = 3, column = 4, rowspan = 2)
  plusb = tk.Button(
    master = plus,
    text = "+",
    width = 5,
    height = 5,
    command = lambda: add("+")
  ).pack()
  
  # minus sign
  minu = tk.Frame(
    master = calcarea
  )
  minu.grid(row = 3, column = 3)
  minub = tk.Button(
    master = minu,
    text = "-",
    width = 5,
    height = 2,
    command = lambda: add("-")
  ).pack()
  
  # multiplication
  mult = tk.Frame(
    master = calcarea
  )
  mult.grid(row = 2, column = 3)
  multb = tk.Button(
    master = mult,
    text = "*",
    width = 5,
    height = 2,
    command = lambda: add("*")
  ).pack()
  
  # division
  div = tk.Frame(
    master = calcarea
  )
  div.grid(row = 2, column = 4)
  divb = tk.Button(
    master = div,
    text = "/",
    width = 5,
    height = 2,
    command = lambda: add("/")
  ).pack()
  
  # left parentheses
  lefp = tk.Frame(
    master = calcarea
  )
  lefp.grid(row = 1, column = 3)
  lefpb = tk.Button(
    master = lefp,
    text = "(",
    width = 5,
    height = 2,
    command = lambda: add("(")
  ).pack()
  
  # right paraentheses
  rigp = tk.Frame(
    master = calcarea
  )
  rigp.grid(row = 1, column = 4)
  rigpb = tk.Button(
    master = rigp,
    text = ")",
    width = 5,
    height = 2,
    command = lambda: add(")")
  ).pack()
  
  # Clear button
  Clr = tk.Frame(
    master = calcarea
  )
  Clr.grid(row = 0, column = 3)
  Clrb = tk.Button(
    master = Clr,
    text = "C",
    width = 5,
    height = 2,
    command = clear
  ).pack()
  
  # backspace
  bck = tk.Frame(
    master = calcarea
  )
  bck.grid(row = 0, column = 4)
  bckb = tk.Button(
    master = bck,
    text = "\N{RIGHTWARDS BLACK ARROW}",
    width = 5,
    height = 2,
    command = backspace
  ).pack()
  
  # This is what kicks the whole thing off, lets it wait for commands.
  calc.mainloop()
  

if __name__ == "__main__":
  import tkinter as tk
  import os
  main()
