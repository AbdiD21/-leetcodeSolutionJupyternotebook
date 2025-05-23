import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Rename the columns
    students = students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })
    return students

# Time Complexity: O(1)
# Space Complexity: O(1)