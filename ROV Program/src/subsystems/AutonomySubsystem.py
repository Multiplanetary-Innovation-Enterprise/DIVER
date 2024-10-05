from subsystems.Subsystem import Subsystem
from components.controllers.Controller import Controller
from dijkstar import Graph, find_path
from math import sqrt


class AutonomySubsystem(Subsystem):
    __isEnabled = False
    __graph = Graph(undirected=True)
    #scale currently somewhat abstract, will be better defined later
    #size of box of points that ROV will navigate through
    __boxSize = 20
    #time between refreshes of algorithm (smaller is more accurate, but more intensive)
    #due to slow speed of ROV refresh rate can be longer
    #
    # ROV Speed =  Box size * refresh rate
    #
    #no need to define points where the ROV won't navigate in the time it takes to refresh
    __refreshPeriod = 10
    #will change density of points
    #denser points are more intensive but more accurate
    __pointdensity = 1
    def __init__(self, controller:Controller, config):
        super().__init__(controller, config)

    #may add thread or process to refresh independently
    def refresh(self,sensorData:list):
        if self.__isEnabled:
            #assuming y is vertical
            #Goal Point will give algorithm a "motivation" to go deeper
            #Will therefore only surface once all other options have been exhausted
            #Need to add ability for the ROV to return to the surface to charge if necessary
            goalPoint = (0,-50,0) 

            #for every point (x, y, z)
            #ROV is defined at being at point (0,0,0)
            for x in range((self.__boxSize * -1 * (1 / self.__pointdensity)),self.__boxSize * (1 / self.__pointdensity)):
                for y in range((self.__boxSize * -1) * (1 / self.__pointdensity),self.__boxSize * (1 / self.__pointdensity)):
                    for z in range((self.__boxSize * -1) * (1 / self.__pointdensity),self.__boxSize * (1 / self.__pointdensity)):
                        #interconnect to 26 closest points (not including self)
                        for xoffset in range(-1,1):
                            for yoffset in range(-1,1):
                                for zoffset in range(-1,1):
                                    #CHANGE THIS WHEN INTEGRATING SENSOR DATA!!!
                                    #Do not allow a point to connect to point if a wall is in between them
                                    #Do this by changing True to a condition that tests if there is a wall between the points
                                    if (True and (self.__graph.get_edge((x,y,z),(x+xoffset,y+yoffset,z+zoffset))) != 1 and not (x == 0 and y ==0 and z == 0)):
                                        self.__graph.add_edge((x,y,z),(x+xoffset,y+yoffset,z+zoffset),1)
            
            #navigate across defined points to goal
            find_path(self.__graph,(0,0,0),goalPoint)


    def getEnabled(self):
        return self.isEnabled
    
    def setEnabled(self,enabled:bool):
        self.__isEnabled = enabled