from importlib.resources import files
from pathlib import Path
from pytest import fixture
import tests.results
from viper.results.NgspiceResultReader import NgspiceResultReader

@fixture
def dc_raw_filepath():
    with files(tests.results) as filepath:
        return Path(filepath) / "bandgap_1v_v01_dcop_testbench.raw"

def test_read_raw_file(dc_raw_filepath: Path):
    result = NgspiceResultReader.read_raw_file(dc_raw_filepath)
    assert result.title == ""

if __name__ == "__main__":
    test_read_raw_file(dc_raw_filepath())