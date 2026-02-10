import tkinter as tk

class GUI:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.geometry("1000x600")

        download_frame = tk.Frame(self.root)

        title = tk.Label(download_frame, text="Download", font=('Arial', 20))
        title.pack(padx=20, pady=20)

        linkLabel = tk.Label(download_frame, text="Incolla il link del video", font=("Arial", 15))
        linkLabel.pack()
        linkInput = tk.Entry(download_frame, font=("Arial", 15))
        linkInput.pack(fill="x", padx=20)

        self.paylist_check_state = tk.IntVar()
        playlist_check = tk.Checkbutton(download_frame, text="Playlist?", font=("Arial", 16), variable=self.paylist_check_state)
        playlist_check.pack(pady=20)

        btn_grid = tk.Frame(download_frame)
        audio_dl_brn = tk.Button(btn_grid, text="Scarica Audio", font=("Arial", 16))
        audio_dl_brn.grid(row=0, column=0, padx=10)

        video_dl_btn = tk.Button(btn_grid, text="Scarica Video", font=("Arial", 16))
        video_dl_btn.grid(row=0, column=1, padx=10)
        btn_grid.pack()

        download_frame.pack(fill="both")

    def set_controller(self, controller):
        self.controller = controller
        # TODO


    def begin(self):
        self.root.mainloop()