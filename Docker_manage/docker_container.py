from subprocess import call, check_output


class DockerContainer(object):

    def __init__(self, image, name=''):
        self.image = image

        self._name = name

        self._id = None

        self._p = dict()

        self._v = dict()

        self._cmd = ''

        self._d = False
        self._i = False
        self._t = False

    @staticmethod
    def _call(command):
        call(command)

    def run(self, cmd=None, d=None, i=None, t=None):
        command = self._run_command(cmd=cmd, d=d, i=i, t=t)
        self._call(command)

        self.get_id()

    def get_id(self):
        if self._name:
            self._id = check_output(['docker', 'ps', '-aqf', 'name={}'.format(self._name)])

    def rm(self, f=False):
        command = ['docker', 'rm']
        if f:
            command.append('-f')
        command.append(self._id or self._name)
        self._call(command)

    def rerun(self, cmd=None, d=None, i=None, t=None):
        self.rm(f=True)
        self.run(cmd=cmd, d=d, i=i, t=t)

    def _run_command(self, cmd, d, i, t):
        command = ['docker', 'run']
        if d is not None:
            if d:
                command.append('-d')
        elif self._d:
            command.append('-d')

        if i is not None:
            if i:
                command.append('-i')
        elif self._i:
            command.append('-i')

        if t is not None:
            if t:
                command.append('-t')
        elif self._t:
            command.append('-t')

        if self._name:
            command.append('--name')
            command.append(self._name)
        if self._p:
            for k, v in self._p.items():
                command.append('-p')
                command.append('{}:{}'.format(k, v))
        if self._v:
            for k, v in self._v.items():
                command.append('-v')
                command.append('{}:{}'.format(k, v))

        command.append(self.image)

        if cmd is not None:
            for _cmd in cmd.split(' '):
                command.append(_cmd)
        elif self._cmd:
            for _cmd in self._cmd.split(' '):
                command.append(_cmd)

        return command

    def name(self, name):
        self._name = name
        return self

    def p(self, host_port, container_port):
        self._p[host_port] = container_port
        return self

    def v(self, host_volume, container_volume):
        self._v[host_volume] = container_volume
        return self

    def d(self):
        self._d = True
        return self

    def i(self):
        self._i = True
        return self

    def t(self):
        self._t = True
        return self

    def cmd(self, cmd):
        self._cmd = cmd
