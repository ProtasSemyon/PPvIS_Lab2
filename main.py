import ui
import command as cmd
import model as md
from tkinter import *
from PIL import Image, ImageTk

class Application():
    def __init__(self):
        traffic_lights = [md.TrafficLight(x*30%23) for x in range(16)]
        city = md.City([md.Road(x*15, "Название улицы" + str(x), [md.Building("Здание" + str(x*10+i)) for i in range(5)], [traffic_lights[x], traffic_lights[x+1]]) for x in range(15)])
        routes = [md.Rout(city.roads[x:-x]) for x in range(1,6)]
        self.app_ui = ui.ApplicationWindow(add_road_command=cmd.AddRoadCommand(city),
                                           add_traffic_light_command=cmd.AddTrafficLightCommand(city),
                                           add_building_command=cmd.AddBuildingCommand(city),
                                           delete_building_command=cmd.DeleteBuildingCommand(city),
                                           delete_road_command=cmd.DeleteRoadCommand(city),
                                           delete_traffic_light_command=cmd.DeleteTrafficLightCommand(city),
                                           change_load_command=cmd.ChangeLoadCommand(city),
                                           change_roadname_command=cmd.ChangeRoadnameCommand(city),
                                           change_throughput_command=cmd.ChangeThroughputCommand(city),
                                           find_shortest_rout_command=cmd.FindShortestRoutCommand(city, routes),
                                           build_rout_command=cmd.BuildRoutCommand(city, routes),
                                           find_fastest_rout_command=cmd.FindFastestRoutCommand(city, routes))
    
    def run(self):
        self.app_ui.run()


if __name__ == '__main__':
    Application().run()