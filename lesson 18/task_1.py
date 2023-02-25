import re

regex = re.compile(r"""
    ^([#][0-9A-Fa-f]{6})?
    (rgb\((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]),
    (\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]),
    (\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\))?$
    """, re.VERBOSE)

hex_color = regex.match("#800080")
print(hex_color)
rgb_color = regex.match("rgb(228,69,33)")
print(rgb_color)