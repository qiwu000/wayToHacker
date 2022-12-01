import requests
import re

# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
# “.*?” 表示非贪心算法，表示要精确的配对。
# “.*”表示贪心算法，表示要尽可能多的匹配
links = re.findall('"((http|ftp)s?://.*?)"', html)

# output links
for link in links:
    print(link[0])
