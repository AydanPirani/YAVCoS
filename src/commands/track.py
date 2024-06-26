import os
from utilities.config_manager import ConfigManager

def execute(args):
    print(args)
    ConfigManager.track_file(os.path.abspath(args.path))
    print("Track command executed")

def validate(input):
    return os.path.exists(input)