import soundtrack
import filesystem as fs
from filesystem import directory as dir
from filesystem import file as fsfile

music_repo = f'{fs.CURRENT_LOCATION}/Music'
converted_repo = f'{fs.CURRENT_LOCATION}/Converted'

if not dir.exists(music_repo):
    dir.create(music_repo)

if not dir.exists(converted_repo):
    dir.create(converted_repo)

music_list = fsfile.get_files(music_repo, True, ".mp3")

soundtrack.separate(music_list, converted_repo)
print(f'Separation completed. Check the output folder "{converted_repo}" for the isolated vocals.')