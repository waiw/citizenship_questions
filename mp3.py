import urllib
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://www.uscis.gov/citizenship/teachers/educational-products/100-civics-questions-and-answers-mp3-audio-english-version'
    s = BeautifulSoup(urllib.urlopen(url).read(), "html.parser")
    links = s.find_all('a',href=True)
    count = 1
    for link in links:
        if link.string and 'MP3' in link.string:
            mp3_url = 'https://www.uscis.gov' + link['href']
            mp3_filename = "%03d.mp3" % (count)
            print mp3_url + ' , ' + mp3_filename + ' , ' + link.string.split(" (")[0]
            urllib.urlretrieve(mp3_url, mp3_filename)
            count += 1
