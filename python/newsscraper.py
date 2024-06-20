import requests
from requests_html import HTMLSession

def fetch_news():
    """
    Fetches news articles from Google News.
    Returns a list of dictionaries with article details (title, channel, link).
    """
    session = HTMLSession()
    try:
        r = session.get('https://news.google.com')
        # Render and scroll (adjust sleep time and scrolldown as needed)
        r.html.render(sleep=1, scrolldown=5)
    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching page: {e}")
        return []
    except Exception as e:
        print(f"Error during rendering: {e}")
        return []

    articles = r.html.find('article')
    newslist = []

    for item in articles:
        try:
            lines = item.text.split('\n')
            # Ensure the length of lines is adequate
            if len(lines) > 2:
                title = lines[2]  
            else:
                title=lines[0]
            channel = lines[0] if len(lines) > 2 else "No Channel"
            context="No context" if len(lines)>2 else lines[1]
             # Find 'a' tag inside the current article item
            link = item.find('a', first=True)
            link_url = list(link.absolute_links)[0] if link else "No Link"
            newsarticle = {
                "title": title,
                "channel": channel,
                "link": link_url,
                "context":context
            }
            newslist.append(newsarticle)
        except AttributeError as e:
            print(f"AttributeError: {e}")
        except IndexError as e:
            print(f"IndexError: {e} - skipping an article.")
        except requests.exceptions.RequestException as ne:
            print(f"NetworkError: {ne}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        # Continue to the next article on any error
        continue  

    return newslist

if __name__ == "__main__":
    newslist = fetch_news()
    for news in newslist:
        print(news)
