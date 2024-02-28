from helpers.parse_source_folders import parse_source_folders
from helpers.tag_id import tag_folder
from pathlib import Path
from helpers.prep_folder_export import prepare_folder_export
SOURCES_ROOT_PATH = Path.cwd() / "source_files"


def main():

    # gather all source folders from .parent/source_files
    source_folders = parse_source_folders(SOURCES_ROOT_PATH)

    for folder in source_folders:
        # add uuid for dataset use
        print("_"*20)
        tag_folder(folder)

        # denoise audio in folder
        # print("_"*20)
        # denoise_folder(folder)

        # generate files for export inside folder/export
        # these are /wavs/*.wav and /metadata.csv
        print("_"*20)
        prepare_folder_export(folder)

        # collect files and copy to other location
        # simulate or real

        print("_"*20)

if __name__ == "__main__":
    main()
