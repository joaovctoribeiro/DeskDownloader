import os
from pytube import YouTube

def download_video(url, download_path):

    """
        Baixa o vídeo do YouTube

        URL: URL do vídeo do YouTube;
        download_path: Caminho para onde o vídeo vai ser salvo;
        return: Mensagem de erro ou sucesso.
    """

    try:

        # Cria um objeto a partir da URL.
        # Seleciona o vídeo na melhor qualidade.
        # Faz o download num diretório especificado.
        # Retorna a mensagem de erro ou sucesso.

        youtube = YouTube(url)
        stream = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download(download_path)
        return f"Vídeo baixado com sucesso em {download_path}"
    
    except Exception:

        return f"Erro ao baixar o vídeo: Verique se a URL está correta."

def download_audio(url, download_path):

    """
        Baixa o áudio do YouTube

        URL: URL do vídeo do YouTube;
        download_path: Caminho para onde o áudio vai ser salvo;
        return: Mensagem de erro ou sucesso.
    """

    try:

        # Cria um objeto a partir da URL.
        # Seleciona o áudio na melhor qualidade.
        # Faz o download num diretório especificado.
        # Retorna a mensagem de erro ou sucesso.

        youtube = YouTube(url)
        stream = youtube.streams.filter(only_audio=True).first()
        out_file = stream.download(download_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        return f"Áudio baixado com sucesso em {download_path}"
        
    except Exception:

        return f"Erro ao baixar o áudio: Verifique se a URL está correta."