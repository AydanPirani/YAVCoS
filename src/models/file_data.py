from dataclasses import dataclass

@dataclass
class FileData:
    path: str
    last_accessed: int
    data: str
