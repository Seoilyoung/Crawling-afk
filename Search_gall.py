from bs4 import BeautifulSoup
import requests as rq

def connect_post(connect_url):
    res = rq.get(connect_url, headers= headers_info)
    soup = BeautifulSoup(res.content,'lxml')
    return soup.select('table.gall_list tbody tr.ub-content.us-post')
def search_post(search_url):
    posts = connect_post(search_url)
    for post in posts:
        a = post.find('a')
        address = 'https://gall.dcinside.com/' + a.attrs['href']
        title = a.text.strip()
        reply_num = post.find('span').text.strip()
        print(title, reply_num, '\n', address)

#헤더 설정(맥/크롬 버전)
headers_info = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

#주소
gall_url = 'https://gall.dcinside.com/mgallery/board/lists?id=' + 'afk' # langrisser afk
################## 입력 키워드############################
keyword = '19-20'
#########################################################
posts = connect_post(gall_url)
for post in posts:
    subject = post.find('td',class_='gall_subject').text.strip()
    if subject == '일반' or '잡담': # 일반은 afk 랑그릿사는 잡담
        post_num = int(post.find('td',class_='gall_num').text.strip()) *(-1)
        break

url = gall_url + '&s_type=search_all&s_keyword=' + keyword
search_post(url)
while post_num < 0:
    post_num += 10000
    page_url = '&page=1&search_pos=%d'%post_num
    search_post(url + page_url)