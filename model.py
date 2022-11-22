from typing import List


class Building():
    def __init__(self, name: str):
        self.name = name

class TrafficLight():
    def __init__(self, throughput: int):
        self.throughput = throughput

class Road():
    def __init__(self, load: int, name: str, buildings: List[Building], trafficLights: List[TrafficLight] ):
        self.name = name
        self.buildings = buildings
        self.trafficLights = trafficLights
        self.load = load

class City():
    def __init__(self, roads: List[Road]):
        self.roads = roads
        
class Rout():
    def __init__(self, roads: List[Road]):
        self.roads = roads
        self.name = str(roads[0].name) +"-" + str(roads[-1].name)




