from pathlib import Path
import shutil
from helpers.check_export_integrity import verify_export_integrity
from helpers.combine_export_files import combine_exports

def gather_consolidate_exported_files(global_export_folder: Path, sources_root_path:Path):
    global_export_wavs = global_export_folder / "wavs"

    try:
        verify_export_integrity(global_export_folder)
    except Exception as e:
        print("Global export folder integrity compromised. Rebuilding...")
        print(str(e))
        print("Rebuilding...")

        shutil.rmtree(str(global_export_folder), ignore_errors=True)
        global_export_folder.mkdir()
        global_export_wavs.mkdir()
        metadata_file = global_export_folder/'metadata.csv'
        metadata_file.open('w').close()
        

    for folder in sources_root_path.iterdir():
        if not folder.is_dir():
            continue
        folder_exports_path = folder/'export'
        try:
            verify_export_integrity(folder_exports_path)
        except Exception as e:
            print(f"Failed verifying exports in folder: {folder}")
            print(e)
            continue
            # optional user input for rebuilding the exports in this folder

        combine_exports(folder_exports_path, global_export_folder)



    

