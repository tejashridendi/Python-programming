#import required modules and libraries
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql as pm
from collections import Counter
from tkinter import *
#Variable declaration
no_notes_label = None
canvas = None

def visualize_notes_status(root):
    """
    Visualizes the count of 'completed' and 'pending' notes using Matplotlib in a Tkinter GUI.

    Args:
    - root (Tk): The Tkinter root window object where the visualization will be displayed.
    """
    global no_notes_label
    global canvas  # Track the canvas for removal

    # Clear previous chart and message if they exist
    if canvas:
        canvas.get_tk_widget().destroy()
    if no_notes_label:
        no_notes_label.grid_remove()

    try:
        # Connect to the database
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()

        # Execute SQL query to fetch status of notes
        cursor.execute("SELECT status FROM notes")
        rows = cursor.fetchall()

        # Count occurrences of each status using Counter
        status_counts = Counter(row[0].lower() for row in rows)

        # Extract counts of 'completed' and 'pending'
        completed_count = status_counts.get('completed', 0)
        pending_count = status_counts.get('pending', 0)

        if completed_count == 0 and pending_count == 0:
            # Display message if no notes are available
            no_notes_label = Label(root, text="No notes are available, please add one.", bg='#145660', fg='white',
                                   font=('Helvetica', 14, 'bold'))
            no_notes_label.place(x=440, y=350)
        else:
            # Plotting
            labels = ['Completed', 'Pending']
            counts = [completed_count, pending_count]

            fig, ax = plt.subplots(figsize=(6, 6))
            ax.bar(labels, counts, color=['green', 'yellow'])
            ax.set_xlabel('Note Status')
            ax.set_ylabel('Number of Notes')
            ax.set_title('Number of Completed and Pending Notes')

            # Ensure y-axis ticks are integers only
            ax.yaxis.get_major_locator().set_params(integer=True)

            # Remove grid lines
            ax.grid(False)

            # Adjust subplot to provide space for xlabel
            fig.subplots_adjust(bottom=0.2)

            # Convert plot to Tkinter compatible format
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()

            # Place canvas in a specific area on the root window
            canvas.get_tk_widget().place(x=440, y=350, width=400, height=300)

    except pm.DatabaseError as e:
        print(f"Database Error: {e}")
    finally:
        # Close cursor and database connection
        cursor.close()
        con.close()


