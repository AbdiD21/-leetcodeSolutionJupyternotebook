import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge customers with orders on customer id, keeping all customers
    merged = customers.merge(orders, left_on='id',
                             right_on='customerId', how='left')
    # Filter where there is no matching order (customerId is NaN)
    result = merged[merged['customerId'].isna()][['name']]
    # Rename column as required by output format
    result.columns = ['Customers']
    return result

# Time: O(n+m)

# Space: O(n+m)