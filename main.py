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
    c.execute('''CREATE TABLE faq
                      (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, category TEXT)''')
    
    # Daten zur Tabelle hinzufügen - Felder: id, question, answer, category
    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
               ("Was ist ein Betriebssystem?", "Ein Betriebssystem ist eine Software, die den Betrieb eines Computers ermöglicht und steuert.", "Betriebssystem"))
    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
               ("Wie kann ich meinen Computer schneller machen?", "Es gibt mehrere Möglichkeiten, um die Leistung Ihres Computers zu verbessern, wie zum Beispiel das Löschen von temporären Dateien, das Deinstallieren unnötiger Programme und das Aktualisieren Ihrer Treiber.", "Computer-Optimierung"))
    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?, ?)",
               ("Wie kann ich mein Passwort ändern?", "Je nachdem, welches Betriebssystem Sie verwenden, können Sie Ihr Passwort normalerweise über die Einstellungen oder Systemsteuerung ändern.", "Passwort-Management"))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    
    print("Keine bestehende Datenbank unter dem angegebenen Dateipfad gefunden....")
    print("Eine neue Datenbank wurde erfolgreich erstellt!")

# Erstellung des TopLevelfensters
#class ToplevelWindow(customtkinter.CTkToplevel):
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.label = customtkinter.CTkLabel(self, text="Die Frage wurde erfolgreich gelöscht!")
        #self.label.pack(padx=20, pady=20)

        # Benachrichtigungsfenster fehlt bislang noch ein Button um die Löschung zu akzeptieren
        #self.main_dismiss = customtkinter.CTkButton(master=self, text="Ok", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
        #                                                    command=self.dismiss)
        #self.main_dismiss.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
    #def dismiss(self):
        #self.destroy()


