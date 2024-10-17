import requests
from bs4 import BeautifulSoup

# Replace 'your_song_name' with a song from your list
song_name = 'Perfect'
url = f"https://www.ultimate-guitar.com/search.php?search_type=title&value={song_name}"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find link to the chord page (this selector might need updating based on the website's current layout)
link = soup.find('a', class_='js-search-results-chords')
if link:
    chord_url = link.get('href')
    print(f"Chord page URL: {chord_url}")