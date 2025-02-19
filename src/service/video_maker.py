import moviepy.editor as mp
from datetime import datetime

from config.config import config
from utils.drawer import Drawer


class VideoMaker:
    '''
    ffmpeg -i movie.mp4 -vf scale=1280:720 movie_new.mp4
    '''
    def __init__(self, drawer: Drawer) -> None:
        self.drawer = drawer

    def make_video(self, video_file_path_list: list):
        try:
            for video_file in video_file_path_list:
                video = mp.VideoFileClip(f'{config.W13_DIR}/{video_file}')
                gif_file = video_file.replace('.mp4', '.gif')
                video.write_gif(f'{config.W13_DIR}/{gif_file}', fps=10)

            dtime_format = '%Y-%m-%d-%H-%M-%S'
            v1_time = datetime.strptime(video_file_path_list[0].split('_')[-1].replace('.mp4', ''), dtime_format)
            v2_time = datetime.strptime(video_file_path_list[1].split('_')[-1].replace('.mp4', ''), dtime_format)
            seconds = (v1_time - v2_time).total_seconds()

            if seconds < 0:
                video = mp.VideoFileClip(f'{config.W13_DIR}/{video_file_path_list[0]}')
                v1 = self.drawer.draw_text_on_video(video, '시공전')
                video = mp.VideoFileClip(f'{config.W13_DIR}/{video_file_path_list[1]}')
                v2 = self.drawer.draw_text_on_video(video, '시공후')
            else:
                video = mp.VideoFileClip(f'{config.W13_DIR}/{video_file_path_list[1]}')
                v1 = self.drawer.draw_text_on_video(video, '시공전')
                video = mp.VideoFileClip(f'{config.W13_DIR}/{video_file_path_list[0]}')
                v2 = self.drawer.draw_text_on_video(video, '시공후')

            fname = f'{config.W13_DIR}/fin.mp4'
            fin_video = mp.concatenate_videoclips([v1, v2], method='compose')
            fin_video.to_videofile(fname, fps=60, remove_temp=True, audio_codec='aac')

        except ValueError:
            pass
        except Exception:
            import traceback
            print(traceback.format_exc())
