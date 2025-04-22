import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
# Time complexity: O(1)
# Space complexity: O(1)