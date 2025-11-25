from newspaper import Article

def extract_news(url):
    article = Article(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
    article.download()
    article.parse()
    return article.title

# Example usage
url = "https://www.geosuper.tv/latest/50482-shadab-khan-ali-raza-feature-in-practice-match-after-rehabilitation"  # replace with any news URL
news = extract_news(url)

# print("Headline:", news["headline"])
# print("\nArticle Text:\n", news["text"])
