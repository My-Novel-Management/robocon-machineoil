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
            inside.look("取り調べ用の部屋",
                "窓がなく、同じように奥にキッチン周りがある",
                "テーブルを挟み、座っている"),
            paul.talk("それで、部屋に入ったときには誰もいなかったと、そう言うんだな？"),
            paul.look("ぴっちりしたスーツに、髪も固めている"),
            emil.talk("はい、そうです"),
            w.eventPoint("殺人事件１", "$emiliaの聴取"),
            w.comment("ここで刑事を登場させ、関係を作っておくと共に、外部の人間が入ってきて困っていることを"),
            paul.do("事件について、最初から順に尋ねていく"),
            paul.talk("もう一度尋ねる", "記録通りならあなたが$niel氏の次に入室したことになっているが、",
                "それは彼と約束があり、その通りにやってきたから、ということでいいんだな？"),
            emil.talk("そうです", "さっきも言いましたが$meは$on_RobertCom社の記者で、今回取材に訪れただけなんです",
                "$nielさんとは面識がありません", "今日社員の方から技術的な話をしてくれる人として彼を紹介してもらったんです"),
            paul.do("端末を操作している", "そこに何か書き込んでいるようだ"),
            paul.talk("監視カメラはないし、入室記録はデータだし、全くこれだからロボットだらけの会社は困るんだ"),
            emil.do("ただ見たことを話した",
                "自分は取材に訪れただけで、面識すらなかったこと等"),
            emil.explain("$uruから聞いたことを、ほぼそのまま話した",
                "部屋には誰もいなかったこと、それは部屋の入出記録からもその通りだと"),
            paul.talk("それじゃあ本当に$nielは何らかの手段でここから出て、それは記録されず、",
                "自分であそこにいって解体されたというのか？"),
            emil.talk("$meは知りません", "詳細は全部$uruさんから聞いたものですから"),
            paul.do("頭を抱える"),
            paul.talk("記録映像では動かなくなった$nielが、まるでゴミのようにロボットに運ばれ、",
                "そのまま彼らによって手足をバラバラにされてから、ベルトコンベアに投げ入れられ、その後、破砕機によって粉々に砕かれている"),
            paul.do("$Sの端末にはその際の映像があった", "白黒に彩度が落とされているのは血を見せないようにとの配慮だろう"),
            paul.talk("では、$nielが前日に契約解除になり、ここを去る準備をしていたことは？"),
            emil.talk("知りませんでした",
                "$uruさんからもそんな話は聞いていません",
                "どういうことなんでしょう？"),
            paul.talk("それを調べるのは$meの仕事だ"),
            emil.think("部屋から出た記録がないのに、どうやって外に出たのかが謎だった"),
            emil.talk("$meはどうすれば"),
            paul.talk(
                "可能ならしばらくここにいて動かないでもらいたいが",
                "重要参考人だからね"),
            emil.talk("記事を書かないといけないんです", "仕事はしてもいいでしょうか？"),
            paul.talk("部屋の中でできることであれば", "自殺とは考えづらいので、やはり何かしら入室記録がつかない殺人鬼でもいるという可能性を考えざるを得ない",
                "幸いここには人が少ない", "部屋に誰も入らなければ安全は担保される"),
            emil.think("$uruさんに掛け合ってみようと考えた"),
            paul.talk("とりあえず連絡が取れるようにしておいてもらいたい",
                "端末は持っているね？"),
            emil.talk("はい"),
            emil.do("腕時計型の端末の連絡アドレスを交換した"),
            stage=w.on_paulroom_int,
            )

