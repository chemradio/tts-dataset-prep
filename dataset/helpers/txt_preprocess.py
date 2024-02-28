from pathlib import Path
from pysbd import Segmenter


def preprocess_txt(txt_file: Path | str) -> list[str]:
    with open(txt_file, "rt") as txt:
        segmenter = Segmenter(language="en", clean=False)
        sents = segmenter.segment(txt.read())
        text_data = [sent.strip() for sent in sents if len(sent) > 1]

    with open(txt_file, "wt") as txt:
        txt.write("\n".join(text_data))

    return text_data
