import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views['author_id'] == views['viewer_id']]
    result = filtered[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'})
    result = result.sort_values('id').reset_index(drop=True)
    return result
