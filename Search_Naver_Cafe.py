from bs4 import BeautifulSoup
import requests as rq
############## 입력 키워드###################
keyword = '14-28'
############################################


#url 구성
url1 = 'https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%22'
url2 = '%22&search.menuid=0&search.searchBy=0&search.sortBy=date&search.clubid=29825724&search.option=0&search.defaultValue=1'
url = url1 + keyword + url2

#헤더 설정(윈도우/크롬 버전)
headers_info = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

res = rq.get(url, headers = headers_info)
soup = BeautifulSoup(res.content, 'lxml')

posts = soup.select('ul.list_tit li')

# 뒤에 랜덤값들은 뭐징 어떻게하면 들어가질까#
for post in posts:
    address = 'https://m.cafe.naver.com/' + post.find('a').attrs['href']
    title = post.find('h3').text.strip()
    print(title,'\n',address,'\n')

    res1 = rq.get(address, headers = headers_info)
    soup1 = BeautifulSoup(res1.content, 'lxml')
    print(soup1)
    break
    posts1 = soup.select('div.lst_wp')

    for post1 in posts1:
        reply = post1.find('p')
        print(reply)