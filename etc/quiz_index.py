
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
# requests.get: 브라우저에서 엔터를 치는 행위를한다고 하네

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
titles=soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number > span > span > span
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number 이게 맞는데
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
a_num=0
for title in titles:    
    a_title=title.select_one('td.info > a.title.ellipsis')
    r_title=a_title.text.strip()
    # a_rank =title.select_one('td.number > span') 번호를 못가져온다...
    if (a_title !=''):
        a_num += 1
        a_name=title.select_one('td.info > a.artist.ellipsis')
        print(a_num,r_title, a_name.text)



