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
            w.symbol("　　　　２"),
            emil.be("#取り調べを受けていた"),
            paul.be("#捜査端末を手に、質問している"),
            emil.do("白い壁はどの部屋でも変わらないらしい",
                "$Sはテーブルを挟んで淡々と事実関係を確認するグレィのスーツ姿の男性を前にして、",
                "ジャケットから手帳を取り出したくなっていた"),
            paul.talk("それで$nielがいる部屋に入った時には誰もいなかった、そう言いたいんだな？"),
            paul.do("声音こそ穏やかだが口調は完全に尋問のそれだ", "&"),
            _.look("ウェーブの掛かった銀色の前髪を何度も掻き上げ、常に眉間に皺を寄せて鋭い眼光を飛ばしている","&"),
            emil.think("$paulという名すらコードネームなんじゃないかと$Sは疑っていた"),
            emil.talk("ええ、そうです", "さっき話した通りです"),
            emil.do("緊張気味に答え、小さく息をつく"),
            paul.talk("入室記録から$nielが部屋に入った四十二分後にあなたが入っている",
                "彼は部屋から出ていない", "そのことについて何か弁解は？"),
            emil.do("だが息を吐き終えるまでに彼は次の質問を差し込んだ"),
            emil.talk("だから$meは$uruさんと一緒に入室しています",
                "そもそも$nielさんの記録が間違っている可能性はないんですか？"),
            inside.look("奥のキッチンやベッドルーム、テーブルの配置が対象になっているだけで、",
                "$uruが取り調べに使って下さいと刑事に用意した部屋は$nielが待っていた場所とほぼ同じ間取りだった"),
            paul.talk("人間の言葉よりコンピュータによる記録の方が正確だという一般論を否定するだけのデータを、",
                "あなたは持っているのか？"),
            emil.talk("それは知ってます", "ですけどこの場合は"),
            paul.talk("部屋に入って$nielがいないと気づいてから$uruがあなたを端末で呼ぶまでの間、何をしていた？"),
            emil.do("反論や意見を口にする間もなく矢継ぎ早に質問が浴びせられる"),
            emil.talk("部屋のどこかに彼がいるんじゃないかと思って改めて探していました"),
            paul.talk("それを証明できるものは？"),
            emil.talk("知りませんよ", "監視カメラはないんですか？"),
            paul.talk("ある", "だが答えられない"),
            emil.do("肝心なことについては何も教えてもらえない",
                "いつもこうだ"),
            emil.do("事件に関する情報について上手く聞き出すのは取材技術だと先輩に教わったが、",
                "最初から教える気のない相手からはどうやっても引き出すことはできないと諦めることも大事だった").omit(),
            w.eventPoint("殺人事件１", "$emiliaの聴取"),
            w.comment("ここで刑事を登場させ、関係を作っておくと共に、外部の人間が入ってきて困っていることを"),
            paul.talk("その後、$nielの遺体が$on_dismantlinghallで発見されるまで部屋から動かなかった、という訳だな？"),
            emil.talk("そうです", "何度も言いますけど、$meは$nielさんのことを全然知らないし、",
                "そもそも今日初めて名前も聞きました", "$uruさんは何て言ってましたか？"),
            paul.do("それは答えられない、と即座に$Sは突っぱねた"),
            emil.talk("もういいですか？", "$meが話せることは全て話しました"),
            emil.do("執拗に同じことを何度も訊かれると、ある程度覚悟をしていても精神的な疲労は相当なものだった",
                "途中で飲み物を欲しいと要求したが聴取が終わるまでは我慢しろと言われ、そのことも輪を掛けて$Sの精神を抑圧した"),
            paul.talk("それではもう一度最初から確認する"),
            emil.think("もういい加減にして欲しいと心の中で特大の溜息をつき、",
                "これで最後であることを願って$paulに付き合った"),
            stage=w.on_paulroom_int,
            time=w.at_askemilia,
            )

