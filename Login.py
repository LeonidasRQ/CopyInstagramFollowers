from instapy import InstaPy


session=InstaPy(username="torombolo546", password="monotiti1").login()
session.like_by_tags(["bmw", "mercedes"], amount=5)