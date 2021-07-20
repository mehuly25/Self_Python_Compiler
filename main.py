from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess

compiler = Tk()
compiler.title("Mehuly IDE for Python")
file_path = ''

def set_filepath(path):
    global file_path
    file_path=path


def run():
    if file_path == '':
        save_prompt=Toplevel()
        text=Label(save_prompt,text="Please save your code!")
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output,error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)

def save_as():
    if file_path=='':
        path=asksaveasfilename(filetype=[('Python Files', "*.py")])
    else:
        path=file_path
    with open(path, 'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_filepath(path)

def open_file():
    path = askopenfilename(filetype=[('Python Files', "*.py")])
    with open(path, 'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_filepath(path)


menubar = Menu(compiler)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_as)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="FILE", menu=filemenu)

runbar = Menu(menubar, tearoff=0)
runbar.add_command(label="Run your code", command=run)
menubar.add_cascade(label="RUN", menu=runbar)
compiler.config(menu=menubar)

editor = Text()
editor.pack()

code_output = Text(height=12)
code_output.pack()
compiler.mainloop()



