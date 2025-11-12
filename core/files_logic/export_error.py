import pandas as pd
from tkinter import filedialog
from core import db_communication

#export data about error
def exportError(error):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM failure WHERE code = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(error, ))
    db_communication.close_connection(connection[1])
    
    connection = db_communication.connect_to_database()
    sql2= "SELECT * FROM faildata WHERE failCode = %s"
    df2 = pd.read_sql(sql2, connection[1], params = (error, ))
    db_communication.close_connection(connection[1])
    
    fn=df2["FN"]
    fn_values = tuple(fn)
    
    connection = db_communication.connect_to_database()
    sql3 = "SELECT FN, GPSdt, fd FROM basics WHERE FN IN {}".format(str(fn_values))
    df3 = pd.read_sql(sql3, connection[1])
    db_communication.close_connection(connection[1])
    
    
    folder_selected = filedialog.askdirectory()
    merged_df = pd.merge(df2, df3, on='FN', how='inner')
    

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/error{error}allAffectedFlights.csv"
        merged_df.to_csv(csv_file_path, index=False)
        print(f"Data exported to: {csv_file_path}")
        
        #maybe one day make a formatted csv file