#Import required modules and libraries
from tkinter import *
from tkinter import ttk
import note_visualization
from view_notes import view_all_notes  # Importing function from view_notes.py
from add_notes import add_note
from edit_delete import edit_delete
from search_status import search_status

def notes_functionality(root):
    """
    Starts the Notespro application using the provided Tkinter root window.
    """
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Note Taking App")
    root.configure(bg='#145660')
    root.geometry('1920x1080')
    root.state('zoomed')  # This line makes the window open in maximized state

    p = Label(root, text='Notespro', height="20", width="40", bg='#145660', fg='white',
              font=('Helvetica', '18', 'bold', 'italic'))
    p.place(x=370, y=10)

    # Add Note button
    add_note_button = Button(root, text="Add Note", bg="red", padx=55, pady=10, bd=7, fg='white',
                             font=('Helvetica', 12, 'bold'), command=lambda: add_note(root))
    add_note_button.place(x=270, y=20)

    # Edit Note button
    edit_delete_button = Button(root, text="Edit Note", command=lambda: edit_delete(root), bg="red", padx=55, pady=10, bd=7,
                 fg='white', font=('Helvetica', 12, 'bold'))
    edit_delete_button.place(x=550, y=20)

    # Dropdown menu for selecting note status
    status_label = Label(root, text='Select Note Status:', bg='#145660', fg='white', font=('Helvetica', '15', 'bold'))
    status_label.place(x=330, y=167)

    status_values = ['Pending', 'Completed']
    status_combobox = ttk.Combobox(root, values=status_values, state='readonly', font=('Helvetica', '15'))
    status_combobox.place(x=530, y=167)

    # Search button
    search_button = Button(root, text="Search By Note Status", bg="red", padx=25, pady=5, bd=5, fg='white',
                           font=('Helvetica', '10', 'bold'), command=lambda: search_status(status_combobox, root))
    search_button.place(x=780, y=160)

    # View Notes button
    view_button = Button(root, text="View Notes", bg="red", padx=55, pady=10, bd=7, fg='white', font=('Helvetica', '12', 'bold'),
                command=view_all_notes)
    view_button.place(x=830, y=20)

    # Visualize notes
    note_visualization.visualize_notes_status(root)

    # Exit button
    exit_fbutton= Button(root, text="Exit", command=root.destroy, bg="red", fg='white', padx=50, pady=10, bd='5',
                   font=('Helvetica', '10', 'bold'))
    exit_fbutton.place(x=710, y=750)
