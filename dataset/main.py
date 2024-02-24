from helpers.parse_source_folders import parse_source_folders
from helpers.txt_preprocess import preprocess_txt
from helpers.tag_id import tag_folders
from pprint import pprint
from pathlib import Path

SOURCES_ROOT_PATH = Path.cwd()/ 'source_files'

def main():
    source_folders = parse_source_folders(SOURCES_ROOT_PATH)
    tagged_folders = tag_folders(source_folders)

    pprint(tagged_folders)
    


if __name__=="__main__":
    main()