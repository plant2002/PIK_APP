import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#def engineCyc_fn(fn_from, fn_to):
def FlightEngineCycleFT(frame, fn_from, fn_to):
    
    connection = db_communication.connect_to_database()

    # Assuming fn_from and fn_to are defined earlier in your code
    sql = "SELECT FN, n1cycles, n2cycles FROM basics WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))

    # Plot the bar chart using Pandas
    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot(kind='bar', x='FN', y=['n1cycles', 'n2cycles'], width=0.8, position=0.5, ax=ax)

    # Set labels and title
    ax.set_xlabel('Flight Numbers')
    ax.set_ylabel('Cycles')
    ax.set_title('Engine cycles on specific flights')

    plt.xticks(rotation=360, ha='right')

    # Display actual numbers on top of the bars with float formatting
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # Set y-axis ticks as floats
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

    # Close the database connection
    db_communication.close_connection(connection[1])