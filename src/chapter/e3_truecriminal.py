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
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("記録映像",
            )

def sc_runaway(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("逃走",
            )

def sc_lookup_sky(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("そして空を見上げた",
            )

## episode
def ep_true_criminal(w: World):
    return w.episode("3.真犯人",
            sc_recordvideo(w),
            sc_runaway(w),
            sc_lookup_sky(w),
            ## NOTE
            ##  - 証拠映像から、自分が操作されて殺人を行っていたことが判明する
            ##  - 人間になるために、逃亡する
            ##  - 真実を知り、自殺する。空を見上げた
            note="自分以外の誰もその現場にいることが不可能だと分かる。手に入れた映像記録から$adam自身が殺人を犯していると判明し、$adamは処理されることになった。彼は人間に近づく為に最後の破壊行為に挑む")

