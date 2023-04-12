from pathlib import Path
import re
import copy


class NgspiceResultReader:
    @staticmethod
    def read_raw_file(filepath: Path):
        data = Path(filepath).read_text()
        ret = {}
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

        # vars
        vars_text = data_parsed.group('vars')
        pattern = (r"\s*(?P<idx>\d+)\s+" r"(?P<name>\S+)\s+" r"(?P<type>.*)\s*")
        m_vars = re.finditer(pattern, vars_text)
        variables = {}
        for i in m_vars:
            variables[i.group("name")] = i.groupdict()
            

        values_text = data_parsed.group("values")
        pattern = (r"^\s*(?P<idx>\d+)\s+" r"(?P<values>\S+(?:\n\s*\S+)*)$")
        values_iter = re.finditer(pattern, values_text, re.MULTILINE)
        values = {}
        for point,value_groups in enumerate(values_iter):
            value_data = value_groups.group("values").split()
            for name,value in zip(variables.keys(),value_data):
                if name not in values.keys():
                    values[name] = []
                values[name].append(float(value))



        return {
            "title": data_parsed.group("title"),
            "date": data_parsed.group("date"),
            "variable count": int(data_parsed.group("no_vars")),
            "point count": int(data_parsed.group("no_points")),
            "outputs": variables,
            "values": values,
        }
    
    # def dict() -> Dict[]