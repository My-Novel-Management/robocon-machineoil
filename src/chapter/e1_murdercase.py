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
            adam.explain("ロボット工学三原則"),
            w.br(),
            adam.explain("第一条　ロボットは人間に危害を加えてはならない。また、その危険を看過することによって、人間に危害を及ぼしてはならない"),
            _.explain("第二条　ロボットは人間にあたえられた命令に服従しなければならない。ただし、あたえられた命令が、第一条に反する場合は、この限りでない"),
            _.explain("第三条　ロボットは、前掲第一条および第二条に反するおそれのないかぎり、自己をまもらなければならない"),
            _.explain("――アイザック・アシモフ『われはロボット』小尾芙佐訳、早川書房　より"),
            camera=w.emilia,
            stage=w.on_herroom,
            day=w.in_reporting, time=w.at_afternoon,
            )

def sc_report_introduction(w: World):
    emil, adam, paul = W(w.emilia), W(w.adam), W(w.paul)
    return w.scene("レポート序文",
            w.comment("$emiliaのレポートという形式の三人称で", "扉と同じページに作る"),
            w.symbol("　　　　※"),
            emil.be("#ホテルの部屋でレポートを書いている"),
            emil.think("ロボットというものについて考える時、$meはいつも彼のことを思い出す",
                "彼と呼ぶことが正しいかどうかはこのレポートを最後まで読んでもらい、各自判断してもらいたい"),
            emil.think("ロボットが一体何者なのかということについて未だに$w_councilではこれといった結論が出されていない",
                "かつては単なる人間の労働の代行者でしかなかった彼らが、知能を手に入れ、人間の姿を手に入れ、",
                "現在では社会生活を支える基盤とも呼べる存在になってしまっても、",
                "そこには漫然とロボットと人間の境界線が存在していると誰もが感じているだろう"),
            emil.think("――レイ・カーツワイルにより予言されたシンギュラリティは来なかった！"),
            emil.think("――未だに人間は人間で、ロボットはロボットである！"),
            emil.think("――人間はロボットの神には成り得なかった！"),
            emil.think("どの新聞記事にもそんな見出しが踊っているが、$meはそう評するのはまだ早計だと考えている"),
            emil.think("ここ二年間におよそ十八件のロボットによる自発的な反乱事件が発生した",
                "完全に自発的だったかどうかは議論の余地が残されているが、結果としてその事件による死者数は一万人を超えているとも云われる", "&"),
            emil.think("もし仮に世界に一億台以上存在するロボットの大部分が人間に牙を向くようなことがあれば、その被害は比較にならないほど甚大になることは予想するまでもないだろう",
                "これについて評議会はこの先百年はロボットが自我を持つことはないと声明を出しているが、",
                "開発者の多くは十年以内に人間の知性をロボットが抜き去るだろうと予測している"),
            emil.think("しかし$meは思うのだ",
                "ロボットと人間を分けているものは一体何なのだろうかと"),
            w.br(),
            emil.do("レポートを書く手を止め、$Sはキーボードに乗せた手をテーブルサイドのカップに伸ばした",
                "そこに注がれた機械油みたいにどす黒い液体を目にし、半年前の出来事を思い出す",
                "口から注ぎ込んだコーヒーはいつもより僅かに苦味が強い気がした"),
            w.comment("何かしら結末と全体の流れを暗示するものを"),
            stage=w.on_herroom_int,
            day=w.in_reporting, time=w.at_midmorning,
            )

