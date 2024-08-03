#Import required modules and libraries
from tkinter import *

# Create the main application window
root = Tk()
root.title("Note Taking Desktop Application")
root.configure(bg='#145660')
root.geometry('400x700')

# Label for the title
p = Label(root, text="Notespro*", height="18", width="250", bg='#145660', fg='white', font=('Helvetica', '20', 'bold', 'italic'))
p.pack()

def launch_notes():
    """
    Function to launch the Notespro desktop application.

    Imports the 'functionality_accessor' module to start the application.
    """
    import functionality_accessor
    functionality_accessor.notes_functionality(root)


# Button to launch the application
launch_btn = Button(root, text="Launch App", command=launch_notes, bg="red", fg='white', padx=40, pady=10, font=('Helvetica', '10', 'bold'))
launch_btn.pack(padx=25, pady=0)

# Button to exit the application
exit_button = Button(root, text="Exit", command=root.destroy, bg="#636466", fg='white', padx=65, pady=8, font=('Helvetica', '10', 'bold'))
exit_button.pack(padx=25, pady=10)

# Start the main event loop
root.mainloop()
