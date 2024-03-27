import re

l = "Beautiful is better than ugly."

matches = re.findall("beautiful",
                     l,
                     re.IGNORECASE)

print(matches)


zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If",
               zen,
               re.MULTILINE)
print(m)

import re

string ="Two too."

m = re.findall("t[ow]o",
               string,
               re.IGNORECASE)
print(m)


line = "123?34 hello?"

m = re.findall("\d",
               line,
               re.IGNORECASE)
print(m)

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

for match in found:
    print(match)


line = "I love $"

m = re.findall("\\$",
               line,
               re.IGNORECASE)

print(m)



zen = "Although that way may not be obvious at first unless you're Dutch."

m = re.findall("Dutch",
               zen,
               re.IGNORECASE)
print(m)


text = "Arizona 479, 501, 870. California 209, 213, 650"

m = re.findall("\d",
               text,
               re.IGNORECASE)
print(m)


sentence = "The ghost that says boo haunts the loo"

m = re.findall("oo", sentence)
print(m)

text = """
       Giraffes have aroused the curiosity of __PLURAL_NOUN__ since earliest times. The giraffe is the
       tallest of all living __PLURAL_NOUN__, but scientists are unable to explain how it got its long
       __PART_OF_THE_BODY__. The giraffe's tremendous height, which might reach __NUMBER__ __PLURAL_NOUN__,
       comes from its legs and __BODYPART__.
       """


def mad_libs(mls):
    """
    :param mls: String with parts the user should fill out surrounded by double underscores. Underscores cannot
    be inside hint e.g., no __hint_hint__ only __hint__.
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            new_word = input("enter a {}".format(word))
            mls = mls.replace(word, new_word, 1)
        print('\n')
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)
