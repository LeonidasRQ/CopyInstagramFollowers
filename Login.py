from instapy import InstaPy

session=InstaPy(username="torombolo546", password="monotiti1")
session.login()
session.follow_user_following('ramlambda',amount=3,randomize=False,interact=False,sleep_delay=600)