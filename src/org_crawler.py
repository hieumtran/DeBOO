import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print("hello world")

r = requests.get('https://depauw.campuslabs.com/engage/organizations')
time.sleep(5)  # suspend execution for 5 secs
# html = r.text
soup = BeautifulSoup(r.content, features="html.parser")
breakpoint()