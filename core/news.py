from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="78af72c8ce374b948228795b44ef6062")

def get_news():
    try:
        top_headlines = newsapi.get_top_headlines(language='en', country='in')
        articles = top_headlines.get('articles', [])
        if not articles:
            return "No news found right now."

        headlines = [article['title'] for article in articles[:5]]
        return "Here are the top headlines:\n" + "\n".join(headlines)
    except Exception as e:
        return f"Error fetching news: {str(e)}"
