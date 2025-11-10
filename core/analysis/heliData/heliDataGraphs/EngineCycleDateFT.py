import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#maximum engineCyc values per day (n1 & n2)
def EngineCycleDateFT(frame, date_from, date_to):
    connection = db_communication.connect_to_database()

    sql = "SELECT FN, n1cycles, n2cycles, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    df['GPSdt'] = pd.to_datetime(df['GPSdt'])  # Convert GPSdt to datetime
    df['date'] = df['GPSdt'].dt.date
    existing_dates = df['date'].unique()

    # Group by date and find the maximum 'n1cycles' for each date
    df_max = df.groupby('date').agg({'n1cycles': 'max', 'n2cycles': 'max'}).reset_index()
    df_max = df_max[df_max['date'].isin(existing_dates)]

    # Plotting the line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_max['date'], df_max['n1cycles'], marker='o', linestyle='-', label='n1cycles')
    for i, txt in enumerate(df_max['n1cycles']):
        ax.annotate(txt, (df_max['date'].iloc[i], df_max['n1cycles'].iloc[i]), textcoords="offset points", xytext=(10, 5), ha='center')
    ax.plot(df_max['date'], df_max['n2cycles'], marker='o', linestyle='-', label='n2cycles')
    for i, txt in enumerate(df_max['n2cycles']):
        ax.annotate(txt, (df_max['date'].iloc[i], df_max['n2cycles'].iloc[i]), textcoords="offset points", xytext=(10, -10), ha='center')

    # Formatting the plot
    ax.set_xlabel('Date')
    ax.set_ylabel('Maximum Cycles')
    ax.set_title('Maximum Cycles over Dates')

    # Set x-axis ticks & grid only for existing dates
    ax.set_xticks(existing_dates)
    ax.tick_params(axis='x', rotation=45, ha='right')
    ax.grid(True, linestyle='--', which='major', color='grey', alpha=0.5, axis='x')

    ax.legend()  # Show legend

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])