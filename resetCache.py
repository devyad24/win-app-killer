import win32com.client
import pandas as pd
from datetime import datetime, date

df = pd.read_csv("appMap.csv")
apps = df['name'].values
fields = ['name','curr_run_time_mins','threshold_time_mins','kill_process']

TASK_ENUM_HIDDEN = 1
scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()

folders = [scheduler.GetFolder('\\')]
while folders:
    folder = folders.pop(0)
    folders += list(folder.GetFolders(0)) 
    tasks = list(folder.GetTasks(TASK_ENUM_HIDDEN))
    for task in tasks:
        if task.Name == 'appkiller' and task.LastRunTime.date() != datetime.now().date():
            for i, rows in df.iterrows():
                df.at[i, 'curr_run_time_mins'] = 0
                df.at[i, 'kill_process'] = 0

df.to_csv('appMap.csv', columns=fields, index=False)