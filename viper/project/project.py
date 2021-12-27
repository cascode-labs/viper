import getpass
from pathlib import Path
from typing import List


class project():
   from .library import library
   
   def __init__(self, project_path: str) -> None:
      self.path = Path(project_path)
      if not self.path.is_dir():
         raise TypeError("Project path must be a directory!") 
      self.name = self.path.stem
      self.username = getpass.getuser()

   @classmethod
   def create(cls, project_path: str) -> None:
      path = Path(project_path)
      if not path.is_dir():
         raise TypeError("Project path must be a directory!") 
      path.mkdir()
      work_libs_path = path / "work_libs"
      work_libs_path.mkdir()
      envs_path = path / "envs"
      envs_path.mkdir()

   def _get_libraries(self):
      self.path /"libs"

   def _create_libraries(self) -> List[library]:
      from .library import library
      self.libs = library(f"{self.name}_work", self)
      user_lib = library(f"{self.name}_{self.username}", self)
      for 
      return [work_lib, user_lib]
