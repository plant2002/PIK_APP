import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#failures
#for drop-down menu of which codes you can check over (which ones are in database at the moment)
def errors_code_selection():
    connection = db_communication.connect_to_database()
    sql1 = "SELECT code, name FROM failure"
    df1 = pd.read_sql(sql1, connection[1])
    db_communication.close_connection(connection[1])
    
    option_mapping = df1.set_index('name')['code'].to_dict()
    return option_mapping