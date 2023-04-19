from pathlib import Path
from typing import List
from viper.typing import PathLike
from viper.simulators.TestSimulator import TestSimulator
from viper.simulators.SimResult import SimResult

class ProjectSimulator:
    def __init__(self, project_dirpath: PathLike):
        self.project_dirpath = Path(project_dirpath)

    def run(self, schematic_path: PathLike) -> List[SimResult]:
        results = []
        for test_dirpath in self.test_dirpaths():
            test_simulator = TestSimulator(schematic_filepath=schematic_path,
                                           test_dirpath=test_dirpath)
            results.append(test_simulator.simulate())
        return results
    
    def test_dirpaths(self) -> List[Path]:
        test_dirpaths = []
        for file in self.tests_dirpath().iterdir():
            if file.is_dir():
                test_dirpaths.append(file)
        return test_dirpaths
    
    @property
    def tests_dirpath(self):
        return self.project_dirpath / "tests"