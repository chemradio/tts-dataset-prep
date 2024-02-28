from pathlib import Path
from helpers.split_audio import split_audio_file
from helpers.txt_preprocess import preprocess_txt
from helpers.enumerates import SplitSource
import shutil
import csv

def prepare_folder_export(
    folder: dict[Path],
    split_source: SplitSource = SplitSource.RAW,
    # resplit_audio: bool = True,
) -> None:
    print("Processing txt script file")
    processed_script = preprocess_txt(folder["script"])

    print("Splitting audio")
    audio_chunks = split_audio_file(
        folder["denoised"] if split_source == SplitSource.DENOISED else folder["audio"]
    )

    if len(processed_script) != len(audio_chunks):
        print(f"Error during script/audio matching in folder: {folder['folder']}")
        print(f"Sentences: {len(processed_script)=}, Audio chunks: {len(audio_chunks)=}")
        return

    export_folder: Path = folder["folder"] / "export"
    shutil.rmtree(str(export_folder), ignore_errors=True)
    export_folder.mkdir(exist_ok=True)
    export_folder_wavs = export_folder/"wavs"
    export_folder_wavs.mkdir(exist_ok=True)

    for index, pair in enumerate(zip(processed_script, audio_chunks)):
        audio_filename = f"{folder['id']}_{index:03}.wav"
        text, audio = pair
        audio.set_frame_rate(48000).set_channels(1).export(
            export_folder_wavs / audio_filename, format="wav"
        )
        with open(export_folder/'metadata.csv', 'a') as csv_file:
            writer = csv.writer(csv_file,delimiter='|')
            writer.writerow([audio_filename,text,text.lower()])