from .sub import sub


def open_map(location):
    assert isinstance(location, str)
    sub(['google-chrome', 'https://www.google.nl/maps/place/' + location])
