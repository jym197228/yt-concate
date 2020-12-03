import time

from pytube import YouTube
import pytube as pt

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            print('Downloading caption for', url)
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError, pt.exceptions.RegexMatchError) as e:
                print('Found an', e, 'while downloading the caption for', url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('it took', end - start, 'seconds while downloading captions.')
