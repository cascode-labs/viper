import datetime
from pandas import DataFrame

class TestDataset:
    def __init__(self, name: str, date: datetime.date, 
                 outputs: DataFrame, values: DataFrame) -> None:
        self.name = name
        self.date = date
        self.outputs = outputs
        self.values = values

    def __str__(self) -> str:
        return (
            f"name: {self.name}\n"
            f"date: {self.date}\n"
            f"# of outputs: {len(self.outputs)}"
            )
