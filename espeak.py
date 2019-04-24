import subprocess


class Speak(object):

    def __init__(self):
        """
        Yet Another Python Wrapper for Espeak.
        This time, in 2.7.
        """
        self.args = {'amplitude': 100,
                     'word_gap': 10,
                     'capitals': 1,
                     'line_lenght': 1,
                     'pitch': 50,
                     'speed': 175,
                     'voice': 'en',
                     'spell_punctuation': '',
                     'split': ''}

    def save(self, text, filename):
        return self._execute(self._espeak_args(text,
                                               filename))

    def _execute(self, cmd):
        return subprocess.check_output(cmd,
                                       stderr=subprocess.PIPE).decode('UTF-8')
