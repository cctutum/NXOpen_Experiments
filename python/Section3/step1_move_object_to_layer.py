# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Created by theScriptingEngineer
#
import math
import NXOpen
import NXOpen.Layer
from typing import List


theSession  = NXOpen.Session.GetSession()
workPart = theSession.Parts.Work
displayPart = theSession.Parts.Display


def move_object_to_layer(object: NXOpen.DisplayableObject, layer: int):
    objectArray1 = [NXOpen.DisplayableObject.Null] * 1 
    objectArray1[0] = object
    workPart.Layers.MoveDisplayableObjects(layer, objectArray1)    


def get_all_bodies() -> List[NXOpen.Body]:
    all_bodies: List[NXOpen.Body] = []
    for item in workPart.Bodies: # type: ignore
        all_bodies.append(item)
    return all_bodies


def main() : 
    all_bodies: List[NXOpen.Body] = get_all_bodies()
    for _, body in enumerate(all_bodies):
        move_object_to_layer(body, 5) # move objects to layer=5


if __name__ == '__main__':
    main()
