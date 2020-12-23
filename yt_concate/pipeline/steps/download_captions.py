import time

import pytube as pt
from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('downloading captions for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            print('Downloading caption for', yt.url)
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError, pt.exceptions.RegexMatchError) as e:
                print('Found an Error: ', e, 'while downloading the caption for', yt.url)
                continue

            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('it took', end - start, 'seconds while downloading captions.')

        return data
