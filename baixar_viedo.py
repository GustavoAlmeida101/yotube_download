from pytube import YouTube


#link do video a ser baixado
url = "https://www.youtube.com/watch?v=4avxH0WpS2k"

#Crie um objeto Yotube
yt = YouTube(url)

#Escolha a melhor qualidade disponivel
video_stream = yt.streams.get_highest_resolution()

#Baixe o video para o diretorio atual
video_stream.download()

print("download completo!!")