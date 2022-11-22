from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class SelectUserWindow():
    def __init__(self, parent):
        self.r_var = BooleanVar()
        self.r_var.set(False)
        self.welcome = Label(text='Добро пожаловать\n в', font=('Arial', 18))
        self.name = Label(text='CityPlanner', foreground="#d516d9", font=('Arial', 18), height = 2)
        self.r1 = Radiobutton(text='Пользователь', variable=self.r_var, value=0, height = 3, font=('Arial', 15))
        self.r2 = Radiobutton(text='Планировщик', variable=self.r_var, value=1,  font=('Arial', 15))
        self.button = Button(text='Запустить', command=lambda: parent.display(self.r_var), font=('Arial', 12))
        
    def display(self):
        self.welcome.pack()
        self.name.pack()
        self.r1.pack(anchor=W)
        self.r2.pack(anchor=W)
        self.button.pack()
        
    def destroy(self):
        self.welcome.destroy()
        self.name.destroy()
        self.r1.destroy()
        self.r2.destroy()
        self.button.destroy()
        
class MainWindow():
    def __init__(self, parent, is_planer_mod):
        self.parent = parent
        self.init_commands()
        self.init_buttons(is_planer_mod)
        self.init_road_table(is_planer_mod)
        self.init_rout_table()
            
    def display(self):
        for button in self.buttons:
            button.pack(anchor=W)
        self.roads.place(x=60, y=0, width = 500, height = 450)
        self.routs.place(x = 560, y = 0, width = 300, height = 450)
        
    def destroy(self):
        for button in self.buttons:
            button.destroy()
        self.roads.destroy()
        self.routs.destroy()
        
    def init_commands(self):
        self.add_road_command = self.parent.commands['add_road_command']
        self.delete_road_command = self.parent.commands['delete_road_command']
        self.add_traffic_light_command = self.parent.commands['add_traffic_light_command']
        self.add_building_command = self.parent.commands['add_building_command']
        self.delete_building_command = self.parent.commands['delete_building_command']
        self.delete_traffic_light_command = self.parent.commands['delete_traffic_light_command']
        self.change_load_command = self.parent.commands['change_load_command']
        self.change_roadname_command = self.parent.commands['change_roadname_command']
        self.find_shortest_rout_command = self.parent.commands['find_shortest_rout_command']
        self.build_rout_command = self.parent.commands['build_rout_command']
        self.find_fastest_rout_command = self.parent.commands['find_fastest_rout_command']
        self.change_throughput_command = self.parent.commands['change_throughput_command']
        
    def init_buttons(self, is_planer_mod):
        self.commands = [self.save,
                         self.open,
                         self.add_road,
                         self.delete_road,
                         self.add_traffic_light,
                         self.delete_traffic_light,
                         self.build_rout,
                         self.change_element,
                         self.exit]
        self.buttons_img = [ImageTk.PhotoImage(Image.open('ui/save.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/open.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/road.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/del_road.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/tl.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/del_tl.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/path.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/edit.png').resize((50,50), Image.ANTIALIAS)),
                            ImageTk.PhotoImage(Image.open('ui/exit.png').resize((50,50), Image.ANTIALIAS))]
        if is_planer_mod:
            self.buttons = [Button(image=self.buttons_img[i], command=self.commands[i]) for i in range(len(self.buttons_img))]
        else:
            self.buttons = [Button(image=self.buttons_img[0], command=self.commands[0]),
                            Button(image=self.buttons_img[1], command=self.commands[1]),
                            Button(image=self.buttons_img[-3], command=self.commands[-3]),
                            Button(image=self.buttons_img[-1], command=self.commands[-1])]
    
    def test(self):
        print('test')
    
    def exit(self):
        self.parent.exit()
    
    def save(self):
        win = Toplevel(self.parent.window)
        Label(win, text="Add save interface for correct working").pack()
        Button(win, text="Close", height=3, width=10, command= win.destroy).pack()
        
    def open(self):
        win = Toplevel(self.parent.window)
        Label(win, text="Add open interface for correct working").pack()
        Button(win, text="Close", height=3, width=10, command= win.destroy).pack()
        
    def add_road(self):
        win = Toplevel(self.parent.window)
        Label(win, text="Название улицы").place(x = 0, y = 0)
        Entry(win).place(x = 150, y = 0)
        Label(win, text="Нагрузка").place(x = 0, y = 20)
        Entry(win).place(x = 150, y = 20)
        def add_and_close():
            self.add_road_command.exec()
            win.destroy()
        Button(win, text="Добавить", width=10, command= add_and_close).place(x = 150, y = 50)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 50)
        
    def delete_road(self):
        win = Toplevel(self.parent.window)
        columns = ("#1")
        delete_roads = ttk.Treeview(win, show="headings", columns=columns)
        delete_roads.heading("#1", text="Улицы")
        ysb = ttk.Scrollbar(orient=VERTICAL, command=delete_roads.yview)
        delete_roads.configure(yscroll=ysb.set)
        for road in self.add_road_command.city.roads:
            value = road.name
            delete_roads.insert("", END, values=[value])
        delete_roads.place(x = 0, y = 0, width = 500, height = 400)
        def delete_road():
            self.delete_road_command.exec()
            win.destroy()
        
        Button(win, text="Отмена", width=10, command=win.destroy).place(x = 0, y = 430)
        Button(win, text="Удалить", width=10, command=delete_road).place(x = 100, y = 430)
        
    def build_rout(self):
        win = Toplevel(self.parent.window)
        options = [value.name for value in self.add_road_command.city.roads]
        road1 = StringVar()
        road1.set(options[0])
        road2 = StringVar()
        road2.set(options[0])
        
        select_road_1 = OptionMenu(win, road1, *options)
        select_road_2 = OptionMenu(win, road2, *options)
        select_road_1.pack(anchor=W)
        select_road_2.pack(anchor=W)
        def build_rout_and_close():
            self.build_rout_command.exec()
            win.destroy()
        Button(win, text="Построить маршрут", width=10, command= build_rout_and_close).place(x = 150, y = 70, width = 200)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 70)

    def add_traffic_light(self):
        win = Toplevel(self.parent.window)
        options = [value.name for value in self.add_road_command.city.roads]
        road1 = StringVar()
        road1.set(options[0])
        road2 = StringVar()
        road2.set(options[0])
        
        select_road_1 = OptionMenu(win, road1, *options)
        select_road_2 = OptionMenu(win, road2, *options)
        select_road_1.pack(anchor=W)
        select_road_2.pack(anchor=W)
        
        Label(win, text="Пропускная способность ").place(x = 0, y = 70)
        Entry(win).place(x = 170, y = 70)
        def add_and_close():
            self.add_traffic_light_command.exec()
            win.destroy()
        Button(win, text="Добавить", width=10, command= add_and_close).place(x = 150, y = 100)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 100)
        
    def delete_traffic_light(self):
        win = Toplevel(self.parent.window)
        options = [value.name for value in self.add_road_command.city.roads]
        road1 = StringVar()
        road1.set(options[0])
        road2 = StringVar()
        road2.set(options[0])
        
        select_road_1 = OptionMenu(win, road1, *options)
        select_road_2 = OptionMenu(win, road2, *options)
        select_road_1.pack(anchor=W)
        select_road_2.pack(anchor=W)
        def delete_and_close():
            self.delete_traffic_light_command.exec()
            win.destroy()
        Button(win, text="Удалить", width=10, command= delete_and_close).place(x = 150, y = 70)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 70)
        
    def init_road_table(self, is_planer_mod):
        columns = ("#1")
        self.roads = ttk.Treeview(show="headings", columns=columns)
        self.roads.heading("#1", text="Улицы")
        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.roads.yview)
        self.roads.configure(yscroll=ysb.set)
        for road in self.add_road_command.city.roads:
            value = road.name
            self.roads.insert("", END, values=[value])
        
        def search_road(roadname):
            for road in self.add_road_command.city.roads:
                if road.name == roadname[0]:
                    return road
                
        def item_selected(event):
            for selected_item in self.roads.selection():
                item = self.roads.item(selected_item)
                record = item['values']
                self.change_road_info(search_road(record))
        if is_planer_mod:    
            self.roads.bind('<<TreeviewSelect>>', item_selected)
            
    def init_rout_table(self):
        columns = ('#1')
        self.routs = ttk.Treeview(show="headings", columns=columns)
        self.routs.heading("#1", text="Маршруты")
        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.roads.yview)
        self.routs.configure(yscroll=ysb.set)
        for rout in self.build_rout_command.routes:
            self.routs.insert("", END, values=[rout.name])
    
    def change_traffic_light(self):
        win = Toplevel(self.parent.window)
        options = [value.name for value in self.add_road_command.city.roads]
        road1 = StringVar()
        road1.set(options[0])
        road2 = StringVar()
        road2.set(options[0])
        
        select_road_1 = OptionMenu(win, road1, *options)
        select_road_2 = OptionMenu(win, road2, *options)
        select_road_1.pack(anchor=W)
        select_road_2.pack(anchor=W)
        
        Label(win, text="Пропускная способность ").place(x = 0, y = 70)
        Entry(win).place(x = 170, y = 70)
        def change_and_close():
            self.change_throughput_command.exec()
            win.destroy()
        Button(win, text="Сохранить", width=10, command= change_and_close).place(x = 150, y = 100)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 100)   
    
    def change_element(self):
        win = Toplevel(self.parent.window)
        Button(win, text="Изменить пропускную\n способность", command=self.change_traffic_light).pack(anchor = W)
        Button(win, text="Отмена", command=win.destroy).place(x = 0, y = 50)
        Button(win, text="Ок", command=win.destroy).place(x = 120, y = 50)
        
    def change_road_info(self, road):
        win = Toplevel(self.parent.window)
        Button(win, text="Добавить здание", command=lambda: self.add_building(road), height = 1, width = 20).pack(anchor = W)
        Button(win, text="Удалить здание", command=lambda: self.delete_building(road), height = 1, width = 20).pack(anchor = W)
        Button(win, text="Изменить нагрузку", command=lambda: self.change_load(road), height = 1, width = 20).pack(anchor = W)
        Button(win, text="Изменить название", command=lambda: self.change_name(road), height = 1, width = 20).pack(anchor = W)
        Button(win, text="Отмена", command=win.destroy).place(x = 0, y = 130)
        Button(win, text="Ок", command=win.destroy).place(x = 125, y = 130)
        
    def add_building(self, road):
        win = Toplevel(self.parent.window)
        Label(win, text="Название здания").place(x = 0, y = 0)
        Entry(win).place(x = 150, y = 0)
        def add_and_close():
            self.add_building_command.exec()
            win.destroy()
        Button(win, text="Добавить", width=10, command= add_and_close).place(x = 150, y = 20)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 20)
    
    def delete_building(self, road):
        win = Toplevel(self.parent.window)
        columns = ('#1')
        delete_buildings = ttk.Treeview(win, show="headings", columns=columns)
        delete_buildings.heading("#1", text="Здание")
        ysb = ttk.Scrollbar(orient=VERTICAL, command=delete_buildings.yview)
        delete_buildings.configure(yscroll=ysb.set)
        for building in road.buildings:
            value = building.name
            delete_buildings.insert("", END, values=[value])
        delete_buildings.place(x = 0, y = 0, width = 500, height = 400)
        def delete_buildings():
            self.delete_road_command.exec()
            win.destroy()
        
        Button(win, text="Отмена", width=10, command=win.destroy).place(x = 0, y = 430)
        Button(win, text="Удалить", width=10, command=delete_buildings).place(x = 100, y = 430)
        
    def change_load(self, road):
        win = Toplevel(self.parent.window)
        Label(win, text="Нагрузка").place(x = 0, y = 0)
        Entry(win).place(x = 150, y = 0)
        def change_and_close():
            self.change_load_command.exec()
            win.destroy()
        Button(win, text="Изменить", width=10, command= change_and_close).place(x = 150, y = 20)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 20)
        
    def change_name(self, road):
        win = Toplevel(self.parent.window)
        Label(win, text="Название улицы").place(x = 0, y = 0)
        Entry(win).place(x = 150, y = 0)
        def change_and_close():
            self.change_roadname_command.exec()
            win.destroy()
        Button(win, text="Изменить", width=10, command= change_and_close).place(x = 150, y = 20)
        Button(win, text="Отмена", width=10, command= win.destroy).place(x = 0, y = 20)
        
        
    
class ApplicationWindow():
    def __init__(self, **kwargs):
        self.window = Tk()
        self.select_user_window = SelectUserWindow(self)
        self.current_window = self.select_user_window
        self.commands = kwargs
        
    def run(self):
        self.current_window.display()
        self.window.mainloop()
    
    def display(self, r_var):
        self.current_window.destroy()
        
        if r_var.get() == True:
            self.main_window = MainWindow(self, True)
            self.current_window = self.main_window
            self.current_window.display()
        if r_var.get() == False:
            self.main_window = MainWindow(self, False)
            self.current_window = self.main_window
            self.current_window.display()
    
    def exit(self):
        self.window.destroy()