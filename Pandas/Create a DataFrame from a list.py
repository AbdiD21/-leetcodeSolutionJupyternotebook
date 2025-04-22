
# Time complexity :  O(n)
# Space complexity: O(n)

import pandas as pd
from typing import List

def createDataframe(student_data):
    
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Example
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

df = createDataframe(student_data)
print(df)
