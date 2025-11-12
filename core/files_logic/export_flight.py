import pandas as pd
from tkinter import filedialog
from core import db_communication

#export data about flight (number)
def exportFlight(fn_spec):
    
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM basics WHERE FN = %s"
    df1 = pd.read_sql(sql1, connection[1], params=(fn_spec, ))
    db_communication.close_connection(connection[1])

    connection = db_communication.connect_to_database()
    sql2 = "SELECT * FROM faildata WHERE FN = %s"
    df2 = pd.read_sql(sql2, connection[1], params=(fn_spec, ))
    db_communication.close_connection(connection[1])
    
    if not df2.empty and 'failCode' in df2.columns:
        code = int(df2["failCode"].iloc[0])
        
        connection = db_communication.connect_to_database()
        sql3 = "SELECT * FROM failure WHERE code = %s"
        df3 = pd.read_sql(sql3, connection[1], params=(code, ))
        db_communication.close_connection(connection[1])

        result_df1 = pd.merge(df1, df2, on='FN', how='left')
        result_df = pd.merge(result_df1, df3, left_on='failCode', right_on='code', how='left')
    else:
        result_df = pd.merge(df1, df2, on='FN', how='left')
    
    # Ask user for the destination folder
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/flight{fn_spec}.csv"
        result_df.to_csv(csv_file_path, index=False)

        print(f"Data exported to: {csv_file_path}")