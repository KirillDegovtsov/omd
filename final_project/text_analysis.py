import re
from collections import Counter
from collections.abc import Iterable


def tokenize(text: str | None) -> list[str]:
    """Выделение английских слов"""
    if not text:
        return []
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())


def top_words(texts: list[str | None], n: int = 10, stopwords: Iterable[str] | None = None) -> list[tuple[str, int]]:
    """n наиболее частых слов"""
    excluded_words = set(stopwords) if stopwords is not None else set()
    frequencies = Counter()

    for text in texts:
        frequencies.update(word for word in tokenize(text) if word not in excluded_words)

    return frequencies.most_common(n)
