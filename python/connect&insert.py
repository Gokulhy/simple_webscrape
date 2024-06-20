import psycopg2
from newsscraper import fetch_news

# Fetch and process news articles
newslist = fetch_news()
print(f"Total articles fetched: {len(newslist)}")

# Define connection details
conn = psycopg2.connect(
    host="localhost",
    database="newsdb",
    user="postgres",
    password="Gokul@123"
)

# Create a cursor
cur = conn.cursor()

# Define function to insert data
def insert_news(title, channel, link):
    print(f"Inserting: Title={title}, Channel={channel}, Link={link}")
    query = """
    INSERT INTO googlenews (title, channel, link)
    VALUES (%s, %s, %s)
    """
    cur.execute(query, (title, channel, link))
    conn.commit()

# Define function to insert data
def insert_newscontext(title,channel, link,context):
    query = """
    INSERT INTO googlenews (title, channel,link,context)
    VALUES (%s, %s, %s,%s)
    """
    cur.execute(query, (title, channel, link,context))
    conn.commit()

# Insert each article
print(newslist[0])
for article in newslist:
    if(article['context']=='No context'):
        insert_news(article['title'], article['channel'], article['link'])
    else:
        insert_newscontext(article['title'], article['channel'], article['link'],article['context'])

# Close the cursor and connection
cur.close()
conn.close()

print("Data insertion complete!")
