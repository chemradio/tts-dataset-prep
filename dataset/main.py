from helpers.parse_source_folders import parse_source_folders
from helpers.tag_id import tag_folder
from pathlib import Path
from helpers.denoise_audio import denoise_folder

SOURCES_ROOT_PATH = Path.cwd() / "source_files"


def main():

    # gather all source folders from .parent/source_files
    source_folders = parse_source_folders(SOURCES_ROOT_PATH)

    for folder in source_folders:
        # add uuid for dataset use
        tag_folder(folder)

        # denoise audio in folder
        denoise_folder(folder)



if __name__ == "__main__":
    main()
