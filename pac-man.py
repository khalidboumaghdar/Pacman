from src.core.game import Game
from src.config.loader import Parser
from src.entities.entity import Entity
from src.entities.player import Player
from src.maze.adapter import MazeAdapter
from src.entities.pickups import Pickups
from src.entities.ghost import Ghost
from src.entities.specialData import SpecialData
from src.ui.hub import Hub
import sys
import pygame
import time


if __name__ == "__main__":
    hub = Hub()
    hub.runMenu()