# -*- coding: utf-8 -*-
"""Episode: 1.殺人事件
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_tobira(w: World):
    adam = W(w.adam)
    return w.scene("アシモフのロボット工学三原則",
            w.comment("扉は冒頭に別枠で作る"),
            adam.be(),
            adam.explain("第一条　ロボットは人間に危害を加えてはならない。また、その危険を看過することによって、人間に危害を及ぼしてはならない"),
            _.explain("第二条　ロボットは人間にあたえられた命令に服従しなければならない。ただし、あたえられた命令が、第一条に反する場合は、この限りでない"),
            _.explain("第三条　ロボットは、前掲第一条および第二条に反するおそれのないかぎり、自己をまもらなければならない"),
            _.explain("――アイザック・アシモフ『われはロボット』小尾芙佐訳、早川書房　より"),
            camera=w.adam,
            stage=w.on_trashcollection,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_report_introduction(w: World):
    emil, adam, paul = W(w.emilia), W(w.adam), W(w.paul)
    return w.scene("レポート序文",
            w.comment("$emiliaのレポートという形式の三人称で", "扉と同じページに作る"),
            w.symbol("　　　　※"),
            emil.be(),
            emil.think("ロボットというものについて考える時、$meはいつも彼のことを思い出す",
                "彼と呼ぶことが正しいかどうかはこのレポートを最後まで読んでもらい、各自判断してもらいたいと思う"),
            w.comment("何かしら結末と全体の流れを暗示するものを"),
            )

def sc_interview(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("取材",
            emil.come(),
            uru.be("案内している"),
            emil.look("ズボンの上に短いスカート、上着はスーツ",
                "現代風だが、小物は未来感を"),
            emil.talk("本日はありがとうございます",
                "まさか取材を受けてもらえるとは"),
            uru.talk("我々も世界に売り出すことを踏まえてオープンにしていこうということです"),
            emil.do("今まで決して取材等、外部の人間を入れなかった$w_cias社だったが、",
                "どういう方針転換だろうと疑っていた"),
            w.eventPoint("$w_cias", "今まで外部の人間を決して入れなかった"),
            emil.do("通路を歩いていると、そこかしこで、作業用$w_droidが作業をしている姿を見かける",
                "どれも$w_cias社のマークがある"),
            emil.talk("ここには何人の人間がいるんですか？"),
            uru.talk("基本的に人間はいません",
                "人間は別の場所から遠隔で管理を行っているだけです"),
            emil.talk("それじゃあたとえば何か異常が発生した時には？"),
            w.eventPoint("ロボットの運用", "遠隔操作でシャットダウンできる"),
            uru.talk("個別にシャットダウンすることもできますし、",
                "施設そのものの電源を落とすことも可能です",
                "$w_droidたちも設備も、すべて電源が必要なので、それで一旦停止しますから、",
                "それから分析を行えばいいだけです"),
            uru.talk("つまり、他社のものと違い、",
                "我々の$w_droidは完全に自律し、人間の手を借りなくてもいいということです"),
            w.comment("ここで$w_droidの説明をする"),
            uru.talk("ではこちらへどうぞ"),
            emil.do("$uruに案内され、作業場に"),
            )

def sc_droidjob(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$w_droidたちの仕事",
            w.eventPoint("$w_droidについて", "$w_droidの仕事"),
            emil.come(),
            uru.come(),
            adam.be("作業している"),
            adam.do("ゴミを解体し、必要なものとそうでないものに分別して、破砕機に送る"),
            inside.look("沢山の$w_droidが並ぶ"),
            emil.do("それを上にあるハッチから見ている"),
            emil.do("$uruから説明を受ける"),
            uru.talk("こちらで彼らは一日十二時間、二交代で働き続けます"),
            emil.talk("半分で交代ですか？"),
            uru.talk("ええ", "多くの方はロボットであれば二十四時間使い続けても大丈夫と考えますが、",
                "機械部品は消耗品です",
                "稼働時間にともない劣化し、壊れます",
                "その耐久時間を考えて、今十二時間稼働にしています"),
            emil.do("その中の一体が、突然動かなくなる"),
            uru.talk("ああやって突然故障するのもロボットの特徴です",
                "人間のように徐々に悪くなる、といったことがほとんどありません"),
            uru.do("端末で連絡し、回収$w_droidを呼ぶ"),
            emil.do("回収されていくのを見ている"),
            adam.do("そのうちの一体が、一瞬運ばれていく仲間を見ていた",
                "だが後続に押されて作業に戻る"),
            camera=w.adam,
            stage=w.on_trashcollection,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_murdercase(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("殺人事件",
            emil.come(),
            uru.come(),
            emil.do("他の作業場も見せてもらった後で、最後に技師の部屋を尋ねる"),
            emil.talk("月に何日かメンテナーが来るんですか"),
            uru.talk("メンテナンス用のシステムの調子が悪かったので、緊急措置ですね",
                "基本的にはメンテナンスも含めて全て$w_droidが行います",
                "それが理想であり、効率として最も良いと結果が出ていますから"),
            uru.talk("こちらが技師の部屋になります",
                "彼が技術的なことについて、より専門的なことを答えてくれるでしょう"),
            uru.do("ドアを開ける"),
            emil.talk("え"),
            emil.do("そこには殺された技師$nielの姿があった"),
            )

## episode
def ep_murdercase(w: World):
    return w.episode("1.殺人事件",
            sc_tobira(w),
            sc_report_introduction(w),
            sc_interview(w),
            sc_droidjob(w),
            sc_murdercase(w),
            ## NOTE
            ##  - 世界観説明
            note="人間の為に労働専用のロボット「$w_droid」たちがいた。彼らはロボット三原則に従い行動していたが、何故か殺人事件が発生してしまう。$adamは人間に近づく為、捜査協力を買って出る")


