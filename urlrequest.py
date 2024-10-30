import requests
from bs4 import BeautifulSoup

#シラバス一覧ページから全学共通科目から総合人間学部（医学部医学科を除く）のそれぞれの科目のURLを取得
url1 = 'https://www.k.kyoto-u.ac.jp/external/open_syllabus/all'
response = requests.get(url1)
soup = BeautifulSoup(response.content, 'html.parser')
urls = []
for i in range(3,len(soup.find_all('a'))):
    url = 'https://www.k.kyoto-u.ac.jp/external/open_syllabus/'+str(soup.find_all('a')[i].attrs['href'])
    if not url in ['https://www.med.kyoto-u.ac.jp/for_students/affairs_m/class/','https://www.k.kyoto-u.ac.jp/external/open_syllabus/https://www.med.kyoto-u.ac.jp/for_students/affairs_m/class/']:
        urls.append(url)
        #医学部医学科はシラバスがPDFなので含めない
    if url == 'https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=10192&departmentNo=61':
        break
        #URLが総合人間学部の最後の科目である英米文学入門になったら終了

#各科目のURLからHTMLをリクエストする。3時間ほどかかる
import requests
from bs4 import BeautifulSoup
htmls = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    htmls.append(str(soup))

#githubは容量が大きいデータを扱えないので、htmlsを2つに分割する
htmls1 = htmls[:3000]
htmls2 = htmls[3000:]

import pickle
path_w1 = 'data1\shirabasu_htmls1.pkl'
with open(path_w1, mode='wb') as f:
    pickle.dump(htmls1, f)
path_w2 = 'data1\shirabasu_htmls2.pkl'
with open(path_w2, mode='wb') as f:
    pickle.dump(htmls2, f)
path_w3 = 'data1\shirabasu_url.pkl'
with open(path_w3, mode='wb') as f:
    pickle.dump(urls, f)