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
def sc_droidjob(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("$w_droidたちの仕事",
            camera=w.adam,
            stage=w.on_trashcollection,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_murdercase(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("殺人事件",
            )

def sc_roborules(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("ロボ規則",
            )

def sc_forbecomeahuman(w: World):
    adam, paul = W(w.adam), W(w.paul)
    return w.scene("人間になる為に",
            )

## episode
def ep_murdercase(w: World):
    return w.episode("1.殺人事件",
            sc_droidjob(w),
            sc_murdercase(w),
            sc_roborules(w),
            sc_forbecomeahuman(w),
            ## NOTE
            ##  - 世界観説明
            note="人間の為に労働専用のロボット「$w_droid」たちがいた。彼らはロボット三原則に従い行動していたが、何故か殺人事件が発生してしまう。$adamは人間に近づく為、捜査協力を買って出る")


