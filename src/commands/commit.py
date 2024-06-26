from utilities.config_manager import ConfigManager
import os
import time
import difflib

def execute(args):
    for path, data in ConfigManager.tracked_files.items():
        if os.path.getmtime(path) > data.last_accessed:
            ConfigManager.touch_file(path)
            print("file changed since last access!")
            difftool = difflib.Differ()
            with open(path, "r") as f:
                diff = difftool.compare(data.data, f.read())
                for d in diff:
                    print(d)
            
        