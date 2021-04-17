from components.illumination.SubseaLight import SubseaLight
from util.RotDirection import RotDirection

light = SubseaLight(None, 5)

pw = light.setBrightness(0.5)
brightness = light.getBrightness()

print("Brightness: " + str(brightness))
