import webbrowser, requests , bs4, re

url = 'http://www.newyorker.com/magazine/fiction/page/7'

res = requests.get(url)
res.raise_for_status()
nyorker = bs4.BeautifulSoup(res.text, "html.parser")
type(nyorker)

for link in nyorker.find_all('a', href=re.compile('http://www.newyorker.com/magazine/20.*')):
    print(link.get('href'))