def sc_interview(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    worker = W(w.worker)
    return w.scene("取材",
            w.symbol("　　　　１"),
            emil.come(),
            uru.be("#案内している"),
            inside.look("見上げた天井は薄暗い", "壁は白っぽいが足元に光源がある為か、うすぼんやりと浮かび上がってあまり心地良いとは言い難い",
                "案内板もなく、", "のっぺりとしたコーティングの通路をどこに行くのかも分からないまま、", "&"),
            emil.do("$Sは歩いていた",
                "ヒールの低いパンプスの音はあまり響かず、", "前を歩く男の革靴も絨毯の上を歩いているかのように静かだ"),
            emil.talk("随分と暗いんですね"),
            emil.do("どういう理由で淡い紫色の間接照明を選んだのか、という尋ね方はしない"),
            uru.talk("本施設は最初から人間ではなく$w_droid専用にと思って造らせたので、",
                "足元の照明すら要らないんじゃないかと設計段階では言われたものを何とか修正させたものでして、",
                "今後あなたのように外部の取材を受けるとなると考えた方が良さそうですね"),
            emil.talk("ムードを演出する為かと思っていました"),
            uru.look("広報の男性は$uruと名乗った",
                "きっちり七三に分けて固められた金髪と白い肌、涼し気な目元に薄い唇は、",
                "どこかロボットを思わせる"),
            w.comment("眼鏡はアシモフの肖像画から"),
            uru.talk("そういうものは人間の為にしか存在しません",
                "我々$w_cias社はそういった考えの押し付けこそが、ロボットが人間社会で活躍する為の弊害だと考えています"),
            uru.look("ライトグリーンの制服の背中には大きな黒い眼鏡を模したマークが描かれている",
                "世界的なロボット企業$w_cias社のトレードマークだ",
                "創業者の$w_cias氏が常用していた眼鏡が元になっていると事前に受け取った資料には書かれていた"),
            uru.look("$Sの両腕の手首には太いバンドが巻かれ、それが簡易端末になっているようで、", "&"),
            uru.do("彼は左手の端末に触れてから「こちらへ」とドアを開け、先に進む", "&"),
            emil.do("$Sは取り出した手帳に簡単な図面を引きつつ、彼に続いた"),
            inside.look("二人の前後五メートルくらいを照らすように、紫の光が移り変わっていく", "&"),
            worker.be(),
            emil.do("その光の中、不意に直立不動の人間が現れた",
                "一瞬ぎょっとして見てしまったけれど相手も大きな目を二つ動かして、彼女のことを見返してくる"),
            uru.talk("驚かなくても大丈夫です",
                "作業中の$w_droidですよ"),
            emil.do("$w_cias社ではロボットとは呼ばずに全て$w_droidと呼ぶことになっているらしい",
                "その理由について以前のロボットという概念と異なるから、と資料には書かれていた").omit(),
            worker.look("体毛がなく、全身がのっぺりとしたモスグリーン一色で塗装されている",
                "ロボットによくある特徴だったが、この$w_cias社の$w_droidは服を着ていない"),
            emil.talk("彼は何を？"),
            uru.talk("それぞれの個体が様々な業務を持っています",
                "廃棄物の解体分別作業以外にもちょっとした清掃作業や機器のメンテナンス、施設の修繕といったことも彼らの業務内容です"),
            worker.do("その$w_droidは挨拶もせず、$emiliaたちが入ってきたドアの方へと歩いて行ってしまった",
                "関節のモータ音が微かに響く", "歩き方もやはり人間のそれとは異なっていた"),
            emil.talk("資料にもありましたが完全に$w_droidだけで運用が可能だとお考えですか？"),
            uru.talk("ここがその為の試験施設でもあります"),
            uru.talk("いいんですよ",
                "流石に$on_RobertComの記者さんだ",
                "若い女性だからと少々侮っていました", "あそこです").omit(),
            uru.do("$Sは薄っすらと笑みを浮かべ、突き当りのエレベータを指した", "&"),
            inside.look("人間というより大型のコンテナ搬入用に使えそうなサイズのドアが、彼の挙げた右手を感知し、両方にスライドして開いた", "&"),
            emil.do("彼に続いて乗り込む"),
            emil.look("中は鏡のように金属がよく反射し、$Sは履いてきたスカートの丈が少し短かっただろうかと気になった").omit(),
            uru.do("彼がボタンに触れるとドアが閉まり、僅かに浮遊感が身体に伝わる").omit(),
            emil.talk("改めて、本日は貴重な取材のお時間をいただきありがとうございます").omit(),
            uru.talk("我々も最初から全てクローズドでやっていくつもりではなかったんですが、",
                    "何かと準備に時間が掛かってしまいまして").omit(),
            emil.do("今まで決して取材等、外部の人間を入れなかった$w_cias社だったが、",
                "突然の態度の変化にデスクは内部で状況が変わったのだろうと穿った見方をしていた").omit(),
            emil.talk("確認なんですが、こちらではロボットではなく$w_droidと呼べば宜しいでしょうか"),
            uru.talk("それは助かります",
                "$meたちもいつも外部の人間が彼らをロボットと言うことに違和感があったのです",
                "彼らは$meたちの製品であり、ロボットと一般に呼称されるそれとは異なると考えているからです"),
            emil.talk("一番の違いは何でしょう"),
            uru.talk("ロボットは旧世紀の、人間に役立つ奴隷を目指して造られたものであり、",
                "$w_droidは人間が生活を円滑に送るための新しい家電や装置、だということでしょうか",
                "だから我が社のものは必ず人間を模している訳ではありません"),
            w.eventPoint("$w_cias", "今まで外部の人間を決して入れなかった"),
            emil.do("到着したのは最下層の地下五階ではなく、地下二階だった"),
            uru.talk("ではこの施設の一番メインとなる$w_hallをお見せしましょう", "どうぞ").omit(),
            emil.do("先に歩き出した彼に続き、$Sもエレベータを出る").omit(),
            w.eventPoint("ロボットの運用", "遠隔操作でシャットダウンできる"),
            stage=w.on_pathway,
            day=w.in_visit, time=w.at_afternoon,
            )

def sc_droidjob(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$w_droidたちの仕事",
            w.br(),
            w.eventPoint("$w_droidについて", "$w_droidの仕事"),
            emil.come("#解体作業ホールにやってくる"),
            uru.come(),
            adam.be("#作業している"),
            inside.look("スチール製の重いドアを開けると、耳に騒音が飛び込んできた"),
            emil.talk("声、聞こえますか？"),
            inside.look("地上三階分の巨大な空間がそこに広がっていた",
                "鼠色のキャットウォークがＬ字型に掛けられていたが、それが音で小さく振動している", "&"),
            uru.do("$uruは慣れているのか、気にした様子もなくその上を歩き出す"),
            emil.talk("あのー").omit(),
            uru.talk("ここがこの施設の中心部になります"),
            emil.do("やはりよほど大声でないと聞こえないらしい",
                "$Sは諦めて一歩、キャットウォークに踏み出した"),
            inside.look("右手側の壁に巨大な回転式の破砕機がいくつも回っていて、そこに流れ込む八本のベルトコンベアから次々と物が落下しては砕かれていく",
                "粉々になったものを更に別のベルトコンベアに分けて載せるのは大量にいる$w_droidたちの仕事だ",
                "皆同じモスグリーンをしていて、一見すると制服姿の作業員が整然と並んでいるように見える"),
            uru.talk("ここでは搬入された各種廃棄物をある程度の大きさになるまで小さくしてから、",
                "彼らの手で分別した後、別室にある素材判別機へ送ります",
                "人間であれば様々な破片で負傷したり、ガス等の化学物質によって阻害される恐れがありますが、",
                "彼ら$w_droidにはそれがありません",
                "再利用可能なものとそうでないものを分け、また別の施設へと搬出します",
                "この辺りの流れについてはお渡しした資料にあった通りです"),
            inside.look("騒音の正体は回転する沢山のブレードがゴミを破壊する瞬間のそれだった",
                "砕かれたものは一番下のフロアへと落ち、そこで一つ一つを$w_droidが拾い上げ、決められたベルトコンベアに置いていく").omit(),
            emil.do("$Sはここでの質問は諦め、手帳を取り出してそれにメモをした"),
            uru.talk("珍しく今どき手書きなんですね？"),
            emil.talk("ええ。最後のところでデジタルデバイスは信用できないと思っているので"),
            emil.do("見下ろすと霧のような粉塵が舞っている",
                "$Sたちの立っている場所までは上がってこないようだが、見ていてあまり心地の良いものではない"),
            uru.talk("半世紀前にはそういった人も沢山いましたが今は希少種でしょうね",
                "では次に行きましょう"),
            emil.do("助かった、という安堵で入り口に戻ろうとして、気づいた"),
            emil.talk("あの！", "あれは特別な$w_droidなんですか？"),
            uru.talk("どれです？"),
            emil.talk("向こうの壁の近くにいる、一部が赤くなっているものです"),
            adam.look("その一体は右肩から胸元に掛け、朱色のように見えるカラーリングがされていた",
                "彼の周囲の$w_droidは黙々と作業をしているのに、彼だけは$emiliaたちを見上げ、動きを止めている"),
            emil.talk("あれは何か特別な役割を？"),
            uru.talk("おそらく修繕の過程で色を切らしていたのでしょう", "まずはここを出ましょう"),
            emil.talk("そうですね").omit(),
            emil.do("一旦部屋を出てドアを閉めると、いくらか耳が楽になった",
                "$uruも苦笑を見せ、続きを話しながら歩き始める"),
            uru.talk("我が社の$w_droidにおいては人間社会のような上司と部下といった関係性はありません",
                "そこにあるのは完全に役割だけで、一時的にグループを統括する為に管理者を置いたりはしても、",
                "それは本当にその時だけです",
                "そもそも個体差がないのでＣＰＵのコアのようにどれに仕事を振っても同じだけの能力を発揮してくれます",
                "人間相手ではこうはいきませんよね？"),
            w.comment("ロボットについて、基本性能などを書いておく"),
            emil.talk("それこそが$w_cias社がロボットに望む姿だということでしょうか"),
            emil.do("通路の向こうから現れた台車の上に一体の$w_droidが横たわっていた",
                    "それは落下でもしたのか右腕があらぬ方向へと曲がり、頭部も一部凹んでいる",
                    "ただ人間と違って特に苦しんでいる様子はなく、天井を見上げていた目を$Sに向けた"),
            uru.talk("まあロボットであってもこのように事故には遭います",
                    "ただ人間と違い修理が容易ですし、使えなくなったらそれはまた分解して新しく作り直せばいいだけです"),
            emil.do("そうですね、と相槌を打ちながら彼女は手帳に短くメモを付ける",
                    "$uruの受け答えが会社の考えそのものという訳ではないだろうけれど、",
                    "それでも言葉の端々に思惑が見えるものだ",
                    "記者としてはそういう行間を読み取る能力を付けるよう普段から厳しく言われている",
                    "これはロボットには無理な作業だと白髪が目立つ上司は豪語していた"),
            uru.talk("本来はロボットを人型に作る必要はないんですよ",
                "社会の様々なものが人間に適用するように作られているからどうしても人型にせざるを得ないだけであって、",
                "今後はそういった部分まで踏まえて社会システムを構築していく必要があると、我々は考えています"),
            emil.do("最近$w_cias社はロボット産業界だけでなく建築や大手ネット通販サイトとも業務提携を発表していたが、",
                    "裏にはそういった事情もあるのかも知れない", "ただそこには他社とは違うと言いながらもロボットを使い捨てようという意図が$Sには感じられた"),
            w.eventPoint("$w_droidについて", "$w_droidの死"),
            camera=w.adam,
            stage=w.on_dismantlinghall_int,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_murdercase(w: World):
    emil, adam, paul, uru = W(w.emilia), W(w.adam), W(w.paul), W(w.uru)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("殺人事件",
            w.symbol("　　　　◆"),
            emil.come(),
            uru.come(),
            emil.do("他の作業場も見せてもらった後で、二階の居住エリアと呼ばれる場所にやってきた",
                "開発に携わった技師から話を聞けるらしい"),
            inside.look("どこも白っぽい壁の同じような通路で案内板すらないので自分の居場所が分からなくなりそうだが、", "&").omit(),
            emil.do("そう伝えると$uruは自分の端末を見せて、すぐにメインサーバから位置情報を取得できると教えてくれた",
                "社員のものでないと繋がらないらしい",
                "彼の端末に表示された情報からどうやらここが一階の居住エリアであることが分かった").omit(),
            emil.talk("将来的にはこのエリアは使わなくなる予定でしょうか？"),
            emil.talk("寮みたいなものですか？").omit(),
            uru.talk("そうですね", "理想としてはそうなんですが、", "&"),
            uru.talk("どうしてもメンテナンスや人の手を必要とする修理作業があった際には、ここを使ってもらうようにしています",
                "会議室や事務仕事用の部屋も兼ねていますが"),
            emil.do("人間を可能な限り排除して$w_droidだけで作業が完結することを目指して造られた、と云われていたのでそんなものがあったことに驚いたが、",
                "流石にまだそこまでの信頼度はないということだろう").omit(),
            uru.do("やや奥歯に物が挟まったように言葉を濁す"),
            uru.talk("実はまだ一ヶ月前にようやく完全に$w_droidだけの運用に切り替えたばかりでして",
                "技術方と開発部で意見の齟齬もあり、現場を説得するまでに少々難航したのですよ",
                "本来なら半年前には移行している予定でした"),
            emil.think("だから技術スタッフがいたのか、と納得がいった",
                "取材を申し込んだ時には広報の人間一人にしかインタビュー機会がないと聞いていたのだ"),
            uru.talk("こちらに技師の$nielが待機しています",
                "彼はソフトウェア、ハードウェア両面に長けていますので、技術面でより専門的なことを答えてくれるでしょう"),
            inside.look("ドアはグレィに塗られ、$uruが脇のパネルに端末を翳すとスムーズにスライドして開いた"),
            uru.talk("中へどうぞ"),
            emil.do("彼に促され、部屋へと入る",
                "小さな会議室程度の広さで、", "テーブルとモニタの付いた端末が一台置かれている",
                "奥にはスライド式のドアがありもう一つ部屋がある",
                "テーブルに山と積み上げられた紙資料やファイルはあるものの、肝心の技術者の姿がない"),
            emil.talk("いませんね").omit(),
            uru.talk("おかしいな", "記録を確認します"),
            uru.do("そう言うと、彼は腕の端末を操作する"),
            emil.do("端末の傍に置かれたメモ用紙には『$w_hisword01』とあった",
                "他にもロボットや$w_droidといった文字が丸で囲まれたりしている", "おそらく取材用に準備していたものだろう"),
            adam.come("#$Sが入ってくる"),
            emil.do("一分ほどして、先程$w_hallで見たカラーリングが一部異なる$w_droidが入ってきた"),
            uru.talk("入室記録を教えてくれ"),
            adam.talk("分かりました",
                "十四時三十五分二十秒に$nielさんが入室しています"),
            uru.talk("彼が退室したのはいつだ？"),
            adam.talk("$nielさんの退室記録はありません"),
            uru.do("再び「おかしい」と呟き、$uruは奥を見に行く", "けれどすぐに首を振って出てきた"),
            uru.talk("この施設内の入退室の記録は全てメインサーバに送られるようになっています",
                "$w_droidを通じてその記録は確認できるのですが、入室したまま出ていないというのは、$nielがまだこの部屋のどこかにいるということになってしまいますね"),
            uru.do("そう説明して彼は苦笑した"),
            w.br(),
            emil.explain("しかしその三十分後、$nielの体が破砕機でバラバラにされていたと、現場を確認した$uruによって報告された"),
            time=w.at_visitniel,
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


