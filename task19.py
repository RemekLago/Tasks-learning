"""Take the code from the How To Decode A Website exercise
(if you didn’t do it or just want to play with some different code,
use the code from the solution), and instead of printing the results to a screen,
write the results to a txt file. In your code, just make up a name for the file you are saving to.
Extras:
Ask the user to specify the name of the output file that will be saved."""

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

filename = input("File to save to: ")

with open(filename, 'w') as f:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            f.write(story_heading.a.text.replace("\n", " ").strip())
        else:
            f.write(story_heading.contents[0].strip())