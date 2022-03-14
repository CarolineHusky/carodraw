from carotools.events import Event


class RevertableEvent(Event):
    def revert(self):
        self.fire(lambda handler: handler.kwargs["revert"])