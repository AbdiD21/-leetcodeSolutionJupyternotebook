import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df = students.dropna(subset=['name'])
    return df

# Time complexity 
# O(n) where n is the number of rows in the DataFrame
# Space complexity
# O(1) since we are not using any extra space that grows with the input size