import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Filter for rows where both 'low_fats' and 'recyclable' are 'Y'
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    # Return only the 'product_id' column
    return result[['product_id']]

# Time Complexity: O(n), where n is the number of rows in the DataFrame.
# Space Complexity: The space complexity is O(k), where k is the number of rows that satisfy the filtering condition. 