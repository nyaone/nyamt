# -*- coding: utf-8 -*-

from translators.ja2en import translate_ja_en
from translators.en2zh import translate_en_zh

from langdetect import detect


def translate(text, target_lang, source_lang='auto'):
    if source_lang == 'auto':
        source_lang = detect(text)

    if target_lang == 'en':  # To EN
        if source_lang == 'ja':
            return translate_ja_en(text)
    elif source_lang == 'en':  # From EN
        if target_lang == 'zh':
            return translate_en_zh(text)
    else:
        return translate(translate(text, 'en', source_lang), target_lang, 'en')

    return ''
