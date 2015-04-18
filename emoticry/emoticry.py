#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        new_name = ''
        for c in name:
            if len(c) == 1:
                new_name += self.table[ord(c)]
            else:
                new_name += c
        return new_name
    
    def untranslate(self, name):
        new_name = ''
        for c in name:
            if len(c) == 1:
                new_name += chr(self.table.index(c))
            else:
                new_name += c
        return new_name


emoji_translation = Translation(
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
        '8⃣',
        '9⃣',
        '7⃣',
        '6⃣',
        '1⃣',
        '0⃣',
        '2⃣',
        '3⃣',
        '5⃣',
        '4⃣',
        '#⃣',
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
        '🍚']
)


def emojify(directory='.', recursive=False, translation=emoji_translation):
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
                os.rename(os.path.join(path, d),
                          os.path.join(path, translation.translate(d)))
                directories[i] = translation.translate(d)
            for i, f in enumerate(filenames):
                os.rename(os.path.join(path, f),
                          os.path.join(path, translation.translate(f)))
                filenames[i] = translation.translate(f)
    else:
        for f in os.listdir(directory):
            os.rename(os.path.join(directory, f),
                      os.path.join(directory, translation.translate(f)))
