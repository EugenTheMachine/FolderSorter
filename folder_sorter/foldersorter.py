import os
import shutil

images = ['.jpeg', '.png', '.jpg', '.svg']
video = ['.avi', '.mp4', '.mov', '.mkv']
documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
music = ['.mp3', '.ogg', '.wav', '.amr', '.m4a']
archives = ['.zip', '.gz', '.tar']
# unknown = everything else

PATH = 'TSC'

сyrillics = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
            'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
            'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
            'э', 'ю', 'я']

transliteration = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
                   'е': 'ye', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
                   'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                   'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                   'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
                   'ш': 'sh', 'щ': 'shch', 'ъ': "'", 'ы': 'y', 'ь': '',
                   'э': 'e', 'ю': 'yu', 'я': 'ya'}  # by Yevhen Ponomarov

def normalize(fn: str) -> str:
    filename = fn  # by Yevhen Ponomarov
    result = ""
    for char in filename:  # by Yevhen Ponomarov
        if char.lower() in сyrillics:
            if char.isupper():
                result += transliteration[char.lower()].capitalize()
            else:  # by Yevhen Ponomarov
                result += transliteration[char]
        else:
            result += char
    return result
  # by Yevhen Ponomarov
folder_names = ['images', 'documents', 'audio', 'video', 'archives']
# by Yevhen Ponomarov

def eraseEmptyFolders(drct: str):
    f_list = os.listdir(drct)
    for item in f_list:
        if os.path.isdir(os.path.join(drct, item)):
            eraseEmptyFolders(os.path.join(drct, item))
            if not os.listdir(os.path.join(drct, item)):
                os.rmdir(os.path.join(drct, item))

def sortFolder(foldername: str):
    f_list = os.listdir(foldername)
    
    for folder_name in folder_names:
        if folder_name not in f_list:
            os.mkdir(os.path.join(foldername, folder_name))
        
    for file in f_list:
        path = os.path.join(foldername, file)
        if os.path.isfile(path):
            new_name = normalize(file)
            if file != new_name:
                os.rename(os.path.join(foldername, file),
                          os.path.join(foldername, new_name))
        elif os.path.isdir(path) and file not in folder_names:
            sortFolder(path)
            new_name = normalize(file)
            if file != new_name:
                os.rename(os.path.join(foldername, file),
                          os.path.join(foldername, new_name))
        else:
            print('ACHTUNG!!! DAS IST NICHT!!')
      # by Yevhen Ponomarov
    f_list = os.listdir(foldername)
    for file in f_list:
        extension = os.path.splitext(file)[1].lower()
        if extension in images:
            path = shutil.move(os.path.join(foldername, file),
                               os.path.join(foldername, 'images'))
        elif extension in video:
            path = shutil.move(os.path.join(foldername, file),
                               os.path.join(foldername, 'video'))
        elif extension in music:  # by Yevhen Ponomarov
            path = shutil.move(os.path.join(foldername, file),
                               os.path.join(foldername, 'audio'))
        elif extension in documents:
            path = shutil.move(os.path.join(foldername, file),
                               os.path.join(foldername, 'documents'))
        elif extension in archives:
            path = shutil.unpack_archive(os.path.join(foldername, file),
                os.path.join(foldername, 'archives', file), extension[1:])
            os.remove(os.path.join(foldername, file))
            # by Yevhen Ponomarov
    eraseEmptyFolders(foldername)
# by Yevhen Ponomarov
sortFolder(sys.argv[1])