def sc_aboutcase2(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("尋問後",
            w.br(),
            emil.be(),
            paul.be(),
            emil.talk("それで、$meはどうすればいいんですか？"),
            emil.do("更に三十分以上たっぷりと尋問を受け、ようやく解放されることになった"),
            paul.talk("こちらに泊まってもらう"),
            emil.talk("ここに、ですか？"),
            paul.talk("そうなるな",
                "快適とは言えないだろうが部屋の前には警備用ロボットも立たせる",
                "外部とやり取りすることは許可できないが、",
                "端末を利用して仕事をすることは許可が出た",
                "ただ本件についての記事を書いたりすることは、分かっていると思うがやめてもらいたい"),
            emil.do("警察と新聞社間の協定を持ち出し、念を押してから立ち上がると、$paulは額を押さえて溜息を零す",
                    "おそらく厄介な事件だと考えているのだろうが、巻き込まれた方はもっと頭が痛いと文句を言いたくなった"),
            emil.talk("あの"),
            emil.do("部屋を出ていこうとした彼を呼び止める"),
            emil.talk("$meの使う部屋はここですか？"),
            paul.talk("いや、", "$uruという社員に手配してもらっている",
                    "誰かが呼びに来るまではここから動かないでもらいたい", "いいな？"),
            emil.do("イエス以外の選択肢がないことを分かっていてわざわざ尋ねるのは相手が精神的にマウントを取る為の手法だと聞いている",
                    "それでも仕方なく「はい」と答えて$Sは、完全に事件について記事する機会を逸したことを理解した"),
            paul.talk("ああ、それから端末を持っているな？",
                    "とりあえず常時応答できる状態にしておくように"),
            emil.talk("はい"),
            emil.do("力なくそう答え、$Sはジャケットから取り出した端末を彼の携帯型端末へと向けた"),
            ).omit()

def sc_research(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("調査",
            w.symbol("　　　　◆"),
            emil.be("#部屋にいる"),
            uru.be(),
            adam.be(),
            emil.do("簡易ベッドの上に座ったその弾力が普段$Sの使っている最低ランクのホテルよりずっと良いことに驚く",
                "彼女が事件に巻き込まれなければ誰も泊まる予定などなかっただろうに、",
                "シーツには塵一つ付着していない"),
            uru.talk("全て$w_droidが普段から整備を担当しています",
                "いずれはホテルも完全に$w_droidだけで営業することも可能になりますよ"),
            emil.do("寝室の入り口に立つ$uruはかつての同僚が亡くなったとは思えないほど快活な笑みを浮かべて説明してくれる"),
            uru.talk("かつてここには常時三十名以上の研究スタッフがいたのですが、",
                "今や一人の人間も必要としなくなっています",
                "ロボットというものは本来こうあるべきなのですよ",
                "それなのに未だに人間の感傷が社会をより豊かにするという選択を邪魔している",
                "愚かだと思いませんか？"),
            emil.talk("ロボットだけであれば殺人すら起きないと？"),
            emil.do("意地悪のつもりはなかったが$uruは目を細めるとつまらなさそうにワークスペースの方へと戻っていく",
                "$Sも立ち上がり、彼に続いた"),
            emil.talk("ところであの刑事にここから出るなと言われたのですが、",
                "部屋の外も歩き回れない感じでしょうか？"),
            emil.do("白いテーブルの上には二十インチのモニタ付き端末が用意されている",
                "スクリーンセーバが蛇行する蛇に似た映像を映しているのを見やってから、$Sは考え込む$uruに視線を戻す"),
            uru.talk("この施設から出ないように言われていますが、",
                "それ以上のことは聞いていないので、ご自分で訊かれたらどうですか",
                "警察の調査ロボットも来ているし、多少のことなら問題ないと思いますがね"),
            emil.talk("この端末は使っても？"),
            uru.talk("刑事の方に言われて外部とのネットは遮断していますが、施設内なら使えます",
                "メインサーバに繋げなくなると困るのでそこは許可を貰っていますが、",
                "仕事をされるんですか？"),
            emil.do("ええ、と返事をしてから椅子に掛けてキーボードを叩いてみた",
                "システムは使い慣れている一般的なもので、ワープロソフトや各種エディタも充実している",
                "データは無線を使ってやり取りすれば大丈夫だった"),
            emil.talk("ワーカホリックなんです", "仕事がない時でも何か考えをまとめたり資料を作ったり、",
                "同僚はみんなそんな感じですね"),
            uru.talk("人間らしさを担保する為に時には無駄なことをするのも良いですよ",
                "例えば$meはピアノを弾きます"),
            emil.do("$uruは笑みを見せて宙で鍵盤を弾く真似をしたが、彼がそれを本気で言っているのかどうか、やはり理解できなかった"),
            uru.talk("必要があれば声を掛けるだけで$meに繋がると思いますが、何かと不便もあると思うので、そうですね"),
            uru.do("彼は腕の端末を操作して入り口を見た"),
            adam.come("一分ほどしてドアがスライドし、右胸から肩に掛けてオレンジのカラーリングがされている、あの作業$w_droidが入ってくる"),
            uru.talk("基本的な世話はこの$full_adamに頼めばいいです",
                "$nielほどじゃないが技術的な質問にもある程度答えられるし、家事能力は$meよりも遥かに高い",
                "将来的には一家に一台、コンシェルジュのような存在にすることも計画にあります",
                "ただまだまだ人間とロボットの共存を危険視する連中は多いようですが"),
            adam.look("頭髪のないつるりとした外観は間近に立たれると威圧感がある",
                "多くのロボットが性別を意識しなくて済むように中性的、かつ体毛のないデザインをしていたが、",
                "$w_cias社のものは肌をべったりとしたカラーリングにしている所為か、",
                "必要以上に非人間性を感じさせた"),
            emil.talk("あの、この個体は特別なんですか？").omit(),
            uru.talk("いえ", "$w_droidには個性は与えていません", "何故ですか？").omit(),
            emil.talk("色が").omit(),
            uru.talk("それはおそらく修繕後の塗装時に同じ色がなかったのでしょう", "よくあることです").omit(),
            adam.look("彼の右肩には$w_cias社のマークが入っていたが、それが上から塗られたオレンジによって消えかかっているようにも見えた").omit(),
            uru.talk("それでは$meは別の用事があるので、これで失礼します"),
            emil.talk("どうもありがとうございました"),
            uru.talk("ああ、そうそう", "警察からも言われていると思いますが、事件のことは記事にしないようにして下さい",
                    "取材時の契約書にもそう書いてあったと思いますが、念の為"),
            emil.do("分かっています、という$Sの返事を待たずに$uruは部屋を出ていってしまった"),
            uru.go("#部屋を出ていく"),
            emil.talk("よろしく……えー、なんてお名前かしら？"),
            adam.talk("$meは$full_adamです"),
            emil.hear("声は男性の、やや高いものを採用していた", "&"),
            emil.think("しかし型番で呼ぶという訳にもいかないと考え、$Sは「$adamではどうかしら」と提案する"),
            adam.talk("$adam", "わかりました$emiliaさん"),
            emil.do("既に彼女の名前は登録済みのようだ", "握手を交わすと体温の低い人間の手の感触と遜色ない",
                    "これなら人間の服を着て体毛を付ければ充分に人間の代役を務めることが可能だろう"),
            emil.do("とりあえず端末に自分の携帯からデータを移し、記事のドラフトを書こうとする",
                    "しかしずっと壁で直立不動の$adamのことが気になり、キーボードに置いた指はミリも動かない"),
            emil.talk("ねえ。この部屋の入室記録ってあなたに聞けば教えてもらえるのかしら？"),
            adam.talk("はい", "それはゲストの$emiliaさんでも許可されています"),
            emil.talk("ためしにこの部屋の入室記録を教えて"),
            adam.talk("分かりました",
                    "二十二時八分四十秒に$uruさんが部屋を出ています"),
            emil.do("自分の携帯で時刻を確認すると確かにさっき彼が出ていった時刻と合致する",
                    "他にも$emiliaと$uruが入室した時刻も正確に記録されていた"),
            emil.talk("あなたの入室記録はないの？"),
            adam.talk("$meは人間ではありません", "入退室記録は人間の出入りを記録したものです"),
            emil.think("全てのものについて記録しているのではないのだと知り一瞬奇妙に思ったが、",
                    "記録とは本来そういうものかも知れないと考え直した"),
            emil.talk("記録を改竄した場合はどうなるの？",
                    "例えば$meが退室した記録を消したりできる？"),
            adam.talk("改竄した、という記録が残ります", "またデータへのアクセス経路が限られているので改竄そのものが難しいという前提があります"),
            emil.think("セキュリティとしては標準レベルのシステムになっているのだと分かった",
                    "$Sはメモ帳にそれを書き込み、少し考える",
                    "時刻は二十三時",
                    "まだ眠るには早い"),
            emil.talk("ねえ$adam", "ここにはお酒はないの？"),
            adam.talk("本施設内では飲料用のアルコールは禁止されています"),
            emil.talk("え？　そうなの？　でもさっき……あ、ねえ、ちょっと聞くんだけど、",
                    "$nielさんの部屋って$meが入ることはできる？"),
            stage=w.on_bedroom_int,
            )

## episode
def ep_investigation(w: World):
    return w.episode("2.事件捜査",
            sc_aboutcase(w),
            sc_aboutcase2(w),
            sc_research(w),
            ## NOTE
            ##  - 第二の殺人事件
            note="人間の捜査官と共に事件について調べる。そのうちに第二の殺人が発生する。そしてそれを調べていた人間は突然目の前から姿を消してしまった")

