import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#flying time per day and per flight number
def FlightTimeDate(frame, date):
    connection = db_communication.connect_to_database()
    sql = "SELECT FN, fd FROM basics WHERE DATE(GPSdt) = %s"
    
    df = pd.read_sql(sql, connection[1], params=(date,))
    
    df['fd_minutes'] = df['fd'].dt.total_seconds() / 60
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(df['FN'], df['fd_minutes'], color='blue')
    ax.set_title(f'Flight Time per flight on {date}')
    ax.set_xlabel('Flight Number')
    ax.set_ylabel('Flight Time (minutes)')

    # Round FN values and set them as x-axis ticks
    ax.set_xticks(df['FN'].round())
    ax.set_xticklabels(df['FN'].round())

    # Add fd_minutes values on top of each bar
    for index, value in enumerate(df['fd_minutes']):
        ax.text(df['FN'].iloc[index], value + 0.1, str(round(value, 2)), ha='center', va='bottom')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])