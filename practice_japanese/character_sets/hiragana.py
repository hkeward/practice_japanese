from enum import Enum


class Hiragana(Enum):
    vowels = {"あ": "a", "え": "e", "い": "i", "お": "o", "う": "u"}

    h = {"は": "ha", "へ": "he", "ひ": "hi", "ほ": "ho", "ふ": "fu"}

    k = {"か": "ka", "け": "ke", "き": "ki", "こ": "ko", "く": "ku"}

    m = {"ま": "ma", "め": "me", "み": "mi", "も": "mo", "む": "mu"}

    n = {"ん": "n", "な": "na", "ね": "ne", "に": "ni", "の": "no", "ぬ": "nu"}

    r = {"ら": "ra", "れ": "re", "り": "ri", "ろ": "ro", "る": "ru"}

    s = {"さ": "sa", "せ": "se", "し": "shi", "そ": "so", "す": "su"}

    t = {"た": "ta", "て": "te", "ち": "chi", "と": "to", "つ": "tsu"}

    w = {"わ": "wa", "を": "o"}

    y = {"や": "ya", "よ": "yo", "ゆ": "yu"}

    hiragana = {**vowels, **h, **k, **m, **n, **r, **s, **t, **w, **y}

    def __str__(self):
        return self._name_


reverse_hiragana = {v: k for k, v in Hiragana.hiragana.value.items()}
