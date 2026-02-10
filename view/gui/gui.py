import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("YouTube Downloader")
        self.root.geometry("1000x600")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # --- RIGA 0: TITOLO ---
        lbl_titolo = tk.Label(self.root, text="Benvenuto", font=("Arial", 20, "bold"))
        lbl_titolo.grid(row=0, column=0, columnspan=3, pady=10)

        # --- RIGA 1 & 2: LABEL + TEXTAREA ---
        lbl_area = tk.Label(self.root, text="Inserisci gli URL dei video (uno per riga):")
        lbl_area.grid(row=1, column=0, sticky="w", padx=20)

        self.link_area = tk.Text(self.root, height=5)
        self.link_area.grid(row=2, column=0, columnspan=3, padx=20, pady=(0, 20), sticky="ew")

        # --- RIGA 3: I DUE MENU E IL PULSANTE ---
        # Colonna 0: Primo Menu
        frame_menu1 = tk.Frame(self.root)
        frame_menu1.grid(row=3, column=0)
        tk.Label(frame_menu1, text="Formato").pack()
        self.combo_tipo = ttk.Combobox(frame_menu1, values=["Audio", "Video"], width=15, state="readonly")
        self.combo_tipo.pack()
        self.combo_tipo.current(0)

        # Colonna 1: Secondo Menu
        frame_menu2 = tk.Frame(self.root)
        frame_menu2.grid(row=3, column=1)
        tk.Label(frame_menu2, text="Playlist").pack()
        self.combo_playlist = ttk.Combobox(frame_menu2, values=["No playlist", "Playlist"], width=15, state="readonly")
        self.combo_playlist.pack()
        self.combo_playlist.current(0)

        # Colonna 2: Pulsante
        btn_azione = ttk.Button(self.root, text="Pulsante", command=self.funzione_pulsante)
        btn_azione.grid(row=3, column=2, sticky="s", pady=5)

        # --- RIGA 4 & 5: PERCENTUALE + PROGRESS BAR ---
        lbl_percentuale = tk.Label(self.root, text="Percentuale")
        lbl_percentuale.grid(row=4, column=0, columnspan=3, pady=(20, 0))

        self.barra_progresso = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.barra_progresso.grid(row=5, column=0, columnspan=3, padx=20, pady=5, sticky="ew")
        self.barra_progresso["value"] = 0

        # --- RIGA 6: MESSAGGI DI OUTPUT ---
        lbl_output_box = tk.Label(self.root, text="Messaggi di output", relief="sunken", bd=1, height=4)
        lbl_output_box.grid(row=6, column=0, columnspan=3, padx=20, pady=20, sticky="ew")

    def set_controller(self, controller):
        self.controller = controller
        # TODO


    def begin(self):
        self.root.mainloop()

    def funzione_pulsante(self):
        print("Pulsante premuto!")
        # Recupera testo dall'area (da riga 1, carattere 0 alla fine)
        contenuto = self.link_area.get("1.0", tk.END).strip()

        tipo = self.combo_tipo.get()
        playlist = self.combo_playlist.get()
        scelta = f"{tipo} - {playlist}"
        
        # Simula avanzamento barra
        self.barra_progresso["value"] = 100
        
        # Mostra finestra di dialogo
        messagebox.showinfo("Risultato", f"Opzione: {scelta}\nTesto inserito: {contenuto}")