def sc_research(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("調査",
            emil.be("部屋にいる"),
            uru.be(),
            adam.be(),
            emil.do("簡易ベッドの感触を確かめ、ホテルと大差ないと驚く"),
            uru.talk("かつて研究スタッフが使っていたものだ", "宿泊機能は一通り揃っているから、ここで我慢してもらいたい"),
            emil.talk("いえ、充分です",
                "それよりも$meはどうすればいいでしょう"),
            uru.talk("外出は出来ないようにしてくれと言われた"),
            uru.do("中の過ごし方を教えてくれる",
                "$adamを迎え入れて"),
            uru.talk("この$full_adamが、全てを記録してくれる",
                "$meの方も何もせずに部屋にいるよう言われているからね"),
            emil.talk("さっきもお世話になったけれど、彼は特別なんですか？"),
            adam.look("右肩のオレンジのカラーリングが目立つ",
                "しかしそれが肩に本来書かれている$w_cias社のマークを隠してしまっていた"),
            uru.talk("ここでは特別な個体はいません",
                "すべてが平等、いや、序列がない、というか、",
                "人間のような上下関係は存在しないんですよ",
                "ただ作業内容によって役割を分けているだけです"),
            emil.think("同じことを言わせてしまったと後悔する"),
            adam.talk("よろしくおねがいします"),
            emil.talk("ええ、こちらこそ"),
            uru.go("部屋を出ていく"),
            emil.talk("あなたに聞けば施設の記録も教えてもらえるのね？"),
            adam.talk("はい、そうです"),
            emil.talk("なんて呼べばいいかしら"),
            adam.talk("$meは$full_adamです"),
            emil.talk("型番とかじゃなくて、そうね……$adamでどうかしら"),
            adam.talk("$adam", "わかりました$emilia様"),
            emil.do("レポートをしようと端末を前にする"),
            emil.talk("そういえばこの部屋の入室記録って、あなたに聞けば教えてもらえるの？"),
            adam.talk("はい", "それはゲストのあなたでも許可されています"),
            emil.do("入室記録を確認すると、確かに入ったことになっている",
                "$uruが出た記録が一番最新だ"),
            emil.do("記録方式を聞いて、考える"),
            emil.talk("でもそれじゃあ上書きしても分かるようになっているのね",
                "分からないわ", "一体どういうことなのか"),
            emil.talk("まずは$nielさんの部屋に案内してもらえないかしら"),
            stage=w.on_bedroom_int,
            )

def sc_nielroom(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$nielの部屋",
            emil.come(),
            adam.come(),
            emil.do("部屋にやってくると、既に綺麗に片付けられていた"),
            inside.look("部屋の内装、改めて描写",
                "どこも同じ間取り",
                "入り口から右手か左手側に机と端末、",
                "テーブル、奥にキッチン",
                "簡易ベッドが置かれて寝室に使えるのがドア向こう"),
            emil.do("$adamから彼らの目が監視カメラ代わりになっていると聞く"),
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
            emil.talk("それじゃあ映像は全てサーバに？"),
            adam.talk("共有すべきものは全てメインサーバに送ります",
                "しかしそうでない情報は二十四時間は各個体のメモリに保持されます"),
            emil.talk("それじゃあ二十四時間以内に移さない映像記録は消えるの？"),
            adam.talk("消えても問題ないものばかりです"),
            emil.talk("何か見落としていることがあるはず"),
            emil.do("もう一度、施設を案内してもらった"),
            stage=w.on_nielroom_int,
            )

def sc_mainroom(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("Re:殺害現場",
            emil.come("メインルームに入る"),
            adam.come(),
            emil.do("$adamに案内してもらい、初めて下に降りた"),
            emil.talk("今は作業停止しているの？"),
            adam.talk("会社から止めるよう指示を受けています"),
            emil.do("見ると殺された後は見つからない"),
            emil.talk("血とかは既に掃除済かしら"),
            adam.talk("作業に支障が出る障害物は清掃用$w_droidによって綺麗にされます"),
            emil.do("一通り見て回る"),
            stage=w.on_dismantlinghall_int,
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
            adam.talk("食事はデリバリーを取りましたので、後で運びます"),
            emil.talk("助かるわ"),
            adam.go("$Sは部屋を出ていく"),
            emil.do("一人になった$Sは端末を前にして、考える"),
            emil.think("用意された水を飲みながら、一つ一つ整理する"),
            emil.think("$adamについて、メモをまとめる"),
            emil.do("メモには$w_droidの特性や、メインサーバとのやり取りのこと、監視カメラの代わりになっていること",
                "そういったことが列記されている"),
            emil.think("そもそも首になったから自殺した、というのはありえそうだ",
                "しかし、直前まで取材を受ける準備をしていたことからそう考えるのは難しい"),
            emil.think("死体はどう認識されるのだろうか"),
            emil.think("どうしても気になり、$uruに連絡を取ってみたが、彼は事情聴取中とのことだった"),
            emil.do("端末を取り出し、レポートをまとめていく"),
            stage=w.on_bedroom_int,
            )

def sc_2ndmurder(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("第二の殺人",
            emil.come("その日の夜、$paulに呼び出され、彼の部屋を訪れる"),
            emil.talk("すみません、$emiliaです"),
            emil.do("不用意に施設内を歩き回ったことを注意されるのだろうと思って立っていたが、",
                "特に入室を促す声などはない"),
            emil.think("返事がなく、妙だと感じて部屋に入ると"),
            emil.talk("え"),
            emil.do("そこには誰もいない"),
            emil.do("彼の端末がそのまま置き去りにされているのを発見する"),
            emil.do("その端末から、彼が何かに気づいて書き残そうとしたところで、",
                "何かあったのだと分かる"),
            emil.think("考えて、$adamを呼ぶ"),
            adam.come(),
            adam.talk("どうかしましたか？"),
            emil.talk("入室記録を教えて"),
            adam.do("この部屋の記録を見せてもらう"),
            emil.talk("あの、今すぐ破砕機を止めて"),
            adam.talk("それはできません"),
            emil.talk("なぜ？"),
            adam.talk("あなたは$w_ciasの社員ではないからです"),
            emil.do("$uruに連絡を取るように言う"),
            emil.talk("もういい！"),
            emil.do("部屋を出て、作業工場に向かう"),
            emil.do("しかしそこにたどり着いた時には、$paulが破砕機によって裁断されるところだった"),
            stage=w.on_paulroom_int,
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
            emil.talk("それはつまり、自殺としか考えられない他殺ということでしょうか"),
            uru.talk("$meは警察ではないからそのあたりの判断は、新しく派遣されてくる刑事に聞くしかないだろう",
                "ただ二日も連続して同じ施設内で起こるのは不自然だから、他殺と考えるのが論理的だと思いますが"),
            emil.think("しかし殺人事件の多くは何か犯人が利益を得る行動を目指したもの、あるいはその結果として起こったものだ",
                "これは犯人が何の利益を得ているのだろうか、と考え込む"),
            emil.talk("$meにはよく分かりません",
                "首になった技官と事件捜査にきた刑事さんに関連性は見出だせない上、",
                "殺人による利益を誰が得ているんでしょう"),
            uru.talk("殺人は人間が行う異常行動の一種です",
                "そこに論理的な回答を求めるのは間違っていると思いますが"),
            emil.talk("なら$uruさんは何故事件が起こったと？"),
            uru.talk("$meは専門家ではない",
                "その前提で聞いてもらえればと思いますが",
                "可能性が高いのは$meたち$w_ciasへの攻撃でしょう",
                "$w_droidを用いた工場は他の企業からすれば驚異でしょう",
                "そこに悪評を立てるというのは企業戦略としてあります"),
            emil.think("それは$Sも考えたが、それこそ他の企業のようにロボットたちが反乱を起こしたとかでもなければおかしい気がした"),
            emil.talk("$w_droidが人を殺すことはないんですよね？"),
            uru.talk("それは他の企業でも同じです",
                "ロボット三原則により厳重に禁止されていますし、",
                "そのプロトコルが仕込まれています",
                "第一条に違反しようとした途端に電源が落ちます"),
            emil.think("あとの可能性は$uruが犯人の可能性だったが、彼にしても殺人を犯すメリットがないようにしか思えなかった"),
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
            stage=w.on_bedroom_int,
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
            stage=w.on_pathway,
            time=w.at_night,
            )

## episode
def ep_investigation(w: World):
    return w.episode("2.事件捜査",
            sc_aboutcase(w),
            sc_research(w),
            sc_nielroom(w),
            sc_mainroom(w),
            sc_aboutadam(w),
            sc_2ndmurder(w),
            sc_cannot_out(w),
            sc_humanworld(w),
            ## NOTE
            ##  - 第二の殺人事件
            note="人間の捜査官と共に事件について調べる。そのうちに第二の殺人が発生する。そしてそれを調べていた人間は突然目の前から姿を消してしまった")

