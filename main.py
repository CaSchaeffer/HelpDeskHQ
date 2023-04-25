import tkinter
import tkinter.messagebox
import customtkinter
import sqlite3
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Datenbankpfad
db_file = 'faq_database.db'

#Überprüfung ob Datenbank bereits vorhanden ist
if os.path.exists(db_file):
    print('Die Datenbank existiert bereits')
else:
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect(db_file)
    
    # Cursor-Objekt erstellen
    cursor = conn.cursor()
    
    # Eine Tabelle erstellen
    cursor.execute('''CREATE TABLE faq
                      (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, category TEXT)''')
    
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    
    print('Die Datenbank wurde erstellt')

#Erstellung der eigentlichen GUI
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("FAQ for You.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Aktionen", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Button1", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Button2", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Suche nach einer bestimmten Frage")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Suche", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("TABS")
        self.tabview.add("Tab 2")
        self.tabview.tab("TABS").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("TABS"), text="Neue Frage Hinzufügen",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="Platzhalter TAB2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)


        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "Textbox der Datenbank\n\n" + "Hier erscheinen zunächst alle Fragen und Antworten aus der SQLite Datenbank, jedoch muss diese zunächst angegeben werden, damit ein Inhalt hier sichtbar wird\n\n" * 20)


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Mach eine Eingabe:", title="Neue Frage")
        print("Gemachte Eingabe: ", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("Button wurde betätigt")

#SQL Abfrage für alle Daten in der DB
    def get_all_faq():
    # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect(db_file)
    
    # Cursor-Objekt erstellen
        cursor = conn.cursor()
    
    # SELECT-Abfrage ausführen
        cursor.execute('SELECT * FROM faq')
    
    # Alle Zeilen abrufen
        rows = cursor.fetchall()
    
    # Verbindung schließen
        conn.close()
    
    # Ergebnis zurückgeben
        return rows
    
    def search_faq():
    # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect(db_file)
    
    # Cursor-Objekt erstellen
        cursor = conn.cursor()
    
    # Suchbegriff aus dem Entry-Widget abrufen
        search_term = search_entry.get()
    
    # SELECT-Abfrage ausführen
        if search_term:
        # Wenn ein Suchbegriff angegeben ist, nach entsprechenden FAQs suchen
            cursor.execute('SELECT * FROM faq WHERE question LIKE ?', ('%' + search_term + '%',))
        else:
        # Wenn kein Suchbegriff angegeben ist, alle FAQs abrufen
            cursor.execute('SELECT * FROM faq')
    
    # Alle Zeilen abrufen
        rows = cursor.fetchall()
    
    # Ergebnis in einem Text-Widget ausgeben
        result_text.delete('1.0', tk.END)
        for row in rows:
            result_text.insert(tk.END, f'{row[0]}. {row[1]}\n\n{row[2]}\n\nCategory: {row[3]}\n\n')
    
    # Verbindung schließen
    conn.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()
