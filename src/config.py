# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("adam", "アダム", "Ａ０４６", 20,(1,1), "male", "ドロイド", "me:ワタシ"),
        ("paul", "ポール", "", 30,(1,1), "male", "刑事", "me:俺"),
        ("emilia", "エミリア", "クラーク,エミリア", 25,(1,1), "female", "女性", "me:わたし"),
        ("uru", "ウル", "", 28,(1,1), "male", "ザイアス工業社員", "me:私"),
        ("niel", "ニール", "ギブスン,ニール", 50,(1,1), "male", "技師", "me:僕"),
        ("worker", "作業ドロイド", "", 99,(1,1), "male", "作業員", "me:ワタシ"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("TK98", "ＴＫ０９８", 1000,1000),
        ("InCias", "ザイアス工業施設内", 1100,1050,),
        ("MN20", "ＭＮ２０００", 10000,10000),
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("moonbase", "月面基地", "MN20"),
        ("tengoku", "エルドラド", "MN20", "人間の暮らす世界"),
        ("cias", "ザイアス工業", "TK98"),
        ("trashcollection", "廃品回収センター", "TK98"),
        ### in facitily
        ("pathway", "施設通路", "InCias"),
        ("bedroom", "宿泊用個室（エミリア）", "InCias"),
        ("nielroom", "ニールの部屋", "InCias"),
        ("paulroom", "ポールの部屋", "InCias"),
        ("dismantlinghall", "解体作業ホール", "InCias"),
        ### Hotel
        ("herroom", "エミリアの部屋（ホテル）", "TK98"),
        ## Company
        ("RobertCom", "ロバート通信", "TK98"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("current", "current", 1,1,2020),
        ("visit", "訪問日", 5,10, 2098),
        ("murder1", "第一の殺人事件発生", 5,10, 2098),
        ("murder2", "第二の殺人事件", 5,11, 2098),
        ("reporting", "レポート作成日", 5,29, 2098),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        ("cias", "ザイアス"),
        ("droid", "ドロイド", "作業用ロボット"),
        ("hisword01", "ロボットとは本来人間の役に立つために生み出された奴隷だ"),
        ("hall", "作業ホール"),
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )

