import wmi
import psutil
import time
import datetime as dt


c = wmi.WMI ()
name = 'rundll32.exe'
server_process = []

stop = False

def run():
    while not stop:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > 90:
            for process in c.Win32_Process(): 
                # server_process.append(process.name)
                if process.name == name:
                    process.Terminate()
                    print("""
                        ################################################################
                        -------------------Process terminated---------------------------
                        ################################################################
                    """)
            # server_process.sort()
            # print(server_process)
            # with open('process.txt', 'w') as f:
            #     for process in server_process:
            #         f.write(process + '\n')
        # stop = True
        now = dt.datetime.now()
        str_now = now.strftime("%d/%m/%Y %H:%M:%S")
        end = now + dt.timedelta(seconds=60)
        str_end = end.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Sleeping from {str_now} until {str_end}")
        print('If you want to close this program please press Ctrl + C')
        time.sleep(60)


if __name__ == '__main__':
    run()
