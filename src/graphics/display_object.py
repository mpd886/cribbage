

class DisplayObject:
    def __init__(self, parent):
        """
        create display object
        :param parent:  GraphicsObject object
        """
        self.parent = parent



    def update(self, elapsed_time):
        """
        Update the display object
        :param elapsed_time: time (ms) since last time it was called
        :return: True if the object is done/disposed/can-be-removed
        """
        return False

    def draw(self):
        """
        Draw the display object
        """
        pass

    def handle_mouse_event(self, evt):
        """
        Handle/process mouse event
        :param evt: pygame mouse event
        :return: True if the event is consumed, false if someone else needs to deal with it.
        """
        return False

    def handle_key_event(self, evt):
        """
        Handle/process keystrokes
        :param evt: pygame key event
        :return: True if the event is consume, False if someone else should deal with it
        """
        return False