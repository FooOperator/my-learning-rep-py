from tkinter import Tk as tk, Label, Entry, Button, Frame, Menu, Scrollbar, Canvas

colors = {
    'blue': '#3C91E6',
    'black': '#342E37',
    'green': '#5C946E',
    'red': '#AA5042',
    'yellow': '#F9DC5C',
    'celeste': '#C5FFFD',
    'gold': '#F1A208',
    'dark blue': '#005377',
    'white': '#EFE6DD'
}

preset_tiers = {
    'S Rank': colors.get('gold'),
    'A Rank': colors.get('blue'),
    'B Rank': colors.get('green'),
    'C Rank': colors.get('yellow'),
    'D Rank': colors.get('red')
}

btn_width = 10
btn_height = 1
btn_fg = colors.get('black')

class Window(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.winfo_toplevel().title('Tier List Maker')
        self.new_tier = None
        self.tier_content = None
        self.added_tiers = []
        self.added_content = []
        self.pack()
        self.winfo_toplevel().geometry('860x600')
        self.winfo_toplevel().resizable(False, False)
        self.make_frames()
        self.menus()
        self.make_widgets()
        
    def make_frames(self):
        self.top_frame = Frame(self)
        self.btn_frame = Frame(self)
        self.tiercolumn_frame = Frame(self)
        
        self.canvas = Canvas(self.tiercolumn_frame)
        self.scrollable_frame = Frame(self.canvas)
        self.scrolly = Scrollbar(self.tiercolumn_frame, orient='vertical', command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrolly.set, scrollregion=self.canvas.bbox('all'))
        
        self.canvas.create_window((500, 0), window=self.scrollable_frame, anchor='nw')

        self.top_frame.pack(side='top')
        self.canvas.pack(side='left', expand=True)
        self.scrolly.pack(side='right', fill='y')
        self.tiercolumn_frame.pack()
        self.btn_frame.pack(padx=(0, 10), side='bottom')
    
    def menus(self):
        self.menu_bar = Menu(self, tearoff=0)
        self.file_bar = Menu(self, tearoff=0)
        self.options_bar = Menu(self, tearoff=0)
        self.right_click = Menu(self.tiercolumn_frame, tearoff=0)
        self.color_select = Menu(self.right_click, tearoff=0)
        
        for color in colors:
            self.color_select.add_command(label=color, command=None)
        
        self.right_click.add_cascade(label='Change Tier Color', menu=self.color_select)
        self.right_click.add_command(label='Delete Tier', command=None)
        self.right_click.add_command(label='Copy Tier', command=None)
        self.right_click.add_command(label='Add Tier Above Tier', command=None)
        self.right_click.add_command(label='Add Tier Below Tier', command=None)
        
        self.file_bar.add_command(label='New Tier List', command=None)
        self.file_bar.add_command(label='Load Tier List', command=None)
        self.file_bar.add_separator()
        self.file_bar.add_command(label='Save Tier List', command=None)
        self.file_bar.add_command(label='Save Tier List As...', command=None)
        
        self.options_bar.add_command(label='Preferences', command=None)
        self.options_bar.add_separator()
        self.options_bar.add_command(label='Set Path', command=None)
        
        self.menu_bar.add_cascade(label='File', menu=self.file_bar)
        self.menu_bar.add_cascade(label='Settings', menu=self.options_bar)
        
        self.winfo_toplevel().config(menu=self.menu_bar)
        
    def do_popup(self, event): 
        self.right_click.tk_popup(event.x_root, event.y_root)  
    
    def add_tier(self, name='New Tier', color=colors.get('white')):
        try:
            self.new_tier = Entry(self.canvas, bg=color)
            self.new_tier.insert(0, name)
            self.tier_content = Entry(self.canvas, disabledbackground='#141414', state='disabled', cursor='arrow')
            
            self.added_tiers.append(self.new_tier)
            self.new_tier.bind("<Button-3>", self.do_popup)
            self.added_content.append(self.tier_content)
            
            self.new_tier.grid(row=len(self.added_tiers), column=0, ipady=20)
            self.tier_content.grid(row=len(self.added_tiers), column=1, ipady=20, ipadx=300)
            
            print('New tier added')
            print(len(self.added_tiers))
        except:
            print('Tier not added')
            print(len(self.added_tiers))
    
    def delete_tier(self):
        try:
            if len(self.added_tiers) > 1 and len(self.added_content) > 1:
                target = self.added_tiers.pop()
                target.destroy()
                target = self.added_content.pop()
                target.destroy()
                print('Tier removed')
                print(len(self.added_tiers))
        except:
            print('Tier not removed')
            print(len(self.added_tiers))
    
    def customize_tier(self):
        pass
    
    def make_widgets(self):
        main_label = Label(self.top_frame, text='Tier List Maker', width=200)
        main_label.config(
            font=('Texturina', 25),
            fg=colors.get('black'),
            bg=colors.get('red')
        )
        main_label.pack()
        
        for index in preset_tiers:
            self.add_tier(index, preset_tiers.get(index))
            print(index, preset_tiers.get(index))
            
        add_button = Button(
            self.btn_frame,
            text='Add',
            font=('Open Sans', 14),
            height=btn_height,
            width=btn_width,
            fg=btn_fg,
            bg=colors.get('green'),
            activebackground=btn_fg,
            activeforeground=colors.get('green'),
            command=self.add_tier
        )
        delete_button = Button(
            self.btn_frame,
            text='Delete',
            font=('Open Sans', 14),
            height=btn_height,
            width=btn_width,
            fg=btn_fg,
            bg=colors.get('red'),
            activebackground=btn_fg,
            activeforeground=colors.get('red'),
            command=self.delete_tier
        )
        add_button.pack(side='left')
        delete_button.pack()

root = tk()
app = Window(parent=root)
root.mainloop()