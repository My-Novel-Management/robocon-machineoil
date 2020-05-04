# -*- coding: utf-8 -*-
"""Episode: 事件捜査
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
def sc_aboutcase(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("事件について",
            emil.be("取り調べを受けていた"),
            paul.be("捜査端末を手に、質問している"),
            paul.talk("それで、部屋に入ったときには亡くなっていたと、そう言うんだな？"),
            paul.look("ぴっちりしたスーツに、髪も固めている"),
            emil.talk("はい、そうです"),
            w.eventPoint("殺人事件１", "$emiliaの聴取"),
            w.comment("ここで刑事を登場させ、関係を作っておくと共に、外部の人間が入ってきて困っていることを"),
            emil.do("ただ見たことを話した",
                "自分は取材に訪れただけで、面識すらなかったこと等"),
            paul.talk("では、$nielが前日に契約解除になり、ここを去る準備をしていたことは？"),
            emil.talk("知りませんでした",
                "$uruさんからもそんな話は聞いていません",
                "どういうことなんでしょう？"),
            paul.talk("それを調べるのは$meの仕事だ"),
            emil.talk("$meはどうすれば"),
            paul.talk("泊まっているホテルの住所、連絡先を教えてもらい、",
                "可能ならしばらくホテルに籠もっていてもらいたい",
                "重要参考人だからね"),
            emil.talk("ここのことを記事にしないといけないんです"),
            paul.talk("取材日は今日だけだったと聞いている",
                "それなのにまだ数日ここにいたいとは、どういうことだ？"),
            emil.talk("ただの好奇心です",
                "ここには今日訪れた$meと$uruさんを除くと、人間は彼だけでした",
                "そこで殺人事件は起こらないはずなんです",
                "外部から侵入した形跡はないんですよね？"),
            paul.talk("だから困ってるし、君か彼のどちらかが犯人だと思っている",
                "というか、どこでそんな情報を？"),
            emil.talk("$uruさんから"),
            emil.do("その後、交渉で、この施設から出ない代わりに、調査して回ることは許可してもらえた",
                "ただし、お目付け役の$w_droidがついた"),
            )

def sc_research(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("調査",
            emil.be(),
            uru.be(),
            adam.be(),
            uru.talk("この$full_adamが、全てを記録してくれる",
                "$meの方も何もせずに部屋にいるよう言われているからね"),
            adam.talk("よろしくおねがいします"),
            emil.talk("ええ、こちらこそ"),
            uru.go("部屋を出ていく"),
            emil.talk("まずは$nielさんの部屋に案内してもらえないかしら"),
            )

def sc_nielroom(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$nielの部屋",
            emil.come(),
            adam.come(),
            emil.do("部屋にやってくると、既に綺麗に片付けられていた"),
            emil.talk("事件当時の現場映像は残っていないの？"),
            adam.talk("その記録は警察により押収されています"),
            emil.talk("困ったわね",
                "$meとのインタビューに備えてここで待機していたと思うのだけれど、",
                "それに関する記録はある？"),
            adam.talk("入室の記録はすぐ照会可能です"),
            emil.do("どうやら部屋に入ってからずっと資料を読み込んでいたらしい"),
            emil.talk("他に部屋に入った人は？"),
            adam.talk("記録にありません"),
            w.eventPoint("殺人事件１", "部屋には誰も入っていない＝人間以外は入っている"),
            emil.talk("つまり、一人で部屋に入って次に$meが入るまで本当に誰も入っていない？"),
            emil.think("密室殺人、というよくある推理ものにある言葉が浮かぶ",
                "しかし現実は何かの細工を使ったり、あるいは観測した状態がそう見えているだけ、",
                "といったものが多い"),
            emil.talk("何か見落としていることがあるはず"),
            emil.do("もう一度、施設を案内してもらった"),
            )

def sc_aboutadam(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$adamについて",
            emil.come("居室に戻ってくる"),
            adam.come(),
            emil.do("施設内を案内してもらったが、どこも機械管理していて、人間の入るすきがない",
                "そもそも何故殺人が起こったのか、$Sには分からなかった"),
            emil.talk("ありがとう"),
            emil.talk("ねえ、あなたのことを教えてくれる？"),
            adam.talk("$meは$full_adamです",
                "解体作業を行います"),
            emil.talk("あなたはどこで生まれたの？"),
            adam.talk("$w_cias社の$w_droid生産工場です"),
            emil.do("基本的な情報しか答えてくれない"),
            emil.talk("じゃあ、好きなものは何？"),
            adam.talk("好きなもの？", "わかりません"),
            emil.do("記録されているもの以外の会話は学習しないようになっているようだ"),
            emil.talk("あなたたちは本当に作業のことしか教えられていないのね",
                "ロボットの反乱事件がいくつか起こっているのを見ると、",
                "ロボットに高度な知能は必要ないのかも知れないとすら思える"),
            adam.go("部屋を出ていく"),
            emil.do("一人になり、整理する"),
            emil.think("どうしても気になり、$uruに連絡を取ってみたが、彼は事情聴取中とのことだった"),
            emil.do("端末を取り出し、レポートをまとめていく"),
            )

def sc_2ndmurder(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("第二の殺人",
            emil.come("その日の夜、$uruに会う為に部屋を訪れる"),
            emil.talk("すみません、$emiliaです"),
            emil.think("妙だと感じて部屋に入ると"),
            emil.talk("え"),
            emil.do("そこには$paulが倒れていた"),
            adam.come(),
            adam.talk("どうかしましたか？"),
            emil.talk("救急車を呼んでください"),
            emil.do("既に息がないように見えた"),
            emil.think("それからこれが第二の殺人事件なんだとようやく気づいて、",
                "この施設内から人間が消されていっているのを感じた"),
            )

def sc_cannot_out(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("出られない",
            emil.be("自室にいる"),
            emil.explain("$paulは搬送用$w_droidにより運び出されていった"),
            uru.come("入ってくる"),
            emil.talk("あの、どうだったんですか？"),
            uru.talk("完全に切断され、亡くなっていたらしい",
                "一件目と同じだ"),
            emil.talk("$meはどうすればいいでしょうか"),
            uru.talk("一時間ほど後に新しい刑事がやってくるそうだ",
                "それまでは待機ということになる"),
            emil.talk("あの、思ったんですが、これって世間で起こっているロボットの反乱ではないんですか？"),
            uru.talk("うちではそれはありえない"),
            emil.talk("確かに他の反乱を起こしたロボットたちは、どれも知性があります",
                "しかしここ$w_ciasのものは完全に専業用に作られたものばかりでした",
                "けれど、それだから安全とは思えないんです",
                "$meはどうも、ここから人間を追い出そうとしているようにしか"),
            uru.talk("そういう余計な推測こそ、人間らしさではないですか？",
                "この件に関しては専門家に任せればいい",
                "あなたは事情聴取が終わり次第、ここを出ていってください"),
            emil.talk("すみませんでした"),
            uru.go("出ていく"),
            )

def sc_humanworld(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    worker = W(w.worker)
    return w.scene("人間に憧れる$w_droidたち",
            emil.come("歩いていた"),
            emil.do("施設内では解体作業だけでなく、多くの$w_droidが働いていた",
                "人間はいない"),
            emil.talk("ねえ、話は理解できるかしら"),
            worker.be(),
            worker.talk("はい、何でしょうか、$emiliaさん"),
            emil.do("どうやら情報は全て共有されているらしい"),
            emil.talk("あなたたちはそれぞれ自分の映像記録を持っているのかしら"),
            worker.talk("はい", "$meたちは個体別にメモリが搭載されています",
                "作業内容に関しては中央サーバに情報を送り共有していますが、",
                "各々がメモリを持つことは禁じられていません"),
            emil.talk("それじゃあ、命じられない限り、各個体のメモリはそのままなのね？"),
            worker.talk("そうです"),
            emil.think("ずっと同じ部屋にいた$adamの記憶を探すことを考える"),
            emil.talk("ねえ、$adamに連絡は取れる？"),
            adam.come("ひっそりと現れた彼"),
            emil.talk("あの、お願いがあるの"),
            #   ここから何かに気づいて、映像記録を確かめる展開
            )

## episode
def ep_investigation(w: World):
    return w.episode("2.事件捜査",
            sc_aboutcase(w),
            sc_research(w),
            sc_nielroom(w),
            sc_aboutadam(w),
            sc_2ndmurder(w),
            sc_cannot_out(w),
            sc_humanworld(w),
            ## NOTE
            ##  - 第二の殺人事件
            note="人間の捜査官と共に事件について調べる。そのうちに第二の殺人が発生する。そしてそれを調べていた人間は突然目の前から姿を消してしまった")

