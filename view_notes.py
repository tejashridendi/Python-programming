# Import required modules and libraries
from tkinter import *
from tkinter import ttk
import pymysql as pm

def view_all_notes():
    """
    Function to create a new window and display all notes from the MySQL database
    in a table with sorting functionality. If no notes are available, a message
    is displayed in the center of the window.
    """
    # Create new window
    view_notes_window = Tk()
    view_notes_window.title("View All Notes")
    view_notes_window.geometry("700x400")
    view_notes_window.configure(bg='#145660')

    # Create a frame for the table with border
    frame = Frame(view_notes_window, bd=1, relief='solid')
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Create a Treeview widget for displaying notes
    tree = ttk.Treeview(frame, columns=("ID", "Note", "Status"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Note", text="Note")
    tree.heading("Status", text="Status")

    def fetch_and_display_notes():
        """
        Fetch notes from the MySQL database and populate the Treeview.
        If no notes are available, display a centered message in the frame.
        """
        # Clear existing data in the Treeview
        for child in tree.get_children():
            tree.delete(child)

        # Connect to MySQL database
        conn = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = conn.cursor()

        # Fetch notes from the database
        cursor.execute("SELECT id, text, status FROM notes")
        rows = cursor.fetchall()

        conn.close()

        # If no rows fetched, display a centered message in the frame
        if not rows:
            no_notes_label = Label(frame, text="There are no notes to display", bg='#145660', fg='white',
                                   font=('Helvetica', 14))
            no_notes_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            # If there are notes, remove the label if it exists
            for widget in frame.winfo_children():
                if isinstance(widget, Label) and widget.cget("text") == "There are no notes to display":
                    widget.place_forget()

            # Insert fetched data into the Treeview
            for row in rows:
                tree.insert("", "end", values=row)

    # Initial fetch and display of notes
    fetch_and_display_notes()

    def sortby_column(col):
        """
        Sort the Treeview by a given column.
        """
        # Get current sort order
        current_sort_order = tree.heading(col, "text")[-1]
        reverse = current_sort_order == '▲'

        # Sort rows
        items = [(tree.set(child, col), child) for child in tree.get_children("")]
        items.sort(reverse=reverse)
        for index, (val, child) in enumerate(items):
            tree.move(child, "", index)

        # Reset column headers
        for col_id in tree["columns"]:
            tree.heading(col_id, text=col_id)

        # Set sorting arrow
        if reverse:
            tree.heading(col, text=col + " ▼")
        else:
            tree.heading(col, text=col + " ▲")

    # Bind column headers to sorting function
    for col in ["ID", "Note", "Status"]:
        tree.heading(col, text=col + " ▲", command=lambda c=col: sortby_column(c))

    # Add borders around the table and configure style
    style = ttk.Style()
    style.configure("Treeview", font=('Helvetica', 12), borderwidth=2, relief="solid")

    # Pack the table and add scrollbar if needed
    tree.pack(expand=True, fill=BOTH)

    # Run the main loop
    view_notes_window.mainloop()


