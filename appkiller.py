import subprocess


import time
import psutil
import win32gui
import win32process
from datetime import datetime, date
import pytz
import pandas as pd
import csv
from tempfile import NamedTemporaryFile 
import shutil


curr_timezone = pytz.timezone('Asia/Kolkata')
df = pd.read_csv("appMap.csv")
apps = df['name'].values
fields = ['name','curr_run_time_mins','threshold_time_mins','kill_process']
for proc in psutil.process_iter():
    name = proc.name()

    if name in apps:
        app_entry = df.query('name == @name')
        if int(app_entry['kill_process'].item()) == 1:
            proc.kill()
            continue
        proc_time = proc.create_time()
        proc_dt = datetime.fromtimestamp(proc_time, tz=curr_timezone)
        runtime = (datetime.combine(date.min, datetime.now().time()) - datetime.combine(date.min, proc_dt.time())).seconds // 60
        df.loc[df['name'] == name, ['curr_run_time_mins']] = int(app_entry['curr_run_time_mins'].item()) + runtime
        if app_entry['curr_run_time_mins'].item() > app_entry['threshold_time_mins'].item():
            app_entry['kill_process'] = 1
            proc.kill()
            df.loc[df['name'] == name, ['kill_process']] = 1
df.to_csv('appMap.csv', columns=fields, index=False)