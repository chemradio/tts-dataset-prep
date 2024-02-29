from pathlib import Path
import csv


def verify_export_integrity(folder_path: Path) -> list[str]:
    assert folder_path.exists()
    
    metadata_file = folder_path / "metadata.csv"
    wavs_folder = folder_path / "wavs"

    with open(metadata_file, "rt") as mdf:
        reader = csv.reader(mdf, delimiter="|")
        metadata = list(reader)
        wav_list_csv = [line[0] for line in metadata]

    for wav in wav_list_csv:
        assert (wavs_folder / wav).exists()

    return metadata
