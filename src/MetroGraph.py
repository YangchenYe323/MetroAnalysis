from typing import List, Dict
from distanceUtil import geometric_distance

class Station:
    '''
    Represent a metro station, a node 
    in the metro graph
    '''
    _name: str

    # longitude and latitude are used to calculate
    # the absolute distance between two stations
    _longitude: float
    _latitude: float

    def __init__(self, name: str, longitude: float, latitude: float) -> None:
        self._name = name
        self._longitude = longitude
        self._latitude = latitude
    
    def __eq__(self, other) -> bool:
        return self._name == other._name

class Line:
    '''
    A line is an array of Stations 
    '''
    _name: str
    # [start, sta, sta, ..., dest]
    _stations: List[Station]
    # if this is a loop line
    _loop: bool

    def __init__(self, name: str, loop: bool) -> None:
        self._name = name
        self._loop = loop
        self._stations = []
    
    def add_station(self, station: Station):
        self._stations.append(station)

    def get_distance(self, station1: Station, station2: Station) -> float:
        try:
            index1 = self._stations.index(station1)
            index2 = self._stations.index(station2)
            distance = abs(index1 - index2)
            if distance == 0:
                return 0
            # if neighbor
            if distance == 1 or (self._loop and distance == len(self._stations) - 1):
                return geometric_distance(station1._longitude, station1._latitude, station2._longitude, station2._latitude)
            return float('inf')
        except ValueError:
            # not in this line
            return float('inf')

class MetroMap:
    '''
    Represents the metro map for a city,
    it maintains a list of stations and a 
    graph describing which stations are
    connected
    '''
    # id -> station
    _stations: Dict[int, Station]
    _lines: Dict[str, Line]

    def __init__(self, stations: Dict[int, Station], lines: Dict[str, Line]) -> None:
        self._stations = stations
        self._lines = lines
    
    def getDistance(self, id1: int, id2: int) -> float:
        station1 = self._stations[id1]
        station2 = self._stations[id2]

        result = float('inf')
        for line in self._lines.values():
            if line.get_distance(station1, station2) < result:
                result = line.get_distance(station1, station2)
        return result
    
    def produce_matrix(self) -> List[List[float]]:
        num_station = len(self._stations)
        matrix = [[float('inf') for i in range(num_station)] for j in range(num_station)]
        for i in range(num_station):
            for j in range(num_station):
                matrix[i][j] = self.getDistance(i, j)
        return matrix

    def produce_absolute_distance_matrix(self) -> List[List[float]]:
        num_station = len(self._stations)
        return [ \
                [geometric_distance(self._stations[i]._longitude, self._stations[i]._latitude, self._stations[j]._longitude, self._stations[j]._latitude) \
                for i in range(num_station)] \
                for j in range(num_station) \
               ]
            
            
            
        

