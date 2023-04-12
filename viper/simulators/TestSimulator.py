from pathlib import Path
from importlib.resources import Package, files
import toml

from viper.schematics.XschemSchematic import XschemSchematic
from viper.simulators.ngspice import NgSpice
from viper.typing import PathLike
from viper.simulators.SimResult import SimResult


class TestSimulator:

    DEFAULT_RESULT_DIR = Path("/tmp/simulation")

    def __init__(self, schematic_filepath: PathLike, 
                 test_dirpath: PathLike) -> None:
        self.schematic_filepath = Path(schematic_filepath)
        self.test_dirpath = Path(test_dirpath)
        self._result_dirpath = None

    def netlist(self) -> Path:
        if not self.netlist_dirpath.exists():
            self.netlist_dirpath.mkdir(755,parents=True, exist_ok=True)
        self.schematic.netlist()
        return self.netlist_filepath

    def simulate(self) -> SimResult:
        if not self.result_dirpath.exists():
            self.result_dirpath.mkdir(755,parents=True, exist_ok=True)
        self.write_result_config()
        return self.simulator.simulate()

    def write_result_config(self):
        config = {
            "name": self.name,
            "schematic_filepath": self.schematic_filepath,
            "netlist_filepath": self.netlist_filepath,
        }
        with open(self.result_config_filepath,"w") as config_file:
            toml.dump(config, config_file)

    @property
    def simulator(self) -> NgSpice:
        return NgSpice(netlist_filepath=self.netlist_filepath,
                       result_dirpath=self.result_dirpath)
    
    @classmethod
    def run(cls, schematic_filepath: PathLike, 
            test_dirpath: PathLike) -> SimResult:
        runner = cls(schematic_filepath, test_dirpath)
        runner.netlist()
        result = runner.simulate()
        return result

    def run_package_tests(cls, schematic_filepath: PathLike, 
                          package: Package):
        with files(package) as package_files:
            for file in package_files:
                if file.isdir():
                    cls.run(schematic_filepath=schematic_filepath,
                            test_dirpath=file)

    @property
    def netlist_dirpath(self) -> Path:
        return self.result_dirpath / "netlist"
    
    @property
    def result_dirpath(self) -> Path:
        if self._result_dirpath is None:
            self._result_dirpath = self.DEFAULT_RESULT_DIR \
                                        / self.schematic_filepath.stem
        return self._result_dirpath

    @property
    def schematic(self):
        return XschemSchematic(
            path=self.schematic_filepath,
            netlist_dirpath=self.netlist_dirpath
            )
    
    @property
    def netlist_filepath(self) -> Path:
        return self.schematic.netlist_filepath

    @property
    def result_config_filepath(self) -> Path:
        return self.result_dirpath / "result.toml"
