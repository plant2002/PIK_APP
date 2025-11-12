import pandas as pd
from tkinter import filedialog
from core import db_communication

#export data about flights between dates
def exportFlightDateFT(date_to, date_from):
    connection = db_communication.connect_to_database()
    sql1 = "SELECT * FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    df1 = pd.read_sql(sql1, connection[1], params=(date_to, date_from))
    db_communication.close_connection(connection[1])
    
    fn=df1["FN"]

    df1['VEMDfd'] = pd.to_timedelta(df1['VEMDfd']).astype(str)
    df1['GPSfd'] = pd.to_timedelta(df1['GPSfd']).astype(str)
    df1['fd'] = pd.to_timedelta(df1['fd']).astype(str)
    
    
    df1['VEMDfd'] = df1['VEMDfd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))
    df1['GPSfd'] = df1['GPSfd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))
    df1['fd'] = df1['fd'].apply(lambda x: ':'.join(str(x).split()[-1].split(':')))

    
    connection = db_communication.connect_to_database()
    sql2 = f"SELECT * FROM faildata WHERE FN IN ({', '.join(map(str, fn))})"
    df2 = pd.read_sql(sql2, connection[1])
    db_communication.close_connection(connection[1])
    
    code = df2["failCode"]
    
    connection = db_communication.connect_to_database()
    sql3 = f"SELECT * FROM failure WHERE code IN ({', '.join(map(str, code))})"
    df3 = pd.read_sql(sql3, connection[1])
    db_communication.close_connection(connection[1])
    
    result_df1 = pd.merge(df1, df2, on='FN', how='left')
    result_df = pd.merge(result_df1, df3, left_on='failCode', right_on='code', how='left')
    
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        # Create CSV file
        csv_file_path = f"{folder_selected}/date{date_from}to{date_to}.csv"
        result_df.to_csv(csv_file_path, index= False)

        print(f"Data exported to: {csv_file_path}")