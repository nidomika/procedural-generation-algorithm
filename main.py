from level import Level
from map_generator import generate_map

if __name__ == "__main__":
    level = Level(70, 30)
    generate_map(level)
    level.print_map()
