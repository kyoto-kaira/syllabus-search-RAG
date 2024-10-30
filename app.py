import streamlit as st
import pickle
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

from shirabasusearch import search,or_search,or_list_search,word_search,hyoka_search,ids_union 
path1 = 'data2\shirabasu_classtype.pkl'
with open(path1, 'rb') as f:
    classtypes = pickle.load(f)
path2 = 'data2\shirabasu_departments.pkl'
with open(path2, 'rb') as f:
    departments = pickle.load(f)
path3 = 'data2\shirabasu_fulltexts.pkl'
with open(path3, 'rb') as f:
    fulltexts = pickle.load(f)
path4 = 'data2\shirabasu_hyoka.pkl'
with open(path4, 'rb') as f:
    hyoka = pickle.load(f)
path5 = 'data2\shirabasu_keywordtexts.pkl'
with open(path5, 'rb') as f:
    keywordtexts = pickle.load(f)
path6 = 'data2\shirabasu_metadatas.pkl'
with open(path6, 'rb') as f:
    metadatas = pickle.load(f)
path7 = 'data2\shirabasu_texts.pkl'
with open(path7, 'rb') as f:
    texts = pickle.load(f)
path8 = 'data2\shirabasu_yojigen.pkl'
with open(path8, 'rb') as f:
    yojigen = pickle.load(f)
professors = [metadata['所属部局、職名、氏名'] for metadata in metadatas]

embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")
store = FAISS.load_local('data2\shirabasu_vectorstore', embedding,allow_dangerous_deserialization=True)
os.environ['GOOGLE_API_KEY'] = '------------------------'


st.title('RAGシステム')

faculity = st.selectbox(
    '学部',
    ['---','全学共通','文学部','教育学部','法学部','経済学部','理学部','医学部（人間）','薬学部','工学部','農学部','総合人間学部']
    )
if faculity == '全学共通':
    group = st.selectbox(
        '群',
        ['---','人文・社会科学','自然科学','外国語','情報','健康・スポーツ','キャリア形成','統合科学','少人数教育','大学院共通','大学院横断教育']
        )
    department = st.multiselect(
        '学科等',
        []
        )
    if group == '人文・社会科学':
        field = st.multiselect(
            '分野',
            ['哲学・思想','歴史・文明','芸術・文学・言語','教育・心理・社会','地域・文化','法・政治・経済','外国文献研究','日本理解']
            )
    elif group == '自然科学':
        field = st.multiselect(
            '分野',
            ['数学','データ科学','物理学','化学','生物学','地球科学','図学']
            )
    elif group == '外国語':
        field = st.multiselect(
            '分野',
            ['英語リーディング','英語ライティング－リスニング','ドイツ語I','フランス語I','中国語I','ロシア語I','スペイン語I','朝鮮語I','アラビア語I','ドイツ語II','ドイツ語III','フランス語II','フランス語III','中国語II','ロシア語II','イタリア語II','スペイン語II','朝鮮語II','アラビア語II','その他']
            )
    elif group == '情報':
        field = st.multiselect(
            '分野',
            []
            )
    elif group == '健康・スポーツ':
        field = st.multiselect(
            '分野',
            ['健康・スポーツ科学','スポーツ実習']
            )
    elif group == 'キャリア形成':
        field = st.multiselect(
            '分野',
            ['国際コミュニケーション','学芸員課程','多文化理解','地域連携','その他']
            )
    elif group == '統合科学':
        field = st.multiselect(
            '分野',
            ['統合科学','環境','森里海連環学','その他']
            )
    elif group == '少人数教育':
        field = st.multiselect(
            '分野',
            []
            )
    elif group == '大学院共通':
        field = st.multiselect(
            '分野',
            ['社会適合','情報テクノサイエンス','コミュニケーション']
            )
    elif group == '大学院横断教育':
        field = st.multiselect(
            '分野',
            ['人文社会科学系','自然科学系','統計・情報・データ科学系','健康・医療系','キャリア形成系','複合領域系']
            )
    else:
        field = st.multiselect(
            '分野',
            []
            )         
elif faculity == '文学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['日本語授業','英語授業','ドイツ語授業','フランス語授業','イタリア語授業','ロシア語授業','中国語授業'],
        key=1
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '教育学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['教育科学科','現代教育基礎学系','教育心理学系','相関教育システム論系','教職科目','公認心理師科目']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '法学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['基礎法学','公法','民刑事法','政治学','1回生配当科目','外国文献研究','特別科目','経済関係科目']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '経済学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['入門演習','入門科目','専門基礎科目','専門科目','演習(３回生)','演習(４回生)','法学部提供科目','特殊講義']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '理学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['共通又は専門基礎科目','数学教室','物理学教室','宇宙物理学教室','地球物理学教室','地質学鉱物学教室','化学教室','生物科学系','境界領域']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '医学部（人間）':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['専門基礎科目','先端看護科学コース','先端リハビリテーション科学コース','先端リハビリテーション科学コース（先端理学療法学講座）','先端リハビリテーション科学コース（先端作業療法学講座）','総合医療科学コース']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '薬学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['薬科学科','薬学科']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '工学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['地球工学科','建築学科','物理工学科','電気電子工学科','理工化学科','情報学科']
        )
    field = st.multiselect(
        '分野',
        []
        )   
elif faculity == '農学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['資源生物科学科','応用生命科学科','地域環境工学科','食料・環境経済学科','森林科学科','食品生物科学科']
        )
    field = st.multiselect(
        '分野',
        []
        )
elif faculity == '総合人間学部':
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        ['人間科学系','国際文明学系','認知情報学系','文化環境学系','自然科学系']
        )
    field = st.multiselect(
        '分野',
        []
        )
