class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [['▮' for _ in range(width)] for _ in range(height)]

    def add_room(self, room):
        """Dodaje pokój do mapy."""
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                self.map[y][x] = '.'

    def add_corridor(self, x1, y1, x2, y2):
        """Dodaje korytarz między dwoma punktami (x1, y1) i (x2, y2)."""
        if x1 == x2:  # Pionowy korytarz
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.map[y][x1] = '.'
        elif y1 == y2:  # Poziomy korytarz
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.map[y1][x] = '.'
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.map[y1][x] = '.'
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.map[y][x2] = '.'

    def print_map(self):
        """Wyświetla mapę w konsoli."""
        for row in self.map:
            print("".join(row))
