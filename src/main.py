#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## assets
from storybuilder.assets import basic, accessory
## local files
from src.chapter.main import ch_main

## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   1.労働ロボット「ドルイド」たちによる殺人事件が発生していた
#   2.作業場から人間たちの暮らす世界で働くために、殺人事件解決に協力する
#   3.人間になろうとしたドルイドは、自分が殺していたことに気づき、自殺する。自殺により人間になって空を見上げた
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("見上げた空は機械油で滲む")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2098)
    w.setBaseArea("Tokyo")
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("作業ロボット「ドルイド」たちによる謎の殺人事件が発生し、人間に憧れるドルイドは事件解決に協力する")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

