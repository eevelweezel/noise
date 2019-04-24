import os
from speek import Speak
from audioread import NoBackendError
from nussl import (
    AudioSignal,
    Repet
)
from pyo import *

def process_audio():
    """
    :a_file: user input of path/to/audio.file

    Step 1: separate audio file (Repet shows the most promise)
    - need to play w/ masks, threshholds

    Step 2: run lyrics through vocoder(?) and match to fg, apply this to bg

    Step 3: profit.
    """
    a_file = raw_input('Path to Audio file:  ')
    try:
        signal = AudioSignal(a_file)
        rep = Repet(signal, 3)
        rep.run()
        fg, bg = rep.make_audio_signals()
        fg.write_audio_to_file('fg_temp.wav')
        bg.write_audio_to_file('bg_temp.wav')
    except NoBackendError:
        print 'No backend for selected media format, please ensure ffmpeg is installed.'

def vocoder():
    """
    :o_file: name of .OGG output file

    Run foreground and lyrics through phase vocoder (pyo)
    """
    # init pyo
    s = Server().boot()
    s.start()
    o_file = raw_input('Name of Output file (.OGG format):  ')

    fg_sig = SfPlayer('fg_temp.wav', loop=False)
    lyr_sig = SfPlayer('lyrics_temp.wav', loop=True)
    bg_sig = SfPlayer('bg_temp.wav', loop=False)
    # ummm... prolly should handle some exceptions

    mix = PVMorph(lyr_sig, fg_sig, fade=0.5)
    output = PVMix(mix, bg_sig)
    savefile(output, o_file, sr=44100, channels=1, fileformat=0)

    print "Output written to {}, in .OGG format".format(o_file)

def process_lyrics():
    """
    :l_file: user input of path/to/lyrics.file

    Process a text file containing new lyrics.
    """
    l_file = raw_input('Path to lyrics file:  ')
    speak = Speak()
    outfile = '{}/lyrics_temp.wav'.format(
                     os.path.dirname(
                         os.path.abspath(__file__)))

    with open(l_file, 'r') as l:
        text = l.read()
        speak.save(text, outfile)
    return

def clean_up():
    """
    Delete temp files.
    """
    print "Cleaning up..."
    os.remove('lyrics_temp.wav')
    os.remove('bg_temp.wav')
    os.remove('fg_temp.wav')


if __name__ == '__main__':
    process_lyrics()
    process_audio()
    vocoder()
    clean_up()
