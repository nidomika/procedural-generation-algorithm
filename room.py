class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center(self) -> tuple:
        """Zwraca współrzędne centrum pokoju."""
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        return (center_x, center_y)
