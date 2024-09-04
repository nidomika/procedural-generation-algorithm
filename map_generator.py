import random
from room import Room

class Leaf:
    def __init__(self, x, y, width, height, level):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room = None
        self.left_child = None
        self.right_child = None
        self.min_size = 10
        self.level = level

    def split(self):
        if self.left_child or self.right_child:
            return False

        split_horizontally = random.choice([True, False])

        if self.width > self.height and self.width / self.height >= 1.25:
            split_horizontally = False
        elif self.height > self.width and self.height / self.width >= 1.25:
            split_horizontally = True

        max_split = (self.height if split_horizontally else self.width) - self.min_size
        if max_split <= self.min_size:
            return False

        split_point = random.randint(self.min_size, max_split)

        if split_horizontally:
            self.left_child = Leaf(self.x, self.y, self.width, split_point, self.level)
            self.right_child = Leaf(self.x, self.y + split_point, self.width, self.height - split_point, self.level)
        else:
            self.left_child = Leaf(self.x, self.y, split_point, self.height, self.level)
            self.right_child = Leaf(self.x + split_point, self.y, self.width - split_point, self.height, self.level)

        return True

    def create_rooms(self):
        if self.left_child or self.right_child:
            if self.left_child:
                self.left_child.create_rooms()
            if self.right_child:
                self.right_child.create_rooms()

        if self.left_child and self.right_child:
            self.create_corridor(self.left_child.get_room(), self.right_child.get_room())
        else:
            room_size = (random.randint(4, self.width - 2), random.randint(4, self.height - 2))
            room_position = (random.randint(self.x, self.x + self.width - room_size[0]),
                             random.randint(self.y, self.y + self.height - room_size[1]))
            self.room = Room(room_position[0], room_position[1], room_size[0], room_size[1])

    def get_room(self):
        if self.room:
            return self.room
        if self.left_child:
            return self.left_child.get_room()
        if self.right_child:
            return self.right_child.get_room()
        return None

    def create_corridor(self, room1, room2):
        x1, y1 = room1.center()
        x2, y2 = room2.center()

        if random.choice([True, False]):
            self.draw_horizontal_corridor(x1, x2, y1)
            self.draw_vertical_corridor(y1, y2, x2)
        else:
            self.draw_vertical_corridor(y1, y2, x1)
            self.draw_horizontal_corridor(x1, x2, y2)

    def draw_horizontal_corridor(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.level.map[y][x] = '.'

    def draw_vertical_corridor(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.level.map[y][x] = '.'

def generate_map(level):
    root = Leaf(0, 0, level.width, level.height, level)
    leaves = [root]
    splitting = True

    while splitting:
        splitting = False
        for leaf in leaves:
            if not leaf.left_child and not leaf.right_child:
                if leaf.split():
                    leaves.append(leaf.left_child)
                    leaves.append(leaf.right_child)
                    splitting = True

    root.create_rooms()

    for leaf in leaves:
        if leaf.room:
            level.add_room(leaf.room)
