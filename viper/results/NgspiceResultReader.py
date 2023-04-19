from pathlib import Path
import re
import copy

from viper.simulators.SimResult import SimResult
from viper.results.Dataset import Dataset

class NgspiceResultReader:

    @staticmethod
    def read_result(sim_result: SimResult) -> Dataset:
        self.read_raw_file(sim_result.raw_output_filepath)

    @classmethod
    def read_raw_file(cls, filepath: Path) -> dict:
        data = Path(filepath).read_text()
        pattern = (
                r"^Title:\s*(?P<title>.*)\s*"
                r"^Date:\s*(?P<date>\w.*?\w)\s*"
                r"Plotname:\s*(?P<plotname>\w.*?\w)\s*"
                r"Flags:\s*(?P<flags>\w.*?\w)\s*"
                r"No\. Variables:\s*(?P<no_vars>\d+)\s*"
                r"No\. Points:\s*(?P<no_points>\d+)\s*"
                r"Variables:\s*$(?P<vars>.*)^"
                r"Values:(?P<values>.*)")
        data_parsed = re.search(pattern, data, re.MULTILINE | re.DOTALL)

        variables = cls._read_raw_variables(data_parsed.group('vars'))
        values = cls._read_raw_ascii_values(data_parsed.group("values"))
        
        return {
            "title": data_parsed.group("title"),
            "date": data_parsed.group("date"),
            "variable count": int(data_parsed.group("no_vars")),
            "point count": int(data_parsed.group("no_points")),
            "outputs": variables,
            "values": values,
        }
    
    @staticmethod
    def _read_raw_variables(variables_section: str) -> dict:
        pattern = (r"\s*(?P<idx>\d+)\s+" r"(?P<name>\S+)\s+" r"(?P<type>.*)\s*")
        m_vars = re.finditer(pattern, variables_section)
        variables = {}
        for i in m_vars:
            variables[i.group("name")] = i.groupdict()
        return variables
    
    @staticmethod
    def _read_raw_ascii_values(values_section: str, variables: dict) -> dict:
        pattern = (r"^\s*(?P<idx>\d+)\s+" r"(?P<values>\S+(?:\n\s*\S+)*)$")
        values_iter = re.finditer(pattern, values_section, re.MULTILINE)
        values = {}
        for point,value_groups in enumerate(values_iter):
            value_data = value_groups.group("values").split()
            for name,value in zip(variables.keys(),value_data):
                if name not in values.keys():
                    values[name] = []
                values[name].append(float(value))
