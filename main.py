import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from PIL import ImageTk, Image
import tkmacosx as tkm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


class SteamEmpiria(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Utworzenie zmiennen container która tworzy ramkę TOP
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Na podstawie każdej klasy zostaje utworzona ramka która jest zpaisywania do słownika.
        # Ramka za pomocą grida jest ustawiona na ekranie
        self.frames = {}
        for FRAME in (GlowneMenu,
                      PorownajTytuly, PorownajDanePlatforms, PorownajDaneGenres, PorownajDanePublisher,
                      OgolneStatystykiPageOne, OgolneStatystykiPageTwo,
                      AdminPanelLogowanie, AdminPanelWybor,
                      AdminPanelDodaj, AdminPanelUsun, AdminPanelModyfikuj):
            page_name = FRAME.__name__
            frame = FRAME(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, ipady=760, ipadx=760, sticky="nsew")

        self.show_frame("GlowneMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def exit_app(self):
        self.destroy()


class GlowneMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = '#255183'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Główne Menu', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=760, y=50, anchor='center')

        self.AdminPNG_B = ImageTk.PhotoImage(Image.open('Ikony/admin.png').resize((60, 60), Image.LANCZOS))
        self.AdminPanel_B = tkm.Button(self, image=self.AdminPNG_B, borderwidth=5, bg=self.maincolor,
                                       command=lambda: app.show_frame("AdminPanelLogowanie"))
        self.AdminPanel_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.NazwaProgramu_L = tk.Label(self, text='Steam Stat\nwersja 0.01', font=('Arial', 22, "bold"), fg='White',
                                        bg=self.maincolor)
        self.NazwaProgramu_L.place(x=150, y=50, anchor='center')

        self.CompareTitlePNG_B = ImageTk.PhotoImage(Image.open('Ikony/compare.png').resize((180, 180), Image.LANCZOS))
        self.CompareTitle_B = tkm.Button(self, image=self.CompareTitlePNG_B, text='Porównaj tytuły', compound='top',
                                         borderwidth=5,
                                         font=('Arial', 20, 'bold'), fg=self.maincolor,
                                         command=lambda: app.show_frame("PorownajTytuly"))
        self.CompareTitle_B.place(x=450, y=350, anchor='center')

        self.StatisticPNG_B = ImageTk.PhotoImage(Image.open('Ikony/stats.png').resize((180, 180), Image.LANCZOS))
        self.Statistic_B = tkm.Button(self, image=self.StatisticPNG_B, text='Ogólne statystyki', compound='top',
                                      borderwidth=5,
                                      font=('Arial', 20, 'bold'), fg=self.maincolor,
                                      command=lambda: app.show_frame("OgolneStatystykiPageOne"))
        self.Statistic_B.place(x=1050, y=350, anchor='center')

        self.CompareDataPNG_B = ImageTk.PhotoImage(
            Image.open('Ikony/compare_data.png').resize((180, 180), Image.LANCZOS))
        self.CompareData_B = tkm.Button(self, image=self.CompareDataPNG_B, text='Porównaj dane', compound='top',
                                        borderwidth=5,
                                        font=('Arial', 20, 'bold'), fg=self.maincolor,
                                        command=lambda: app.show_frame("PorownajDanePlatforms"))
        self.CompareData_B.place(x=760, y=650, anchor='center')


class PorownajTytuly(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = "#139E36"

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Porównaj Tytuły', font=('Arial', 40, "bold"),
                                     fg='White', bg=self.maincolor)
        self.NazwaFrame_L.place(x=760, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjscieTytuly()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Tytul1_L = tk.Label(self, text="Nazwa tytułu 1", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Tytul1_L.place(x=380, y=160, anchor='center')

        self.Tytul1_E = tk.Entry(self, width=22, fg=self.maincolor, highlightbackground=self.maincolor)
        self.Tytul1_E.place(x=580, y=160, anchor='center')

        self.Tytul2_L = tk.Label(self, text="Nazwa tytułu 2", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Tytul2_L.place(x=850, y=160, anchor='center')

        self.Tytul2_E = tk.Entry(self, width=22, highlightbackground=self.maincolor, fg=self.maincolor)
        self.Tytul2_E.place(x=1050, y=160, anchor='center')

        self.WykonajPorownanie_B = tkm.Button(self, text='Wykonaj', width=160, height=40, font=('Arial', 24, 'bold'),
                                              foreground='white', background=self.maincolor,
                                              command=lambda: [self.PorownanieTytulWykres()])
        self.WykonajPorownanie_B.place(x=1400, y=160, anchor='center')

        self.Tytul1_Data_L = Label(self)
        self.Tytul2_Data_L = Label(self)
        self.Legenda_L = Label(self)

        self.figure = None
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)

        self.figure2 = None
        self.canvas2 = FigureCanvasTkAgg(self.figure2, self)

    def PorownanieTytulWykres(self):
        con = sqlite3.connect("/Users/radekk/PracaMGR.db")
        cur = con.cursor()

        self.Tytul1_Data_L.destroy()
        self.Tytul2_Data_L.destroy()
        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()

        if self.Tytul1_E.get() == '' or self.Tytul2_E.get() == '':
            messagebox.showerror('Error', "Należy podać nazwy tytułów")
        else:
            self.SQLCOM = ("""select S.name, S.release_date, S.publisher, S.platforms, S.genres, S.owners, S.price
                          from Steam S
                          where S.name like ?""")

            data1 = cur.execute(self.SQLCOM, ('%' + self.Tytul1_E.get(),))
            tytul1_data = ''
            for t1 in data1.fetchall()[0]:
                tytul1_data += str(t1) + '\n'

            data2 = cur.execute(self.SQLCOM, ('%' + self.Tytul2_E.get(),))
            tytul2_data = ''
            for t2 in data2.fetchall()[0]:
                tytul2_data += str(t2) + '\n'

            self.Legenda_L = tk.Label(self, text="Nazwa: \nData Wydania:  \nWydawca:"
                                                 "  \nPlatforma:  \nRodzaj:  \nIlość graczy:  \nCena:",
                                      font=('Arial', 20, 'bold'), fg=self.maincolor)
            self.Legenda_L.place(x=230, y=290, anchor='center')

            self.Tytul1_Data_L = Label(self, text=tytul1_data, font=('Arial', 20, 'bold'), fg=self.maincolor)
            self.Tytul1_Data_L.place(x=530, y=300, anchor='center')
            self.Tytul2_Data_L = Label(self, text=tytul2_data, font=('Arial', 20, 'bold'), fg=self.maincolor)
            self.Tytul2_Data_L.place(x=1000, y=300, anchor='center')

            self.SQLCOM_PLOT = """select S.name, S.positive_ratings, S.negative_ratings
            from Steam S 
            where S.name like ? or S.name like ?"""

            # Utworzenie ramki dnaych z zapytania
            self.DataTytul = pd.read_sql_query(self.SQLCOM_PLOT, con, params=[tytul1_data.split('\n')[0],
                                                                              tytul2_data.split('\n')[0]])

            # Utworzenie Figury dla wykresu
            self.figure = Figure(figsize=(6, 3), facecolor=self.maincolor)

            # Utworzenie wykresu
            self.fig1 = self.figure.add_subplot(111)
            self.bar1 = self.fig1.bar(self.DataTytul['name'], self.DataTytul['positive_ratings'],
                                      width=0.5, color='white', edgecolor='black')
            self.fig1.bar_label(self.bar1, label_type='center', color='black')
            self.fig1.set_title('Ilość pozytywnych opini dla:', fontsize=10, color='White')
            self.fig1.set_facecolor(self.maincolor)
            self.fig1.tick_params(axis='x', colors='white')
            self.fig1.tick_params(axis='y', colors='white')

            # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
            self.canvas1 = FigureCanvasTkAgg(self.figure, self)
            self.canvas1.get_tk_widget().place(x=400, y=600, anchor='center')
            self.canvas1.draw()

            # Utworzenie Figury dla wykresu
            self.figure2 = Figure(figsize=(6, 3), facecolor=self.maincolor)

            # Utworzenie wykresu
            self.fig2 = self.figure2.add_subplot(111)
            self.bar2 = self.fig2.bar(self.DataTytul['name'], self.DataTytul['negative_ratings'], width=0.5,
                                      color='white', edgecolor='black')
            self.fig2.bar_label(self.bar2, label_type='center', color='black')
            self.fig2.set_title('Ilość negatywnych opini dla:', fontsize=10, color='White')
            self.fig2.set_facecolor(self.maincolor)
            self.fig2.tick_params(axis='x', colors='white')
            self.fig2.tick_params(axis='y', colors='white')

            # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
            self.canvas2 = FigureCanvasTkAgg(self.figure2, self)
            self.canvas2.get_tk_widget().place(x=1100, y=600, anchor='center')
            self.canvas2.draw()

        con.close()

    def WyjscieTytuly(self):
        self.Tytul1_E.delete(0, END)
        self.Tytul2_E.delete(0, END)

        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()

        self.Tytul1_Data_L.destroy()
        self.Tytul2_Data_L.destroy()

        self.Legenda_L.destroy()


class PorownajDanePlatforms(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.maincolor = '#2C59B9'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Porównaj Dane - Platforma ', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=760, y=50, anchor='center')

        self.Page1_B = ImageTk.PhotoImage(Image.open('Ikony/dot_red.png').resize((40, 40), Image.LANCZOS))
        self.Page1_B = tkm.Button(self, image=self.Page1_B, bg=self.maincolor, borderwidt=5)
        self.Page1_B.place(x=40, y=50, anchor='center')

        self.Page2_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page2_B = tkm.Button(self, image=self.Page2_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("PorownajDaneGenres"), self.WyjsciePlatforms()])
        self.Page2_B.place(x=120, y=50, anchor='center')

        self.Page3_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page3_B = tkm.Button(self, image=self.Page3_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("PorownajDanePublisher"), self.WyjsciePlatforms()])
        self.Page3_B.place(x=200, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjsciePlatforms()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Platforma1_L = tk.Label(self, text="Platforma 1", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Platforma1_L.place(x=330, y=140, anchor='center')

        self.Platforma1_CBOX = ttk.Combobox(self, values=['windows', 'linux', 'mac'])
        self.Platforma1_CBOX.current(0)
        self.Platforma1_CBOX.config(width=20)
        self.Platforma1_CBOX.place(x=510, y=140, anchor='center')

        self.Platforma2_L = tk.Label(self, text="Platforma 2", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Platforma2_L.place(x=900, y=140, anchor='center')

        self.Platforma2_CBOX = ttk.Combobox(self, values=['windows', 'linux', 'mac'])
        self.Platforma2_CBOX.current(0)
        self.Platforma2_CBOX.config(width=20)
        self.Platforma2_CBOX.place(x=1080, y=140, anchor='center')

        self.WykonajPorownanie_B = tkm.Button(self, text='Wykonaj', width=160, height=35, font=('Arial', 24, 'bold'),
                                              foreground='white', background=self.maincolor,
                                              command=lambda: [self.IloscGierPlatforms(),
                                                               self.SumSredniCzasPlatforms(),
                                                               self.DarmoweGryPlatforms(),
                                                               self.PlatneGryPlatforms()])
        self.WykonajPorownanie_B.place(x=1350, y=140, anchor='center')

        self.figure = None
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas4 = FigureCanvasTkAgg(self.figure, self)

    def IloscGierPlatforms(self):
        self.canvas1.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(S.name) as liczba
        from Steam S where 
        S.platforms like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataPlatform1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma1_CBOX.get() + '%'])
        self.DataPlatform2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(4, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.bar(self.Platforma1_CBOX.get(), self.DataPlatform1['liczba'], width=0.3, color='white',
                                  edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.bar(self.Platforma2_CBOX.get(), self.DataPlatform2['liczba'], width=0.3, color='white',
                                  edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Ilość gier na platformę:', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='x', colors='white')
        self.fig1.tick_params(axis='y', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas1.get_tk_widget().place(x=400, y=370, anchor='center')
        self.canvas1.draw()

        con.close()

    def SumSredniCzasPlatforms(self):
        self.canvas2.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select round(SUM(S.average_playtime)/1000000.0,2) as czas
        from Steam S where 
        S.platforms like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataPlatform1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma1_CBOX.get() + '%'])
        self.DataPlatform2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(5, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.bar(self.Platforma1_CBOX.get(), self.DataPlatform1['czas'], width=0.2, color='white',
                                  edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.bar(self.Platforma2_CBOX.get(), self.DataPlatform2['czas'], width=0.2, color='white',
                                  edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Suma AVG czasu na platformie: (x 1 000 000)', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='x', colors='white')
        self.fig1.tick_params(axis='y', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2.get_tk_widget().place(x=1100, y=370, anchor='center')
        self.canvas2.draw()

        con.close()

    def DarmoweGryPlatforms(self):
        self.canvas3.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(CASE WHEN S.price = 0 THEN 1 END) as GryFree
                          from Steam S
                          WHERE S.platforms like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataPlatform1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma1_CBOX.get() + '%'])
        self.DataPlatform2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(6, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.barh(self.Platforma1_CBOX.get(), int(self.DataPlatform1['GryFree']), height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.barh(self.Platforma2_CBOX.get(), int(self.DataPlatform2['GryFree']), height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Ilość darmowych gier na platformę:', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors='white')
        self.fig1.tick_params(axis='x', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3.get_tk_widget().place(x=400, y=720, anchor='center')
        self.canvas3.draw()

        con.close()

    def PlatneGryPlatforms(self):
        self.canvas4.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(CASE WHEN S.price > 0 THEN 1 END) as GryPlatne
                          from Steam S
                          WHERE S.platforms like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataPlatform1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma1_CBOX.get() + '%'])
        self.DataPlatform2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Platforma2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(6, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.barh(self.Platforma1_CBOX.get(), int(self.DataPlatform1['GryPlatne']), height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.barh(self.Platforma2_CBOX.get(), int(self.DataPlatform2['GryPlatne']), height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Ilość platnych gier na platformę:', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors='white')
        self.fig1.tick_params(axis='x', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas4 = FigureCanvasTkAgg(self.figure, self)
        self.canvas4.get_tk_widget().place(x=1100, y=720, anchor='center')
        self.canvas4.draw()

        con.close()

    def WyjsciePlatforms(self):
        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()
        self.canvas3.get_tk_widget().destroy()
        self.canvas4.get_tk_widget().destroy()


class PorownajDaneGenres(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.maincolor = '#2C59B9'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Porównaj Dane - Gatunek', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=745, y=50, anchor='center')

        self.Page1_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page1_B = tkm.Button(self, image=self.Page1_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("PorownajDanePlatforms"), self.WyjscieGenres()])
        self.Page1_B.place(x=40, y=50, anchor='center')

        self.Page2_B = ImageTk.PhotoImage(Image.open('Ikony/dot_red.png').resize((40, 40), Image.LANCZOS))
        self.Page2_B = tkm.Button(self, image=self.Page2_B, bg=self.maincolor, borderwidt=5)
        self.Page2_B.place(x=120, y=50, anchor='center')

        self.Page3_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page3_B = tkm.Button(self, image=self.Page3_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("PorownajDanePublisher"), self.WyjscieGenres()])
        self.Page3_B.place(x=200, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjscieGenres()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Gatunek1_L = tk.Label(self, text="Gatunek 1", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Gatunek1_L.place(x=330, y=140, anchor='center')

        self.GatunekCon = self.con.cursor()
        self.GatunekCon.execute("select distinct Genres from SteamUQ limit 29")
        self.GatunekConResult = self.GatunekCon.fetchall()
        self.GatunekList = [i[0] for i in self.GatunekConResult]

        self.Gatunek1_CBOX = ttk.Combobox(self, values=self.GatunekList)
        self.Gatunek1_CBOX.current(0)
        self.Gatunek1_CBOX.config(width=20)
        self.Gatunek1_CBOX.place(x=510, y=140, anchor='center')

        self.Gatunek2_L = tk.Label(self, text="Gatunek 2", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Gatunek2_L.place(x=900, y=140, anchor='center')

        self.Gatunek2_CBOX = ttk.Combobox(self, values=self.GatunekList)
        self.Gatunek2_CBOX.current(0)
        self.Gatunek2_CBOX.config(width=20)
        self.Gatunek2_CBOX.place(x=1080, y=140, anchor='center')

        self.WykonajPorownanie_B = tkm.Button(self, text='Wykonaj', width=160, height=35, font=('Arial', 24, 'bold'),
                                              foreground='white', background=self.maincolor,
                                              command=lambda: [self.IloscGierGenres(),
                                                               self.PozytywneOpinieGenres(),
                                                               self.NegatywneOpinieGenres(),
                                                               self.SumSredniCzasGenres()])
        self.WykonajPorownanie_B.place(x=1350, y=140, anchor='center')

        self.figure = None
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas4 = FigureCanvasTkAgg(self.figure, self)

    def IloscGierGenres(self):
        self.canvas1.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(S.name) as liczba
        from Steam S where 
        S.genres like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataGatunek1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek1_CBOX.get() + '%'])
        self.DataGatunek2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(7, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.barh(self.Gatunek1_CBOX.get(), self.DataGatunek1['liczba'], height=0.3, color='white',
                                   edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.barh(self.Gatunek2_CBOX.get(), self.DataGatunek2['liczba'], height=0.3, color='white',
                                   edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Ilość gier dla gatunku:', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='x', colors=self.maincolor)
        self.fig1.tick_params(axis='y', colors='white')

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas1.get_tk_widget().place(x=370, y=330, anchor='center')
        self.canvas1.draw()

        con.close()

    def SumSredniCzasGenres(self):
        self.canvas2.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select round(SUM(S.average_playtime)/1000000.0,3) as czas
        from Steam S where 
        S.genres like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataGatunek1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek1_CBOX.get() + '%'])
        self.DataGatunek2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(7, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.barh(self.Gatunek1_CBOX.get(), self.DataGatunek1['czas'], height=0.2, color='white',
                                   edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.barh(self.Gatunek2_CBOX.get(), self.DataGatunek2['czas'], height=0.2, color='white',
                                   edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Suma AVG czasu dla gatunku: (x 1 000 000)', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='x', colors=self.maincolor)
        self.fig1.tick_params(axis='y', colors='white')

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2.get_tk_widget().place(x=1130, y=330, anchor='center')
        self.canvas2.draw()

        con.close()

    def PozytywneOpinieGenres(self):
        self.canvas3.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select round(SUM(S.positive_ratings)/100000.0,2) as suma from Steam S
                          WHERE S.genres like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataGatunek1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek1_CBOX.get() + '%'])
        self.DataGatunek2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(6, 4), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.bar(self.Gatunek1_CBOX.get(), self.DataGatunek1['suma'], width=0.2,
                                  color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.bar(self.Gatunek2_CBOX.get(), self.DataGatunek2['suma'], width=0.2,
                                  color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Suma pozytywnych opini na platformie: (x 100 000)', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors=self.maincolor)
        self.fig1.tick_params(axis='x', colors='white')

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3.get_tk_widget().place(x=360, y=700, anchor='center')
        self.canvas3.draw()

        con.close()

    def NegatywneOpinieGenres(self):
        self.canvas4.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select round(SUM(S.negative_ratings)/100000.0,2) as suma from Steam S
                          WHERE S.genres like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataGatunek1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek1_CBOX.get() + '%'])
        self.DataGatunek2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Gatunek2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(6, 4), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.bar(self.Gatunek1_CBOX.get(), self.DataGatunek1['suma'], width=0.2,
                                  color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.bar(self.Gatunek2_CBOX.get(), (self.DataGatunek2['suma']), width=0.2,
                                  color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Suma negatywnych opini na platformie: (x 100 000)', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors=self.maincolor)
        self.fig1.tick_params(axis='x', colors='white')

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas4 = FigureCanvasTkAgg(self.figure, self)
        self.canvas4.get_tk_widget().place(x=1120, y=700, anchor='center')
        self.canvas4.draw()

        con.close()

    def WyjscieGenres(self):
        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()
        self.canvas3.get_tk_widget().destroy()
        self.canvas4.get_tk_widget().destroy()


class PorownajDanePublisher(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.maincolor = '#2C59B9'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Porównaj Dane - Wydawca', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=753, y=50, anchor='center')

        self.Page1_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page1_B = tkm.Button(self, image=self.Page1_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("PorownajDanePlatforms"), self.WyjsciePublisher()])
        self.Page1_B.place(x=40, y=50, anchor='center')

        self.Page2_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page2_B = tkm.Button(self, image=self.Page2_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("PorownajDaneGenres"), self.WyjsciePublisher()])
        self.Page2_B.place(x=120, y=50, anchor='center')

        self.Page3_B = ImageTk.PhotoImage(Image.open('Ikony/dot_red.png').resize((40, 40), Image.LANCZOS))
        self.Page3_B = tkm.Button(self, image=self.Page3_B, bg=self.maincolor, borderwidt=5)
        self.Page3_B.place(x=200, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjsciePublisher()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.WydawcaCon = self.con.cursor()
        self.WydawcaCon.execute("select distinct Publisher from SteamUQ")
        self.WydawcaConResult = self.WydawcaCon.fetchall()
        self.WydawcaList = [i[0] for i in self.WydawcaConResult]

        self.Wydawca1_L = tk.Label(self, text="Wydawca 1", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Wydawca1_L.place(x=330, y=140, anchor='center')

        self.Wydawca1_CBOX = ttk.Combobox(self, values=self.WydawcaList)
        self.Wydawca1_CBOX.current(0)
        self.Wydawca1_CBOX.config(width=20)
        self.Wydawca1_CBOX.place(x=510, y=140, anchor='center')

        self.Wydawca2_L = tk.Label(self, text="Wydawca 2", font=('Arial', 24, "bold"), fg=self.maincolor)
        self.Wydawca2_L.place(x=900, y=140, anchor='center')

        self.Wydawca2_CBOX = ttk.Combobox(self, values=self.WydawcaList)
        self.Wydawca2_CBOX.current(0)
        self.Wydawca2_CBOX.config(width=20)
        self.Wydawca2_CBOX.place(x=1080, y=140, anchor='center')

        self.WykonajPorownanie_B = tkm.Button(self, text='Wykonaj', width=160, height=35, font=('Arial', 24, 'bold'),
                                              foreground='white', background=self.maincolor,
                                              command=lambda: [self.IloscGierPublisher(),
                                                               self.DarmoweGryPublisher(),
                                                               self.PozytywneOpinieGenres(),
                                                               self.NegatywneOpinieGenres()])
        self.WykonajPorownanie_B.place(x=1350, y=140, anchor='center')

        self.figure = None
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas4 = FigureCanvasTkAgg(self.figure, self)

    def IloscGierPublisher(self):
        self.canvas1.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(S.name) as liczba
        from Steam S where 
        S.publisher like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataWydawca1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca1_CBOX.get() + '%'])
        self.DataWydawca2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(4, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.bar(self.Wydawca1_CBOX.get(), self.DataWydawca1['liczba'], width=0.3, color='white',
                                  edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.bar(self.Wydawca2_CBOX.get(), self.DataWydawca2['liczba'], width=0.3, color='white',
                                  edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Ilość gier wydanych przez:', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='x', colors='white')
        self.fig1.tick_params(axis='y', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas1.get_tk_widget().place(x=400, y=330, anchor='center')
        self.canvas1.draw()

        con.close()

    def DarmoweGryPublisher(self):
        self.canvas2.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(CASE WHEN S.price = 0 THEN 1 END) as GryFree
                          from Steam S
                          WHERE S.publisher like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataWydawca1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca1_CBOX.get() + '%'])
        self.DataWydawca2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(4, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.bar(self.Wydawca1_CBOX.get(), int(self.DataWydawca1['GryFree']), width=0.2,
                                  color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.bar(self.Wydawca2_CBOX.get(), int(self.DataWydawca2['GryFree']), width=0.2,
                                  color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Ilość darmowych gier wydawcy:', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors=self.maincolor)
        self.fig1.tick_params(axis='x', colors='white')

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2.get_tk_widget().place(x=1130, y=330, anchor='center')
        self.canvas2.draw()

        con.close()

    def PozytywneOpinieGenres(self):
        self.canvas3.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select round(SUM(S.positive_ratings)/100000.0,2) as suma from Steam S
                          WHERE S.publisher like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataWydawca1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca1_CBOX.get() + '%'])
        self.DataWydawca2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(7, 4), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.barh(self.Wydawca1_CBOX.get(), self.DataWydawca1['suma'], height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.barh(self.Wydawca2_CBOX.get(), self.DataWydawca2['suma'], height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Suma pozytywnych opini wydawcy: (x 100 000)', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors='white')
        self.fig1.tick_params(axis='x', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3.get_tk_widget().place(x=360, y=700, anchor='center')
        self.canvas3.draw()

        con.close()

    def NegatywneOpinieGenres(self):
        self.canvas4.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select round(SUM(S.negative_ratings)/100000.0,2) as suma from Steam S
                          WHERE S.publisher like ?"""

        # Utworzenie ramki dnaych z zapytania
        self.DataWydawca1 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca1_CBOX.get() + '%'])
        self.DataWydawca2 = pd.read_sql_query(self.SQL_COM, con, params=['%' + self.Wydawca2_CBOX.get() + '%'])

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(7, 4), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)

        self.bar1 = self.fig1.barh(self.Wydawca1_CBOX.get(), self.DataWydawca1['suma'], height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar1, label_type='center', color='black')

        self.bar2 = self.fig1.barh(self.Wydawca2_CBOX.get(), (self.DataWydawca2['suma']), height=0.2,
                                   color='white', edgecolor='black')
        self.fig1.bar_label(self.bar2, label_type='center', color='black')

        self.fig1.set_title('Suma negatywnych gier wydawcy: (x 100 000)', fontsize=10, color='White')
        self.fig1.set_facecolor(self.maincolor)
        self.fig1.tick_params(axis='y', colors='white')
        self.fig1.tick_params(axis='x', colors=self.maincolor)

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas4 = FigureCanvasTkAgg(self.figure, self)
        self.canvas4.get_tk_widget().place(x=1120, y=700, anchor='center')
        self.canvas4.draw()

        con.close()

    def WyjsciePublisher(self):
        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()
        self.canvas3.get_tk_widget().destroy()
        self.canvas4.get_tk_widget().destroy()


class OgolneStatystykiPageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.maincolor = '#F3C149'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Ogólne statystyki - strona 1', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=760, y=50, anchor='center')

        self.Page1_B = ImageTk.PhotoImage(Image.open('Ikony/dot_red.png').resize((40, 40), Image.LANCZOS))
        self.Page1_B = tkm.Button(self, image=self.Page1_B, bg=self.maincolor, borderwidt=5)
        self.Page1_B.place(x=40, y=50, anchor='center')

        self.Page2_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page2_B = tkm.Button(self, image=self.Page2_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("OgolneStatystykiPageTwo"), self.WyjscieStatystyki()])
        self.Page2_B.place(x=120, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjscieStatystyki()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Pokaz_B = tkm.Button(self, text='Pokaż statystyki', width=220, height=35, font=('Arial', 24, 'bold'),
                                  foreground='white', background=self.maincolor,
                                  command=lambda: [self.PlotReleaseGames(),
                                                   self.PlotAgeGames()])
        self.Pokaz_B.place(x=760, y=140, anchor='center')

        self.figure = None
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)

    def PlotAgeGames(self):
        self.canvas1.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(S.name) as ilosc, S.required_age as wiek
        from Steam S
        where S.required_age>0
        group by S.required_age"""

        # Utworzenie ramki dnaych z zapytania
        self.DataSQL = pd.read_sql_query(self.SQL_COM, con)

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(6, 5), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.legend = ['wiek 3', 'wiek 7', 'wiek 12', 'wiek 16', 'wiek 18']
        self.fig1 = self.figure.add_subplot(111)
        self.pie1 = self.fig1.pie(self.DataSQL['ilosc'], radius=0.9,
                                  pctdistance=1.2, labeldistance=0.6,
                                  explode=(0.6, 0.6, 0, 0, 0),
                                  textprops=dict(color='black'), autopct='%1.1f%%')

        self.fig1.set_title('Procent gier dla wieku:', fontsize=10, color='black')
        self.fig1.legend(self.legend, loc='center', bbox_to_anchor=(1.0, 0.1))

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas1.get_tk_widget().place(x=370, y=500, anchor='center')
        self.canvas1.draw()

        con.close()

    def PlotReleaseGames(self):
        self.canvas2.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(S.name) as ilosc, strftime ('%Y',S.release_date) as rok
        from Steam S
        where strftime ('%Y',S.release_date) >= '2012'
        group by strftime ('%Y',S.release_date)"""

        # Utworzenie ramki dnaych z zapytania
        self.DataSQL = pd.read_sql_query(self.SQL_COM, con)

        # Utworzenie Figury dla wykresu
        self.legend = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
        self.figure = Figure(figsize=(6, 5), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)
        self.pie1 = self.fig1.pie(self.DataSQL['ilosc'], radius=1.0,
                                  pctdistance=1.1, labeldistance=.6,
                                  explode=(0.6, 0.6, 0, 0, 0, 0, 0, 0),
                                  textprops=dict(color='black'),
                                  autopct=lambda x: '{:.0f}'.format(x * self.DataSQL['ilosc'].sum() / 100))

        self.fig1.set_title('Ilość wydanych gier od 2012:', fontsize=10, color='black')
        self.fig1.legend(self.legend, loc='center', bbox_to_anchor=(0.0001, 0.1))

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2.get_tk_widget().place(x=1100, y=500, anchor='center')
        self.canvas2.draw()

        con.close()

    def WyjscieStatystyki(self):
        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()


class OgolneStatystykiPageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.maincolor = '#F3C149'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Ogólne statystyki - strona 2', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=760, y=50, anchor='center')

        self.Page1_B = ImageTk.PhotoImage(Image.open('Ikony/dot_black.png').resize((40, 40), Image.LANCZOS))
        self.Page1_B = tkm.Button(self, image=self.Page1_B, bg=self.maincolor, borderwidt=5,
                                  command=lambda: [app.show_frame("OgolneStatystykiPageOne"), self.WyjscieStatystyki()])
        self.Page1_B.place(x=40, y=50, anchor='center')

        self.Page2_B = ImageTk.PhotoImage(Image.open('Ikony/dot_red.png').resize((40, 40), Image.LANCZOS))
        self.Page2_B = tkm.Button(self, image=self.Page2_B, bg=self.maincolor, borderwidt=5)
        self.Page2_B.place(x=120, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjscieStatystyki()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Pokaz_B = tkm.Button(self, text='Pokaż statystyki', width=220, height=35, font=('Arial', 24, 'bold'),
                                  foreground='white', background=self.maincolor,
                                  command=lambda: [self.PlotEngGames(),
                                                   self.PlotPrice(),
                                                   self.PlotAvgPlayGames()])
        self.Pokaz_B.place(x=760, y=140, anchor='center')

        self.figure = None
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)

    def PlotPrice(self):
        self.canvas1.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(name) as ilosc,
            case
                when round(price * 4.5,2)>= 0 and round(price * 4.5,2) < 25 then '< 25 zł'
                when round(price * 4.5,2)>= 25 and round(price * 4.5,2) < 50 then ' 25-50 zł'
                when round(price * 4.5,2)>= 50 and round(price * 4.5,2) < 100 then '50-100 [zł]'
                when round(price * 4.5,2)>= 100 and round(price * 4.5,2) < 200 then '100-200 [zł]'
                when round(price * 4.5,2)>= 200 then '> 200 zł'
            end cena
        from Steam
        group by cena
        order by ilosc"""

        # Utworzenie ramki dnaych z zapytania
        self.DataSQL = pd.read_sql_query(self.SQL_COM, con)

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(5, 5), facecolor=self.maincolor)
        self.legend = ['< 25 zł', ' 25-50 zł', '50-100 [zł]', '100-200 [zł]', '> 200 zł']

        # Utworzenie wykresu
        self.fig1 = self.figure.add_subplot(111)
        self.bar1 = self.fig1.pie(self.DataSQL['ilosc'],
                                  pctdistance=1.1,
                                  explode=(0.3, 0.3, 0, 0, 0),
                                  textprops=dict(color='black'),
                                  autopct=lambda x: '{:.0f}'.format(x * self.DataSQL['ilosc'].sum() / 100))

        self.fig1.set_title('Ilosć gier dla przedziału cenowego:', fontsize=10, color='black')
        self.fig1.legend(self.legend, loc='center', bbox_to_anchor=(0.95, 0.05))

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas1 = FigureCanvasTkAgg(self.figure, self)
        self.canvas1.get_tk_widget().place(x=265, y=450, anchor='center')
        self.canvas1.draw()

        con.close()

    def PlotEngGames(self):
        self.canvas2.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(S.name) as ilosc, S.english as eng
        from Steam S
        group by S.english"""

        # Utworzenie ramki dnaych z zapytania
        self.DataSQL = pd.read_sql_query(self.SQL_COM, con)

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(4, 3), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.legend = ['Nie', 'Tak']
        self.fig1 = self.figure.add_subplot(111)
        self.bar1 = self.fig1.pie(self.DataSQL['ilosc'],
                                  explode=(0, 0.6),
                                  autopct='%1.1f%%', pctdistance=1.3,
                                  colors=['black', 'Green'], textprops=dict(color='black'))

        self.fig1.set_title('Procent gier posiadająych język angielski:', fontsize=10, color='black')
        self.fig1.legend(self.legend, loc='center', bbox_to_anchor=(1.0, 0.1))

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas2 = FigureCanvasTkAgg(self.figure, self)
        self.canvas2.get_tk_widget().place(x=760, y=690, anchor='center')
        self.canvas2.draw()

        con.close()

    def PlotAvgPlayGames(self):
        self.canvas3.get_tk_widget().destroy()

        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        self.SQL_COM = """select count(name) as ilosc,
            case
                when average_playtime >= 0 and average_playtime < 50 then 'do 50 min'
                when average_playtime >= 50 and average_playtime < 100 then 'od 50 do 100 [min]'
                when average_playtime >= 100 and average_playtime < 200 then 'od 100 do 200 [min]'
                when average_playtime >= 200 then 'powyżej 200 min'
            end przedzial
        from Steam
        group by przedzial
        order by ilosc"""

        # Utworzenie ramki dnaych z zapytania
        self.DataSQL = pd.read_sql_query(self.SQL_COM, con)

        # Utworzenie Figury dla wykresu
        self.figure = Figure(figsize=(5, 5), facecolor=self.maincolor)

        # Utworzenie wykresu
        self.legend = ['< 50 min', '50 - 100 [min]', '100 - 200 [min]', '> 200 min']
        self.fig1 = self.figure.add_subplot(111)
        self.bar1 = self.fig1.pie(self.DataSQL['ilosc'],
                                  pctdistance=1.3, textprops=dict(color='black'),
                                  autopct=lambda x: '{:.0f}'.format(x * self.DataSQL['ilosc'].sum() / 100))

        self.fig1.set_title('Ilość tytułów dla spędzonego średniego czasu:', fontsize=10, color='black')
        self.fig1.legend(self.legend, loc='center', bbox_to_anchor=(0.9, 0.02))

        # Wstawienie figury do 'płótna', wyświetlenie figury na ekranie
        self.canvas3 = FigureCanvasTkAgg(self.figure, self)
        self.canvas3.get_tk_widget().place(x=1250, y=450, anchor='center')
        self.canvas3.draw()

        con.close()

    def WyjscieStatystyki(self):
        self.canvas1.get_tk_widget().destroy()
        self.canvas2.get_tk_widget().destroy()
        self.canvas3.get_tk_widget().destroy()


class AdminPanelLogowanie(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = '#293B7E'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Panel Administratora', font=('Arial', 40, "bold"), fg='White',
                                     bg=self.maincolor)
        self.NazwaFrame_L.place(x=790, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: app.show_frame("GlowneMenu"))
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Login_L = Label(self, text="Podaj login", font=('Arial', 28, "bold"), fg=self.maincolor)
        self.Login_L.place(x=620, y=260, anchor='center')

        self.Login_E = Entry(self, width=27, fg=self.maincolor, highlightbackground=self.maincolor)
        self.Login_E.place(x=830, y=260, anchor='center')

        self.Haslo_L = Label(self, text="Podaj hasło", font=('Arial', 28, "bold"), fg=self.maincolor)
        self.Haslo_L.place(x=620, y=380, anchor='center')

        self.Haslo_E = Entry(self, width=27, show='*', highlightbackground=self.maincolor, fg=self.maincolor)
        self.Haslo_E.place(x=830, y=380, anchor='center')

        self.Zaloguj_B = tkm.Button(self, text='Zaloguj', width=200, height=60, font=('Arial', 35, 'bold'),
                                    foreground='white', background=self.maincolor,
                                    command=self.Logowanie)
        self.Zaloguj_B.place(x=780, y=500, anchor='center')

    def Logowanie(self):
        if self.Login_E.get() == 'admin' and self.Haslo_E.get() == 'admin':
            app.show_frame("AdminPanelWybor")
            self.Login_E.delete(0, END)
            self.Haslo_E.delete(0, END)
        else:
            tk.messagebox.showinfo(title='Błąd', message='Podano zły login lub hasło', icon='warning')


class AdminPanelWybor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = '#293B7E'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Panel Administratora - Wybór', font=('Arial', 40, "bold"),
                                     fg='White', bg=self.maincolor)
        self.NazwaFrame_L.place(x=770, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: app.show_frame("GlowneMenu"))
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.Text_L = tk.Label(self, text='Wybierz jedno z poniższych:', font=('Arial', 28, "bold"), fg=self.maincolor,
                               bg='White')
        self.Text_L.place(x=790, y=150, anchor='center')

        self.Dodaj_B = tkm.Button(self, text='Dodaj dane', width=280, height=60, font=('Arial', 28, 'bold'),
                                  foreground='white', background=self.maincolor,
                                  command=lambda: app.show_frame("AdminPanelDodaj"))
        self.Dodaj_B.place(x=790, y=250, anchor='center')

        self.Usun_B = tkm.Button(self, text='Usuń dane', width=280, height=60, font=('Arial', 28, 'bold'),
                                 foreground='white', background=self.maincolor,
                                 command=lambda: app.show_frame("AdminPanelUsun"))
        self.Usun_B.place(x=790, y=350, anchor='center')

        self.Modyfikuj_B = tkm.Button(self, text='Modyfikuj dane', width=280, height=60, font=('Arial', 28, 'bold'),
                                      foreground='white', background=self.maincolor,
                                      command=lambda: app.show_frame("AdminPanelModyfikuj"))
        self.Modyfikuj_B.place(x=790, y=450, anchor='center')


class AdminPanelDodaj(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = '#293B7E'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Panel Administratora - Dodaj dane', font=('Arial', 40, "bold"),
                                     fg='White', bg=self.maincolor)
        self.NazwaFrame_L.place(x=730, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"), self.WyjscieDodaj()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.PowrotPNG_B = ImageTk.PhotoImage(Image.open('Ikony/back.png').resize((60, 60), Image.LANCZOS))
        self.Powrot_B = tkm.Button(self, image=self.PowrotPNG_B, bg=self.maincolor, borderwidt=5,
                                   command=lambda: [app.show_frame("AdminPanelWybor"), self.WyjscieDodaj()])
        self.Powrot_B.place(x=50, y=50, anchor='center')

        self.name_L = Label(self, text="Nazwa:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.name_L.place(x=60, y=150, anchor='center')
        self.name_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.name_E.place(x=190, y=150, anchor='center')

        self.release_date_L = Label(self, text="Data wydania:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.release_date_L.place(x=400, y=150, anchor='center')
        self.release_date_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.release_date_E.place(x=565, y=150, anchor='center')

        self.developer_L = Label(self, text="Deweloper:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.developer_L.place(x=80, y=210, anchor='center')
        self.developer_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.developer_E.place(x=230, y=210, anchor='center')

        self.publisher_L = Label(self, text="Wydawca:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.publisher_L.place(x=420, y=210, anchor='center')
        self.publisher_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.publisher_E.place(x=565, y=210, anchor='center')

        self.english_L = Label(self, text="Angielski:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.english_L.place(x=73, y=270, anchor='center')
        self.english_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.english_E.place(x=220, y=270, anchor='center')

        self.platforms_L = Label(self, text="Platforma (OS):", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.platforms_L.place(x=420, y=270, anchor='center')
        self.platforms_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.platforms_E.place(x=590, y=270, anchor='center')

        self.categories_L = Label(self, text="Kategoria gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.categories_L.place(x=850, y=150, anchor='center')
        self.categories_E = Entry(self, width=20, highlightbackground=self.maincolor, fg=self.maincolor)
        self.categories_E.place(x=1030, y=150, anchor='center')

        self.genres_L = Label(self, text="Typ gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.genres_L.place(x=1200, y=150, anchor='center')
        self.genres_E = Entry(self, width=20, highlightbackground=self.maincolor, fg=self.maincolor)
        self.genres_E.place(x=1350, y=150, anchor='center')

        self.requireds_age_L = Label(self, text="Wymagany wiek:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.requireds_age_L.place(x=1045, y=210, anchor='center')
        self.requireds_age_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.requireds_age_E.place(x=1230, y=210, anchor='center')

        self.positive_ratings_L = Label(self, text="Pozytywne opinie:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.positive_ratings_L.place(x=170, y=490, anchor='center')
        self.positive_ratings_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.positive_ratings_E.place(x=360, y=490, anchor='center')

        self.negative_ratings_L = Label(self, text="Negatywne opinie:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.negative_ratings_L.place(x=170, y=550, anchor='center')
        self.negative_ratings_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.negative_ratings_E.place(x=360, y=550, anchor='center')

        self.average_playtime_L = Label(self, text="Średni czas gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.average_playtime_L.place(x=670, y=490, anchor='center')
        self.average_playtime_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.average_playtime_E.place(x=850, y=490, anchor='center')

        self.median_playtime_L = Label(self, text="Mediana czasu gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.median_playtime_L.place(x=660, y=550, anchor='center')
        self.median_playtime_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.median_playtime_E.place(x=850, y=550, anchor='center')

        self.achievements_L = Label(self, text="Ilość nagród:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.achievements_L.place(x=1130, y=490, anchor='center')
        self.achievements_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.achievements_E.place(x=1300, y=490, anchor='center')

        self.owners_L = Label(self, text="Ilosć graczy:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.owners_L.place(x=1130, y=550, anchor='center')
        self.owners_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.owners_E.place(x=1300, y=550, anchor='center')

        self.price_L = Label(self, text="Cena:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.price_L.place(x=680, y=650, anchor='center')
        self.price_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.price_E.place(x=800, y=650, anchor='center')

        self.DodajTytul_B = tkm.Button(self, text='Dodaj', width=250, height=60, font=('Arial', 32, 'bold'),
                                       foreground='white', background=self.maincolor,
                                       command=lambda: self.DodajTytul())
        self.DodajTytul_B.place(x=790, y=850, anchor='center')

    def DodajTytul(self):
        con = sqlite3.connect("/Users/radekk/PracaMGR.db")
        if self.name_E.get() == '':
            messagebox.showerror('Error', "Nalezy podać nazwę gry")
        else:
            c = con.cursor()
            c.execute("""INSERT INTO Steam(name, release_date, english, developer, publisher, platforms, 
            required_age, categories, genres, achievements, positive_ratings, negative_ratings, 
            average_playtime, median_playtime, owners, price) 
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (self.name_E.get(), self.release_date_E.get(), self.english_E.get(), self.developer_E.get(),
                       self.publisher_E.get(), self.platforms_E.get(), self.requireds_age_E.get(),
                       self.categories_E.get(),
                       self.genres_E.get(), self.achievements_E.get(), self.positive_ratings_E.get(),
                       self.negative_ratings_E.get(),
                       self.average_playtime_E.get(), self.median_playtime_E.get(), self.owners_E.get(),
                       self.price_E.get()))
            con.commit()
            messagebox.showinfo('Informacja', "Dodano nowy tytuł")
        con.close()

    def WyjscieDodaj(self):
        self.name_E.delete(0, END)
        self.release_date_E.delete(0, END)
        self.english_E.delete(0, END)
        self.developer_E.delete(0, END)
        self.publisher_E.delete(0, END)
        self.platforms_E.delete(0, END)
        self.requireds_age_E.delete(0, END)
        self.categories_E.delete(0, END)
        self.genres_E.delete(0, END)
        self.achievements_E.delete(0, END)
        self.positive_ratings_E.delete(0, END)
        self.negative_ratings_E.delete(0, END)
        self.average_playtime_E.delete(0, END)
        self.median_playtime_E.delete(0, END)
        self.owners_E.delete(0, END)
        self.price_E.delete(0, END)


class AdminPanelUsun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = '#293B7E'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Panel Administratora - Usuń dane', font=('Arial', 40, "bold"),
                                     fg='White', bg=self.maincolor)
        self.NazwaFrame_L.place(x=730, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"),
                                                  self.WyjscieUsun()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.PowrotPNG_B = ImageTk.PhotoImage(Image.open('Ikony/back.png').resize((60, 60), Image.LANCZOS))
        self.Powrot_B = tkm.Button(self, image=self.PowrotPNG_B, bg=self.maincolor, borderwidt=5,
                                   command=lambda: [app.show_frame("AdminPanelWybor"),
                                                    self.WyjscieUsun()])
        self.Powrot_B.place(x=50, y=50, anchor='center')

        self.Znajdz_L = tk.Label(self, text='Znajdź dane:', font=('Arial', 36, "bold"), fg=self.maincolor,
                                 bg='White')
        self.Znajdz_L.place(x=790, y=150, anchor='center')

        self.Tytul_L = Label(self, text="Tytuł - ", font=('Arial', 32, "bold"), fg=self.maincolor)
        self.Tytul_L.place(x=180, y=250, anchor='center')
        self.Tytul_E = Entry(self, width=24, highlightbackground=self.maincolor, fg=self.maincolor)
        self.Tytul_E.place(x=350, y=250, anchor='center')

        self.Wynik_L = Label(self, text="Wynik wyszukiwania:", font=('Arial', 30, "bold"), fg=self.maincolor)
        self.Wynik_L.place(x=1200, y=250, anchor='center')

        self.ZnajdzTytul_B = tkm.Button(self, text='Znajdz tytuł', width=160, height=40, font=('Arial', 24, 'bold'),
                                        foreground='white', background=self.maincolor,
                                        command=lambda: self.PokazTytul())
        self.ZnajdzTytul_B.place(x=280, y=300, anchor='center')

        self.WynikKoncowy_L = Label(self)

        self.Usun_L = tk.Label(self, text='Usuń dane:', font=('Arial', 36, "bold"), fg=self.maincolor,
                               bg='White')
        self.Usun_L.place(x=790, y=680, anchor='center')

        self.IDTytul_L = Label(self, text="ID - ", font=('Arial', 32, "bold"), fg=self.maincolor)
        self.IDTytul_L.place(x=450, y=750, anchor='center')
        self.IDTytul_E = Entry(self, width=24, highlightbackground=self.maincolor, fg=self.maincolor)
        self.IDTytul_E.place(x=600, y=750, anchor='center')

        self.UsunIDTytul_B = tkm.Button(self, text='Usuń tytuł', width=160, height=40, font=('Arial', 24, 'bold'),
                                        foreground='white', background=self.maincolor,
                                        command=lambda: self.UsunTytul())
        self.UsunIDTytul_B.place(x=950, y=750, anchor='center')

    def PokazTytul(self):
        con = sqlite3.connect("/Users/radekk/PracaMGR.db")
        cur = con.cursor()

        self.WynikKoncowy_L.destroy()

        if self.Tytul_E.get() == '':
            messagebox.showerror('Error', "Należy podać nazwę apliakcji")
        else:
            self.SQLCOM = ("""select id,name
                    from Steam
                    where name like ? limit 5""")

            data = cur.execute(self.SQLCOM, ('%' + self.Tytul_E.get() + '%',))
            tytul_data = ''
            for td in data.fetchall():
                tytul_data += str(td[0]) + " - " + str(td[1]) + "\n" + "\n"

            self.WynikKoncowy_L = Label(self, text=tytul_data, font=('Arial', 22, "bold"), fg=self.maincolor)
            self.WynikKoncowy_L.place(x=1200, y=440, anchor='center')

        con.close()

    def UsunTytul(self):
        con = sqlite3.connect("/Users/radekk/PracaMGR.db")

        if self.IDTytul_E.get() == '':
            messagebox.showerror('Error', "Należy podać identyfikator apliakcji")
        else:
            c = con.cursor()
            c.execute("DELETE from Steam where id= " + self.IDTytul_E.get())
            self.IDTytul_E.delete(0, END)
            con.commit()
            messagebox.showinfo('Informacja', "Aplikacja została usunięta")

    def WyjscieUsun(self):
        self.WynikKoncowy_L.destroy()
        self.Tytul_E.delete(0, END)
        self.IDTytul_E.delete(0, END)


class AdminPanelModyfikuj(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.maincolor = '#293B7E'

        self.canvas = Canvas(self, height=200, width=3024, bg=self.maincolor)
        self.canvas.place(x=0, y=0, anchor='center')

        self.NazwaFrame_L = tk.Label(self, text='Panel Administratora - Modyfikuj dane', font=('Arial', 40, "bold"),
                                     fg='White', bg=self.maincolor)
        self.NazwaFrame_L.place(x=730, y=50, anchor='center')

        self.MenuPNG_B = ImageTk.PhotoImage(Image.open('Ikony/home-button.png').resize((60, 60), Image.LANCZOS))
        self.Menu_B = tkm.Button(self, image=self.MenuPNG_B, bg=self.maincolor, borderwidt=5,
                                 command=lambda: [app.show_frame("GlowneMenu"),
                                                  self.WyjscieModyfikuj()])
        self.Menu_B.place(x=1350, y=50, anchor='center')

        self.WyjsciePNG_B = ImageTk.PhotoImage(Image.open('Ikony/exit.png').resize((60, 60), Image.LANCZOS))
        self.Wyjscie_B = tkm.Button(self, image=self.WyjsciePNG_B, bg=self.maincolor, borderwidt=5,
                                    command=lambda: app.exit_app())
        self.Wyjscie_B.place(x=1450, y=50, anchor='center')

        self.PowrotPNG_B = ImageTk.PhotoImage(Image.open('Ikony/back.png').resize((60, 60), Image.LANCZOS))
        self.Powrot_B = tkm.Button(self, image=self.PowrotPNG_B, bg=self.maincolor, borderwidt=5,
                                   command=lambda: [app.show_frame("AdminPanelWybor"),
                                                    self.WyjscieModyfikuj()])
        self.Powrot_B.place(x=50, y=50, anchor='center')

        self.IDTytul_L = Label(self, text="ID:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.IDTytul_L.place(x=500, y=130, anchor='center')
        self.IDTytul_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.IDTytul_E.place(x=600, y=130, anchor='center')

        self.SzukajIDTytul_B = tkm.Button(self, text='Szukaj', width=180, height=40, font=('Arial', 20, 'bold'),
                                          foreground='white', background=self.maincolor,
                                          command=lambda: self.PokazTytul())
        self.SzukajIDTytul_B.place(x=900, y=130, anchor='center')

        self.name_L = Label(self, text="Nazwa:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.name_L.place(x=60, y=280, anchor='center')
        self.name_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.name_E.place(x=190, y=280, anchor='center')

        self.release_date_L = Label(self, text="Data wydania:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.release_date_L.place(x=400, y=280, anchor='center')
        self.release_date_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.release_date_E.place(x=565, y=280, anchor='center')

        self.developer_L = Label(self, text="Deweloper:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.developer_L.place(x=80, y=340, anchor='center')
        self.developer_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.developer_E.place(x=230, y=340, anchor='center')

        self.publisher_L = Label(self, text="Wydawca:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.publisher_L.place(x=420, y=340, anchor='center')
        self.publisher_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.publisher_E.place(x=565, y=340, anchor='center')

        self.english_L = Label(self, text="Angielski:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.english_L.place(x=73, y=400, anchor='center')
        self.english_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.english_E.place(x=220, y=400, anchor='center')

        self.platforms_L = Label(self, text="Platforma (OS):", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.platforms_L.place(x=420, y=400, anchor='center')
        self.platforms_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.platforms_E.place(x=590, y=400, anchor='center')

        self.categories_L = Label(self, text="Kategoria gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.categories_L.place(x=850, y=280, anchor='center')
        self.categories_E = Entry(self, width=20, highlightbackground=self.maincolor, fg=self.maincolor)
        self.categories_E.place(x=1030, y=280, anchor='center')

        self.genres_L = Label(self, text="Typ gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.genres_L.place(x=1200, y=280, anchor='center')
        self.genres_E = Entry(self, width=20, highlightbackground=self.maincolor, fg=self.maincolor)
        self.genres_E.place(x=1350, y=280, anchor='center')

        self.requireds_age_L = Label(self, text="Wymagany wiek:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.requireds_age_L.place(x=1045, y=340, anchor='center')
        self.requireds_age_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.requireds_age_E.place(x=1230, y=340, anchor='center')

        self.positive_ratings_L = Label(self, text="Pozytywne opinie:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.positive_ratings_L.place(x=170, y=540, anchor='center')
        self.positive_ratings_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.positive_ratings_E.place(x=360, y=540, anchor='center')

        self.negative_ratings_L = Label(self, text="Negatywne opinie:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.negative_ratings_L.place(x=170, y=600, anchor='center')
        self.negative_ratings_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.negative_ratings_E.place(x=360, y=600, anchor='center')

        self.average_playtime_L = Label(self, text="Średni czas gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.average_playtime_L.place(x=670, y=540, anchor='center')
        self.average_playtime_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.average_playtime_E.place(x=850, y=540, anchor='center')

        self.median_playtime_L = Label(self, text="Mediana czasu gry:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.median_playtime_L.place(x=660, y=600, anchor='center')
        self.median_playtime_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.median_playtime_E.place(x=850, y=600, anchor='center')

        self.achievements_L = Label(self, text="Ilość nagród:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.achievements_L.place(x=1130, y=540, anchor='center')
        self.achievements_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.achievements_E.place(x=1300, y=540, anchor='center')

        self.owners_L = Label(self, text="Ilosć graczy:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.owners_L.place(x=1130, y=600, anchor='center')
        self.owners_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.owners_E.place(x=1300, y=600, anchor='center')

        self.price_L = Label(self, text="Cena:", font=('Arial', 22, "bold"), fg=self.maincolor)
        self.price_L.place(x=680, y=700, anchor='center')
        self.price_E = Entry(self, width=17, highlightbackground=self.maincolor, fg=self.maincolor)
        self.price_E.place(x=800, y=700, anchor='center')

        self.DodajTytul_B = tkm.Button(self, text='Modyfikuj', width=250, height=60, font=('Arial', 32, 'bold'),
                                       foreground='white', background=self.maincolor,
                                       command=lambda: self.ModyfikujTytul())
        self.DodajTytul_B.place(x=790, y=850, anchor='center')

    def PokazTytul(self):
        con = sqlite3.connect("/Users/radekk/PracaMGR.db")
        cur = con.cursor()

        if self.IDTytul_E.get() == '':
            messagebox.showerror('Error', "Należy podać identyfikator apliakcji")
        else:
            self.SQLCOM = ("""select *
                    from Steam
                    where id like ?""")

            self.data = cur.execute(self.SQLCOM, (self.IDTytul_E.get(),))

        for record in self.data:
            self.name_E.delete(0, END)
            self.name_E.insert(0, record[0])

            self.release_date_E.delete(0, END)
            self.release_date_E.insert(0, record[1])

            self.english_E.delete(0, END)
            self.english_E.insert(0, record[2])

            self.developer_E.delete(0, END)
            self.developer_E.insert(0, record[3])

            self.publisher_E.delete(0, END)
            self.publisher_E.insert(0, record[4])

            self.platforms_E.delete(0, END)
            self.platforms_E.insert(0, record[5])

            self.requireds_age_E.delete(0, END)
            self.requireds_age_E.insert(0, record[6])

            self.categories_E.delete(0, END)
            self.categories_E.insert(0, record[7])

            self.genres_E.delete(0, END)
            self.genres_E.insert(0, record[8])

            self.achievements_E.delete(0, END)
            self.achievements_E.insert(0, record[9])

            self.positive_ratings_E.delete(0, END)
            self.positive_ratings_E.insert(0, record[10])

            self.negative_ratings_E.delete(0, END)
            self.negative_ratings_E.insert(0, record[11])

            self.average_playtime_E.delete(0, END)
            self.average_playtime_E.insert(0, record[12])

            self.median_playtime_E.delete(0, END)
            self.median_playtime_E.insert(0, record[13])

            self.owners_E.delete(0, END)
            self.owners_E.insert(0, record[14])

            self.price_E.delete(0, END)
            self.price_E.insert(0, record[15])

        con.close()

    def ModyfikujTytul(self):
        con = sqlite3.connect("/Users/radekk/PracaMGR.db")
        c = con.cursor()
        self.SQLCOM = ("""
          UPDATE Steam SET 
          name = ?, release_date = ?, english = ?, developer = ?,
          publisher = ?, platforms = ?, required_age = ?, categories = ?,
          genres = ?, achievements = ?, positive_ratings = ?, negative_ratings = ?,
          average_playtime = ?, median_playtime = ?, owners = ?, price = ?
          WHERE
          id = ?""")
        c.execute(self.SQLCOM, [self.name_E.get(), self.release_date_E.get(), self.english_E.get(),
                                self.developer_E.get(), self.publisher_E.get(), self.platforms_E.get(),
                                self.requireds_age_E.get(), self.categories_E.get(), self.genres_E.get(),
                                self.achievements_E.get(), self.positive_ratings_E.get(), self.negative_ratings_E.get(),
                                self.average_playtime_E.get(), self.median_playtime_E.get(),
                                self.owners_E.get(), self.price_E.get(), self.IDTytul_E.get()])
        con.commit()
        messagebox.showinfo('Informacja', "Zmiany zostały wprowadzone")

    def WyjscieModyfikuj(self):
        self.IDTytul_E.delete(0, END)
        self.name_E.delete(0, END)
        self.release_date_E.delete(0, END)
        self.english_E.delete(0, END)
        self.developer_E.delete(0, END)
        self.publisher_E.delete(0, END)
        self.platforms_E.delete(0, END)
        self.requireds_age_E.delete(0, END)
        self.categories_E.delete(0, END)
        self.genres_E.delete(0, END)
        self.achievements_E.delete(0, END)
        self.positive_ratings_E.delete(0, END)
        self.negative_ratings_E.delete(0, END)
        self.average_playtime_E.delete(0, END)
        self.median_playtime_E.delete(0, END)
        self.owners_E.delete(0, END)
        self.price_E.delete(0, END)


if __name__ == "__main__":
    app = SteamEmpiria()
    app.title("Steam Stat")
    app.mainloop()
