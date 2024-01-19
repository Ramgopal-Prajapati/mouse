import tkinter as tk
from pytube import YouTube

# Create the main window
root = tk.Tk()
root.geometry('500x300')
root.title("YouTube Video Downloader")

# Create Entry Widget to enter URL
link = tk.StringVar()
tk.Label(root, text="Paste Link Here:", font="arial 15 bold").pack()
link_enter = tk.Entry(root, width=70, textvariable=link).pack(pady=5)

# Function to download video
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension="mp4")

    # Download options
    video[0].download()  # 360p
    video[1].download()  # 720p
    video[2].download()  # 1080p

    tk.Label(root, text="Video Downloaded Successfully", font="arial 15").pack()

# Create Button Widget to download video
tk.Button(root, text="Download Video", font="arial 15 bold", bg="pale violet red", padx=2, command=Downloader).pack()

# Start the main loop
root.mainloop()
