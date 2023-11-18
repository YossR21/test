class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        if self.__status:
            self.__muted = False

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


# class Television:
#     # Class variables
#     MIN_VOLUME = 0
#     MAX_VOLUME = 2
#     MIN_CHANNEL = 0
#     MAX_CHANNEL = 3
#
#     def __init__(self):
#         # Instance variables (private)
#         self._status = False
#         self._muted = False
#         self._volume = self.MIN_VOLUME
#         self._channel = self.MIN_CHANNEL
#
#     def power(self):
#         self._status = not self._status
#
#     def mute(self):
#         self._muted = not self._muted
#         if self._muted:
#             self._volume = self.MIN_VOLUME
#
#     def channel_up(self):
#         if self._status:
#             self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)
#
#     def channel_down(self):
#         if self._status:
#             self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)
#
#     def volume_up(self):
#         if self._status:
#             self._muted = False  # Unmute if volume is adjusted
#             self._volume = min(self._volume + 1, self.MAX_VOLUME)
#
#     def volume_down(self):
#         if self._status:
#             self._muted = False  # Unmute if volume is adjusted
#             self._volume = max(self._volume - 1, self.MIN_VOLUME)
#
#     def __str__(self):
#         return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"
#
#
