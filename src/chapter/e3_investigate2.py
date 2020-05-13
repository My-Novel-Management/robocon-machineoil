# -*- coding: utf-8 -*-
"""Episode: 事件捜査その２
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
def sc_nielroom(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$nielの部屋",
            emil.come("$nielの部屋の前に警備用のロボットすら立っていなかった"),
            adam.come(),
            emil.do("中に入るとテーブルの上に積み上げられていた資料は綺麗になくなっていて、",
                "既に$w_droidによる清掃の手が入った後のようだった",
                "$Sは気にせずそのまま奥のキッチンを覗く"),
            inside.look("移動するだけで照明が灯され、ピカピカに磨かれたシンクに僅かに水滴が残っているのが確認できた",
                "コンロにはケトルが一つ置かれていたが中は空っぽだ",
                "背面の棚は食器が並び、蓋がされている方には調味料が揃えられていた"),
            emil.talk("やっぱりあった"),
            emil.do("メモはしてなかったが設置されている冷蔵庫の中に缶ビールが六本、冷えていた",
                "$nielを探していた時に確認したものだ"),
            emil.talk("これは$nielさんが注文したの？"),
            adam.talk("彼の記録は抹消されています", "参照することができません"),
            emil.think("どういうことだろう", "既に社員じゃなくなった$nielに関するものは全て削除したということだろうか",
                "一応メモを取っておき、後で$uruにそれとなく質問してみようと思った"),
            emil.talk("これ、お一つ貰っても？"),
            emil.do("缶を手にするとひやりとした感覚が心地良い"),
            adam.talk("その冷蔵庫の中身は$meの管理下にないので、返答できません"),
            emil.talk("まあ、そっか"),
            emil.do("これも後で$uruに訊いて、問題なければいただこうと考えた"),
            emil.do("ベッドルームも確認したが、全然使われた形跡がない", "そもそも掃除されているなら今更調べても何も見つかりはしないだろう",
                "こうなると$paulから教えてもらえなかった監視カメラの記録映像が気になる"),
            emil.talk("ねえ$adam"),
            emil.do("ワークルームに戻り、そこの端末を動かしながら尋ねてみる"),
            emil.talk("メインサーバには全ての記録が残っているのよね？"),
            adam.talk("全て、ではありません"),
            emil.do("想定していた返答と違っていた"),
            emil.talk("記録に漏れがあるということ？　それともメインサーバとは別にどこかにバックアップがあって、",
                "そちらに全部保存されているとか？"),
            adam.do("$Sは淡々とした口調で答える"),
            adam.talk("記録は各$w_droidのメモリに一旦保管され、定期的にメインサーバに送られます",
                "記録する情報のレベルに応じて異なり、入退室の記録は一番間隔が短いものになります"),
            emil.talk("えっと、部屋の記録も$w_droid、つまりあなたたちなの？"),
            emil.do("$Sは慌てて部屋を見回す",
                "人型をしていないものもあるとは$uruから聞いていたが、どこにもそれらしいロボットは見つけられない",
                "壁や天井に埋め込まれているのだろうか"),
            adam.talk("部屋の入退室はセンサーで感知しています",
                "詳細については話せませんが、そこから近くにいる$w_droidに送信されて記録されます"),
            emil.talk("つまり、今はあなたに記録されているということかしら"),
            adam.talk("ゲストの方には答えられません"),
            emil.talk("まあそうよね",
                "でもそれじゃあ監視カメラの映像記録もあなたたちに記録されるのか",
                "それも各部屋のセンサーで記録したものが送られてくるの？"),
            emil.do("ロボットの受け答えは決められた規則を忠実に守る",
                "けれどそこには忠実さ故の弱点もあった",
                "$Sは彼の返答から事実を毟り取っていく"),
            adam.talk("各$w_droidの目が監視カメラの役割を兼ねています",
                "カメラで見えないところはセンサーで検知してデータを集めます"),
            emil.think("施設に入ってからずっと奇妙な視線を感じていた理由がそれなのだ",
                "だとすると$nielが殺された時も誰かがそれを見ていたのだろうか"),
            w.eventPoint("殺人事件１", "部屋には誰も入っていない＝人間以外は入っている"),
            emil.talk("$adam、この部屋の映像記録は参照できる？"),
            adam.talk("どのような映像記録であっても外部の人間にはその権限がありません"),
            emil.talk("それじゃあ入退室記録を教えて"),
            adam.talk("分かりました"),
            emil.do("彼から聞いた記録上では刑事が言っていたのと同じく、$nielは入室した後にこの部屋を出ていないことになっていた"),
            emil.talk("記録上はまだ$nielさんはこの部屋にいることになるのかしら"),
            adam.talk("施設内に現在人間は三人、です", "その中に$nielさんは含まれていません"),
            emil.think("彼に関する記録が消されていたと言っていたことを思い出す",
                    "亡くなったから削除した",
                    "本当にただそれだけなのだろうか",
                    "誰かが目的をもって彼を殺したとすれば、そこに理由のヒントが隠れているような気がする"),
            emil.talk("$meは警察じゃない"),
            adam.talk("はい", "$emiliaさんは警察ではありません"),
            emil.talk("分かっているからいちいち繰り返さないで", "それより$adam",
                    "あなたは何ができるの？"),
            emil.do("あまりに漠然とした質問だったからか、彼はじっとこちらを見たまま瞬きすらしない"),
            emil.talk("あー、えっとね、得意なことは何？"),
            adam.talk("ソフトがあれば何でも得意になります"),
            emil.talk("そうじゃなくてね……じゃあ好きなものは何？　お酒は飲む？"),
            emil.do("下手をすると二、三日ここに閉じ込められることになるかも知れない",
                    "そんな時に$uruはとても話し相手にはなってくれそうにないし、",
                    "お酒の相手になってくれると助かるのだけれどと考えたのだ"),
            adam.talk("好きなものは、まだ登録されていません",
                    "$emiliaさんの好きなものは何ですか？"),
            emil.talk("$meは、そうね、お酒や美味しい料理", "花もいいわね",
                    "それからやっぱり星", "夜空を見たことはある？"),
            emil.do("小さい頃、$Sは宇宙飛行士を夢見たものだった",
                    "小説や映画では技術の進歩で宇宙を気軽に旅行できるように描かれているものもよく見るが、",
                    "ロボットがこれだけ世間に普及しても未だにごく一部の人間を除いて宇宙に出ることは難しかった"),
            adam.talk("$meはこの施設から出たことはありません",
                    "星は綺麗ですか？"),
            emil.talk("ここは都市部が近いからそこまでじゃないけど、",
                    "$meが生まれた故郷の街なら真夜中になれば一面にばらまいたような星の絨毯が広がるわ",
                    "それを芝生に寝転んで見上げるの", "そうすれば自分なんてちっぽけな存在でしかないんだなって思えて、",
                    "どんな悩みでも大したことないって考えられた",
                    "いつかあなたも見られると良いわね"),
            camera=w.emilia,
            stage=w.on_nielroom_int,
            day=w.in_murder1, time=w.at_night,
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
            ).omit()

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
            ).omit()

def sc_2ndmurder(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("第二の殺人",
            w.symbol("　　　　◆"),
            emil.come("呼び出しを受けて$paulの部屋の前までやってきた時には、既に夜中の一時を回っていた"),
            adam.come(),
            emil.talk("すみません、$emiliaです"),
            emil.do("あれからすぐ自室に帰らず、しばらく$adamに施設内を色々と案内してもらっていたのがバレたのだろう"),
            emil.talk("あの？"),
            emil.do("覚悟をしてやってきたのに「入れ」の一言もない",
                "そのまま一、二分ほど声を掛けながら待っていたが何の応答もないので流石にどうかと思い、$Sはドアを開けた"),
            emil.do("部屋は無人だ"),
            emil.talk("ねえ$adam", "この部屋の入退室記録は分かる？"),
            emil.do("一緒に付いてきてもらった彼に尋ねる", "同じ二階にある部屋だから彼にもデータが届いているかも知れない"),
            adam.talk("分かります",
                "十一時四十八分三十秒に$paulさんが入室しています"),
            emil.do("今から一時間も前だ"),
            emil.talk("退室記録は？"),
            adam.talk("ありません"),
            emil.think("嫌な予感だった",
                "$Sは慌てて奥のベッドルームやキッチンを覗く",
                "しかしそこには誰の姿もない"),
            emil.talk("$adam"),
            adam.talk("何でしょう？"),
            emil.talk("今すぐ$w_hallの破砕機を止めて"),
            adam.talk("それはできません"),
            emil.talk("なぜ？"),
            adam.talk("あなたは$w_ciasの社員ではないからです"),
            emil.do("確かに彼の言う通りだった",
                "けれど状況は限りなく$nielが死んだ時に似ている",
                "$Sは慌てて$adamに$uruと連絡を取るように言った"),
            emil.talk("それから今すぐ機械を止めるようにお願いして"),
            stage=w.on_paulroom_int,
            )

def sc_cannot_out(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("出られない",
            w.symbol("　　　　◆"),
            emil.be("#自室にいる"),
            emil.explain("$paulの遺体は破砕機によって砕かれる寸前だった",
                "遺体と言っても腕や足が胴から切り離され、とても人間と呼べる代物ではなかったそうだ",
                "警察のロボットにより運び出され、一応検死に回されると聞いた"),
            uru.come("部屋のドアがスライドし、$Sがやや青白い顔をして入ってくる"),
            emil.talk("あの、どうだったんですか？"),
            uru.talk("事前に殺害され、その後でバラバラにされた状態でベルトコンベアに乗せられたらしい",
                "警察の話では一件目と同じだそうです"),
            emil.talk("つまり、完全に他殺で間違いないということですか？"),
            uru.talk("$meは警察ではないからそのあたりの判断は新しく派遣されてくる刑事に確認するしかないでしょう",
                "ただこうも立て続けに同じ状態で死人が出るのは他殺と考える方が論理的だと思いますが"),
            emil.think("しかし殺人事件の多くは何か犯人が利益を得る行動を目指したもの、あるいはその結果として起こったものだ",
                "これは犯人が何の利益を得ているのだろうか、と$Sは考え込んでいた",
                "$nielは元社員だから$w_ciasに何か関係があってもおかしくない",
                "だが二件目の$paulは刑事だ",
                "この二人に何か共通項があるとは思えない"),
            emil.talk("$uruさん",
                "あなたは何故$nielさんが殺されたとお考えですか？",
                "彼は何か会社にとって厄介な人間だったのでしょうか？"),
            uru.talk("何故そんな質問を？",
                "もし仮に彼が我が社に恨みを持っていたとして、それを$meが殺害したとでも言いたいんですか？"),
            emil.do("殺人を行うのは人間だ",
                "その前提に立った時、外部犯の可能性を排除すれば必然$uru犯人説が浮上する",
                "警察もおそらくその方向から捜査を始めたことだろう",
                "ただ人を殺してまで守りたい何かがあるとは$Sには思えない",
                "それは気分を害している$uruの表情を見ても、変わらない気持ちだった"),
            uru.talk("殺人というのは人間が行う異常行動の一種です",
                "ロボットでは起こり得ません",
                "だからあなたが$meを犯人と考えるのもまともな推論と言えます",
                "しかし残念ながら$meは彼とほぼ面識がない",
                "$meは会社の広報で、彼は技術者だ",
                "名前以上の情報を$meは持っていません"),
            emil.do("それが本当かどうかは確かめようがない",
                "それでも$uru犯人説は今こうやって話している$Sを手に掛けようとしないことからも、かなり可能性の低い説と言わざるを得なかった"),
            emil.talk("なら$uruさんは何故事件が起こったと？"),
            uru.talk("$meは専門家ではない、という前提で聞いて下さい",
                "一番可能性が高いのは$meたち$w_ciasへの攻撃でしょうね",
                "$w_droidを用いた工場は他の企業からすれば驚異になります",
                "事実、あなたたちのニュースでも我々のライバル企業の提灯記事ばかり書いているでしょう"),
            emil.think("一部はその通りだが$Sは全くタッチしていない",
                "それでも言い返せるほどの公明正大さは無く、黙ってばつの悪いのを我慢するしかなかった"),
            uru.talk("今やロボット技術を持つ者が社会をリードするのです",
                "その中において情報戦というのは強力な武器であり、あなたをここに招いたのもその一環だったのです",
                "ただこんな事件が起きてしまいましたが"),
            emil.talk("もし人為的なものではない場合、他の考えられる可能性は$w_droidが人を殺した、ということになります",
                "それについてはどうなんですか？"),
            uru.talk("それは他の企業同様、有り得ません",
                "ロボット工学三原則により厳重に禁止されていますし、",
                "そうプログラミングされています",
                "もし第一条に違反しようものなら即座に機能停止し、異状を知らせる信号が送られるようになっています"),
            emil.do("$uruの返答は予想通りのものだった",
                    "ロボットに殺人は犯せない",
                    "しかし今までに幾つか記事を書いたロボット反乱事件では実際にロボットによる殺人が起こっていた",
                    "確かにそれらはプロテクトを破って人為的にプログラムをクラッキングすることでそれを可能にしていたが、",
                    "今回の場合もそういったことはない、とは言えないと$Sは思っている"),
            emil.talk("それで、$meはどうすればいいでしょうか"),
            emil.think("警察のロボットは残っているとは言っても、彼らが殺人鬼ではない保証はない"),
            uru.talk("一時間ほど後に新しい刑事がやってくるそうです",
                "それまではこちらで待機ですかね", "部屋に閉じ籠もって誰も入れなければおそらく安全ですよ",
                "別に$meと一緒にここで待つという選択もあります"),
            emil.do("薄く笑みを浮かべる$uruを見てその選択肢は真っ先に切り捨てられた"),
            emil.talk("自室で待たせてもらいます",
                    "刑事さんが来たらそう伝えて下さい"),
            emil.do("つまらなさそうに「わかりました」と答えた$uruに業務用の笑顔を向けてから、席を立った"),
            emil.talk("あ、一つだけ", "$nielさんの部屋の冷蔵庫にあった缶ビール、少しいただいてもいいですか？"),
            uru.do("彼は一瞬困ったように眉を顰めた後で、こう答えた"),
            uru.talk("この施設内は業務用以外のアルコールは厳禁なんですよ"),
            stage=w.on_bedroom_int,
            )

def sc_humanworld(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    worker = W(w.worker)
    return w.scene("人間に憧れる$w_droidたち",
            emil.come("$uruと別れた後、$Sは真っ直ぐ部屋には戻らずにぼんやり考え事をしながら通路を歩いていた"),
            inside.look("すぐ側を台車型の$w_droidが梱包ケースを載せて通り過ぎていく",
                "他にも何の作業をしているのか分からないが、手ぶらで歩いているモスグリーンカラーの$w_droidたちとすれ違った", "&"),
            emil.think("彼らは皆一様に肩や装甲に眼鏡を模した$w_cias社のマークが描かれていて、",
                "それはずっとどこかで見た光景に似ていると思っていたのだけれど、不意に陸軍の取材に同行した時に見たものだと分かった",
                "どの$w_droidものっぺりと同じ色で決められた通りに動いているのが軍隊のそれに見えるのだ"),
            emil.talk("ねえ、ちょっといいかしら"),
            worker.be(),
            emil.do("通路を歩いていた一体の$w_droidに声を掛けてみる"),
            worker.talk("はい、何でしょうか、$emiliaさん"),
            emil.do("やはり$Sの情報は共有されている"),
            emil.talk("あなたたちは個人のメモリを持っていると聞いたけれど、",
                "そこには映像記録もあるのよね？"),
            worker.talk("はい",
                "$meたちは個体毎にメモリがあり、そこに蓄積された情報は原則二十四時間保持されます"),
            emil.talk("二十四時間経つとその記録はどうなるの？"),
            worker.talk("必要なものを除き処分されます",
                "つまり必要とされる情報だけがメインサーバに送られ、蓄積されます"),
            emil.talk("そう", "分かったわ", "ありがとう"),
            emil.do("お礼を言ってその$w_droidを見送ると、$Sは急いで携帯端末で$adamに連絡を取ろうとした"),
            adam.come("#ひっそりと現れた彼"),
            adam.talk("何かご用でしょうか、$emilia様"),
            emil.do("振り返ると背後一メートルに、彼は立って彼女を見つめていた"),
            emil.talk("あの、お願いがあるの"),
            #   ここから何かに気づいて、映像記録を確かめる展開
            stage=w.on_pathway,
            time=w.at_night,
            )

## episode
def ep_investigation2(w: World):
    return w.episode("3.事件捜査その２",
            sc_nielroom(w),
            sc_mainroom(w),
            sc_aboutadam(w),
            sc_2ndmurder(w),
            sc_cannot_out(w),
            sc_humanworld(w),
            ## NOTE
            ##  - 第二の殺人事件
            note="人間の捜査官と共に事件について調べる。そのうちに第二の殺人が発生する。そしてそれを調べていた人間は突然目の前から姿を消してしまった")
