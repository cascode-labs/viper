from .project import project

class library():
   def __init__(self, name: str, project_in: project) -> None:
      self.project = project_in
