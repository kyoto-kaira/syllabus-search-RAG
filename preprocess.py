import pickle
path1 = 'data1\shirabasu_htmls1.pkl'
with open(path1, 'rb') as f:
    htmls1 = pickle.load(f)
path2 = 'data1\shirabasu_htmls2.pkl'
with open(path2, 'rb') as f:
    htmls2 = pickle.load(f)
path3 = 'data1\shirabasu_url.pkl'
with open(path3, 'rb') as f:
    urls = pickle.load(f)
htmls = htmls1 + htmls2

rp = {'   ':'',
      '\n':'',
      '\u3000':'',
      '\t':'',
      '\y':'',
      '\xa0':'',
      '京都大学教務情報システムEnglish | 日本語 シラバス検索  (科目ナンバリング)':'科目ナンバリングは',
      '(科目名)':'。科目名は',
      '(英 訳)':'。英訳は',
      '(所属部局)(職 名)(氏 名)':'。所属部局、職 名、氏 名は',
      '(使用言語)':'。使用言語は',
      '(単位数)':'。単位数は',
      '(時間数)':'。時間数は',
      '(授業形態)':'。授業形態は',
      '(開講年度・開講期)':'。開講年度・開講期は',
      '(配当学年)':'。配当学年は',
      '(対象学生)':'。対象学生は',
      '(曜時限)':'。曜時限は',
      '(授業の概要・目的)':'。授業の概要・目的は',
      '(到達目標)':'。到達目標は',
      '(履修要件)':'。履修要件は',
      '(成績評価の方法・観点)':'。成績評価の方法・観点は',
      '(授業計画と内容)':'。授業計画と内容は',
      '(教科書)':'。教科書は',
      '(参考書等)':'。参考書等は',
      '(関連URL)':'。関連URLは',
      '(授業外学修（予習・復習）等)':'。授業外学修（予習・復習）等は',
      '(キーワード)':'。キーワードは',
      '(題目)':'。題目は',
      '(実務経験のある教員による授業)':'。実務経験のある教員による授業は',
      '。。':'。',
      '。 。':'。',
      '.。':'。',
      '. 。':'。',
      'external/open_syllabus/la_syllabus.jsp':'',
      'external/open_syllabus/department_syllabus.jsp':''}

def yojigen(data):
    """各科目の曜時限データをリストにする

    Args:
        data (str): 各科目のシラバスの曜時限のテキスト

    Returns:
        list: リストの中には'月1'から'金5'、'集中'などがある
    """
    if data == '月火水木3.4.5':
        l = ['月1','月2','月3','火1','火2','火3','水1','水2','水3','木1','木2','木3']
    else:
        l = []
        if '月1' in data:
            l.append('月1')
        if '月2' in data:
            l.append('月2')
        if '月3' in data:
            l.append('月3')
        if '月4' in data:
            l.append('月4')
        if '月5' in data:
            l.append('月5')
        if '火1' in data:
            l.append('火1')
        if '火2' in data:
            l.append('火2')
        if '火3' in data:
            l.append('火3')
        if '火4' in data:
            l.append('火4')
        if '火5' in data:
            l.append('火5')
        if '水1' in data:
            l.append('水1')
        if '水2' in data:
            l.append('水2')
        if '水3' in data:
            l.append('水3')
        if '水4' in data:
            l.append('水4')
        if '水5' in data:
            l.append('水5')
        if '木1' in data:
            l.append('木1')
        if '木2' in data:
            l.append('木2')
        if '木3' in data:
            l.append('木3')
        if '木4' in data:
            l.append('木4')
        if '木5' in data:
            l.append('木5')
        if '金1' in data:
            l.append('金1')
        if '金2' in data:
            l.append('金2')
        if '金3' in data:
            l.append('金3')
        if '金4' in data:
            l.append('金4')
        if '金5' in data:
            l.append('金5')
        if '集中' in data:
            l.append('集中')
    return l

