from yt_concate.model.found import Found
from .step import Step


class Search(Step):
    def process(self, data, inputs, utils):
        search_term = inputs['search_term']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue

            for caption in captions:
                if search_term in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        print('found', len(found), '"', inputs['search_term'], '" in all the captions we have.')
        return found
