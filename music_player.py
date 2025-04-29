import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x200")

        pygame.mixer.init()
        self.music_files = []
        self.current_track_index = 0
        self.is_paused = False

        # GUI Elements
        self.label = tk.Label(root, text="No folder selected", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause/Resume", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.music_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith((".mp3", ".wav"))]
            self.current_track_index = 0
            self.label.config(text=f"Folder selected: {os.path.basename(folder)}")

    def play_music(self):
        if not self.music_files:
            self.label.config(text="No music files found!")
            return

        track = self.music_files[self.current_track_index]
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        self.label.config(text=f"Now Playing: {os.path.basename(track)}")

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            if self.is_paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            self.is_paused = not self.is_paused

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
