from pydub import AudioSegment
from pathlib import Path


def convert_audio_48_mono_wav(input_path: Path | str, output_path: Path | str) -> None:
    sound = AudioSegment.from_file(input_path)
    sound = sound.set_frame_rate(48000)
    sound = sound.set_channels(1)
    sound.export(output_path, format="wav")
