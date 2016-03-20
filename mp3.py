import urllib
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://www.uscis.gov/citizenship/teachers/educational-products/100-civics-questions-and-answers-mp3-audio-english-version'
    s = BeautifulSoup(urllib.urlopen(url).read(), "html.parser")
    links = s.find_all('a',href=True)
    for link in links:
        if link.string and 'MP3' in link.string:
            mp3_url = 'https://www.uscis.gov' + link['href']
            mp3_filename = link.string.replace(" ","").split("(")[0]+'.mp3'
            print mp3_url + ' , ' + mp3_filename
            urllib.urlretrieve(mp3_url, mp3_filename)
