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
        ("adam", "Ａ０４６", "", 20,(1,1), "male", "ドロイド", "me:私"),
        ("paul", "ポール", "", 30,(1,1), "male", "刑事", "me:俺"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("TK98", "ＴＫ０９８", 1000,1000),
        ("MN20", "ＭＮ２０００", 10000,10000),
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("trashcollection", "廃品回収センター", "TK98"),
        ("moonbase", "月面基地", "MN20"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("current", "current", 1,1,2020),
        ("murder1", "第一の殺人事件発生", 5,10, 2098),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        ("droid", "ドロイド", "作業用ロボット"),
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )

