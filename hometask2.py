import os
from datetime import datetime

def write_log(text, file_name=None, folder_name=None):

    current_date = datetime.now().strftime('%Y-%m-%d')

    if file_name is None:
        file_name = f"{current_date}.txt"
    if folder_name is None:
        folder_name = current_date.split('-')[0] 

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    
    file_path = os.path.join(folder_name, file_name)

    with open(file_path, 'a') as file:
        file.write(text + '\n')
    
    print(f"Log written to {file_path}")


write_log("This is a log message.")
