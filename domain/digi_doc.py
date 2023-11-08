from dataclasses import dataclass

@dataclass
class DigiDoc:
    path: str
    file_name: str
    content: str
    metadata: dict