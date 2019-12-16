#!/usr/bin/env python
# -*- coding: utf-8 -*-

from probe import Probe

import unittest


class TestProbe(unittest.TestCase):

    def setUp(self):
      self._probe = Probe()

    def test_stop_method(self):
      self._probe.stop()
      self.assertEqual('stop method', self._probe.run())

    def test_install_method(self):
      self._probe.install()
      self.assertEqual('install method', self._probe.run())      

    def test_read_method(self):
      self._probe.read()
      self.assertEqual('read method', self._probe.run())

    def test_uninstall_method(self):
      self._probe.uninstall()
      self.assertEqual('uninstall method', self._probe.run())            


if __name__ == '__main__':
    unittest.main()