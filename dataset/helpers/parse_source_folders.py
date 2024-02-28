from pathlib import Path


def parse_source_folders(sources_root_path: Path | str) -> list:
    assert sources_root_path.exists()
    source_folders = []
    for folder in sources_root_path.iterdir():
        if folder.is_dir():
            script_files = list(folder.glob("*.txt")) + list(folder.glob("*.rtf"))
            if not script_files:
                print(f"Folder missing script: {str(folder)}")
                continue

            audio_files = (
                list(folder.glob("*.mp3"))
                + list(folder.glob("*.wav"))
                + list(folder.glob("*.MP3"))
            )
            if not audio_files:
                print(f"Folder missing audio: {str(folder)}")
                continue
           
            if script_files and audio_files:
                source_folders.append(
                    {
                        "folder": folder,
                        "script": script_files[0],
                        "audio": audio_files[0],
                    }
                )
            
            if (folder/"denoised").exists():
                denoised_audio_files = list((folder/"denoised").glob("*.wav"))
                if denoised_audio_files:
                    source_folders[-1]["denoised"] = denoised_audio_files[0]

            if (folder/"export").exists():
                source_folders[-1]["export"] = folder/"export"
            
    return source_folders
