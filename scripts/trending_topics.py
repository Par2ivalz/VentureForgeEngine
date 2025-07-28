"""
Fetch trending topics using Google Trends.

Requires:
    pip install pytrends
"""

from pytrends.request import TrendReq


def fetch_trending_topics(keywords, region="US"):
    """
    Fetches rising related queries for each keyword using Google Trends.

    Args:
        keywords (list): List of keywords to fetch trends for.
        region (str): Two-letter country code (default 'US').

    Returns:
        dict: Dictionary mapping keyword -> DataFrame of rising queries.
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_data = {}
    
    for kw in keywords:
        pytrends.build_payload([kw], cat=0, timeframe='now 7-d', geo=region)
        related = pytrends.related_queries()
        rising = related.get(kw, {}).get('rising', None)
        trending_data[kw] = rising
    
    return trending_data


if __name__ == "__main__":
    keywords = ['AI productivity', 'sustainability tips']
    topics = fetch_trending_topics(keywords)
    for kw, df in topics.items():
        print(f"Trending queries for {kw}:")
        if df is not None:
            print(df.head(10))
        else:
            print("No rising queries found.")
