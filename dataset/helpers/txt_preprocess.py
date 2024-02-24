from pathlib import Path


def preprocess_txt(txt_file: Path | str) -> str:
    with open(txt_file, "rt") as txt:
        text_data = [
            line.strip() + "." for line in txt.read().split(".") if len(line) > 1
        ]
    return text_data


