from models.file_data import FileData
import time

TEST_PATH="/Users/aydanpirani/programming-stuff/yavcos/staging/test.txt"

class ConfigManager:
    tracked_files = {TEST_PATH: FileData(TEST_PATH, 1, "hi")}

    @staticmethod
    def get_tracked_files():
        return ConfigManager.tracked_files
    
    @staticmethod
    def track_file(filepath):
        print("tracking", filepath)
        ConfigManager.tracked_files[filepath] = FileData()
        print(ConfigManager.get_tracked_files())
    
    @staticmethod
    def touch_file(filepath, timestamp=time.time()):
        ConfigManager.tracked_files[filepath].last_accessed = timestamp