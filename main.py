from audioread import NoBackendError
from gtts import gTTS
from numpy import fft
from nussl import (
    AudioSignal,
    Repet
)
from pyo import *

def process_audio(lyrics):
    """
    :a_file - user input of path/to/audio.file
    :o_file - user input of path/to/output.file

    Step 1: separate audio file (Repet shows the most promise)
    - need to play w/ masks, threshholds

    Step 2: run lyrics through vocoder(?) and match to fg, apply this to bg

    Step 3: profit.
    """
    a_file = raw_input('Path to Audio file:  ')
    o_file = raw_input('Path to Output file:  ')
    try:
        signal = nussl.AudioSignal(a_file)
        lyrics = AudioSignal(lyrics)
        rep = Repet(signal, 3)
        rep.run()
        fg, bg = rep.make_audio_signals()
        fg.write_audio_to_file('fg_temp.wav')
        bg.write_audio_to_file('bg_temp.wav')
        # TODO: need to determine which is fg...
        # Also, damn... projet takes a while.
        # probably need to find a vector from fg and
        # apply it to lyrics... or something.

        # init pyo
        s = Server().boot()
        s.start()
        # TODO: how do I actually read from files...?
        payload = PVMorph(lyrics, fg_signal, fade=0.5)
        output = PVMix(payload, bg_signal
        savefile(output, o_file, sr=44100, channels=1, fileformat=7)

    except NoBackendError:
        print 'No backend for selected media format, please ensure ffmpeg is installed.'
    return

def process_lyrics():
    """
    :l_file - user input of path/to/lyrics.file
    Process a text file containing new lyrics.
    """
    l_file = raw_input('Path to lyrics file')
    with open(l_file, 'r') as l:
        return gTTS(l_file)


if __name__ == '__main__':
    lyrics = process_lyrics()
    process_audio(lyrics)
