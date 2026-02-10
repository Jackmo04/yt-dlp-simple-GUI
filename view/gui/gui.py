import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading

class GUI:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("YouTube Downloader")
        self.root.geometry("1000x600")

        self.style = ttk.Style(self.root)
        self.style.configure("Grande.TButton", font=("Arial", 14, "bold"))
        
        self.root.columnconfigure(0, weight=1, uniform="col")
        self.root.columnconfigure(1, weight=1, uniform="col")

        # --- TITOLO ---
        lbl_titolo = tk.Label(self.root, text="Benvenuto", font=("Arial", 20, "bold"))
        lbl_titolo.grid(row=0, column=0, columnspan=2, pady=20)

        # --- AREA LINK ---
        lbl_area = tk.Label(self.root, text="Inserisci gli URL dei video (uno per riga):")
        lbl_area.grid(row=1, column=0, sticky="w", padx=20)

        self.link_area = tk.Text(self.root, height=5)
        self.link_area.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

        # --- OPZIONI ---
        frame_menu1 = tk.Frame(self.root)
        frame_menu1.grid(row=3, column=0, pady=10)
        tk.Label(frame_menu1, text="Formato").pack()
        self.combo_tipo = ttk.Combobox(frame_menu1, values=["Audio (mp3)", "Video (mp4)"], width=20, state="readonly")
        self.combo_tipo.current(0)
        self.combo_tipo.pack()

        frame_menu2 = tk.Frame(self.root)
        frame_menu2.grid(row=3, column=1, pady=10)
        tk.Label(frame_menu2, text="Sono delle playlist?").pack()
        self.combo_playlist = ttk.Combobox(frame_menu2, values=["No", "Sì"], width=20, state="readonly")
        self.combo_playlist.current(0)
        self.combo_playlist.pack()

        # --- PULSANTE ---
        self.btn_azione = ttk.Button(self.root, text="Scarica tutto", command=self.download, width=20, style="Grande.TButton")
        self.btn_azione.grid(row=4, column=0, columnspan=2, pady=20)

        # --- PERCENTUALE + PROGRESS BAR ---
        self.lbl_perc_singolo = tk.Label(self.root, text="Video 0 di 0 | Completamento: 0%")
        self.lbl_perc_singolo.grid(row=5, column=0, columnspan=2, pady=(20, 0))

        self.progresso_singolo = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.progresso_singolo.grid(row=6, column=0, columnspan=3, padx=20, pady=5, sticky="ew")
        self.progresso_singolo["value"] = 0

        self.lbl_perc_totale = tk.Label(self.root, text="Totale | Completamento: 0%")
        self.lbl_perc_totale.grid(row=7, column=0, columnspan=2, pady=(10, 0))

        self.progresso_totale = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.progresso_totale.grid(row=8, column=0, columnspan=3, padx=20, pady=5, sticky="ew")
        self.progresso_totale["value"] = 0

    def set_controller(self, controller):
        self.controller = controller
        if self.controller.is_update_available():
            self.show_update_available()

    def begin(self):
        self.root.mainloop()

    def download(self):
        def start_download():
            urls = self.link_area.get("1.0", tk.END).strip().splitlines()
            tipo = self.combo_tipo.get()
            playlist = self.combo_playlist.get() == "Sì"

            if not urls or urls == [""]:
                self.display_error("Errore", "Per favore, inserisci almeno un URL.")
                return

            self.btn_azione.config(state="disabled")
            self.root.protocol("WM_DELETE_WINDOW", self.on_close_during_download)

            if tipo == "Audio (mp3)":
                self.controller.download_audio(urls, playlist)
            else:
                self.controller.download_video(urls, playlist)

            # After the download is complete, reset the UI
            self.link_area.delete("1.0", tk.END)
            self.btn_azione.config(state="normal")
            self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        threading.Thread(target=start_download).start()

    def on_close_during_download(self):
        r = messagebox.askyesno("Download in corso", "Un download è attualmente in corso. Sei sicuro di voler chiudere il programma? Il download verrà interrotto.")
        if r:
            self.root.destroy()

    def display_error(self, title, message):
        messagebox.showerror(title, message)

    def display_success(self, title, message):
        messagebox.showinfo(title, message)

    def update_single_progress(self, current, todo, percent):
        self.progresso_singolo["value"] = percent
        self.lbl_perc_singolo.config(text=f"Video {current} di {todo} | Completamento: {percent}%")
        self.root.update_idletasks()

    def update_total_progress(self, percent):
        self.progresso_totale["value"] = percent
        self.lbl_perc_totale.config(text=f"Totale | Completamento: {percent}%")
        self.root.update_idletasks()
        
    def show_update_available(self):
        r = messagebox.askyesno("Aggiornamento disponibile", 
                                "È disponibile una nuova versione del software. Vuoi scaricarla?\n"
                                "(Se sì, il sowftware verrà riavviato)")
        if not r:
            return
        
        popup = tk.Toplevel(self.root)
        popup.title("Attendere...")
        popup.geometry("300x100")
        popup.grab_set() # Rende il popup modale

        popup.protocol("WM_DELETE_WINDOW", lambda: None) # Disabilita la chiusura del popup

        update_progress = ttk.Progressbar(popup, orient="horizontal", mode="indeterminate")
        update_progress.pack(pady=10, padx=20, fill="x")
        update_progress.start(10) # Avvia l'animazione della barra di progresso

        tk.Label(popup, text="Aggiornamento in corso...").pack(pady=20)
        popup.update_idletasks() # Assicura che il popup venga disegnato prima di iniziare l'aggiornamento

        def run_update():
            ok = self.controller.update()
            self.root.after(0, lambda: self.finish_update(ok, popup)) # Esegue finish_update nel thread principale dopo che l'aggiornamento è completato

        threading.Thread(target=run_update).start()
        
    def finish_update(self, ok, popup):
        popup.destroy()

        if ok:
            messagebox.showinfo("Aggiornamento completato", "L'aggiornamento è stato completato con successo. Il software ora si riavvierà.")
            self.controller.restart()
        else:
            messagebox.showerror("Errore", "Si è verificato un errore durante l'aggiornamento. Riprova più tardi.")