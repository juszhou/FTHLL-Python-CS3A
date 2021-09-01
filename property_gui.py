import tkinter
class PropertyGUI:
    def __init__(self):
# Create the main window
        self.main_window = tkinter.Tk()
# Create frames

# one each for value, asses, tax and a bottom frame
        self.value_frame = tkinter.Frame(self.main_window)
        self.assess_frame = tkinter.Frame(self.main_window)
        self.tax_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

# Create the widgets for the value frame
        self.value_label = tkinter.Label(self.value_frame,
                                         text='Enter the property value: $')
        self.value_entry = tkinter.Entry(self.value_frame, width=10)

# Pack the value frame widgets
        self.value_label.pack(side='bottom')
        self.value_entry.pack(side='bottom')

# Create the widget for the assess frame
        self.assess_label = tkinter.Label(self.assess_frame, \
                                  text='Enter your assessment value: $')

# Create a blank label for assessment value
        self.assess_val = tkinter.Label(self.assess_frame, text ='')

# Pack the assess frame widgets
        self.assess_label.pack(side='bottom')
        self.assess_val.pack(side='bottom')

# Create the widget for the tax frame
        self.tax_label = tkinter.Label(self.tax_frame,
                               text='Enter the property tax: %')

# Create a blank label for property tax value
        self.tax_val = tkinter.Label(self.tax_frame, text = '')

# Pack the tax frame widgets
        self.tax_label.pack(side='bottom')
        self.tax_val.pack(side='bottom')

# Create the two buttons in the bottom frame

# "Calculate" and "Quit"
        self.calc_button = tkinter.Button(self.bottom_frame,
                                  text='Calculate',
                                  command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                  text='Quit',
                                  command=self.main_window.destroy)

# Pack the widgets in the bottom frame
        self.calc_button.pack(side='bottom')
        self.quit_button.pack(side='bottom')

# Pack the frames
        self.value_frame.pack()
        self.assess_frame.pack()
        self.tax_frame.pack()
        self.bottom_frame.pack()

# Enter the tkinter main loop
        tkinter.mainloop()

# Define the show_info function
    def calculate(self):

# Get the values entered
        self.value = float(self.value_entry.get())

# Calculate assessment
        assess_percent = 0.60
        self.assessment = (self.value * assess_percent)

# Update the assessment label - display a dollar sign too
        self.assess_val = tkinter.StringVar
        self.assess_val.set(self.assessment)

# Calculate tax
        self.tax = (self.assessment / 100) * 0.75

# Update the tax label
        self.tax_val = tkinter.StringVar
        self.tax_val.set(self.tax)

# Create an instance of PropertyGUI
prop_gui = PropertyGUI()