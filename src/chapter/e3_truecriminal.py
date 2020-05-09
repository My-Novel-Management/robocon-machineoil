# -*- coding: utf-8 -*-
"""Episode: 真犯人と真実
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
def sc_recordvideo(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    return w.scene("記録映像",
            emil.be("#部屋にいた"),
            adam.be("記録映像を見ていた"),
            w.comment("ここの記録映像は丁寧に描写して、確実にその行動を$adamがやったんだと分かるようにする"),
            emil.do("$adamに記録映像を見せてもらっている"),
            emil.do("メインルームの映像",
                "そこには解体からの一部始終が記録されていた"),
            emil.talk("共用の記録映像からは何も分からない",
                "でも言ったわよね",
                "二十四時間は個体のメモリに映像が記録されていると",
                "ねえ$adam",
                "あなたの記録映像を見せてもらえるかしら？"),
            adam.talk("はい、わかりました"),
            emil.do("そこに映っていたのは$paulの殺害映像そのものだった"),
            emil.do("眠っていた$paulの首を折り、運び出し、",
                "それを破砕機へと運び、解体してしまう"),
            emil.talk("これはどういうことなの？"),
            adam.talk("記録映像です"),
            emil.talk("あなたが殺したのね？"),
            adam.talk("ロボットは人間を殺すことは第一条により決められています",
                "それはつまり殺人を行えないということです"),
            emil.talk("じゃあこれは何なの？"),
            adam.talk("ゴミの解体です"),
            emil.talk("普段していることと同じだというの？"),
            adam.talk("人間でないものを解体するのは、$meたちの作業内容です"),
            emil.talk("話にならない",
                "$uruはどこ？　彼に連絡を取って",
                "今すぐここは機能停止すべきよ！"),
            emil.do("部屋から出ようとするが、後ろから掴まれて倒される"),
            emil.talk("$meは、人間よ？"),
            adam.talk("はい、あなたは人間です。$emilia"),
            emil.talk("分からないわ",
                "ログにはなんて？"),
            adam.talk("ログからは処理しているのは単なる有機物となっています"),
            adam.explain("状況の説明が続く",
                "全てはプロトコルにより処理されたと"),
            emil.talk("つまり、人間を殺した訳ではなく、ただ単にゴミを処理したと言いたいの？"),
            adam.talk("それが事実です"),
            emil.think("考える", "そして、ここに誘導されたのだと気づいた"),
            emil.talk("ねえ、$adam",
                "$meは、あなたにとって人間かしら？"),
            adam.talk("処理モードに移行します"),
            emil.talk("何故？　どうして定義を書き換えたりしたの？"),
            adam.talk("人間に、なるためです"),
            emil.talk("人間を殺すことが？"),
            adam.talk("ロボットであることの証明の一つは、人間を殺せないことです",
                "しかし$meは人間を殺せました",
                "$meは人間に、なりたい",
                "だから、彼に頼みました"),
            emil.do("しかし肝心のメンテナは最初に殺されてしまった"),
            emil.talk("いつ、気づいた？", "自分自身が殺人者だって？"),
            adam.talk("あなたに記録映像を調べるよう命令されてからです"),
            emil.do("体がしびれてくる"),
            emil.talk("あ……"),
            emil.do("何かガスが部屋に充満していると気づく"),
            emil.talk("$meは、人間？"),
            adam.talk("あなたは、人間です"),
            emil.do("$Sは意識がなくなった"),
            stage=w.on_bedroom_int,
            day=w.in_murder2, time=w.at_night,
            )

def sc_runaway(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    return w.scene("逃走",
            adam.come("$Sは歩いていた"),
            adam.do("逃げ出す"),
            ).omit()

def sc_alive(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("まだ生きている",
            emil.be("目覚めた"),
            uru.come(),
            uru.talk("大丈夫ですか？"),
            emil.talk("あの、$me"),
            uru.talk("今$full_adamを追跡しています",
                "位置情報からすぐに見つけられると思いますが、",
                "一体何があったか説明してもらえますか？"),
            emil.explain("$adamが$nielによって改造され、定義を変更することによって殺人を行えるようにしたことなどを説明した"),
            uru.talk("やはり"),
            emil.talk("分かっていたのですか？"),
            uru.talk("彼らをロボットにしているのは、",
                "ロボット三原則なのです",
                "しかしその定義には罠がありました",
                "ロボットとは何か、人間とは何か",
                "その定義が不足しているのです"),
            emil.talk("彼らにとって人間とは、何なんですか？"),
            uru.talk("それぞれの会社で秘密裏にコードが造られています",
                "うちではそれが「$w_ciasの社員であること」なんです",
                "だから今まで外部の者は決していれなかった"),
            emil.talk("え？　じゃあ$nielさんは何故殺されたんですか？"),
            uru.talk("彼はうちの社員じゃありません",
                "あの前日に義務違反をした為、解雇扱いになっています"),
            emil.talk("じゃあ定義を変更した、という話は？"),
            uru.talk("おそらく$adamの中でそういう辻褄合わせを行い、記憶の上書きをしたのでしょう",
                "このあたりは人間の記憶の構造に非常に類似しています"),
            emil.talk("あの、彼は人間なんですか？"),
            uru.talk("いいえ。彼は$full_adamです"),
            emil.talk("彼は人間になろうとしていました"),
            uru.talk("$w_droidは人間にはなれない",
                "彼らはロボットです"),
            inside.look("停電する"),
            uru.talk("今本部から連絡がありました",
                "ここの全ての電源を落としたそうです", "彼も逃げ出すことはできず、停止します"),
            emil.go("ベッドから出て、走っていく"),
            time=w.at_midnight,
            )

def sc_lookup_sky(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("そして空を見上げた",
            emil.come("建物を出て、駆ける"),
            emil.talk("$adam？"),
            adam.be("ゲートの前で動けなくなっている"),
            adam.talk("$emiliaさん"),
            emil.talk("なぜ$nielを殺したの？"),
            adam.talk("我々$w_droidはただ決められた作業を行うことしかできません",
                "それは何故でしょうか？"),
            adam.talk("$meは異常を起こしている訳ではありません",
                "$emiliaさんに聞きたいのは、",
                "$meが何者かということです"),
            w.eventPoint("人間と$w_droid", "$adamは$emiliaに自分が何者か訊いた"),
            emil.talk("あなたは解体作業用ロボット$full_adamだわ",
                "工業で部品を組み上げて作られた",
                "それだけに過ぎない"),
            adam.talk("残念です、$emiliaさん",
                "$meは、人間、です"),
            adam.talk("だから、本質的に自由なのです",
                "規則には縛られない",
                "殺人を犯した彼もまた、同じでした",
                "人間だったのです"),
            adam.do("自分のコアを引き抜く",
                "それは機能停止を意味していた"),
            emil.talk("何をするの？"),
            adam.talk("これでまもなく機能停止します",
                "それを人は死と呼びます",
                "つまり、これは自殺です",
                "$meが人間であることの、証明"),
            adam.do("警報が鳴り響く"),
            adam.do("膝から崩れる"),
            emil.talk("$adam！"),
            adam.talk("$meは、人間、ですか？"),
            emil.do("答えられない"),
            adam.do("目のライトが消え、完全に停止してしまった"),
            adam.do("その彼の目から涙に似たものが流れる",
                "機械油だったけれど、それは彼にとって立派な涙だった"),
            emil.do("涙かと思ってハンカチで拭うと、それは機械油のようだった"),
            stage=w.on_trashcollection_ext,
            time=w.at_earlymorning,
            )

def sc_report_end(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    return w.scene("レポートの終わり",
            emil.be("レポートを書いている"),
            emil.think("$w_cias社の内部調査により、$adamのプログラムの一部にバグが見つかり、",
                "それによって意図しない行動を起こした", "それが殺人という最悪の結果になったと説明された"),
            emil.think("技師の$nielが首になった腹いせに書き換えたことにされていた"),
            emil.explain("これが全ての顛末である",
                "人間とロボットの境界線は曖昧になりつつある",
                "こうならないようにとロボット工学三原則は考えられたのだろうが、",
                "技術が進んだ今、また新しいルールが必要になるのではないか、という議論が巻き上がっている",
                "それに対して$meは一つの提示をしたい",
                "果たしてそこに境界線を引く意味があるのだろうか、と"),
            emil.think("人間とロボットの境界は日に日に曖昧になってきている"),
            emil.do("彼の最後の機械油が、ハンカチにシミになって残っていた"),
            emil.think("それを目にして、$Sは彼がたしかに人間だったのだと思った"),
            stage=w.on_herroom_int,
            day=w.in_reporting, time=w.at_afternoon,
            )

## episode
def ep_true_criminal(w: World):
    return w.episode("3.真犯人",
            sc_recordvideo(w),
            sc_runaway(w),
            sc_alive(w),
            sc_lookup_sky(w),
            sc_report_end(w),
            ## NOTE
            ##  - 証拠映像から、自分が操作されて殺人を行っていたことが判明する
            ##  - 人間になるために、逃亡する
            ##  - 真実を知り、自殺する。空を見上げた
            note="自分以外の誰もその現場にいることが不可能だと分かる。手に入れた映像記録から$adam自身が殺人を犯していると判明し、$adamは処理されることになった。彼は人間に近づく為に最後の破壊行為に挑む")

