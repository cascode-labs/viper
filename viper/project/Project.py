from pathlib import Path
from typing import Optional


class Project():
    def __init__(self, name: str, path: Optional[Path]) -> None:
        self._name = name
        self._path = path
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def path(self) -> Optional[Path]:
        return self._path
    