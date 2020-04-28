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
def sc_research(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("調査",
            )

def sc_2ndmurder(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("第二の殺人",
            )

def sc_humanworld(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("人間に憧れる$w_droidたち",
            )

def sc_killed(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("$paulが殺された",
            )

## episode
def ep_investigation(w: World):
    return w.episode("2.事件捜査",
            sc_research(w),
            sc_2ndmurder(w),
            sc_humanworld(w),
            sc_killed(w),
            ## NOTE
            ##  - 第二の殺人事件
            note="人間の捜査官と共に事件について調べる。そのうちに第二の殺人が発生する。そしてそれを調べていた人間は突然目の前から姿を消してしまった")

