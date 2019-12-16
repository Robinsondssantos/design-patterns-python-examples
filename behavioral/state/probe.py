from abc import ABC, abstractmethod


class ProbeState(ABC):

    def __init__(self, parent):
        self._parent = parent

    @abstractmethod
    def stop(self):
        pass        

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def uninstall(self):
        pass

    @abstractmethod
    def run(self):
        pass


class ProbeStoppedState(ProbeState):

    def __init__(self, parent):
        super().__init__(parent)

    def stop(self):
        pass

    def read(self):
        self._parent.state = ProbeReadingState(self._parent)

    def install(self):
        self._parent.state = ProbeInstallingState(self._parent)

    def uninstall(self):
        self._parent.state = ProbeUninstallingState(self._parent)

    def run(self):
        return 'stop method'


class ProbeReadingState(ProbeState):

    def __init__(self, parent):
        super().__init__(parent)

    def stop(self):
      self._parent.state = ProbeStoppedState(self._parent)        

    def read(self):
        pass

    def install(self):
        self._parent.state = ProbeInstallingState(self._parent)

    def uninstall(self):
        self._parent.state = ProbeUninstallingState(self._parent)

    def run(self):
        return 'read method'


class ProbeInstallingState(ProbeState):

    def __init__(self, parent):
        super().__init__(parent)

    def stop(self):
      self._parent.state = ProbeStoppedState(self._parent)        

    def read(self):
        self._parent.state = ProbeReadingState(self._parent)

    def install(self):
        pass

    def uninstall(self):
        self._parent.state = ProbeUninstallingState(self._parent)

    def run(self):
        return 'install method'


class ProbeUninstallingState(ProbeState):

    def __init__(self, parent):
        super().__init__(parent)

    def stop(self):
      self._parent.state = ProbeStoppedState(self._parent)        

    def read(self):
        self._parent.state = ProbeReadingState(self._parent)

    def install(self):
        self._parent.state = ProbeInstallingState(self._parent)

    def uninstall(self):
        pass

    def run(self):
        return 'uninstall method'


class Probe(object):

    def __init__(self):
        self.state = ProbeStoppedState(self)

    def stop(self):
      self.state.stop()      

    def read(self):
        self.state.read()

    def install(self):
        self.state.install()

    def uninstall(self):
        self.state.uninstall()

    def run(self):
        return self.state.run()


def main():
    probe = Probe()
    print(probe.run())
    probe.install()
    print(probe.run())
    probe.read()
    print(probe.run())
    probe.uninstall()
    print(probe.run())


if __name__ == '__main__':
    main()      