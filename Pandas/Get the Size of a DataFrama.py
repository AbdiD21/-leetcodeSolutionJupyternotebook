import pandas as pd
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

# Time complexity: O(1)
# Space complexity: O(1)

'''
import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows, cols = players.shape
    return [rows, cols]

# Time complexity: O(1)
# Space complexity: O(1)
'''