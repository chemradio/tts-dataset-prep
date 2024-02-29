from pathlib import Path
import shutil
import csv


def combine_exports(source_path: Path, destination_path: Path) -> None:
    source_path_wavs = source_path / "wavs"
    source_metadata_file = source_path / "metadata.csv"
    with open(source_metadata_file, "rt") as f:
        source_metadata = list(csv.reader(f, delimiter="|"))

    destination_path_wavs = destination_path / "wavs"
    destination_metadata_file = destination_path / "metadata.csv"
    with open(destination_metadata_file, "rt") as f:
        destination_metadata = list(csv.reader(f, delimiter="|"))

    for line in source_metadata:
        if line in destination_metadata:
            continue

        shutil.copy(
            str(source_path_wavs / line[0]), str(destination_path_wavs / line[0])
        )
        with open(destination_metadata_file, "a") as f:
            csv.writer(f, delimiter="|").writerow(line)
