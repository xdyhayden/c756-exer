"""
Return a unique hex hash for use in testing.
"""

# Standard libraries
import hashlib

def exercise_hash(ex_string):
    """
    Return a unique hex hash for this student and exercise.

    Parameters
    ----------
    ex_string: string
        A string identifying this exercise.
    
    Template variable
    -----------------
    ZZ-REG-ID: string
        A userid for the container registry used in this course
        (typically ghcr.io).
    
    Returns
    -------
    string
        A unique hex string, generated from the two parameters.
    """
    h = hashlib.sha256()
    h.update('ZZ-REG-ID'.encode('UTF-8'))
    h.update(ex_string.encode('UTF-8'))
    return h.hexdigest()