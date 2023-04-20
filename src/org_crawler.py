import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# import HTMLSession from requests_html
from requests_html import HTMLSession
 
# create an HTML Session object
session = HTMLSession()

# Use the object above to connect to needed webpage
resp = session.get('https://depauw.campuslabs.com/engage/organizations')

# Run JavaScript code on webpage
resp.html.render()
breakpoint()