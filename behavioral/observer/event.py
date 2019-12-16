class EventPool(object):

    def __init__(self):
        self._events = {}

    def register(self, event_name, *args, **kwargs):
        if self._events.get(event_name):
            return self._events[event_name].register(args, kwargs)
        return 0

    def _remove_event(self, event):
        if self._events.get(event.get_name()):
            self._events.pop(event.get_name())

    def add_event(self, event):
        self._remove_event(event)
        self._events[event.get_name()] = event
        return self

    def remove_event(self, event):
        self._remove_event(event)
        return self

    def get_events(self):
        return self._events

    def clear_events(self):
        self._events = {}


class Event(object):

    def __init__(self, name):
        self._name = name
        self._handlers = {}

    def get_name(self):
        return self._name

    def register(self, *args, **kwargs):
        return self._notify(args, kwargs)

    def _remove_handler(self, handle):
        if self._handlers.get(id(handle)):
            self._handlers.pop(id(handle))

    def add_handler(self, handler):
        self._handlers[id(handler)] = handler
        return self

    def remove_handler(self, handler):
        self._remove_handler(handler)
        return self

    def get_handlers(self):
        return self._handlers

    def _notify(self, *args, **kwargs):
        count = 0
        for handle in self._handlers.values():
            handle(args, kwargs)
            count += 1
        return count

    def clear_handlers(self):
        self._handlers = {}

    def __str__(self):
        return self.get_name()     


def main():

    def event_handler1(*args, **kwargs):
        print('args',args)
        print('kwargs', kwargs)

    def event_handler2(*args, **kwargs):
        print('args',args)
        print('kwargs', kwargs)              

    event = Event('temperature.high')
    event.add_handler(event_handler1)
    event.add_handler(event_handler2)
    # print('notified', event.register('event', value = 45))
    print('event', event.get_handlers())

    event_pool = EventPool()
    event_pool.add_event(event)
    print('notifired:', event_pool.register('temperature.high', 'event', {'value': 45}))


if __name__ == '__main__':
    main()      


