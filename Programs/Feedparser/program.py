import requests
import feedparser
import smtplib
import ssl
import getpass


def get_talkpython_rss():
    print('Retrieving talk python rss feed data')
    URL = "https://talkpython.fm/episodes/rss"
    r = requests.get(URL)
    with open('talkpython.xml', 'wb') as f:
        f.write(r.content)


def parse_rss_feed():
    print('Parsing the Talk Python rss feed data')
    FEED_FILE = "talkpython.xml"
    feed = feedparser.parse(FEED_FILE)
    article_list = []
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published
        description = entry.description

        article = {
            'title': title,
            'link': link,
            'published': published,
            'description': description
        }

        article_list.append(article)


def send_rss_email():
    print('Sending Rss feed data to email address')
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL
    sender_email = "hoybytepython@gmail.com"
    receiver_email = 'hoybyte@gmail.com'
    message = """

    Subject: Newest Podcast

    {newest_podcast}

    """

    print('Please Enter your email password below: ')
    password = getpass.getpass()

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    get_talkpython_rss()
    parse_rss_feed()
    send_rss_email()
