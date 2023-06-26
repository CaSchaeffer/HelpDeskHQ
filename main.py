# Benötigte Module
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
db_file = "faq_database.db"

#Überprüfung ob Datenbank bereits vorhanden ist
print("GUI wird gestartet...")
if os.path.exists(db_file):
    print("Eine vorhandene Datenbank wurde gefunden!")

# Datenbank wird neu Erstellt und befüllt mir 3 Standartfragen und Antworten
else:
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect(db_file)
    
    # Cursor-Objekt erstellen
    c = conn.cursor()
    
    # Eine Tabelle erstellen
    c.execute('''CREATE TABLE questions (
	                                        id integer PRIMARY KEY AUTOINCREMENT,
	                                        question text,
	                                        answer text,
	                                        date datetime,
	                                        q_id integer,
                                            FOREIGN KEY (q_id) REFERENCES categorys(category_id)
                                            )''')

    
    # Daten zur Tabelle questions hinzufügen - Felder: question, answer, date, q_id
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was versteht man unter Big Data?', 'Unter Big Data versteht man die Verarbeitung und Analyse von großen Datenmengen, die herkömmliche Datenverarbeitungs- und Analysemethoden überfordern würden.', '2023-05-08', 1))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
               ('Was ist eine API?', 'Eine API (Application Programming Interface) ist eine Schnittstelle, die es ermöglicht, dass verschiedene Anwendungen miteinander kommunizieren und Daten austauschen können.', '2023-05-08', 2))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
               ('Was ist Cloud Computing?', 'Cloud Computing bezeichnet die Bereitstellung von IT-Ressourcen (z.B. Rechenleistung, Speicherplatz) über das Internet, anstatt sie lokal auf einem eigenen Rechner oder Server zu betreiben.', '2023-05-08', 3))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist künstliche Intelligenz?', 'Künstliche Intelligenz bezeichnet die Fähigkeit von Maschinen, Aufgaben auszuführen, die normalerweise menschliche Intelligenz erfordern würden.', '2023-06-26', 4))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist Blockchain?', 'Die Blockchain ist eine dezentrale und transparente Datenbank, die Informationen in Blöcken speichert und eine sichere Verkettung dieser Blöcke gewährleistet.', '2023-06-26', 5))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist das Internet der Dinge (IoT)?', 'Das Internet der Dinge bezieht sich auf die Vernetzung von physischen Geräten und Objekten, die über Sensoren und Netzwerkverbindungen miteinander kommunizieren und Daten austauschen können.', '2023-06-26', 6))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist Virtual Reality (VR)?', 'Virtual Reality ist eine computergenerierte Umgebung, die es Benutzern ermöglicht, in eine immersive Erfahrung einzutauchen und interaktiv mit virtuellen Objekten und Szenarien zu interagieren.', '2023-06-26', 7))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist Augmented Reality (AR)?', 'Augmented Reality bezieht sich auf die erweiterte Darstellung der realen Welt durch computergenerierte Informationen und virtuelle Elemente, die in Echtzeit in die Umgebung des Benutzers eingeblendet werden.', '2023-06-26', 8))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist Machine Learning?', 'Machine Learning bezieht sich auf die Entwicklung von Algorithmen und Modellen, die es Computern ermöglichen, aus Erfahrungen zu lernen und automatisch Entscheidungen zu treffen, ohne explizit programmiert zu sein.', '2023-06-26', 9))
    c.execute("INSERT INTO questions (question, answer, date, q_id) VALUES (?, ?, ?, ?)",
                ('Was ist Data Mining?', 'Data Mining bezeichnet den Prozess der Entdeckung von Mustern, Zusammenhängen und Informationen aus großen Datenmengen, um nützliche Erkenntnisse zu gewinnen.', '2023-06-26', 10))

    # Daten zur Tabelle categorys hinzufügen - Felder: category_id, category
    c.execute('''CREATE TABLE categorys (
	                                        category_id integer PRIMARY KEY AUTOINCREMENT,
	                                        category text
                                            )''')
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (1, 'Big Data'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (2, 'API'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (3, 'Cloud Computing'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (4, 'Künstliche Intelligenz'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (5, 'Blockchain'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (6, 'Internet of Things (IoT)'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (7, 'Virtual Reality (VR)'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (8, 'Augmented Reality (AR)'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (9, 'Machine Learning'))
    c.execute("INSERT INTO categorys (category_id, category) VALUES (?, ?)",
                (10, 'Data Mining'))        
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    
    print("Keine bestehende Datenbank unter dem angegebenen Dateipfad gefunden....")
    print("Eine neue Datenbank wurde erfolgreich erstellt!")


# Erstellung der GUI
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # SQL-Abfrage zum Abrufen aller Werte aus beiden Tabellen
        sql = "SELECT category FROM categorys"
        c.execute(sql)
        global row 
        row = c.fetchall()
        global category_filter_options
        category_filter_options = []
        for row in row:
            counter = 0
            category= row
            category1 = category[counter]
            category_filter_options.append(f"{category1}")
            counter+=1



        # Konfiguriert den Mainframe des Programmes mit Titel und Pixelgröße des Fensters
        self.title("HelpDeskHQ - Das FAQ in Sachen Computerfragen")
        self.geometry(f"{1300}x{580}")

        # Konfiguriert das Netz was für das Layout zuständig ist
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Erstellt das Nebenfenster ( Rechte Seite) mit den dazugehörigen Buttons
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Erstellt Label "Aktionen" und Button zum Neuladen
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Aktionen", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Daten neu Laden",
                                                             command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=(10,0))

        # Button 2 unter "Aktionen" vorerst deaktiviert da keine Funktion
        #self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="-", command=self.sidebar_button_event)
        #self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Hier beginnen die Sonderfunktionen wie das Umstellen des Modus und das Anpassen der Vergrößerung

        # Darstellungsmodus
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Darstellung:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))

        # Vergößerung
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Skalierung:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))


        # Erstellt den Mainframe für die GUI - Hauptfenster - Hier ist auch die Suchleiste mit dem "Suchen-Button" zu finden

        # Untere Suchleiste
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Geben Sie hier eine zu suchende Frage ein... ")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # Suchknopf
        self.main_button_1 = customtkinter.CTkButton(master=self, text="Suchen", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                                            command=self.search_database)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Erstellt die große, mittige Textbox
        self.textbox = customtkinter.CTkTextbox(self, width=450 , height=450)
        self.textbox.grid(row=0, column=1, padx=(30, 0), pady=(30, 0), sticky="nsew")
        self.textbox.configure(state="normal")

        # Erstellt das Tabfenster mit mehren Mini- Seiten - 
        self.tabview = customtkinter.CTkTabview(self, width=100)
        self.tabview.grid(row=0, column=3, padx=(20, 0), pady=(10, 0), sticky="nsew")
        self.tabview.add("Menü")
        self.tabview.tab("Menü").grid_columnconfigure(0, weight=1)

        # TAB2 vorerst deaktiviert
        # self.tabview.add("Tab 2")
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="Platzhalter TAB2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # Erstellt die einzelnen Buttons auf der Menüseite 1
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Menü"), text="Neue Frage stellen",command=self.open_toplevel_new)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_button_2 = customtkinter.CTkButton(self.tabview.tab("Menü"), text="Eine Frage bearbeiten", command= self.open_toplevel_edit)

        self.string_input_button_2.grid(row=3, column=0, padx=20, pady=(10,10)) 

        self.string_input_button_3 = customtkinter.CTkButton(self.tabview.tab("Menü"), text="Eine Frage löschen", command= self.open_toplevel_delete)

        self.string_input_button_3.grid(row=4, column=0, padx=20, pady=(10,10))

        self.string_dropdown_label= customtkinter.CTkLabel(self.tabview.tab("Menü"), text="Kategorien filtern: ")
        self.string_dropdown_label.grid(row=5, column=0, padx=20, pady=(10,10))

        self.string_dropdown = customtkinter.CTkOptionMenu(self.tabview.tab("Menü"),  dynamic_resizing=False,
                                                        values=category_filter_options)
        self.string_dropdown.grid(row=6, column=0, padx=20, pady=(20, 10))

        # Setzt die Standartwerte für die GUI - Hier muss der Inhalt für die Textbox eingeben werden
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
        self.textbox.insert(tkinter.END, "Fragen und Antworten des HelpDeskHQ's" +"\n\n") 
        
        sql = "SELECT * FROM questions"

       # Ausführen der Abfrage
        c.execute(sql,)

        # Ergebnisse abrufen
        row = c.fetchall()
        self.textbox.delete("0.0",tkinter.END)
        for row in row:
            counter = 0
            id, question , answer, date, q_id = row          
            self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
            self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
            c.execute("SELECT category FROM categorys WHERE category_id = '"+str(q_id)+"'")
            category = c.fetchone()
            category1 = category[counter]
            self.textbox.insert(tkinter.END, "Kategorie ID: " + F"{q_id}"+ "\n\n"+ category1  + "\n\n")
            self.textbox.insert(tkinter.END,"Erstellt am: " + date + "\n\n")  
            counter += 1
        conn.close()           

        
    # Funktion für das ändern des Anzeigemodus (light,dark oder vom System gegebener Modus)
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Funktion für das Vergrößern/Verkleinern der Ansicht
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    # Neuladebutton der die Daten nochmals frisch aus der Datenbank abruft - nützlich nach neuen Eingaben
    def sidebar_button_event(self):

        conn.close()

    # Filterabfrage die auf den "Suche-Button" reagiert
    def search_database(self):
        #Verbindung mit der Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # Suchabfrage ausführen für eine bestimmte Frage oder Kategorie
        search_request = self.entry.get()
        category_filter_option_selected = self.string_dropdown.get()
        self.entry.delete(0,100)

        if search_request !="":
            # SQL-Abfrage zum Suchen in allen Feldern der Tabelle
            sql = "SELECT * FROM questions WHERE question LIKE ? OR answer LIKE ? OR date LIKE ?"

            # Platzhalterwerte für die Suchbegriffe angeben
            suchbegriff_wildcard = f"%{search_request}%"
            werte = (suchbegriff_wildcard, suchbegriff_wildcard, suchbegriff_wildcard)

            # Ausführen der Abfrage
            c.execute(sql, werte)

            # Ergebnisse abrufen
            row = c.fetchall()
            self.textbox.delete("0.0",tkinter.END)
            for row in row:
                id, question , answer, date, q_id = row
                self.textbox.insert(tkinter.END, "Treffer im HelpDeskHQ für folgende Sucheingabe:  "+ search_request +"\n\n")            
                self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
                self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
                self.textbox.insert(tkinter.END, "Kategorie ID: " + F"{q_id}"+ "\n\n" + category_filter_option_selected + "\n\n")
                self.textbox.insert(tkinter.END,"Erstellt am: " + date + "\n\n")  
            conn.close()

        elif category_filter_option_selected !="":

            # SQL-Abfrage zum Abrufen des passenden Datensatzes
            sql = '''SELECT * FROM questions WHERE q_id = (
                    SELECT category_id FROM categorys WHERE category = ?
                    )'''

            # Platzhalterwert für die ausgewählte Kategorie angeben
            werte = (category_filter_option_selected,)

            # Ausführen der Abfrage
            c.execute(sql, werte)
            row = c.fetchall()
            self.textbox.delete("0.0",tkinter.END)
            for row in row:
                id, question , answer, date, q_id = row
                self.textbox.insert(tkinter.END, "Treffer im HelpDeskHQ für folgende Sucheingabe:  "+ search_request+ category_filter_option_selected +"\n\n")            
                self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
                self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
                self.textbox.insert(tkinter.END, "Kategorie ID: " + F"{q_id}"+ "\n\n" + category_filter_option_selected + "\n\n")
                self.textbox.insert(tkinter.END,"Erstellt am: " + date + "\n\n")  
            conn.close()

    def open_toplevel_new(self):
        #Verbindung mit der Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()


        self.toplevel_window_new = ToplevelWindow_new(self)

    def open_toplevel_edit(self):
        #Verbindung mit der Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()


        self.toplevel_window_edit = ToplevelWindow_edit(self)

    def open_toplevel_delete(self):
        #Verbindung mit der Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()


        self.toplevel_window_delete = ToplevelWindow_delete(self)

class ToplevelWindow_new(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("HelpDeskHQ - Eine Frage eingeben")
        self.geometry("950x500")
        
        # Textfelder (3 Stück) zum Bearbeiten der ausgewählten Frage
        self.grid()

        # Erstelle das erste Textfeld
        self.label1 = customtkinter.CTkLabel(self, text="Neue Frage eingeben:")
        self.label1.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox1 = customtkinter.CTkTextbox(self, height=30, width=900)
        self.textbox1.grid(row=4, column=0, padx=10, pady=10)

        # Erstelle das zweite Textfeld
        self.label2 = customtkinter.CTkLabel(self, text="Neue Antwort eingeben:")
        self.label2.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, height=30, width=900)
        self.textbox2.grid(row=6, column=0, padx=10, pady=10)

        # Button zum Speichern der Änderungen
        self.save_button = customtkinter.CTkButton(self, text="Speichern", command= self.open_toplevel_confirm_new)
        self.save_button.grid(row=10, column=0, padx=10, pady=10)

        # Dropdownmenü zur Auswahl
        self.string_dropdown = customtkinter.CTkOptionMenu(self,  dynamic_resizing=False,
                                                        values=category_filter_options)
        self.string_dropdown.grid(row=8, column=0, padx=20, pady=(20, 10))

        # Button zum Verwerfen der Änderungen
        self.cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command= self.dismiss_changes_new)
        self.cancel_button.grid(row=9, column=0, padx=10, pady=10)


    def open_toplevel_confirm_new(self):
        global textbox1_answer1
        textbox1_answer1= self.textbox1.get("0.0","end")
        global textbox2_answer2
        textbox2_answer2= self.textbox2.get("0.0","end")
        global textbox3_answer3
        textbox3_answer3= self.string_dropdown.get()
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        # Schreibbefehl der entweder den alten Wert bei keiner Eingabe nimmt oder den Wert der gemachten Eingabe
        c.execute("INSERT INTO questions (question,answer) VALUES (?,?)", (textbox1_answer1, textbox2_answer2))
        conn.commit()
        c.execute("SELECT id FROM questions WHERE question = ?", (textbox1_answer1))
        question_number =c.fetchone
        c.execute("SELECT category_id FROM categorys WHERE category = ?", (textbox3_answer3,))
        result = c.fetchone()
        c.execute("UPDATE questions SET q_id = ? WHERE id LIKE ?",(f"%{result}%", f"%{question_number}%"))
        conn.commit()
        ToplevelWindow_new.destroy(self)

    def dismiss_changes_new(self):
        # Hier kannst du den Code einfügen, um die Änderungen zu verwerfen
        ToplevelWindow_new.destroy(self)
        print("Vorgang abgebrochen")
    
 
class ToplevelWindow_edit(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("HelpDeskHQ - Eine Frage bearbeiten")
        self.geometry("950x500")

        sql = "SELECT question FROM questions"
        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
       # Ausführen der Abfrage
        c.execute(sql)

        # Ergebnisse abrufen
        row = c.fetchall()
        question_filter_options=[]
        for row in row:
            counter = 0
            question = row          
            question1 = question[counter]
            question_filter_options.append(f"{question1}")
            counter += 1
        conn.close()

        # Dropdown zum Auswählen der Frage
        self.string_dropdown = customtkinter.CTkOptionMenu(self,height=40 ,width=650, dynamic_resizing=False, values=question_filter_options)
        self.string_dropdown.grid(row=1, column=0, padx=20, pady=(20, 30),sticky="nsew")
        
        # Bestätigungsbutton für die ausgewählte Frage
        self.confirm_button = customtkinter.CTkButton(self, text="Bestätigen", command=self.select_to_edit)
        self.confirm_button.grid(row=2, column=0, padx=20, pady=10)
        
        # Textfelder (3 Stück) zum Bearbeiten der ausgewählten Frage
        self.grid()

        # Erstelle das erste Textfeld
        self.label1 = customtkinter.CTkLabel(self, text="Frage:")
        self.label1.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox1 = customtkinter.CTkTextbox(self, height=30, width=900)
        self.textbox1.grid(row=4, column=0, padx=10, pady=10)

        # Erstelle das zweite Textfeld
        self.label2 = customtkinter.CTkLabel(self, text="Antwort:")
        self.label2.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, height=30, width=900)
        self.textbox2.grid(row=6, column=0, padx=10, pady=10)

        # Erstelle das dritte Textfeld
        self.label3 = customtkinter.CTkLabel(self, text="Kategorie:")
        self.label3.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox3 = customtkinter.CTkTextbox(self, height=10, width=500)
        self.textbox3.grid(row=8, column=0, padx=10, pady=5)

        # Button zum Speichern der Änderungen
        self.save_button = customtkinter.CTkButton(self, text="Speichern", command= self.save_changes)
        self.save_button.grid(row=10, column=0, padx=10, pady=10)

        # Dropdownmenü für die Auswahl der Kategorie - Admineingabe


        # Button zum Verwerfen der Änderungen
        self.cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command= self.dismiss_changes)
        self.cancel_button.grid(row=9, column=0, padx=10, pady=10)

    def select_to_edit(self):
        question_filter_option_selected = self.string_dropdown.get()
        print(question_filter_option_selected)

        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # SQL-Abfrage zum Abrufen des passenden Datensatzes
        sql = "SELECT * FROM questions WHERE question LIKE ?"

        # Platzhalterwert für die ausgewählte Kategorie angeben
        werte = (question_filter_option_selected,)

        # Ausführen der Abfrage
        c.execute(sql, werte)
        rows = c.fetchall()

        # Textboxen leeren
        self.textbox1.delete("1.0", tkinter.END)
        self.textbox2.delete("1.0", tkinter.END)
        self.textbox3.delete("1.0", tkinter.END)

        for row in rows:
            id, question, answer, date, q_id = row

            self.textbox1.insert(tkinter.END, question+"\n")
            self.textbox2.insert(tkinter.END, answer+"\n")

            c.execute("SELECT category FROM categorys WHERE category_id LIKE ?", (q_id,))
            category = c.fetchone()
            if category:
                category1 = category[0]
                self.textbox3.insert(tkinter.END, category1)
        conn.close()

    def save_changes(self):
        question_filter_option_selected = self.string_dropdown.get()
        global textbox1_answer1
        textbox1_answer1= self.textbox1.get("0.0","end")
        global textbox2_answer2
        textbox2_answer2= self.textbox2.get("0.0","end")
        global textbox3_answer3
        textbox3_answer3= self.textbox3.get("0.0","end")

        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        to_edit_question = question_filter_option_selected

        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        # Greift den Datensatz mit der passenden Nummer ab
        c.execute("SELECT q_id FROM questions WHERE question LIKE ?", ('%' + to_edit_question + '%',))
        row=c.fetchone()
        row=row[0]
        print(f"{row}")
        # Schreibbefehl der entweder den alten Wert bei keiner Eingabe nimmt oder den Wert der gemachten Eingabe
        c.execute("UPDATE questions SET question = ?, answer = ? WHERE id LIKE ?", (textbox1_answer1, textbox2_answer2, f"%{row}%"))
        conn.commit()
        c.execute("UPDATE categorys SET category = ? WHERE category_id LIKE ?",(textbox3_answer3, f"%{row}%"))
        row= c.fetchone()  
        conn.commit()

    def dismiss_changes(self):
        ToplevelWindow_delete.destroy(self)
        print("Vorgang abgebrochen")   
 
