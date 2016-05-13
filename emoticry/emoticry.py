#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os


"""emoticry.emoticry

This file contains the bulk of logic for the emoticry library.
"""


class Translation(object):
    """
    A generic Translation class for translating filenames.

    By default Translates names into hex.
    """
    def __init__(self, table=[hex(_)[2:] for _ in range(256)]):
        self.table = table

    def translate(self, name):
        new_name = []
        for c in name.encode('utf-8'):
            new_name.append(self.table[ord(c)])
        return ' '.join(new_name)
    
    def untranslate(self, name):
        chars = name.split()
        new_name = str()
        for c in chars:
            new_name += chr(self.table.index(c))
        return new_name.decode('utf-8')


class EmojiTranslation(Translation):
    """
    The default Emoji Translation class, based on Translation class.
    Defines default Emoji Translation table.
    """
    def __init__(self):
        Translation.__init__(
            self,
            table=[
                '😁',
                '😂',
                '😃',
                '😄',
                '😅',
                '😆',
                '😉',
                '😊',
                '😋',
                '😌',
                '😍',
                '😏',
                '😒',
                '😓',
                '😔',
                '😖',
                '😘',
                '😚',
                '😜',
                '😝',
                '😞',
                '😠',
                '😡',
                '😢',
                '😣',
                '😤',
                '😥',
                '😨',
                '😩',
                '😪',
                '😫',
                '😭',
                '😰',
                '😱',
                '😲',
                '😳',
                '😵',
                '😷',
                '😸',
                '😹',
                '😺',
                '😻',
                '😼',
                '😽',
                '😾',
                '😿',
                '🙀',
                '🙅',
                '🙆',
                '🙇',
                '🙈',
                '🙉',
                '🙊',
                '🙋',
                '🙌',
                '🙍',
                '🙎',
                '✂',
                '✅',
                '✈',
                '✉',
                '✊',
                '✋',
                '✌',
                '✏',
                '✒',
                '✔',
                '✖',
                '✨',
                '✳',
                '✴',
                '❄',
                '❇',
                '❌',
                '❎',
                '❓',
                '❔',
                '❕',
                '❗',
                '❤',
                '➕',
                '➖',
                '➗',
                '➡',
                '➰',
                '🚀',
                '🚃',
                '🚄',
                '🚅',
                '🚇',
                '🚉',
                '🚌',
                '🚏',
                '🚑',
                '🚒',
                '🚓',
                '🚕',
                '🚗',
                '🚙',
                '🚚',
                '🚢',
                '🚤',
                '🚥',
                '🚧',
                '🚨',
                '🚩',
                '🚪',
                '🚫',
                '🚬',
                '🚭',
                '🚲',
                '🚶',
                '🚹',
                '🚺',
                '🚻',
                '🚼',
                '🚽',
                '🚾',
                '🛀',
                'Ⓜ',
                '©',
                '®',
                '‼',
                '⁉',
                '🐀',
                '🐁',
                '🐂',
                '🐃',
                '🐄',
                '🐅',
                '🐆',
                '🐇',
                '🐈',
                '🐉',
                '🐊',
                '™',
                'ℹ',
                '↔',
                '↕',
                '↖',
                '↗',
                '↘',
                '↙',
                '↩',
                '↪',
                '⌚',
                '⌛',
                '⏩',
                '⏪',
                '⏫',
                '⏬',
                '⏰',
                '⏳',
                '▪',
                '▫',
                '▶',
                '◀',
                '◻',
                '◼',
                '◽',
                '◾',
                '☀',
                '☁',
                '☎',
                '☔',
                '☕',
                '☝',
                '☺',
                '♈',
                '♉',
                '♊',
                '♋',
                '♌',
                '♍',
                '♎',
                '♏',
                '♐',
                '♑',
                '♒',
                '♓',
                '♠',
                '♥',
                '♦',
                '♨',
                '♿',
                '⚓',
                '⚠',
                '⚡',
                '⚪',
                '⚫',
                '⚾',
                '⛄',
                '⛅',
                '⛔',
                '⛪',
                '⛲',
                '⛵',
                '⛺',
                '⛽',
                '⤵',
                '⬅',
                '⬆',
                '⬛',
                '⬜',
                '⭐',
                '〰',
                '〽',
                '㊗',
                '🃏',
                '🌀',
                '🌁',
                '🌂',
                '🌄',
                '🌅',
                '🌆',
                '🌈',
                '🌉',
                '🌊',
                '🌋',
                '🌑',
                '🌓',
                '🌔',
                '🌕',
                '🌙',
                '🌛',
                '🌟',
                '🌠',
                '🌰',
                '🌱',
                '🌴',
                '🌸',
                '🌹',
                '🌺',
                '🌼',
                '🌽',
                '🌾',
                '🍀',
                '🍁',
                '🍂',
                '🍄',
                '🍅',
                '🍆',
                '🍈',
                '🍉',
                '🍊',
                '🍌',
                '🍎',
                '🍏',
                '🍑',
                '🍓',
                '🍔',
                '🍕',
                '🍖',
                '🍗',
                '🍙',
                '🍚'])


def emojify(directory=u'.',
            recursive=False,
            rescue=False,
            translation=EmojiTranslation()):
    """
    For the given directory, iterate over all files and folders within it
    (optionally recursively) and translate the file name characters to emoji.
    """
    if recursive:
        for files in os.walk(directory, topdown=True):

            path = files[0]
            directories = files[1]
            filenames = files[2]

            for i, d in enumerate(directories):

                if rescue:
                    new_name = translation.untranslate(d)
                else:
                    new_name = translation.translate(d)

                os.rename(os.path.join(path, d),
                          os.path.join(path, new_name))

                directories[i] = new_name

            for i, f in enumerate(filenames):

                if rescue:
                    new_name = translation.untranslate(f)
                else:
                    new_name = translation.translate(f)

                os.rename(os.path.join(path, f),
                          os.path.join(path, new_name))
                filenames[i] = new_name
    else:
        for f in os.listdir(directory):

            if rescue:
                new_name = translation.untranslate(f)
            else:
                new_name = translation.translate(f)

            os.rename(os.path.join(directory, f),
                      os.path.join(directory, new_name))
