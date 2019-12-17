class Event(object):

    def do(self):
        print('do something')


class EventWrapper(object):

    def __init__(self, event):
        self._event = event

    def do(self):
        print('do something before')
        self._event.do()


def main():
    event = Event()
    # event.do()
    event_wrapper = EventWrapper(event)
    # event_wrapper.do()
    another_event_wrapper = EventWrapper(event_wrapper)
    another_event_wrapper.do()


if __name__ == '__main__':
    main()