class ToplevelWindow_delete(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("HelpDeskHQ - Eine Frage löschen")
        self.geometry("950x500")

        sql = "SELECT question FROM questions"
        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
       # Ausführen der Abfrage
        c.execute(sql)

        # Ergebnisse abrufen
        row = c.fetchall()
        question_filter_options=[]
        for row in row:
            counter = 0
            question = row          
            question1 = question[counter]
            question_filter_options.append(f"{question1}")
            counter += 1
        conn.close()

        # Dropdown zum Auswählen der Frage
        self.string_dropdown = customtkinter.CTkOptionMenu(self,height=40 ,width=650, dynamic_resizing=False, values=question_filter_options)
        self.string_dropdown.grid(row=1, column=0, padx=20, pady=(20, 30),sticky="nsew")
        
        # Bestätigungsbutton für die ausgewählte Frage
        self.confirm_button = customtkinter.CTkButton(self, text="Bestätigen", command=self.select_to_edit)
        self.confirm_button.grid(row=2, column=0, padx=20, pady=10)
        
        # Textfelder (3 Stück) zum Bearbeiten der ausgewählten Frage
        self.grid()

        # Erstelle das erste Textfeld
        self.label1 = customtkinter.CTkLabel(self, text="Frage:")
        self.label1.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox1 = customtkinter.CTkTextbox(self, height=30, width=900)
        self.textbox1.grid(row=4, column=0, padx=10, pady=10)

        # Erstelle das zweite Textfeld
        self.label2 = customtkinter.CTkLabel(self, text="Antwort:")
        self.label2.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, height=30, width=900)
        self.textbox2.grid(row=6, column=0, padx=10, pady=10)

        # Erstelle das dritte Textfeld
        self.label3 = customtkinter.CTkLabel(self, text="Kategorie:")
        self.label3.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
        self.textbox3 = customtkinter.CTkTextbox(self, height=10, width=500)
        self.textbox3.grid(row=8, column=0, padx=10, pady=5)

        # Button zum Speichern der Änderungen
        self.save_button = customtkinter.CTkButton(self, text="Löschen", command= self.open_toplevel_confirm)
        self.save_button.grid(row=10, column=0, padx=10, pady=10)

        # Button zum Verwerfen der Änderungen
        self.cancel_button = customtkinter.CTkButton(self, text="Abbrechen", command= self.dismiss_changes)
        self.cancel_button.grid(row=9, column=0, padx=10, pady=10)

    def select_to_edit(self):
        question_filter_option_selected = self.string_dropdown.get()
        print(question_filter_option_selected)

        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # SQL-Abfrage zum Abrufen des passenden Datensatzes
        sql = "SELECT * FROM questions WHERE question LIKE ?"

        # Platzhalterwert für die ausgewählte Kategorie angeben
        werte = (question_filter_option_selected,)

        # Ausführen der Abfrage
        c.execute(sql, werte)
        rows = c.fetchall()

        # Textboxen leeren
        self.textbox1.delete("1.0", tkinter.END)
        self.textbox2.delete("1.0", tkinter.END)
        self.textbox3.delete("1.0", tkinter.END)

        for row in rows:
            id, question, answer, date, q_id = row

            self.textbox1.insert(tkinter.END, question+"\n")
            self.textbox2.insert(tkinter.END, answer+"\n")

            c.execute("SELECT category FROM categorys WHERE category_id LIKE ?", (q_id,))
            category = c.fetchone()
            if category:
                category1 = category[0]
                self.textbox3.insert(tkinter.END, category1)

        conn.close()
    def open_toplevel_confirm(self):
        global question_filter_option_selected
        question_filter_option_selected = self.string_dropdown.get()
        global textbox1_answer1
        textbox1_answer1= self.textbox1.get("0.0","end")
        global textbox2_answer2
        textbox2_answer2= self.textbox2.get("0.0","end")
        global textbox3_answer3
        textbox3_answer3= self.textbox3.get("0.0","end")
        ToplevelWindow_confirm_delete(self)  

    def dismiss_changes(self):
        # Hier kannst du den Code einfügen, um die Änderungen zu verwerfen
        ToplevelWindow_delete.destroy(self)
        print("Vorgang abgebrochen")
    
