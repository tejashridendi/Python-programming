#Import required modules and libraries
import pymysql as pm
from tkinter import *
from tkinter import ttk, messagebox
import note_visualization

#Function  to perform edit and delete operations
def edit_delete(mainroot):
    """
    Opens a new window for editing, deleting, and managing notes.

    Args:
    - mainroot (Tk): The main Tkinter root window object from which this window is spawned.
    """
    root = Toplevel(mainroot)
    root.title("Edit Note")
    root.geometry("980x400")
    root.configure(bg='#145660')

    def populate_treeview():
        """
        Populates the Treeview widget with notes from the database.
        Clears existing rows and displays new data.
        """
        try:
            # Connect to the database
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            cursor.execute("SELECT * FROM notes")
            rows = cursor.fetchall()

            # Clear existing rows in the Treeview
            for row in tree.get_children():
                tree.delete(row)

            if rows:
                # Hide the no notes message if data is available
                message_label.grid_remove()
                # Insert new rows into the Treeview
                for i, row in enumerate(rows):
                    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                    tree.insert('', 'end', values=row, tags=(tag,))
            else:
                # Show the no notes message if no data is available
                message_label.grid()

            con.commit()
        except pm.DatabaseError as e:
            if con:
                con.rollback()
            # Display an error message if there's a database error
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            con.close()

    def update_row():
        """
        Opens a new window to edit the selected note from the Treeview.
        """
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a note to edit.")
            return

        item_values = tree.item(selected_item)['values']
        note_id = item_values[0]

        # Create a new window for editing the selected note
        edit_window = Toplevel()
        edit_window.title("Edit Note")
        edit_window.geometry("800x450")
        edit_window.configure(bg='#145660')

        # Note ID
        Label(edit_window, text="Note ID:", bg='#636466', fg="white", font=('Helvetica', '18', 'italic')).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=20,
                                                                                                               pady=10,
                                                                                                               sticky='w')
        Label(edit_window, text=note_id, bg='#636466', fg="white", font=('Helvetica', '18')).grid(row=0, column=1,
                                                                                                  padx=20, pady=10,
                                                                                                  sticky='w')

        # Note Text
        Label(edit_window, text="Note Text:", bg='#636466', fg="white", font=('Helvetica', '18', 'italic')).grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=20,
                                                                                                                 pady=10,
                                                                                                                 sticky='w')
        txt_edit = Text(edit_window, height=10, width=60, font=('Helvetica', '15'))
        txt_edit.insert(END, item_values[1])
        txt_edit.grid(row=1, column=1, padx=20, pady=10, sticky='w')

        # Note Status
        Label(edit_window, text="Status:", bg='#636466', fg="white", font=('Helvetica', '18', 'italic')).grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=20,
                                                                                                              pady=10,
                                                                                                              sticky='w')
        status_values = ['Pending', 'Completed']
        status_combobox = ttk.Combobox(edit_window, values=status_values, state='readonly', font=('Helvetica', '15'))
        status_combobox.set(item_values[2])
        status_combobox.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        def save_changes():
            """
            Saves changes made to the note and updates the Treeview and chart.
            """
            new_text = txt_edit.get("1.0", "end-1c")
            new_status = status_combobox.get()

            try:
                # Connect to the database
                con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
                cursor = con.cursor()
                update_query = "UPDATE notes SET text=%s, status=%s WHERE id=%s"
                cursor.execute(update_query, (new_text, new_status, note_id))
                con.commit()
                messagebox.showinfo("Success", "Note updated successfully.")
                edit_window.destroy()
                populate_treeview()
                # Update the chart after saving changes
                note_visualization.visualize_notes_status(mainroot)
            except pm.DatabaseError as e:
                if con:
                    con.rollback()
                # Display an error message if there's a database error
                messagebox.showerror("Database Error", str(e))
            finally:
                cursor.close()
                con.close()

        # Save Changes Button
        Button(edit_window, text="Save Changes", command=save_changes, bg="red", padx=10, pady=5, fg='white',
               font=('Helvetica', '14')).grid(row=3, column=1, padx=20, pady=20, sticky='w')

    def delete_row():
        """
        Deletes the selected note from the Treeview and database after confirmation.
        """
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a note to delete.")
            return

        item_values = tree.item(selected_item)['values']
        note_id = item_values[0]

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this note?")
        if not confirm:
            return

        try:
            # Connect to the database
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            delete_query = "DELETE FROM notes WHERE id=%s"
            cursor.execute(delete_query, (note_id,))
            con.commit()
            messagebox.showinfo("Success", "Note deleted successfully.")
            populate_treeview()
            # Update the chart after deletion
            note_visualization.visualize_notes_status(mainroot)
        except pm.DatabaseError as e:
            if con:
                con.rollback()
            # Display an error message if there's a database error
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            con.close()

    def delete_all_rows():
        """
        Deletes all notes from the Treeview and database after confirmation.
        """
        if not tree.get_children():
            messagebox.showerror("Error", "No note available to delete.")
            return

        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all notes?")
        if not confirm:
            return

        try:
            # Connect to the database
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            delete_query = "DELETE FROM notes"
            cursor.execute(delete_query)
            con.commit()
            messagebox.showinfo("Success", "All notes deleted successfully.")
            populate_treeview()
            # Update the chart after deletion
            note_visualization.visualize_notes_status(mainroot)
        except pm.DatabaseError as e:
            if con:
                con.rollback()
            # Display an error message if there's a database error
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            con.close()

    # Create and configure the Treeview widget
    tree = ttk.Treeview(root, columns=('ID', 'Text', 'Status'), show='headings', height=20)
    tree.heading('ID', text='Note ID')
    tree.heading('Text', text='Note Text')
    tree.heading('Status', text='Status')
    tree.column("ID", width=100)
    tree.column("Text", width=600)
    tree.column("Status", width=100)
    tree.grid(row=1, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')

    tree.tag_configure('evenrow', background='#E8E8E8')
    tree.tag_configure('oddrow', background='#DFDFDF')

    # Label for displaying no notes message
    message_label = Label(root, text="There is no note to edit or delete.", bg='#145660', fg='white',
                          font=('Helvetica', '18', 'italic'))
    message_label.grid(row=1, column=0, padx=20, pady=20, columnspan=4)
    message_label.grid_remove()

    # Buttons for interacting with notes
    Button(root, text="Refresh Notes", command=populate_treeview, bg="red", padx=20, pady=10, fg='white',
           font=('Helvetica', '14')).grid(row=0, column=0, padx=20, pady=20, sticky='w')
    Button(root, text="Edit Selected Note", command=update_row, bg="red", padx=20, pady=10, fg='white',
           font=('Helvetica', '14')).grid(row=0, column=1, padx=20, pady=20, sticky='e')
    Button(root, text="Delete Selected Note", command=delete_row, bg="red", padx=20, pady=10, fg='white',
           font=('Helvetica', '14')).grid(row=0, column=2, padx=20, pady=20, sticky='e')
    Button(root, text="Delete All Notes", command=delete_all_rows, bg="red", padx=20, pady=10, fg='white',
           font=('Helvetica', '14')).grid(row=0, column=3, padx=20, pady=20, sticky='e')

    # Populate the Treeview with initial data
    populate_treeview()
    root.mainloop()
