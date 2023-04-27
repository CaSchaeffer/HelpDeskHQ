# Benötigte Module
import tkinter # GUI
import tkinter.messagebox # GUI Fenster in Fenster
import customtkinter # Verbessertes Design für die GUI
import sqlite3 # Anbindung für eine lokale Datenbank
import os # Anbindung zu Dateipfaden und Ordnern zum Lokalisieren der .db Datei


#Grundeinstellungen der GUI - Modus und Farbe werden hier übergeben
customtkinter.set_appearance_mode("System")  # Modi: "System" (standart), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themen: "blue" (standart), "green", "dark-blue"


#Datenbankpfad - Muss im gleichen Ordner wie das Programm liegen -> sonst muss hier der vollständige Dateipfad angegeben werden
db_file = 'faq_database.db'

#Überprüfung ob Datenbank bereits vorhanden ist
if os.path.exists(db_file):
    print('Die Datenbank existiert bereits')
# Datenbank wird neu Erstellt und befüllt mir 3 Standartfragen und Antworten
else:
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect(db_file)
    
    # Cursor-Objekt erstellen
    c = conn.cursor()
    
    # Eine Tabelle erstellen
    c.execute('''CREATE TABLE faq
                      (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, category TEXT)''')
    # Daten zur Tabelle hinzufügen
    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
               ("Was ist ein Betriebssystem?", "Ein Betriebssystem ist eine Software, die den Betrieb eines Computers ermöglicht und steuert.", "Betriebssystem"))
    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
               ("Wie kann ich meinen Computer schneller machen?", "Es gibt mehrere Möglichkeiten, um die Leistung Ihres Computers zu verbessern, wie zum Beispiel das Löschen von temporären Dateien, das Deinstallieren unnötiger Programme und das Aktualisieren Ihrer Treiber.", "Computer-Optimierung"))
    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
               ("Wie kann ich mein Passwort ändern?", "Je nachdem, welches Betriebssystem Sie verwenden, können Sie Ihr Passwort normalerweise über die Einstellungen oder Systemsteuerung ändern.", "Passwort-Management"))


    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    
    print('Die Datenbank wurde erstellt')



#Erstellung der GUI
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Konfiguriert den Mainframe des Programmes mit Titel und Pixelgröße des Fensters
        self.title("HelpDeskHQ")
        self.geometry(f"{1100}x{580}")

        # Konfiguriert das Netz was für das Layout zuständig ist
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Erstellt das Nebenfenster ( Rechte Seite) mit den dazugehörigen Buttons
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Aktionen", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Login", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Button2", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Hier beginnen die Sonderfunktionen wie das Umstellen des Modus und das Anpassen der Vergrößerung
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

        # Erstellt den Mainframe für die GUI - Hauptfenster - Hier ist auch die Suchleiste mit dem "Suchen-Button" zu finden
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Geben Sie hier eine zu suchende Frage ein... ")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Suchen", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                                            command=self.search_database)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Erstellt die große, mittige Textbox
        self.textbox = customtkinter.CTkTextbox(self, width=1200 , height=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.configure(state="normal")

        # Erstellt das Tabfenster mit mehren Mini- Seiten - TAB2 vorerst deaktiviert
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(30, 0), pady=(30, 0), sticky="nsew")
        self.tabview.add("TABS")
        # self.tabview.add("Tab 2")
        self.tabview.tab("TABS").grid_columnconfigure(0, weight=1)  # Hier können die einzelnen Tabs bearbeitet werden
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("TABS"), text="Neue Frage stellen",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

# Tabseite 2 zunächst Deaktiviert bis diese benötigt wird

        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="Platzhalter TAB2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)


        # Setzt die Standartwerte für die GUI - Hier muss der Inhalt für die Textbox eingeben werden
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0","")
        
    # Öffnet zwei Dialogfenster - zunächst kann eine Frage eingegeben werden, dann kann das 2. Fenster für die Antwort genutzt werden 
    # - Anbindung an Datenbank fehlt bzw Eingabe wird nicht als String anerkannt und auch nicht weiterverarbeitet von der SQL-Abfrage
    def open_input_dialog_event(self):
        antwort = customtkinter.CTkInputDialog(text="Gebe eine Antwort ein: ", title="Antwort")
        antwortInput = antwort.get_input()
        frage = customtkinter.CTkInputDialog(text="Gebe eine Frage ein", title="Neue Frage stellen")
        frageInput = frage.get_input()
        print("Frage: ", frage.get_input())
        print("Antwort: ",antwort.get_input())

        # Funktion zum schreiben neuer Fragen und Antworten
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        c.execute("INSERT INTO faq (question, answer) VALUES (?, ?)",(frageInput,antwortInput))
        conn.commit()
        conn.close()

    # Funktion für das ändern des Anzeigemodus (light,dark oder vom System gegebener Modus)
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Funktion für das Vergrößern/Verkleinern der Ansicht
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    # Funktionierdende Abfrage die zunächst alle Einträge in der Datenbank sichtbar macht -> muss noch im allgemeinen Code hinzugefügt werden, sodass beim Starten des Programms alle Daten gezogen werden
    # Aktuell werden alle Daten angezeigt, sobald man auf den Button "Login" klickt
    def sidebar_button_event(self):
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        c.execute('SELECT id, question, answer FROM faq')
        global rows 
        rows = c.fetchall()
        for row in rows:
            counter = 1
            id, question , answer = row
            self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
            self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
            counter += 1
        conn.close()

    # Unfertige gefilterte Abfrage; hier fehlt das Löschen aller alten Einträge und die verbesserte Darstellung des gefundenen Datensatzes
    def search_database(self):
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
    
        # Suchabfrage ausführen
        anfrage = self.entry.get()
        self.entry.delete(0,100)

        # Funktion zum Löschen der ersten Datenbankabfrage, sodass nur noch eine passende Frage dargestellt wird 
        c.execute("SELECT question, answer FROM faq WHERE question LIKE ?", ('%' + anfrage + '%',))
        rows = c.fetchall()
        question = rows
        self.textbox.insert(tkinter.END, question)
        print("Folgende Eingabe wurde gemacht: ",
               anfrage)
        conn.close()

# start der GUI
if __name__ == "__main__":
    app = App()
    app.mainloop()