def faculty(i,d):
    """URLのIDから各科目の'学部'、'群'、'分野'、'学科など'をメタデータ（辞書）に追加する

    Args:
        i (int): 科目のID
        d (dict): メタデータ

    Returns:
        dict: メタデータ
    """
    if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=20082&departmentNo=1'):
        d['学部'] = '全学共通'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54259'):
            d['群'] = '人文・社会科学'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=53751'):
                d['分野'] = '哲学・思想'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=53644'):
                d['分野'] = '歴史・文明'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=53702'):
                d['分野'] = '芸術・文学・言語'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=53710'):
                d['分野'] = '教育・心理・社会'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=53783'):
                d['分野'] = '地域・文化'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56247'):
                d['分野'] = '法・政治・経済'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56024'):
                d['分野'] = '外国文献研究'
            else:
                d['分野'] = '日本理解'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55594'):
            d['群'] = '自然科学'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54382'):
                d['分野'] = '数学'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54124'):
                d['分野'] = 'データ科学'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54150'):
                d['分野'] = '物理学'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54197'):
                d['分野'] = '化学'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54207'):
                d['分野'] = '生物学'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54227'):
                d['分野'] = '地球科学'
            else:
                d['分野'] = '図学'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54510'):
            d['群'] = '外国語'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55868'):
                d['分野'] = '英語リーディング'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55075'):
                d['分野'] = '英語ライティング－リスニング'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55242'):
                d['分野'] = 'ドイツ語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55342'):
                d['分野'] = 'フランス語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54426'):
                d['分野'] = '中国語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54980'):
                d['分野'] = 'ロシア語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=57194'):
                d['分野'] = 'スペイン語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=57310'):
                d['分野'] = '朝鮮語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55119'):
                d['分野'] = 'アラビア語I'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55123'):
                d['分野'] = 'ドイツ語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55243'):
                d['分野'] = 'ドイツ語III'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55240'):
                d['分野'] = 'フランス語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55322'):
                d['分野'] = 'フランス語III'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54434'):
                d['分野'] = '中国語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54458'):
                d['分野'] = 'ロシア語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55018'):
                d['分野'] = 'イタリア語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54454'):
                d['分野'] = 'スペイン語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54442'):
                d['分野'] = '朝鮮語II'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54468'):
                d['分野'] = 'アラビア語II'
            else:
                d['分野'] = 'その他'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54492'):
            d['群'] = '情報'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56318'):
            d['群'] = '健康・スポーツ'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56591'):
                d['分野'] = '健康・スポーツ科学'
            else:
                d['分野'] = 'スポーツ実習'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=55489'):
            d['群'] = 'キャリア形成'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54776'):
                d['分野'] = '国際コミュニケーション'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=57113'):
                d['分野'] = '学芸員課程'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54900'):
                d['分野'] = '多文化理解'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54790'):
                d['分野'] = '地域連携'
            else:
                d['分野'] = 'その他'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54716'):
            d['群'] = '統合科学'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54601'):
                d['分野'] = '統合科学'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54953'):
                d['分野'] = '環境'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=54398'):
                d['分野'] = '森里海連環学'
            else:
                d['分野'] = 'その他'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56561'):
            d['群'] = '少人数教育'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56635'):
            d['群'] = '大学院共通'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56525'):
                d['分野'] = '社会適合'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56589'):
                d['分野'] = '情報テクノサイエンス'
            else:
                d['分野'] = 'コミュニケーション'
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=20082&departmentNo=1'):
            d['群'] = '大学院横断教育'
            if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56498'):
                d['分野'] = '人文社会科学系'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56510'):
                d['分野'] = '自然科学系'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56499'):
                d['分野'] = '統計・情報・データ科学系'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56501'):
                d['分野'] = '健康・医療系'
            elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/la_syllabus?lectureNo=56560'):
                d['分野'] = 'キャリア形成系'
            else:
                d['分野'] = '複合領域系'
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6143&departmentNo=4'):
        d['学部'] = '文学部'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=19959&departmentNo=1'):
            d['学科など'] = ['日本語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=20275&departmentNo=1'):
            d['学科など'] = ['英語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=20296&departmentNo=1'):
            d['学科など'] = ['日本語授業','英語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=19973&departmentNo=1'):
            d['学科など'] = ['ドイツ語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=21585&departmentNo=1'):
            d['学科など'] = ['フランス語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=21387&departmentNo=1'):
            d['学科など'] = ['イタリア語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=21411&departmentNo=1'):
            d['学科など'] = ['ロシア語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=21413&departmentNo=1'):
            d['学科など'] = ['中国語授業']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=21836&departmentNo=1'):
            d['学科など'] = ['日本語授業','中国語授業']
        else:
            d['学科など'] = ['日本語授業','イタリア語授業']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2767&departmentNo=6'):
        d['学部'] = '教育学部'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=5852&departmentNo=4'):
            d['学科など'] = ['教育科学科']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6067&departmentNo=4'):
            d['学科など'] = ['現代教育基礎学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=5877&departmentNo=4'):
            d['学科など'] = ['教育心理学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=5957&departmentNo=4'):
            d['学科など'] = ['相関教育システム論系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6116&departmentNo=4'):
            d['学科など'] = ['教職科目']
        else:
            d['学科など'] = ['公認心理師科目']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8679&departmentNo=8'):
        d['学部'] = '法学部'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2857&departmentNo=6'):
            d['学科など'] = ['基礎法学']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2863&departmentNo=6'):
            d['学科など'] = ['公法']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2814&departmentNo=6'):
            d['学科など'] = ['民刑事法']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2879&departmentNo=6'):
            d['学科など'] = ['政治学']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2802&departmentNo=6'):
            d['学科など'] = ['1回生配当科目']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2911&departmentNo=6'):
            d['学科など'] = ['外国文献研究']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=2921&departmentNo=6'):
            d['学科など'] = ['特別科目']
        else:
            d['学科など'] = ['経済関係科目']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8084&departmentNo=10'):
        d['学部'] = '経済学部'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8623&departmentNo=8'):
            d['学科など'] = ['入門演習']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8631&departmentNo=8'):
            d['学科など'] = ['入門科目']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8930&departmentNo=8'):
            d['学科など'] = ['専門基礎科目']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8689&departmentNo=8'):
            d['学科など'] = ['専門科目']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8760&departmentNo=8'):
            d['学科など'] = ['演習(３回生)']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8752&departmentNo=8'):
            d['学科など'] = ['演習(４回生)']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8745&departmentNo=8'):
            d['学科など'] = ['法学部提供科目']
        else:
            d['学科など'] = ['特殊講義']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=4290&departmentNo=117'):
        d['学部'] = '理学部'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=7657&departmentNo=10'):
            d['学科など'] = ['共通又は専門基礎科目']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=7659&departmentNo=10'):
            d['学科など'] = ['数学教室']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=7664&departmentNo=10'):
            d['学科など'] = ['物理学教室']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=7665&departmentNo=10'):
            d['学科など'] = ['宇宙物理学教室']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8016&departmentNo=10'):
            d['学科など'] = ['地球物理学教室']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=7672&departmentNo=10'):
            d['学科など'] = ['地質学鉱物学教室']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=7675&departmentNo=10'):
            d['学科など'] = ['化学教室']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=8191&departmentNo=10'):
            d['学科など'] = ['生物科学系']
        else:
            d['学科など'] = ['境界領域']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=3046&departmentNo=14'):
        d['学部'] = '医学部（人間）'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=4146&departmentNo=117'):
            d['学科など'] = ['専門基礎科目']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=4156&departmentNo=117'):
            d['学科など'] = ['先端看護科学コース']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=4268&departmentNo=117'):
            d['学科など'] = ['先端リハビリテーション科学コース']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=4224&departmentNo=117'):
            d['学科など'] = ['先端リハビリテーション科学コース（先端理学療法学講座）']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=4163&departmentNo=117'):
            d['学科など'] = ['先端リハビリテーション科学コース（先端作業療法学講座）']
        else:
            d['学科など'] = ['総合医療科学コース']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=3135&departmentNo=14'):
        d['学部'] = '薬学部'
        d['学科など'] = ['薬科学科','薬学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11736&departmentNo=16'):
        d['学部'] = '薬学部'
        d['学科など'] = ['薬学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11633&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['地球工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11622&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['建築学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11619&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['物理工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11953&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['物理工学科','情報学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11982&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['電気電子工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=12010&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['電気電子工学科','物理工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=12090&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['理工化学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11829&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['情報学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11956&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['情報学科','物理工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=11634&departmentNo=16'):
        d['学部'] = '工学部'
        d['学科など'] = ['情報学科','電気電子工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6623&departmentNo=18'):
        d['学部'] = '工学部'
        d['学科など'] = ['地球工学科','建築学科','理工化学科','電気電子工学科','物理工学科','情報学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6997&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['資源生物科学科','地域環境工学科','森林科学科','応用生命科学科','食料・環境経済学科','食品生物科学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6630&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['応用生命科学科','食品生物科学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6953&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['資源生物科学科','地域環境工学科','森林科学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6687&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['資源生物科学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6896&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['応用生命科学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6763&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['地域環境工学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6800&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['食料・環境経済学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=6916&departmentNo=18'):
        d['学部'] = '農学部'
        d['学科など'] = ['森林科学科']
    elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=9729&departmentNo=61'):
        d['学部'] = '農学部'
        d['学科など'] = ['食品生物科学科']
    else:
        d['学部'] = '総合人間学部'
        if i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=9928&departmentNo=61'):
            d['学科など'] = ['人間科学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=9914&departmentNo=61'):
            d['学科など'] = ['国際文明学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=9954&departmentNo=61'):
            d['学科など'] = ['認知情報学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=9891&departmentNo=61'):
            d['学科など'] = ['文化環境学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=9971&departmentNo=61'):
            d['学科など'] = ['自然科学系']
        elif i < urls.index('https://www.k.kyoto-u.ac.jp/external/open_syllabus/department_syllabus?lectureNo=10192&departmentNo=61'):
            d['学科など'] = ['人間科学系','認知情報学系']
        else:
            d['学科など'] = ['人間科学系','国際文明学系']
    return d

def E_subject(text,d):
    """科目名からE科目の情報をメタデータに追加する

    Args:
        text (str): 科目名
        d (dict): メタデータ

    Returns:
        dict: メタデータ
    """
    if 'E1'in text:
        d['E科目'] = 'E1'
    elif 'E2'in text:
        d['E科目'] = 'E2'
    elif 'E3'in text:
        d['E科目'] = 'E3'
    return d

def class_type(d):
    if '授業形態' in d.keys():        
        if d['授業形態'] == '特殊講義':
            d['授業形態'] = ['特殊講義']
        else:
            l = []
            for text in ['講義','演習','実習','実験','語学','講読','卒業研究','ゼミナール']:
                if text in d['授業形態']:
                    l.append(text)
            d['授業形態'] = l
        return d
    else:
        d['授業形態'] = []
        return d

from bs4 import BeautifulSoup
texts = []
#textsは科目名、授業の概要・目的、到達目標、授業計画と内容を含み、主に類似度検索に用いられる
keywordtexts = []
#keywordtextsはtextsの内容に加えて、題目、キーワード、履修要件、成績評価の方法・観点、教科書、参考書等を含み、主にキーワード検索に用いられる
fulltexts = []
#fulltextsはシラバスのテキストの情報を全て含み、シラバスの要約生成に用いられる
metadatas = []
#metadatasは科目名やURL、単位数などの様々な情報をdict形式(str:str)で保存する。これらの情報で科目の絞り込みを行うときに用いられる
yoji = []
#yojiは曜時限データをリストで保存する
departments = []
#departmentsは学部の専門科目の学科などの属性をリストで保存する
classtype = []
#classtypeは各科目の授業形態をリストで保存する
for i,html in enumerate(htmls):
    d = {}
    html = html.replace('０','0').replace('１','1').replace('２','2').replace('３','3').replace('４','4').replace('５','5').replace('６','6').replace('７','7').replace('８','8').replace('９','9')
    soup = BeautifulSoup(html, 'html.parser')
    d = faculty(i,d)
    d['ID'] = str(i)
    d['URL'] = urls[i]
    d['科目ナンバリング'] = soup.find_all('tr',valign="top")[0].find_all('td')[1].get_text().replace('  ','').replace('\n','').replace('\t','')
    d['所属部局、職名、氏名']= soup.find_all('tr',valign="top")[1].find_all('td', class_ ="lesson_plan_sell")[1].get_text().replace('\n','').replace('  ','').replace('\u3000','') .replace('\t','').replace('(所属部局)(職 名)(氏 名)','')
    d['科目名'] = soup.find_all('tr',valign="top")[1].find('b').get_text().replace('  ','').replace('\n','').replace('\t','')
    d = E_subject(d['科目名'],d)
    for i in range(2, len(soup.find_all('tr',valign="top"))):
        for j in range(int(len(soup.find_all('tr',valign="top")[i].find_all('td'))/2)):
            if '題目' in soup.find_all('tr',valign="top")[i].find_all('td')[0].get_text():
                d['題目'] = soup.find_all('tr',valign="top")[i].find_all('td')[2].get_text().replace(' ','').replace('\n','').replace('\t','')
            else:
                d[soup.find_all('tr',valign="top")[i].find_all('td')[2*j].get_text().replace('(','').replace(')','')] = soup.find_all('tr',valign="top")[i].find_all('td')[2*j+1].get_text().replace(' ','').replace('\n','').replace('\t','').replace('\u3000','')
    if not d['使用言語'] in ['日本語','英語','日本語及び英語']:
        d['使用言語'] = 'その他'
    d = class_type(d)
    text = [div.get_text() for div in soup.find_all('div', class_ ="h120")]
    text.insert(0,'科目名は'+soup.find_all('tr',valign="top")[1].find('b').get_text())
    text = ''.join(text).split('(履修要件)')[0]+'。'
    keyword = [div.get_text() for div in soup.find_all('div', class_ ="h120")]
    keyword.insert(0,soup.find_all('tr',valign="top")[1].find('b').get_text())
    if 'キーワード' in d.keys():
        keyword.insert(1,d['キーワード'])
    if '題目' in d.keys():
        keyword.insert(1,d['題目'])
    keywordtext = ''.join(keyword)
    fulltext = soup.get_text()
    for k, v in rp.items():
        text = text.replace(k, v)
        keywordtext = keywordtext.replace(k, v)
        fulltext = fulltext.replace(k, v)
    if '学科など' in d.keys():
        departments.append(d['学科など'])
        d.pop('学科など')
        metadatas.append(d)
    else:
        departments.append('なし')
        metadatas.append(d)
    texts.append(text)
    keywordtexts.append(keywordtext)
    fulltexts.append(fulltext)
    yoji.append(yojigen(d['曜時限']))
    classtype.append(d['授業形態'])
    

path_w1 = 'data2/shirabasu_texts.pkl'
with open(path_w1, mode='wb') as f:
    pickle.dump(texts, f)
path_w2 = 'data2/shirabasu_metadatas.pkl'
with open(path_w2, mode='wb') as f:
    pickle.dump(metadatas, f)
path_w3 = 'data2/shirabasu_fulltexts.pkl'
with open(path_w3, mode='wb') as f:
    pickle.dump(fulltexts, f)
path_w4 = 'data2/shirabasu_yojigen.pkl'
with open(path_w4, mode='wb') as f:
    pickle.dump(yoji, f)
path_w5 = 'data2/shirabasu_keywordtexts.pkl'
with open(path_w5, mode='wb') as f:
    pickle.dump(keywordtexts, f)
path_w6 = 'data2/shirabasu_departments.pkl'
with open(path_w6, mode='wb') as f:
    pickle.dump(departments, f)
path_w7 = 'data2/shirabasu_classtype.pkl'
with open(path_w7, mode='wb') as f:
    pickle.dump(classtype, f)
