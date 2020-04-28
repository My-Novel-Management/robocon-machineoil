# -*- coding: utf-8 -*-
"""Chapter: main story
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files
from src.chapter.e1_murdercase import ep_murdercase
from src.chapter.e2_investigate import ep_investigation
from src.chapter.e3_truecriminal import ep_true_criminal


## define alias
W = Writer
_ = W.getWho()

## chapter
def ch_main(w: World):
    return w.chapter("main",
            ep_murdercase(w),
            ep_investigation(w),
            ep_true_criminal(w),
            note="労働ロボット「ドルイド」たちによる殺人事件が発生する。主人公のドルイドは事件解決に協力し、特典である人間が暮らす世界での労働を手に入れる為に調査を始める")
