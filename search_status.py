#importing required libraries and modules
import pymysql as pm
from tkinter import *
from tkinter import ttk, messagebox

# Function to perform search and display results in a new window
def search_status(status_combobox, root):
    """
    Function to search for notes based on selected status.

    Retrieves notes from the 'notes' table in the 'Notespro' database that match the selected status
    and displays them in a new window using a Treeview widget.
    """
    selected_status = status_combobox.get()

    # Check if a status is selected
    if not selected_status:
        messagebox.showerror("Input Error", "Please select a status to search for notes.")
        return

    try:
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        search_query = "SELECT * FROM notes WHERE status=%s"
        cursor.execute(search_query, (selected_status,))
        data = cursor.fetchall()

        # Create a new window for displaying search results
        result_window = Toplevel(root)
        result_window.title("Search Results")
        result_window.geometry("700x400")
        result_window.configure(bg='#145660')

        if not data:
            # Display message if no notes found
            no_results_label = Label(result_window, text="No notes found. Please add a note.",
                                     bg='#145660', fg='white', font=('Helvetica', 14, 'bold'))
            no_results_label.pack(pady=20)
        else:
            # Frame for Treeview
            result_frame = Frame(result_window, bg='#145660')
            result_frame.place(x=50, y=50, width=600, height=300)

            # Treeview for displaying search results
            tree = ttk.Treeview(result_frame, columns=('ID', 'Text', 'Status'), show='headings', selectmode='browse')
            tree.heading('ID', text='ID')
            tree.heading('Text', text='Text')
            tree.heading('Status', text='Status')
            tree.pack(fill='both', expand=True)

            # Style the Treeview widget to include borders
            style = ttk.Style()
            style.configure("Treeview", bordercolor="black", borderwidth=1, relief="solid", font=('Helvetica', 12))
            style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'))

            # Insert new data into treeview
            for row in data:
                tree.insert('', 'end', values=row)

        con.commit()
    except pm.DatabaseError as e:
        # Handle database errors
        if con:
            con.rollback()
        messagebox.showerror("Database Error", str(e))
    finally:
        # Close cursor and database connection
        cursor.close()
        con.close()
