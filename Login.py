from instapy import InstaPy
from instapy import InstaPy
from instapy.util import smart_run

session=InstaPy(username="torombolo546", password="monotiti1").login()

session.follow_by_list()
