#libraries and modules here
import tkinter as tk  # I haven't done a lot of python and im learning through this project, if you're using this you're going to see a lot of comments talking to myself because thats how I learn.
import time  # I've learned that I need to make virtual environments in folders everytime i start a project because it wont disturb other projects i make with python and it will save room in my disk space and it is easier to navigate through because its organized in a folder.
import threading  # allows parallel processing
import json
import psutil
import pygetwindow as gw



# devlog #1 12/28/2024 remember that tkinter cant run when application is closed, i need to add a external library for background running. I'll either do that or optimize the parallel processes and create a system tray.
#if you're reading this, 10,000 hours is 36,000,000, or 36 million seconds!


#=====================================================================================================================================================================================
# variables, references and constants over here, have something else like a different script store data.
UPDATE_CONSTANT = 1  # THIS VARIABLE UPDATES BY MINUTES
DataStorage = "localDatabase.json" #reference
session_time = 0.0 #local session time until you close your computer
is_tracking = False #status for active tabs
total_time = 0.0 # GLOBAL VARIABLE
#apps that this program recognizes as productive workflows | you can add "ChannelExpertise" to this list if you want it to count towards the time.
coding_apps = ["Visual Studio Code", "Sublime Text", "LeetCode", "NeetCode", "Notepad", "Notepad++", "Vim", "GVIM", "Atom", "Brackets", "Emacs", "Geany", "TextMate", "BBEDIT", "Coda", "IntelliJ IDEA", "PyCharm", "Apache NetBeans", "XCode", "Android Studio", "Komodo IDE", "jupyter", "jupytersnotebook", "Replit", "CodePen", "Visualgo", "TopCode", "CoderPad", "Hack The Box", "GitHub", "GitLab", "Git", "git", "Codewars"] #add whatever or fix whichever one doesn't have the right name into this list.
#=====================================================================================================================================================================================







#=====================================================================================================================================================================================
#change setting procedural section:
window_transparency = 0.7
text_color = "lime"
#=====================================================================================================================================================================================







#=====================================================================================================================================================================================
# procedural or scratch code over here
window = tk.Tk()
window.title("ChannelExpertise")
window.geometry("1000x600")
window.attributes("-alpha", window_transparency)  # transparent background
window.configure(bg="black")

# text graphics
Introduction_label = tk.Label(window, 
    text="Thanks for using ChannelExpertise!\nThis program was inspired by Anders Ericsson's 10k hour concept for expertise,\nwhere you need to practice something for 10k hours to truly master it.\n\n\nThis program works by reading your active window name and seeing if it is relevant to\ncoding. Look in the config files to configure or email yipeng.dev@gmail.com for help or\nsuggestions, read the github README for config instructions.", 
    font=("Courier", 14), 
    fg=text_color, 
    bg="black", 
    anchor="w", 
    width=80,  # Adjust width to your preference
    justify="left"  # Ensures text is left-aligned properly
)
Introduction_label.pack(fill="x", padx=20, pady=30)




total_time_label = tk.Label(window, text="Total time spent coding: 0.00 s", font=("Courier", 14), fg=text_color, bg="black", anchor="w")
total_time_label.pack(pady=10, fill="x", padx=20)  # Makes the label span the width of the window

time_label = tk.Label(window, text="Time spent coding this session: 0.00 s", font=("Courier", 14), fg=text_color, bg="black", anchor="w")  # Align text to the right
time_label.pack(fill="x", padx=20)  # Makes the label span the width of the window


config_info_label = tk.Label(window, text="To change your time, go in json file and edit \"time_spent\" ", font=("Courier", 14), fg=text_color, bg="black", anchor="w")
config_info_label.pack(fill="x", padx=20, pady=70)
#=====================================================================================================================================================================================


