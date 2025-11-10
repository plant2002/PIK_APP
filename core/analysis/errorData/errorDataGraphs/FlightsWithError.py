import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#all flights with specific error (chosen with errors_code_selection drop-down menu) and their specs
#still have to figure out how to connect this with my graphs
def FLightsWithError(code):
    #all rows with error code same as input, FN to connect to table basics
    connection = db_communication.connect_to_database()
    sql1 = "SELECT FN, failCode FROM faildata WHERE failCode = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(code, ))
    db_communication.close_connection(connection[1])
    
    #number of rows with this code error
    number_of_flights=df1.shape[0]
    
    #information about flights from table basics that showed up in previous connection 
    connection = db_communication.connect_to_database()
    sql2 = f"SELECT FN, GPSdt, fd FROM basics WHERE FN IN ({', '.join(map(str, df1['FN']))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    
    #information about the flight from table failData via code and FN
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT * FROM faildata WHERE FN IN ({', '.join(map(str, df1['FN']))}) AND failCode = %s"
    df3 = pd.read_sql(sql3, connection[1], params=(code, ))
    db_communication.close_connection(connection[1])
    
    #merged_df = pd.merge(df2, df3, on='FN', how='inner')
    return df2