import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import VideoFileClip

def choose_download_path():
    download_path = filedialog.askdirectory()
    link.set(download_path)

def download_and_convert_audio():
    try:
        url = YouTube(str(link.get()))

        # Get the highest resolution video stream
        video_stream = url.streams.get_highest_resolution()

        # Download the video to the selected path
        video_stream.download(output_path=link.get())

        # Get the downloaded video file path
        video_file_path = f"{link.get()}/{url.title}.mp4"

        # Extract audio and save as MP3
        video_clip = VideoFileClip(video_file_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(f"{link.get()}/{url.title}.mp3", codec='mp3')

        # Close the clips to release resources
        video_clip.close()
        audio_clip.close()

        # Remove the original video file
        video_clip.reader.close()
        video_clip.audio.reader.close_proc()
        video_clip.audio.reader.proc.terminate()

        tk.Label(root, text="Downloaded", font="Arial 15").place(x=100, y=120)
    except Exception as e:
        tk.Label(root, text="Error: " + str(e), font="Arial 12", fg="red").place(x=100, y=120)

root = tk.Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube MP3 Audio Downloader')

tk.Label(root, text="Download YouTube audio in MP3!", font='sans-serif 14 bold').grid(row=0, column=0, pady=10, padx=10, columnspan=3)
tk.Label(root, text="Choose download path", font='sans-serif 15 bold').grid(row=1, column=0, pady=5, padx=10, sticky='e')
link = tk.StringVar()
link_enter = tk.Entry(root, width=40, textvariable=link)
link_enter.grid(row=1, column=1, pady=5, padx=10, sticky='w')
tk.Button(root, text='Browse', font='sans-serif 12 bold', command=choose_download_path).grid(row=1, column=2, pady=5, padx=10, sticky='w')

tk.Button(root, text='Download Video and Audio', font='sans-serif 16 bold', bg='green', padx=2, command=download_and_convert_audio).grid(row=2, column=0, pady=10, padx=10, columnspan=3)

root.mainloop()
