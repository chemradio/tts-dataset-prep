from pathlib import Path
from uuid import uuid4

def tag_folders(folders:list[dict[Path]]) -> list[dict[Path]]:
    for folder in folders:
        if (folder['folder']/'id').exists():
            with open(folder['folder']/'id', 'r') as f:
                id_ = f.read()
            folder['id'] = id_
        else:
            id_ = uuid4()
            folder['id'] = id_
            with open(folder['folder']/'id', 'w') as f:
                f.write(str(id_)) 

    return folders