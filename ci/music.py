"""
Perform requests to the music service.
"""

# Standard library modules

# Installed packages
import requests


class Music():
    """Perform requests to the music service.

    Parameters
    ----------
    url: string
        The URL for accessing the music service. Often
        'http://cmpt756s2:30001/'. Note the trailing slash.
    auth: string
        Authorization code to pass to the music service. For many
        implementations, the code is required but its content is
        ignored.
    """
    def __init__(self, url, auth):
        self._url = url
        self._auth = auth
    
    def create(self, artist, song):
        """Create an artist, song pair.

        Parameters
        ----------
        artist: string
            The artist performing song.
        song: string
            The name of the song.

        Returns
        -------
        (number, string)
            The number is the HTTP status code returned by Music.
            The string is the UUID of this song in the music database.
        """
        r = requests.post(
            self._url,
            json={'Artist': artist,
                 'SongTitle': song},
            headers={'Authorization': self._auth}
        )
        return r.status_code, r.json()['music_id']

    def read(self, m_id):
        """Read an artist, song pair.

        Parameters
        ----------
        m_id: string
            The UUID of this song in the music database.

        Returns
        -------
        number
            The HTTP status code returned by Music.
        
        Notes
        -----
        This routine should return the song title and artist in
        addition to the status code.
        """
        r = requests.get(
            self._url + m_id,
            headers={'Authorization': self._auth}
            )
        return r.status_code

    def delete(self, m_id):
        """Delete an artist, song pair.

        Parameters
        ----------
        m_id: string
            The UUID of this song in the music database.

        Returns
        -------
        Does not return anything. The music delete operation
        always returns 200, HTTP success.
        """
        requests.delete(
            self._url + m_id,
            headers={'Authorization': self._auth}
        )
