# -*-coding: utf-8 -*-
import re


text = """Giraffes have aroused
the curiosity of __PLURAL_NOUN__
since earliest times. The 
giraffes is the tallest of all
living __PLURAL_NOUN__, but 
scientists are unable to
explain how it got its long
__PART_OF_THE_BODY__. The 
giraffe's tremendous height,
which might reach __NUMBER__
__PLURAL_NOUN__, comes from
it legs and __BODYPART__.
"""


def mad_libs(mls):
    """

    :param mls: 字符串
    双下划线部分的内容需要由玩家来补充。
    双下划线不能出现在提示语中，如不能出现 __hint__hint__，只能是 __hint__。
    """
    hints = re.findall("__.*?__", mls)

    if hints is not None:
        print(hints)
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        # mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")


mad_libs(text)
