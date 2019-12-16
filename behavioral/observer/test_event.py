#!/usr/bin/env python
# -*- coding: utf-8 -*-


from event import Event
from event import EventPool

import unittest


def handler_temperature_event1(*args, **kwargs):
    pass
    # print('args', args)
    # print('kwargs', kwargs)

def handler_temperature_event2(*args, **kwargs):
    pass
    # print('args', args)
    # print('kwargs', kwargs)    


class TestEvent(unittest.TestCase):

    def setUp(self):
        self._event = Event('temperature.high')

    def test_add_handler(self):
        self._event.add_handler(handler_temperature_event1)
        self.assertEqual(handler_temperature_event1, 
                         self._event.get_handlers()[id(handler_temperature_event1)])

    def test_remove_handler(self):
        self._event.add_handler(handler_temperature_event1)
        self._event.remove_handler(handler_temperature_event1)
        self.assertEqual({}, self._event.get_handlers())

    def test_count_handlers(self):
        self._event.add_handler(handler_temperature_event1)
        self._event.add_handler(handler_temperature_event1)
        self._event.add_handler(handler_temperature_event2)
        self._event.add_handler(handler_temperature_event2)
        self.assertEqual(2, len(self._event.get_handlers()))

    def test_count_notified(self):
        self._event.add_handler(handler_temperature_event1)
        self._event.add_handler(handler_temperature_event2)
        self.assertEqual(2, self._event.register('payload'))       

    def test_clear_handlers(self):
        self._event.add_handler(handler_temperature_event1)
        self._event.add_handler(handler_temperature_event2)
        self._event.clear_handlers()
        self.assertEqual(0, len(self._event.get_handlers()))



class TestEventPool(unittest.TestCase):

    def setUp(self):
        self._event_high_temperature = Event('temperature.high')
        self._event_low_temperature = Event('temperature.low')
        self._event_high_temperature.add_handler(handler_temperature_event1)
        self._event_low_temperature.add_handler(handler_temperature_event2)
        self._event_pool = EventPool()

    def test_add_event(self):
        self._event_pool.add_event(self._event_low_temperature)
        self.assertEqual(self._event_low_temperature, 
                         self._event_pool.get_events()[self._event_low_temperature.get_name()])

    def test_remove_event(self):
        self._event_pool.add_event(self._event_low_temperature)
        self._event_pool.remove_event(self._event_low_temperature)
        self.assertEqual({}, self._event_pool.get_events())

    def test_count_events(self):
        self._event_pool.add_event(self._event_high_temperature)
        self._event_pool.add_event(self._event_low_temperature)
        self.assertEqual(2, len(self._event_pool.get_events()))

    def test_count_notified(self):
        self._event_pool.add_event(self._event_high_temperature)
        self._event_pool.add_event(self._event_low_temperature)
        self.assertEqual(1, self._event_pool.register('temperature.high', 'payload'))           

    def test_clear_events(self):
        self._event_pool.add_event(self._event_high_temperature)
        self._event_pool.add_event(self._event_low_temperature)
        self._event_pool.clear_events()
        self.assertEqual(0, len(self._event_pool.get_events()))


if __name__ == '__main__':
    unittest.main()





