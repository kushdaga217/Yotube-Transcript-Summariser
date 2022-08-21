# GUI Library
from youtubeSummarizer import *
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont

# GUI BLOCK
root = Tk(baseName="Video Summarizer")
root.title("Caption Based Video Summarizer")
root.configure(background='#009688')
root.geometry("600x400+400+200")
root.resizable(0, 0)

# Main Title Label
title = Label(root, text="Video Summarizer", font="bold 26",
              bg="#009688", padx=140, pady=10).grid(row=0, column=0)

# URL Label
url_label = Label(root, text="URL:", font="bold",
                  bg='#009688', justify="right", bd=1)
url_label.place(height=50, x=100, y=70)

# Model Label
model_label = Label(root, text="Model:", font="bold",
                    bg='#009688', justify="right", bd=1)
model_label.place(height=50, x=90, y=135)

# Fraction Label
fraction_label = Label(root, text="Fraction:", font="bold",
                       bg='#009688', justify="right", bd=1)
fraction_label.place(height=50, x=80, y=210)

# Folder Label
folder_label = Label(root, text="Location:", font="bold",
                     bg='#009688', justify="right", bd=1)
folder_label.place(height=50, x=75, y=280)

# Entry --> String
get_url = Entry(root, width=40)
get_url.place(width=300, height=30, x=150, y=80)

# DropDown
options = ["TfIdf-Based", "Frequency-Based", "Using Both"]
# Declaring Variable and choosing default one
default_option = StringVar(root)
default_option.set(options[0])
drop = OptionMenu(root, default_option, *options)
drop.place(width=200, x=150, y=145)

# Entry --> Float
get_fraction = Entry(root, width=40)
get_fraction.place(width=300, height=30, x=150, y=220)

# Ask folder path
get_folder = Entry(root, width=40)
get_folder.place(width=300, height=30, x=150, y=290)

# Button --> Browse
folder = StringVar(root)


def browse():
    global folder
    folder = filedialog.askdirectory(initialdir='/')
    get_folder.insert(0, folder)


browse = Button(root, text="Browse", command=browse)
browse.place(height=30, x=475, y=290)


# Button Clear --> Reset all settings to default
def on_clear():
    default_option.set(options[0])
    get_url.delete(0, END)
    get_folder.delete(0, END)
    get_fraction.delete(0, END)


clear = Button(root, text="Clear", command=on_clear)
clear.place(width=50, x=240, y=350)
# Function on Submit


def on_submit():
    global url, choice, frac, current, folder
    url = get_url.get()
    choice = default_option.get()
    frac = float(get_fraction.get())
    current = os.getcwd()
    folder = get_folder.get()
    os.chdir(folder)
    print(url,choice,frac,folder)
    corpus, video_title = get_caption(url)
    with open("corpus.txt",'w+') as c:
        print(corpus,file=c)
    # Calling the main summarizer function
    summary = summarizer(corpus, choice, frac)
    filename = video_title+" "+choice+'.txt'
    filename = re.sub(r'[\/:*?<>|]', ' ', filename)
    with open(filename, 'w+') as f:
        print(summary, file=f)
    os.remove(os.getcwd()+'\\test.en.vtt')
    os.chdir(current)
    openpath = Button(root, text="Open Folder",
                      command=lambda: os.startfile(get_folder.get()))
    openpath.place(x=360, y=350)


# Button -->Submit
submit = Button(root, text="Submit", command=on_submit)
submit.place(width=50, x=300, y=350)

# Button Open Folder to view Saved files

root.mainloop()