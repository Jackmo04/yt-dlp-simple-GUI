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
        tk.Label(frame_menu2, text="Sono delle playlist").pack()
        self.combo_playlist = ttk.Combobox(frame_menu2, values=["No", "Sì"], width=20, state="readonly")
        self.combo_playlist.current(0)
        self.combo_playlist.pack()

        # --- PULSANTE ---
        btn_azione = ttk.Button(self.root, text="Scarica tutto", command=self.start_download, width=20, style="Grande.TButton")
        btn_azione.grid(row=4, column=0, columnspan=2, pady=20)

        # --- PERCENTUALE + PROGRESS BAR ---
        lbl_percentuale = tk.Label(self.root, text="Completamento: 0%")
        lbl_percentuale.grid(row=5, column=0, columnspan=2, pady=(20, 0))

        self.barra_progresso = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.barra_progresso.grid(row=6, column=0, columnspan=3, padx=20, pady=5, sticky="ew")
        self.barra_progresso["value"] = 0

        # --- OUTPUT ---
        lbl_output_box = tk.Label(self.root, text="Messaggi di output", relief="sunken", bd=1, height=4)
        lbl_output_box.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    def set_controller(self, controller):
        self.controller = controller
        if self.controller.is_update_available():
            self.show_update_available()

    def begin(self):
        self.root.mainloop()

    def start_download(self):
        urls = self.link_area.get("1.0", tk.END).strip().splitlines()
        tipo = self.combo_tipo.get()
        playlist = self.combo_playlist.get()
        
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