# Erstellung der GUI
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Daten neu Laden", anchor="n",
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

        # Kontextlabel zur Begrüßung und zur Erklärung - Vorerst Deaktiviert - Verschiebung der Textbox nötig
        # info_context = ("Herzlich Willkommen!" + "\n" + "Im HelpDeskHQ können sowohl neue Fragen eingetragen werden als auch bestehende Fragen "+ "\n"+ "gesucht, bearbeitet oder gelöscht werden. Viel Spaß wünscht Projekt-Gruppe Cool :)")
        # self.infolabel_1 = customtkinter.CTkLabel(self,width=100, text=f"{info_context}")
        # self.infolabel_1.grid(row=0,column=1,padx=(30,0),pady=(30,0),sticky="nsew")

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
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Menü"), text="Neue Frage stellen",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_button_2 = customtkinter.CTkButton(self.tabview.tab("Menü"), text="Eine Frage bearbeiten",
                                                             command=self.edit_database_selected)

        self.string_input_button_2.grid(row=3, column=0, padx=20, pady=(10,10)) 

        self.string_input_button_3 = customtkinter.CTkButton(self.tabview.tab("Menü"), text="Eine Frage löschen",
                                                             command=self.del_database_entry)

        self.string_input_button_3.grid(row=4, column=0, padx=20, pady=(10,10))

        # Setzt die Standartwerte für die GUI - Hier muss der Inhalt für die Textbox eingeben werden
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")


        # Zieht erstmalig alle Daten aus der Datenbank und stellt diese für die Textbox bereit - tut dies nicht wenn ein Fehler vorliegt
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM faq')
        global rows 
        rows = c.fetchall()
        
        self.textbox.insert(tkinter.END, "Fragen und Antworten des HelpDeskHQ's" +"\n\n") 
        for row in rows:
            counter = 1
            id, question , answer, category = row
            try:
                self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
                self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
                self.textbox.insert(tkinter.END, "Kategorie: " +  "\n\n" + category + "\n\n\n") 
            except:
                self.textbox.insert(tkinter.END,"Fehlerhafter Datensatz in Datensatz Nr.: "+f"{id}")
                if question=="":
                    print("Frage fehlerhaft oder leer")
                elif answer=="":
                    print("Antwort fehlerhaft oder leer")
                elif category=="":
                    print("Kategore fehlerhaft oder leer")
                else:
                    print("Datenbankfehler - Datenbank sollte gelöscht werden")
                pass
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
        # Verbindung zur Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM faq')

        # Globale rows Funktion damit hiermit weitergearbeitet werden kann - auserhalb der Funktion
        global rows 
        rows = c.fetchall()

        # FetchAll-Funktion um die aktualisierten Daten direkt abzubilden - Fehlerhafte Datensätze können hierdurch Sichtbar gemacht werden        
        self.textbox.delete("0.0",tkinter.END)
        self.textbox.insert(tkinter.END, "Fragen und Antworten des HelpDeskHQ's" +"\n\n") 
        for row in rows:
            counter = 1
            id, question , answer, category = row
            try:               
                self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
                self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
                self.textbox.insert(tkinter.END, "Kategorie: " +  "\n\n" + category + "\n\n\n") 
            except:
                self.textbox.insert(tkinter.END,"Fehlerhafter Datensatz in Datensatz Nr.: "+f"{id}")
                if question=="":
                    print("Frage fehlerhaft oder leer")
                elif answer=="":
                    print("Antwort fehlerhaft oder leer")
                elif category=="":
                    print("Kategore fehlerhaft oder leer")
                else:
                    print("Datenbankfehler - Datenbank sollte gelöscht werden")
                pass
            counter += 1
        conn.close()

    # Filterabfrage die auf den "Suche-Button" reagiert und nach Inhalt in der Suchleite sucht und diese danach leert
    def search_database(self):
        #Verbindung mit der Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()
    
        # Suchabfrage ausführen für eine bestimmte Frage oder Kategorie
        search_request = self.entry.get()
        self.entry.delete(0,100)
        c.execute("SELECT id, question, answer FROM faq WHERE question LIKE ? OR category LIKE ?", ('%' + search_request+ '%','%' + search_request + '%'))
        rows = c.fetchall()

        # Darstellen des gefundenen Datensatz mit löschung der vorherigen Eingabe
        self.textbox.delete("0.0",tkinter.END)
        self.textbox.insert(tkinter.END, "Suchtreffer für dein gesuchtes Schlagwort:" +"\n"+f"{search_request}"+ "\n\n") 
        for row in rows:
            counter = 1
            id, question , answer, category = row
            self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
            self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
            self.textbox.insert(tkinter.END, "Kategorie: " +  "\n\n" + category + "\n\n\n")
            counter += 1
        print("Eingegebenes Schlagwort: ",
               search_request)
        conn.close()

    # Öffnet drei Dialogfenster - zunächst kann eine Fragedialog,Antwortdialog,Kategoriedialog
    def open_input_dialog_event(self):
        new_question = customtkinter.CTkInputDialog(text="Gebe eine Frage ein", title="Neue Frage stellen")
        new_question_Input = new_question.get_input()
        print(new_question_Input)

        new_answer = customtkinter.CTkInputDialog(text="Gebe eine Antwort ein: ", title="Antwort der zur Frage" + f'{new_question_Input}')
        new_answer_Input = new_answer.get_input()
        print(new_answer_Input)

        new_category = customtkinter.CTkInputDialog(text="Gebe eine Kategorie der Frage an", title="")
        new_category_Input = new_category.get_input()
        print(new_category_Input)

        # Funktion zum schreiben neuer Fragen und Antworten - prüft ob überhaupt eine Eingabe gemacht wird da es sonst zu einem Fehler in der Datenbank kommt
        if new_question_Input=="":
            if new_answer_Input=="":
                if new_category_Input=="":
                    pass
                else:
                    conn = sqlite3.connect('faq_database.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO faq (question, answer, category) VALUES (?, ?,?)",(new_question_Input,new_answer_Input,new_category_Input))
                    conn.commit()
                    conn.close()
        
        # FetchAll um die aktualisierten Daten direkt abzubilden
        c.execute('SELECT * FROM faq')
        rows = c.fetchall()


        self.textbox.delete("0.0",tkinter.END)
        self.textbox.insert(tkinter.END, "Fragen und Antworten des HelpDeskHQ's" +"\n\n")
        for row in rows:
            counter = 1
            id, question , answer, category = row
            self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
            self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
            self.textbox.insert(tkinter.END, "Kategorie: " +  "\n\n" + category + "\n\n\n")
            counter += 1
        conn.close()
        print("Frage wurde aktualisiert")

    # Funktion zum Auswählen einer Frage nach Nummer (Frage id) welche dann bearbeitet werden kann
    def edit_database_selected(self):
        # Verbindung zur Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # Abfrage zum Selektieren einer Frage nach der Nummer 1-...-999
        to_edit = customtkinter.CTkInputDialog(text="Welche Frage soll bearbeitet werden?" + "\n" + "(Fragenummer angeben)", title="Frageauswahl")
        to_edit_nb = to_edit.get_input()

        # Greift den Datensatz mit der passenden Nummer ab
        c.execute("SELECT * FROM faq WHERE id LIKE ?", ('%' + to_edit_nb + '%',))
        print(to_edit_nb)
        rows = c.fetchall()
        for row in rows:
            counter = 1
            id, question , answer, category = row
            counter += 1

        # Dialogfenster zur Frage die zu bearbeiten ist
        edit_question = customtkinter.CTkInputDialog(text="Bearbeite die Frage: " + "\n" + f" {question}", title="Frage zu Nr." + f" {id} " + "bearbeiten")
        edited_question = edit_question.get_input()
        if edited_question == "":
            edited_question = question
        print(edited_question)

        # Dialogfenster zur Antwort die zu bearbeiten ist
        edit_answer = customtkinter.CTkInputDialog(text="Bearbeite die Antwort: "  + "\n" + f" {answer}", title="Antwort zu Nr." + f" {id} " + "bearbeiten" )
        edited_answer = edit_answer.get_input()
        if edited_answer == "":
            edited_answer = answer
        print(edited_answer)

        # Dialogfenster zur Kategorie die zu bearbeiten ist
        edit_categoy = customtkinter.CTkInputDialog(text="Bearbeite die Kategorie: "  + "\n" + f" {category}", title="Kategorie zu Nr." + f" {id} " + "bearbeiten" )
        edited_category = edit_categoy.get_input()
        if edited_category == "":
            edited_category = category
        print(edited_category)

        # Schreibbefehl der entweder den alten Wert bei keiner Eingabe nimmt oder den Wert der gemachten Eingabe
        c.execute("UPDATE faq SET question = ?, answer = ?, category = ? WHERE id LIKE ?", (edited_question, edited_answer, edited_category, to_edit_nb))
        conn.commit()

        # FetchAll-Funktion um die aktualisierten Daten direkt abzubilden
        self.textbox.delete("0.0",tkinter.END)
        c.execute('SELECT * FROM faq')
        rows = c.fetchall()
        self.textbox.insert(tkinter.END, "Fragen und Antworten des HelpDeskHQ's" +"\n\n")
        for row in rows:
            counter = 1
            id, question , answer, category = row
            self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
            self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
            self.textbox.insert(tkinter.END, "Kategorie: " +  "\n\n" + category + "\n\n\n")
            counter += 1
        conn.close()
        print("Frage wurde aktualisiert")


    # SQL Befehl zum löschen der ausgewählten Frage
    def del_database_entry(self):
        # Verbindung zur Datenbank
        conn = sqlite3.connect('faq_database.db')
        c = conn.cursor()

        # Dialogfenster zur Auswahl der Frage
        to_edit = customtkinter.CTkInputDialog(text="Welche Frage soll gelöscht werden?" + "\n" + "(Fragenummer angeben)", title="Frageauswahl zum Löschen")
        to_edit_nb = to_edit.get_input()

        # Auswahl des Datensatz indem die Nummer übereinstimmt
        c.execute("SELECT id, question, answer FROM faq WHERE id LIKE ?", ('%' + to_edit_nb + '%',))
        print("Datensatz Nr.: " + to_edit_nb + " wird gelöscht...")

        # SQL-Befehl zum löschen des ausgewählten Datensatz
        c.execute("DELETE FROM faq WHERE id LIKE ?",(to_edit_nb))
        conn.commit        
        print("Datensatz erfolgreich gelöscht!")

        # FetchAll-Funktion um die aktualisierten Daten direkt abzubilden
        self.textbox.delete("0.0",tkinter.END)
        c.execute('SELECT id, question, answer FROM faq')
        rows = c.fetchall()
        self.textbox.insert(tkinter.END, "Fragen und Antworten des HelpDeskHQ's" +"\n\n")
        for row in rows:
            counter = 1
            id, question , answer, category = row
            self.textbox.insert(tkinter.END, f"{id}" + ". " "Frage: "+ "\n\n" + question + "\n\n")
            self.textbox.insert(tkinter.END, "Antwort: " +  "\n\n" + answer + "\n\n")
            self.textbox.insert(tkinter.END, "Kategorie: " +  "\n\n" + category + "\n\n\n")
            counter += 1
        conn.close()
        print("Fragen wurde aktualisiert")

        # Benachrichtigung für den USER - Vorerst deaktiviert da Button noch fehlt
        #self.toplevel_window = None
        #if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        #    self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        #else:
        #    self.toplevel_window.focus()  # if window exists focus it


# start der GUI
if __name__ == "__main__":
    app = App()
    app.mainloop()
