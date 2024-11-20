import requests
from bs4 import BeautifulSoup
import json

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
htmls = []
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    htmls.append(str(soup))

#githubは容量が大きいデータを扱えないので、htmlsを2つに分割する
htmls1 = htmls[:3000]
htmls2 = htmls[3000:]

with open('data1/syllabus_htmls1.json', 'wt') as f:
    json.dump(htmls1, f)

with open('data1/syllabus_htmls2.json', 'wt') as f:
    json.dump(htmls2, f)

with open('data1/syllabus_urls.txt', mode='w') as f:
    f.write('\n'.join(urls))