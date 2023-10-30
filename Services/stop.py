import os 
import subprocess
def stop():
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            db_directory = os.path.join(script_directory.replace("Services", "db"))
            subprocess.run(f'cd {db_directory} && docker-compose down', shell=True, check=True, universal_newlines=True)
            print("GPM is currently down, To bring it back up, use 'gpm start' .")
        except Exception as e:
              print(f"Error in Stop Services: Please Review Services/stop: {e}")