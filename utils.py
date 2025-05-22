import os
import uuid
from moviepy.editor import VideoFileClip
import yt_dlp

def download_video_and_extract_audio(url: str) -> str:
    try:
        unique_id = str(uuid.uuid4())
        video_path = f"temp_video_{unique_id}.mp4"
        audio_path = f"audio_{unique_id}.wav"

        # yt-dlp options to download best mp4 video + audio merged
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': video_path,
            'quiet': True,
            'no_warnings': True,
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from URL: {url}")
            ydl.download([url])

        print(f"Video downloaded at: {video_path}")

        clip = VideoFileClip(video_path)
        if clip.audio is None:
            print("No audio stream found in the video.")
            clip.close()
            os.remove(video_path)
            return None

        clip.audio.write_audiofile(audio_path, codec='pcm_s16le')
        clip.close()

        os.remove(video_path)
        return audio_path

    except Exception as e:
        print(f"Error in download_video_and_extract_audio: {e}")
        import traceback
        traceback.print_exc()
        return None
