import subprocess


class Speak(object):

    def __init__(self):
        """
        Yet Another Python Wrapper for Espeak.
        This time, in 2.7.
        """
        self.args = ['-a 100',
                     ' -g 10',
                     ' -k 1',
                     ' -l 1',
                     ' -p 50',
                     ' -s 175',
                     ' -v en']

    def save(self, text, filename):
        args = ''.join(self.args)
        cmd = 'espeak {} -w {} "{}"'.format(args, filename, text)
        return self._execute(cmd)

    def _execute(self, cmd):
        return subprocess.check_output(
                   cmd,
                   stderr=subprocess.PIPE,
                   shell=True)

