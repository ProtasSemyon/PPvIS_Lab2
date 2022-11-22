from abc import abstractclassmethod
from typing import List
from model import City, Rout


class Command():
    @abstractclassmethod
    def exec(self):
        pass
    
class AddRoadCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("add road")
    
class AddTrafficLightCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("add traffic light")
        
class DeleteRoadCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("delete road")
        
class DeleteTrafficLightCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("delete traffic light")
        
class AddBuildingCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("add building")
        
class DeleteBuildingCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("delete traffic light")
        
class ChangeRoadnameCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("change roadname command")
        
class ChangeLoadCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("change load")
        
class ChangeThroughputCommand(Command):
    def __init__(self, city: City):
        self.city = city
    def exec(self):
        print("change throughput")
        
class BuildRoutCommand(Command):
    def __init__(self, city: City, routes: List[Rout]):
        self.city = city
        self.routes = routes
    def exec(self):
        print("build rout")
        
class FindShortestRoutCommand(Command):
    def __init__(self, city: City, routes: List[Rout]):
        self.city = city
        self.routes = routes
    def exec(self):
        print("find shortest route")

class FindFastestRoutCommand(Command):
    def __init__(self, city: City, routes: List[Rout]):
        self.city = city
        self.routes = routes
    def exec(self):
        print("find shortest route")    

