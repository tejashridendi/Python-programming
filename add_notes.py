#Import required modules and libraries
import pymysql as pm
from tkinter import *
from tkinter import ttk, messagebox
import note_visualization


# Function to add a new note
def add_note(root):
    """
    Function to open a dialog box for adding a new note.

    This function creates a dialog box with a text area for entering note text and a button to save the note to the database.
    """

    # Function to handle saving the note
    def save_note():
        """
        Saves the entered note text to the database.

        Inserts the note text and a default status ('Pending') into the 'notes' table of the 'Notespro' database.
        """
        text = note_text.get("1.0", END).strip()
        status = "Pending"  # Default status is set to Pending

        if not text or text == "Please add a note here.":
            messagebox.showerror("Input Error", "Please enter note text.")
            return

        try:
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            insert_query = "INSERT INTO notes (text, status) VALUES (%s, %s)"
            cursor.execute(insert_query, (text, status))
            con.commit()
            messagebox.showinfo("Success", "Note added successfully.")
            # Clear the text area
            note_text.delete("1.0", END)
            note_text.insert("1.0", "Please add a note here.")  # Reset placeholder text
            # Update the chart
            note_visualization.visualize_notes_status(root)
        except pm.DatabaseError as e:
            if con:
                con.rollback()
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            con.close()
            add_note_dialog.destroy()

    # Function to handle focus in event
    def on_focus_in(event):
        """
        Clears the placeholder text when the text area gains focus.
        """
        if note_text.get("1.0", END).strip() == "Please add a note here.":
            note_text.delete("1.0", END)
            note_text.config(fg='black')

    # Function to handle focus out event
    def on_focus_out(event):
        """
        Restores the placeholder text if the text area is empty when it loses focus.
        """
        if not note_text.get("1.0", END).strip():
            note_text.insert("1.0", "Please add a note here.")
            note_text.config(fg='grey')

    # Create a dialog box for adding a new note
    add_note_dialog = Toplevel(root)
    add_note_dialog.title("Add Note")
    add_note_dialog.geometry("700x400")
    add_note_dialog.configure(bg='#145660')

    # Text area for note text
    note_label = Label(add_note_dialog, text='Enter Note Text:', bg='#145660', fg='white', font=('Helvetica', '15', 'bold'))
    note_label.pack(pady=5)

    note_text = Text(add_note_dialog, height=15, width=50, font=('Helvetica', '10', 'italic'), fg='grey')
    note_text.pack(pady=5)

    # Insert placeholder text into the text area
    note_text.insert("1.0", "Please add a note here.")
    note_text.bind("<FocusIn>", on_focus_in)
    note_text.bind("<FocusOut>", on_focus_out)

    # Save button
    save_button = Button(add_note_dialog, text="Save Note", bg="red", padx=25, pady=5, bd=5, fg='white', font=('Helvetica', '10', 'bold'), command=save_note)
    save_button.pack(pady=10)
