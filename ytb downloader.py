import os
from shutil import move

from moviepy.editor import *
from youtubesearchpython import *
from yt_dlp import YoutubeDL


def downloadmusic():
    pesquisa = (input('Digite o nome de uma musica q deseja baixar: '))
    pesquisa = pesquisa + 'Official audio'
    busca = VideosSearch(pesquisa, limit = 1)
    for i in range(1):
        url = [busca.result()['result'][i]['link']]
        titulo = [busca.result()['result'][i]['title']]
        id = [busca.result()['result'][i]['id']]
        print(url)
        print(titulo)
        print(id)
        
        
        titulo = ' '.join([str(x) for x in titulo])
        
        id = ' '.join([str(x) for x in id])
        
    with YoutubeDL() as ydl:
        ydl.download(url)
        
        for root, dirs, files in os.walk(r'c:\Users\Cliente\Documents\vs code'):
            for file in files:
                if file.endswith('.mp4'):

                    mp4_file = os.path.join(root, file)
        
                    audioclip = AudioFileClip(mp4_file)
                    audioclip = audioclip.write_audiofile(mp4_file[:-4] + ".mp3")
                    AudioClip.close
        
                    os.remove(mp4_file)


def MoverArquivos(): 
    
    De = r'c:\Users\Cliente\Documents\vs code'
    Para = r'c:\Users\Cliente\Music'
    
    for root, dirs, files in os.walk(r'c:\Users\Cliente\Documents\vs code'):
        for file in files:
            if file.endswith('.mp3'):
                
                Pasta = De + file
                Destino = Para + file
                
                move(file, Para)
                    


downloadmusic()

while True:
    if input('deseja baixar mais alguma musica? ') == 'sim':
        downloadmusic()
    else:
        MoverArquivos()
        break
