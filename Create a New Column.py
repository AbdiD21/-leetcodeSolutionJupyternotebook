import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


# Time Complexity: O(n), where n is the number of rows in the DataFrame.

# Space Complexity: O(1). The operation is performed in place.