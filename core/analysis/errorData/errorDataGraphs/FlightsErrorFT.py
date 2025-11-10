#TF - to/from
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#error occurrences in flight from fn_from to fn_to
def FLightsErrorFT(frame, fn_from, fn_to):
    connection = db_communication.connect_to_database()

    all_flight_numbers = pd.DataFrame({'FN': range(int(fn_from), int(fn_to)+1)})

    # Fetch data from the database for the specified flight_number range
    sql = "SELECT FN, occr FROM faildata WHERE FN BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(fn_from, fn_to))

    # Merge the data with all_flight_numbers to fill missing flight_numbers with 0 occurrences
    if df.empty:
        merged_df = all_flight_numbers.assign(occr=0)
    else:
        # Merge the data with all_flight_numbers to fill missing flight_numbers with 0 occurrences
        merged_df = all_flight_numbers.merge(df, on='FN', how='left').fillna(0)

    # Plotting the graph with formatting adjustments
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(merged_df['FN'], merged_df['occr'])
    ax.set_xlabel('Flight Number (FN)')
    ax.set_ylabel('Number of Occurrences (occr)')
    ax.set_title('Occurrences of Errors per Flight Number')

    # Format y-axis to display only integer values
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Set x-axis ticks for all flight numbers
    ax.set_xticks(merged_df['FN'])
    ax.tick_params(axis='x', rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])