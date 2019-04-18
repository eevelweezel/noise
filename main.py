import nussl
from audioread import NoBackendError


def process_file():
    a_file = raw_input('Path to Audio file')
    try:
        repet = nussl.Repet(a_file)
        repet.run()
        rpt_period = repet.repeating_period
        fg, bg = repet.make_audio_signals()
    except NoBackendError:
        print 'No backend for selected media format, please ensure ffmpeg is installed.'


if __name__ == '__main__':
    # TODO: do that thing...
    process_file()