class ToplevelWindow_confirm_delete(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("HelpDeskHQ - Bestätigen des Löschens")
        self.geometry("400x150")

        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # Bestätigungslabel
        self.confirm_label = customtkinter.CTkLabel(self,text="Bist du sicher das du die Auswahl löschen möchtest?")
        self.confirm_label.grid(row=0, column=0, padx=20,pady=10)
        # Bestätigungsbutton für die ausgewählte Frage
        self.confirm_button = customtkinter.CTkButton(self, text="Löschen", command=self.delete_entry)
        self.confirm_button.grid(row=1, column=0, padx=20, pady=10)
        # Abbrechbutton
        self.confirm_button = customtkinter.CTkButton(self, text="Abbrechen", command=self.dismiss_changes)
        self.confirm_button.grid(row=2, column=0, padx=20, pady=10)

        ToplevelWindow_confirm_delete.focus(self)

    def delete_entry(self):
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        to_edit_question = question_filter_option_selected

        # Greift den Datensatz mit der passenden Nummer ab
        c.execute("SELECT q_id FROM questions WHERE question LIKE ?", ('%' + to_edit_question + '%',))
        row=c.fetchone()
        row=row[0]
        print(f"{row}")
        # Schreibbefehl der entweder den alten Wert bei keiner Eingabe nimmt oder den Wert der gemachten Eingabe
        c.execute("DELETE FROM questions WHERE question = ?, answer = ? WHERE id LIKE ?", (textbox1_answer1, textbox2_answer2, f"%{row}%"))
        conn.commit()
        c.execute("DELETE FROM categorys WHERE category = ? WHERE category_id LIKE ?",(textbox3_answer3, f"%{row}%"))
        row= c.fetchone()  
        conn.commit()
        
        ToplevelWindow_confirm_delete.destroy(self)
        print("Eintrag gelöscht")

        conn.close()
       
    def dismiss_changes(self):
        # Hier kannst du den Code einfügen, um die Änderungen zu verwerfen
        ToplevelWindow_confirm_delete.destroy(self)
        print("Vorgang abgebrochen")
         

# start der GUI
if __name__ == "__main__":
    app = App()
    app.mainloop()
