from probe import Probe
import unittest


class TestProbe(unittest.TestCase):

    def setUp(self):
      self._probe = Probe()

    def test_stop_method(self):
      self._probe.stop()
      self.assertEqual(self._probe.run(), 'stop method')

    def test_install_method(self):
      self._probe.install()
      self.assertEqual(self._probe.run(), 'install method')      

    def test_read_method(self):
      self._probe.read()
      self.assertEqual(self._probe.run(), 'read method')

    def test_uninstall_method(self):
      self._probe.uninstall()
      self.assertEqual(self._probe.run(), 'uninstall method')            


if __name__ == '__main__':
    unittest.main()