else:
    group = st.selectbox(
        '群',
        ['---']
        )
    department = st.multiselect(
        '学科等',
        []
        )
    field = st.multiselect(
        '分野',
        []
        )
with st.form('rag'):
    st.text('曜時限')
    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        mo1 = st.checkbox('月1')
        mo2 = st.checkbox('月2')
        mo3 = st.checkbox('月3')
        mo4 = st.checkbox('月4')
        mo5 = st.checkbox('月5')
        syu = st.checkbox('集中')
    with c2:
        tu1 = st.checkbox('火1')
        tu2 = st.checkbox('火2')
        tu3 = st.checkbox('火3')
        tu4 = st.checkbox('火4')
        tu5 = st.checkbox('火5')
    with c3:
        we1 = st.checkbox('水1')
        we2 = st.checkbox('水2')
        we3 = st.checkbox('水3')
        we4 = st.checkbox('水4')
        we5 = st.checkbox('水5')
    with c4:
        th1 = st.checkbox('木1')
        th2 = st.checkbox('木2')
        th3 = st.checkbox('木3')
        th4 = st.checkbox('木4')
        th5 = st.checkbox('木5')
    with c5:
        fr1 = st.checkbox('金1')
        fr2 = st.checkbox('金2')
        fr3 = st.checkbox('金3')
        fr4 = st.checkbox('金4')
        fr5 = st.checkbox('金5')
    yj =[]
    yj1 = [mo1,mo2,mo3,mo4,mo5,tu1,tu2,tu3,tu4,tu5,we1,we2,we3,we4,we5,th1,th2,th3,th4,th5,fr1,fr2,fr3,fr4,fr5,syu]
    yj2 = ['月1','月2','月3','月4','月5','火1','火2','火3','火4','火5','水1','水2','水3','水4','水5','木1','木2','木3','木4','木5','金1','金2','金3','金4','金5','集中']
    for i in range(26):
        if yj1[i]:
            yj.append(yj2[i])
    classtype = st.multiselect(
        '授業形態',
        ['講義','演習','実習','実験','特殊講義','語学','講読','卒業研究','ゼミナール']
        )
    language = st.multiselect(
        '使用言語',
        ['日本語','英語','日本語及び英語','その他']
        )
    period = st.multiselect(
        '開講年度・開講期',
        ['2024・前期','2024・後期','2024・通年','2024・前期集中','2024・後期集中','2024・通年集中','2024・前期不定','2024・後期不定','2024・通年不定','2024・前期前半','2024・前期後半','2024・後期前半','2024・後期後半']
        )
    target = st.multiselect(
        '対象学生',
        ['全学向','文系向','理系向','留学生']
        )
    esubject = st.multiselect(
        'E科目',
        ['E1','E2','E3']
        )
    keyword = st.text_input('キーワード')
    professor = st.text_input('教授・教員')
    grade = st.multiselect(
        '成績評価方法',
        ['平常点','課題','発表','討論','小レポート','小テスト','期末レポート','期末試験']
        )

    graderatio = st.text_input('成績評価の占める最低パーセント','0')
    
    query = st.text_input('質問','大学で学べる科目は何ですか。')
    
    k = st.text_input('検索数','4')
    
    submit_btn = st.form_submit_button('検索')
    cancel_btn = st.form_submit_button('キャンセル')

if submit_btn:
    #入力を統合する
    ids = []
    if faculity != '---':
        ids.append(search(faculity,'学部',metadatas))
    if group != '---':
        ids.append(search(group,'群',metadatas))
    if len(department) != 0:
        ids.append(or_list_search(department,departments))
    if len(field) != 0:
        ids.append(or_search(field,'分野',metadatas))
    if len(yj) != 0:
        ids.append(or_list_search(yj,yojigen))
    if len(classtype) != 0:
        ids.append(or_list_search(classtype,classtypes))
    if len(language) != 0:
        ids.append(or_search(language,'使用言語',metadatas))
    if len(period) != 0:
        ids.append(or_search(period,'開講年度・開講期',metadatas))
    if len(target) != 0:
        ids.append(or_search(target,'対象学生',metadatas))
    if len(esubject) != 0:
        ids.append(or_search(esubject,'E科目',metadatas))
    if len(keyword) != 0:
        ids.append(word_search(keyword,keywordtexts))
    if len(professor) != 0:
        ids.append(word_search(professor,professors))
    if len(grade) != 0:
        ids.append(hyoka_search(grade,int(graderatio),hyoka))
    if len(ids) != 0:
        store.delete(ids_union(ids))
    
    #質問で検索するための検索候補の個数を求める
    ID = [str(i) for i in range(len(texts))]
    for i in ids_union(ids):
        ID.remove(i)
    st.text('検索候補は'+str(len(ID))+'個')

    if len(ID) > 0:
        #類似度が高い順に科目を検索する
        a = store.similarity_search(query,k=int(k))
        st.text('該当する科目は以下の通りです。')
        #検索した科目を列挙する
        for i in range(len(a)):
            st.text(a[i].metadata['科目名']+'   URL:'+a[i].metadata['URL'])
        #LLMで科目の要約を生成する
        llm = ChatGoogleGenerativeAI(model='gemini-pro')
        for i in range(len(a)):
            st.text('---------------------------------------')
            st.text(a[i].metadata['科目名']+'の概要')
            sumtext = llm.invoke('以下の文章を日本語で箇条書きで要約を生成してください。'+fulltexts[int(a[i].metadata['ID'])])
            st.text(sumtext.content)

    