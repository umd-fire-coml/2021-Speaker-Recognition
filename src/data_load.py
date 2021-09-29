import os

def load_libre_data(dirc):
    
    flac_files = []
    ids = []
    
    if not os.path.exists(dirc):
        return False

    for speaker in os.listdir(dirc):
        for chapter in os.listdir(dirc + '/' + speaker):
            for fil in os.listdir(dirc + '/' + speaker + "/" + chapter):
                if fil.endswith('.flac'):
                    flac_files.append(dirc + '/' + speaker + '/' + chapter + '/' + fil)
                    ids.append(fil.split("-", 1)[0])
    
    return zip(ids, flac_files)
