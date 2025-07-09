from pytubefix import YouTube

url = input("Cole a sua url: ")

try:
    video = YouTube(url, use_oauth=True, allow_oauth_cache=True)
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Verifique se o objeto video foi criado com sucesso antes de prosseguir
if 'video' in locals() and video:
    mp4_streams = video.streams.get_highest_resolution()

    try:
        mp4_streams.download()
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")
else:
    print("Não foi possível processar o vídeo. Verifique a URL.")