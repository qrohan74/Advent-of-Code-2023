import re
from operator import itemgetter
from dataclasses import dataclass
from aoc2023.common.logger import Logger
from aoc2023.common.puzzle import DailyPuzzle


@dataclass
class MapItem:
    """
    An item data class
    """
    destination_start: int
    source_start: int
    size: int
    destination_end: int = 0
    source_end: int = 0

    def __post_init__(self):
        self.destination_end = self.destination_start + self.size - 1
        self.source_end = self.source_start + self.size - 1


class Map:
    """
    A map class
    """

    def __init__(self):
        """
        Map creation
        """
        self.items = []

    def add(self, item: MapItem):
        self.items.append(item)

    def get(self, x: int) -> int:
        for item in self.items:
            if item.source_start <= x <= item.source_end:
                return item.destination_start + x - item.source_start
        return x

    def length(self) -> int:
        return len(self.items)


class Puzzle(DailyPuzzle):
    """
    A puzzle class
    """

    def __init__(self):
        """
        Puzzle creation
        """
        super().__init__(5, 1, self.go)
        self.seeds = []
        self.map_seed_to_soil = Map()
        self.map_soil_to_fertilizer = Map()
        self.map_fertilizer_to_water = Map()
        self.map_water_to_light = Map()
        self.map_light_to_temperature = Map()
        self.map_temperature_to_humidity = Map()
        self.map_humidity_to_location = Map()

    def parse_puzzle(self):
        """
        parse puzzle input
        """
        map_current = None
        for line in self.lines:
            if line.startswith("seeds:"):
                self.seeds = [int(n) for n in re.findall(r'\d+', line[7:])]
            elif line.startswith("seed-to-soil"):
                map_current = self.map_seed_to_soil
            elif line.startswith("soil-to-fertilizer"):
                map_current = self.map_soil_to_fertilizer
            elif line.startswith("fertilizer-to-water"):
                map_current = self.map_fertilizer_to_water
            elif line.startswith("water-to-light"):
                map_current = self.map_water_to_light
            elif line.startswith("light-to-temperature"):
                map_current = self.map_light_to_temperature
            elif line.startswith("temperature-to-humidity"):
                map_current = self.map_temperature_to_humidity
            elif line.startswith("humidity-to-location"):
                map_current = self.map_humidity_to_location
            else:
                if line:
                    (destination, source, size) = [int(s) for s in itemgetter(0, 1, 2)(line.split(' '))]
                    map_current.add(MapItem(destination_start=destination, source_start=source, size=size))

    def go(self):
        """
        Run puzzle
        """
        self.parse_puzzle()
        locations = [
            self.map_humidity_to_location.get(
                self.map_temperature_to_humidity.get(
                    self.map_light_to_temperature.get(
                        self.map_water_to_light.get(
                            self.map_fertilizer_to_water.get(
                                self.map_soil_to_fertilizer.get(
                                    self.map_seed_to_soil.get(n))))))) for n in self.seeds]
        Logger.debug("Locations=%s" % locations)
        Logger.info("Result=%d" % min(locations))
