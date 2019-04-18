import nussl
from audioread import NoBackendError
from gtts import gTTS

def process_audio(lyrics):
    """
    :lyrics -  gtts audio generated from lyrics
    :a_file - user input of path/to/audio.file

    Step 1: separate audio file (Repet shows the most promise)
    - need to play w/ masks, threshholds

    Step 2: apply a stft to lyrics based on fg, apply this to bg

    Step 3: profit.
    """
    a_file = raw_input('Path to Audio file')
    try:
        repet = nussl.Repet(a_file)
        repet.run()
        rpt_period = repet.repeating_period
        # TODO: do something neat with these.
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
    lyrics = process_lyrics()
    process_audio(lyrics)
