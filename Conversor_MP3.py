import csv
import os
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip

def read_links_and_titles_from_csv(csv_file):
    links_with_titles = []
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            links_with_titles.append((row[0], extract_video_title(row[0])))
    return links_with_titles

def extract_video_title(link):
    ydl_opts = {'quiet': True}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)
            return info.get('title', None)
    except Exception as e:
        print(f"Erro ao extrair título de {link}: {e}")
        return None

def prompt_download_confirmation(links_with_titles):
    print("Lista de vídeos para baixar:")
    for link, title in links_with_titles:
        print(f"- {title}")

    valid_responses = {"sim", "yes", "no", "nao", "não", "n", "s"}
    while True:
        response = input("Deseja baixar esses vídeos? (sim/não): ").strip().lower()
        if response in valid_responses:
            break
        else:
            print("Entrada inválida. Por favor, digite 'sim' ou 'não'.")

    return response in {"sim", "yes", "s"}

def download_videos(links_with_titles):
    downloaded_videos = []
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.expanduser("~/Music/%(title)s.%(ext)s"),
        'quiet': True,
    }

    for link, title in links_with_titles:
        try:
            with YoutubeDL(ydl_opts) as ydl:
                print(f"Baixando {title}...")
                ydl.download([link])
                print(f"{title} foi baixado com sucesso!")
                downloaded_videos.append(title)
        except Exception as e:
            print(f"Erro ao baixar {title}: {e}")
    return downloaded_videos

def convert_to_mp3(mp4_directory):
    for filename in os.listdir(mp4_directory):
        if filename.endswith(".mp4"):
            mp4_file = os.path.join(mp4_directory, filename)
            mp3_file = os.path.join(mp4_directory, os.path.splitext(filename)[0] + ".mp3")

            try:
                video_clip = VideoFileClip(mp4_file)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(mp3_file)
                audio_clip.close()
                video_clip.close()
                os.remove(mp4_file)
                print(f"{filename} foi convertido para MP3 com sucesso!")
            except Exception as e:
                print(f"Erro ao converter {filename} para MP3: {e}")


if __name__ == "__main__":
    csv_file = "youtube_links.csv"
    links_with_titles = read_links_and_titles_from_csv(csv_file)
    
    if prompt_download_confirmation(links_with_titles):
        downloaded_videos = download_videos(links_with_titles)
        directory = os.path.expanduser("~/Music")
        convert_to_mp3(directory)
    else:
        print("Download cancelado.")
