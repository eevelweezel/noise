import nussl
from audioread import NoBackendError
from gtts import gTTS

def process_audio():
    """
    Separate audio file.
    So far, Repet shows the most promise.
    """
    a_file = raw_input('Path to Audio file')
    try:
        repet = nussl.Repet(a_file)
        repet.run()
        rpt_period = repet.repeating_period
        # TODO: do something with these.
        fg, bg = repet.make_audio_signals()
    except NoBackendError:
        print 'No backend for selected media format, please ensure ffmpeg is installed.'
    return fg, bg

def process_lyrics():
    """
    Process a text file containing new lyrics.
    """
    l_file = raw_input('Path to lyrics file')
    with open(l_file, 'r') as l:
        text = list(l)
    lyrics = []
    for i in text:
        lyrics.append(gTTS(i))
    return lyrics


if __name__ == '__main__':
    # TODO: do that thing...
    process_file()
    process_lyrics()
