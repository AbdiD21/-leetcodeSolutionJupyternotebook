import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


# The time complexity is O(1) because the code accesses and modifies a single column in the DataFrame, regardless of the number of rows.

# The space complexity is O(1) as well because the conversion is done in place, without requiring extra space proportional to the input size.