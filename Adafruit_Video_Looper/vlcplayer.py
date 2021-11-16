# License: GNU GPLv2, see LICENSE.txt
import vlc

class VLCPlayer:
    def __init__(self, config):
        """Create an instance of a video player that runs omxplayer in the
        background.
        """
        print("Initializing VLC player")
        self._player = vlc.MediaPlayer()
        self._player.set_fullscreen(True)
        self._extensions = ["mp4", "avi"]

    def supported_extensions(self):
        """Return list of supported file extensions."""
        return self._extensions

    def play(self, movie, loop=None, vol=0):
        media = vlc.Media(movie.filename)
        media.parse()

        self._player.set_media(media)
        self._player.play()

    def is_playing(self):
        """Return true if the video player is running, false otherwise."""
        state = self._player.get_state()
        if state == vlc.State.Opening or state == vlc.State.Playing:
            return True
        else:
            return False

    def stop(self, block_timeout_sec=0):
        """Stop the video player.  block_timeout_sec is how many seconds to
        block waiting for the player to stop before moving on.
        """
        self._player.stop()

    @staticmethod
    def can_loop_count():
        return False

def create_player(config):
    """Create new video player based on VLC."""
    return VLCPlayer(config)
