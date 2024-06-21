import sys
import os
def exiting(exit_button):
    def exit():
        sys.exit()
    exit_button.configure(command = exit)      
def restarting(restart_button):
    def restart_game():
        os.system("python Layout.py")
    restart_button['command'] = restart_game
    return
