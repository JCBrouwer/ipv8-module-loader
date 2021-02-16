

import abc
import six


class EventProcessor(six.with_metaclass(abc.ABCMeta, object)):

    @abc.abstractmethod
    def process_event(self, event):
        pass
