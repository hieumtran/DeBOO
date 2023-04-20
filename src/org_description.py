import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import json
import lxml

def scrap_data(web):
    html = requests.get(web)
    # if html.status_code != 200:
    # Collect description
    data = re.search(r'window\.initialAppState = ({.*});', html.text)
    data = json.loads(data.group(1))
    desc = data['preFetchedData']['organization']['description']
    
    if desc != None:
        # Clean description
        desc = desc.replace('&nbsp;', '')
        desc = desc.replace('\n<p>', '\n ')
        desc = desc.replace('</p>', ' ')
        desc = desc.replace('<p>', '')
    else:
        desc = ''

    # Images
    imageID = data['preFetchedData']['organization']['profilePicture']
    if imageID != None: image = data['imageServerBaseUrl'] + imageID
    else: image = ''

    # Summary
    summary = data['preFetchedData']['organization']['organizationType']['name']
    if summary == None: summary = ''
    return image, desc, summary


def main():
    df = pd.read_csv('./data/DPU_Org_Description.csv')
    arr_desc = []
    arr_img = []
    arr_summary = []
    for i in range(len(df)):
        image, desc, summary = scrap_data(df['URL'][i])
        print(df['Org'][i], ' Success')
        arr_desc.append(desc)
        arr_img.append(image)
        arr_summary.append(summary)
    df['Description'] = arr_desc
    df['Image'] = arr_img
    df['Summary'] = arr_summary
    df.to_csv('./data/DPU_desc.csv', index=False)
main()