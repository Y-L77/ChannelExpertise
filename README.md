# <p align="center">CHANNEL EXPERTISE</p>
<p align="center">An open-source TUI application that tracks productivity for programmers by monitoring active coding IDEs, text editors and more.</p>

![CEpreview](https://i.imgur.com/X2fWHTM.png)

# Why use Channel Expertise?
ChannelExpertise is a tracking tool used to record and track productivity by recording coding sessions time.
Inspired by **Anders Ericsson's** 10,000 expertise hour rule, this program aims to help users reach their programming mastery by tracking the time across development enviroments.

# How to install

1. Clone the repository (git clone https://github.com/Y-L77/ChannelExpertise.git)
2. navigate to the dist folder, create a shortcut or copy the "main" application to your desktop
3. you may need to disable your antivirus to run the main.exe because all the python dependencies are compiled with pyinstaller.
4. open application for it to run, no background and boot up feature yet.
5. data gets stored locally by the json and the program should run correctly now, you're good to go!

# Customize

I've done my best to keep the code modular, readable, and easy to modify even for non-deveopers.
The default look of the TUI is a retro black and green terminal but you can change the color and transparency with a single variable.
This program works by reading your active window and by looking at keywords in the "codingapps" list. It also reads websites so if you want to add ChatGPT or any productivity site like google classroom, go for it!
if you wish to update your data between devices you may edit the json directly.
![CEpreview](https://i.imgur.com/0TUVdN3.png)


# Contributing

If you're interested in contributing I'd gladly look over pull requests but this is more of a features tab I might add if my project gets a bit of attention.

1. mercy time and keyboard listeners to determine if user is AFK or typing
2. graphics and analytics maybe with either spreadsheet, github commit hash, or matplotlib
3. SQL for login and cloud data
4. builtin settings so you don't need to edit source code directly
5. background running and optimizations for startup boot without taking a lot of resources
6. session history
7. gamification
8. user feedback











