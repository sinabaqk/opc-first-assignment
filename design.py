class Design:

    def __init__(self, name, lower_left_x, lower_left_y, upper_right_x,	upper_right_y, polygon_count, md5sum):
        self.name = name
        self.md5sum = md5sum
        area = (upper_right_x - lower_left_x) * (upper_right_y - lower_left_y) / 1000000
        self.density = polygon_count / area
