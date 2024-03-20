def normalize_word(raw_word: dict) -> dict:
    return {raw_word["word"]: raw_word["translation"]}


def readable_format(words: dict):
    res = ""
    for key, value in words.items():
        res += f"{key} - {value}\n"
    return res
