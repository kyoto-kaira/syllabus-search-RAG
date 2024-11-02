from bs4 import BeautifulSoup
import google.generativeai as genai
from google.colab import userdata
import json
import time

with open('data1/shirabasu_htmls1.json', 'rt') as f:
    htmls1 = json.load(f)

with open('data1/shirabasu_htmls2.json', 'rt') as f:
    htmls2 = json.load(f)

htmls = htmls1 + htmls2

#各科目の成績評価の方法・観点のテキストを抽出する
rp = {'   ':'',
      '\n':'',
      '\u3000':'',
      '\t':'',
      '\y':'',
      '\xa0':''}
seisekitexts = []
for html in htmls:
    zenkaku_to_hankaku = str.maketrans('０１２３４５６７８９', '0123456789')
    html = html.translate(zenkaku_to_hankaku)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div')
    for i,d in enumerate(div):
        if '<div class="lesson_plan_subheading">(成績評価の方法・観点)</div>' == str(d):
            seiseki = div[i+1].get_text()
    for k, v in rp.items():
        seiseki = seiseki.replace(k, v)
    seisekitexts.append('成績評価の方法・観点は'+seiseki)

#成績評価の平常点や期末テストの占める割合をLLMで生成
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash',generation_config={"response_mime_type": "application/json"})

hyoka = []
for i,text in enumerate(seisekitexts):
    print(i)
    prompt = "次のJSONスキーマを使用して、"+text+"""
    成績評価の方法・観点について、平常点、課題、発表、討論、小テスト、小レポート、期末レポート、期末試験のいずれか占める割合をリストアップしてください。

    seiseki = {'平常点': int,'課題': int,'発表': int,'討論': int,'小レポート': int,'小テスト': int,'期末レポート': int,'期末試験': int}
    Return: seiseki"""
    raw_response = model.generate_content(prompt)
    hyoka.append(json.loads(raw_response.text.replace('\n','')))
    time.sleep(4)
    #一分間にLLMにリクエストできる上限が15回なので、リクエストに間隔をあけている

#実際は、一日にLLMにリクエストできる上限が1500回程度なので、Googlecolabで分割して実行した

with open('data2/shirabasu_hyoka.json', 'wt') as f:
    json.dump(hyoka, f)