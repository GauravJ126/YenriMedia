import time

from moviepy import *
from instapy_cli import client
from pytube import YouTube
import random
import os


class ErrorHandler:
    def __init__(self):
        pass


class Handler:
    Location = 'C:/Users/user/Desktop/Projects/Gaurav/learn/YenriMedia'

    def __init__(self, link):
        self.link = link
        self.get_video()

    def get_video(self):
        try:
            yt = YouTube(self.link)
        except Exception as e:
            raise f"Error with link {e}"

        mp4 = yt.streams.filter(file_extension="mp4").all()
        video = mp4[-1]

        try:
            video.download(output_path=self.Location)
        except Exception as e:
            raise f'Error downloading video,{e}'

        return video


class VideoManager:
    def __init__(self):
        self.Location = 'C:/Users/user/Desktop/Projects/Gaurav/learn/YenriMedia/brain_rot.mp4'
        self.Location = 'C:/Users/user/Desktop/Projects/Gaurav/learn/YenriMedia/content.mp4'
        try:
            self.content = VideoFileClip(self.Location)
            self.brain_rot = VideoFileClip(self.Location)
            self.content_length = round(self.content.duration)
            self.brain_rot_length = round(self.brain_rot.duration)

            if self.content_length > self.brain_rot_length:
                self.content = self.content.subclipped(0, self.brain_rot_length)
                self.content_length = round(self.content.duration)
            elif self.content_length < self.brain_rot_length:
                self.brain_rot = self.brain_rot.subclipped(0, self.content_length)
                self.brain_rot_length = round(self.brain_rot.duration)

            self.clips(self.brain_rot, self.content, self.content_length)
        except Exception as e:
            raise f"Error processing video {e}"

    def clips(self, up_video, down_video, duration):
        noc = round(duration / 15)
        for i in range(0, noc):
            up_clip = up_video.subclipped((i * 15), ((i + 1) * 15))
            down_clip = down_video.subclipped((i * 15), ((i + 1) * 15))
            clip = [[up_clip], [down_clip]]
            blank = TextClip(f"", fontsize=75, colour="black",
                             text_align="center", horizontal_align="center", vertical_align="center",
                             duration="10")
            text = TextClip(f"Part {i}", fontsize=75, colour="black",
                            text_align="center", horizontal_align="center", vertical_align="center",
                            duration="5")
            text_clip = concatenate_videoclips(blank, text)
            clip = CompositeVideoClip(clip, text_clip)
            clip = clip.cropped(x_center=clip.w / 2, y_center=clip.h / 2)  # Alter the dimension in 9x16 accordingly
            # clip.preview(fps=24)  #to preview the video
            clip.write_videofile(f"{self.Location}/Nam_media/Reel_{i}")


class PostManager:


    def __init__(self):
        self.user_name = ""
        self.password = ""
        self.Location = 'C:/Users/user/Desktop/Projects/Gaurav/learn/YenriMedia/Nam_media'
        self._upload()

    def _upload(self):
        # Should find a way to do the same for youtube shorts also
        hastags = ["#love", "#instagood", "#photooftheday", "#fashion", "#beautiful",
                   "#art", "#photography", "#happy", "#picoftheday", "#nature",
                   "#travel", "#wanderlust", "#travelphotography", "#vacation", "#beach",
                   "#adventure", "#explore", "#travelgram", "#sunset", "#roadtrip",
                   "#food", "#foodie", "#foodporn", "#yummy", "#homemade",
                   "#chef", "#delicious", "#healthyfood", "#eatclean", "#vegan",
                   "#fitness", "#workout", "#health", "#fitfam", "#motivation",
                   "#gym", "#yoga", "#healthylifestyle", "#wellness", "#exercise",
                   "#style", "#outfitoftheday", "#makeup", "#skincare", "#ootd",
                   "#fashionblogger", "#beauty", "#shopping", "#streetstyle", "#hairstyle",
                   "#entrepreneur", "#business", "#startup", "#success", "#motivational",
                   "#goals", "#branding", "#marketing", "#hustle", "#money",
                   "#tech", "#technology", "#gadgets", "#innovation", "#programming",
                   "#developer", "#ai", "#coding", "#robotics", "#software",
                   "#music", "#movie", "#dancing", "#funny", "#memes",
                   "#actor", "#model", "#party", "#singing", "#dj",
                   "#sports", "#football", "#basketball", "#soccer", "#cricket",
                   "#tennis", "#running", "#cycling", "#fitnessmotivation", "#training",
                   "#quotes", "#selfie", "#family", "#friends", "#dog",
                   "#cat", "#pets", "#traveladdict", "#explorer", "#weekend"
                   ]

        caption = (f"The greatest of content in the world, what is your thoughts on this!"
                   f"\n\n\n\n {random.sample(hastags, 15)}")
        for content in self.Location:
            if content.endswith('.mp4')
                with client(self.user_name,self.password) as cli:
                    cli.upload(content,caption)
                    print(f"posted a reel @{time.time()}")
            else:
                continue



