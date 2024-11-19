#FAISSのvectorstoreのdelete関数を検索に利用する。そのため、検索関数は、入力に該当するIDではなく、該当しないIDを戻り値とする。
#metadataは各科目の学部、群、授業形態、開講時期などの情報が辞書形式で保存されている
#yojigenは各科目の曜時限（月1から金5、集中）の情報がリスト形式で保存されている
#classtypeは各科目の授業形態の情報がリスト形式で保存されている
#departmentsは各科目の学科などの情報がリスト形式で保存されている
#keywordtextsは各学科の授業内容などの情報がテキスト形式で保存されている
#professorsは各科目の教授名がテキスト形式で保存されている
#hyokaは成績評価の平常点や期末テストの占める割合をLLMで生成して辞書形式で保存されている

def search(input,key,metadatas):
    """ inputと各科目のメタデータが完全に一致する科目を検索する
    Args:
        input (str): 科目の情報
        key (str): メタデータのキー
        metadatas (list): メタデータ

    Returns:
        set: 検索に該当しないIDの集合
    """
    a = set()
    for i,metadata in enumerate(metadatas):
        if key in metadata.keys():
            if not metadata[key] == input:
                a.add(str(i))
        else:
            a.add(str(i))
    return a

def or_search(input,key,metadatas):
    """ inputに各科目のメタデータ（）が含まれる科目を検索する
    Args:
        input (list): 科目の情報
        key (str): メタデータのキー
        metadatas (list): メタデータ

    Returns:
        set: 検索に該当しないIDの集合
    """
    a = set()
    for i,metadata in enumerate(metadatas):
        if key in metadata.keys():
            if not metadata[key] in input:
                a.add(str(i))
        else:
            a.add(str(i))
    return a

def or_list_search(input,data):
    """ inputに各科目のリストデータ（classtype,departments,yojigen）の要素が1以上含まれる科目を検索する
    Args:
        input (list): 科目の情報
        data (str): メタデータのキー

    Returns:
        set: 検索に該当しないIDの集合
    """
    a = set()
    for i,y in enumerate(data):
        b = 0
        for d in y:
            if d in  input:
                b = 1
        if b == 0:
            a.add(str(i))
    return a

def word_search(input,texts):
    """ inputを空白で単語に分割し、単語が各科目の検索用テキスト（keywordtexts,professors）に含まれる科目を検索する
    Args:
        input (str): 検索したい単語
        texts (list): 検索用テキスト

    Returns:
        set: 検索に該当しないIDの集合
    """
    a = set()
    tokens = input.split()
    for i,text in enumerate(texts):
        for token in tokens:
            if not token in text:
                a.add(str(i))
    return a

def hyoka_search(input,ratio,hyoka):
    """ inputの評価基準の割合がratio以上の科目を検索する
    Args:
        input (list): 評価基準（平常点や期末レポート）
        texts (int): 成績評価の占める最低パーセント
        hyoka (list):それぞれの評価基準の占める割合

    Returns:
        set: 検索に該当しないIDの集合
    """
    seiseki = []
    for d in hyoka:
        a = []
        for k,v in d.items():
            if v >= ratio:
                a.append(k)
        if len(a) == 0:
            a.append('なし')
        seiseki.append(a)
    return or_list_search(input,seiseki)

def ids_union(ids):
    """検索関数で求めた検索に該当しないIDの集合を統合する

    Args:
        ids (list): 検索に該当しないIDの集合のリスト

    Returns:
        list: 統合した検索に該当しないIDの集合
    """
    if len(ids) == 1:
        return list(ids[0])
    else:
        for i in range(len(ids)-1):
            if i == 0:
                a = ids[0] | ids[1]
            else:
                a = a | ids[i+1]
    return list(a)