from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path


def split_audio_file(file_path: Path | str) -> list[AudioSegment]:
    sound = AudioSegment.from_file(file_path)
    chunks = split_on_silence(
        sound, min_silence_len=500, silence_thresh=-40, keep_silence=300
    )
    return [chunk for chunk in chunks if len(chunk) >= 700]
