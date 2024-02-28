from pathlib import Path
from uuid import uuid4

def tag_folder(folder:dict[Path]) -> dict[Path]:
    print(f"Tagging folder: {str(folder['folder'])}")
    if (folder['folder']/'id').exists():
        print("Folder had an ID already")
        with open(folder['folder']/'id', 'r') as f:
            id_ = f.read()
        folder['id'] = id_
    else:
        print("Creating a new tag")
        id_ = uuid4()
        folder['id'] = id_
        with open(folder['folder']/'id', 'w') as f:
            f.write(str(id_)) 

    return folder