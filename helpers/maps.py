from .sub import sub


def open_map(location):
    assert isinstance(location, str)
    sub(['xdg-open', 'https://www.google.nl/maps/place/' + location])
