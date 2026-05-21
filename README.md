## Intro
- A simple python script that administers usage limits on apps. This can be usefull if you use apps like discord or play games and would like to set a usage limit on those apps.

## Setup
- Clone the repo first: `git clone git@github.com:devyad24/win-app-killer.git`
- Update the csv with the apps you want to manage your usage for. For example if you want to add Pubg, search for the process in task manager:
  <img width="1082" height="298" alt="image" src="https://github.com/user-attachments/assets/fb845eb8-b365-4655-8b94-14b9e8aafc93" />

  Check for the executable name by right clicking on properties:
  <img width="536" height="670" alt="image" src="https://github.com/user-attachments/assets/adbac473-d701-45a3-9eb8-00ac93343a57" />

  ---
  Add an entry in `appMap.csv` for setting usage limit for 1hr on pubg
  ```csv
  name,curr_run_time_mins,threshold_time_mins,kill_process
  TslGame.exe,0,60,0
  ```
  ---
- Open task scheduler and click on 'Create Task' on righthand side panel
- Set the following settings and save the task:
  <img width="790" height="600" alt="image" src="https://github.com/user-attachments/assets/8c213c8e-1e94-462b-9b84-c42e1670c7ff" />

  Here you can change how often you want the script to run, I have set it to run every 15mins in the screenshot:
  <img width="737" height="645" alt="image" src="https://github.com/user-attachments/assets/1b1e4a60-8ecd-4e6e-99a7-804c2d768d44" />
  
  Here's a little tricky part:
  <br>
  <img width="567" height="625" alt="image" src="https://github.com/user-attachments/assets/50fef6fe-f6dc-491a-9af6-b496e21f7e9f" />

  Generally to run a python script we just do `python <modulename.py>` but windows won't know the exact path of the python binary or the module.
  So you need to open command prompt and run `where python` and add its full path in the script option. Then add `appkiller.py` as argument,
  and then add the full path to `appkiller.py` as the 'Start in' option.

  ---

  <img width="790" height="600" alt="image" src="https://github.com/user-attachments/assets/be2896bd-a2ed-4077-aa40-e409272e4ed5" />
  After this save the task, if you get asked for creds then make sure you're running task scheduler as admin.

  ---

- Create another task to reset usage limits to 0 everyday. Use the `resetCache.py` script and schedule it for 00:00 recurring everyday like so:
  <br>
  <img width="737" height="645" alt="image" src="https://github.com/user-attachments/assets/bddb77a7-77f7-4340-ba5c-f677c5843d7e" />
  <img width="567" height="625" alt="image" src="https://github.com/user-attachments/assets/d6e18bf7-abb9-442c-aee0-5b5cea6c11bd" />