S0dlcpavplwjdAm49fkfkalQ8761937Hd9Dh98sh0ad8dh098HSsadb78a9sgYUGdsuayg_originalGithubRepositoryToken_sdiuyGISYUGPADiOQIkbSDJhvouaysvdSPDOYvoasuydSDVouyvsaoiduiwayoSUDV96512039SDBLajsbdlasudgoSUYDGSDSDMNmVBCSDVNMmSBDVMnbvMBSNDVi7yTSGDIuyTISUYDtI = "https://github.com/Y-L77/ChannelExpertise"


#=====================================================================================================================================================================================
# have all the functions at the bottom to make it easier to navigate
# Load data from JSON file
def load_data():
    try:
        with open(DataStorage, "r") as file:
            data = json.load(file)  # Load the JSON data into a Python dictionary
        return data
    except FileNotFoundError:
        return {"time_spent": 0.0}  # Default value if the file doesn't exist

# Save data to JSON file
def save_data(data):
    with open(DataStorage, "w") as file:
        json.dump(data, file, indent=4)  # Serialize the Python object and write to the file

#check your computer's active window
def is_coding_IDE_or_text_editor_active():
    active_window = gw.getActiveWindow()
    if active_window:
        window_title = active_window.title
        for app in coding_apps:
            if app in window_title:
                return True
    return False

# Real-time save function
def save_session_time():
    while True:
        global session_time
        data = load_data()  # Load current data
        data["time_spent"] += session_time  # Add session time to total time
        save_data(data)  # Save updated data
        time.sleep(UPDATE_CONSTANT * 60)  # Save every UPDATE_CONSTANT minutes


def format_time(seconds): #make it so that it isnt just seconds with like 8 digit places.
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# count time function
def track_totaltime():
    global session_time, is_tracking, last_active_time
    session_start_time = time.time()  # Record the start time of the session
    while True:
        if is_coding_IDE_or_text_editor_active():
            if not is_tracking:
                # Start or resume tracking if not already tracking
                is_tracking = True
                last_active_time = time.time()  # Reset last active time to the current time
            session_time += time.time() - last_active_time  # Add time since last activity check
            last_active_time = time.time()  # Update last active time to now
        else:
            if is_tracking:  # Stop tracking if not in a coding app
                is_tracking = False
                last_active_time = time.time()  # Reset last_active_time to avoid unnecessary increments

        print(f"Time spent coding: {session_time} s")
        session_time_formatted = format_time(session_time)
        time_label.config(text=f"Time spent coding this session: {session_time_formatted} s")
        
        data = load_data()  # Load current data
        total_time = data["time_spent"] + session_time  # Calculate total time
        total_time_formatted = format_time(total_time)
        total_time_label.config(text=f"Total time spent coding: {total_time_formatted} s")
        
        time.sleep(UPDATE_CONSTANT)  # Update every 0.1 minutes


def start_tracking():
    threading.Thread(target=track_totaltime, daemon=True).start()  # tracks the global time with a new thread
    threading.Thread(target=save_session_time, daemon=True).start()  # tracks session time with a thread

def on_closing():
    window.destroy()

#=====================================================================================================================================================================================

oggithublink = tk.Label(window, text=S0dlcpavplwjdAm49fkfkalQ8761937Hd9Dh98sh0ad8dh098HSsadb78a9sgYUGdsuayg_originalGithubRepositoryToken_sdiuyGISYUGPADiOQIkbSDJhvouaysvdSPDOYvoasuydSDVouyvsaoiduiwayoSUDV96512039SDBLajsbdlasudgoSUYDGSDSDMNmVBCSDVNMmSBDVMnbvMBSNDVi7yTSGDIuyTISUYDtI, font=("Courier", 14), fg=text_color, bg="black", anchor="w") #to make it more tedious to change.
oggithublink.pack(fill="x", padx=20)


#end code
window.protocol("WM_DELETE_WINDOW", on_closing)  # closing event function

start_tracking()

window.mainloop()  # every program with tkinter ends with this because it loads all the widgets and displays the screen.
