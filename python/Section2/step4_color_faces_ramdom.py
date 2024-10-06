# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Created by theScriptingEngineer
#
import NXOpen
from typing import List
from random import randint


theSession  = NXOpen.Session.GetSession()
workPart: NXOpen.Part = theSession.Parts.Work
displayPart = theSession.Parts.Display


def get_all_bodies() -> List[NXOpen.Body]:
    all_bodies: List[NXOpen.Body] = []
    for item in workPart.Bodies:
        all_bodies.append(item)
    return all_bodies


def get_all_faces(body: NXOpen.Body) -> List[NXOpen.Face]:
    # all_faces: List[NXOpen.Face] = []
    # all_faces = body.GetFaces()
    return body.GetFaces()


def color_object(Displayable_object: NXOpen.DisplayableObject, color: int = 42) -> None:
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    displayModification1.ApplyToAllFaces = True
    displayModification1.ApplyToOwningParts = False
    displayModification1.NewColor = color
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    # body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    objects1[0] = Displayable_object
    displayModification1.Apply(objects1)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    displayModification1.Dispose()


def main() :
    all_bodies: List[NXOpen.Body] = get_all_bodies()

    for _, body in enumerate(all_bodies):
        all_faces: List[NXOpen.Face] = get_all_faces(body)
        for _, face in enumerate(all_faces):
            color_object(face, randint(1, 216))

    
if __name__ == '__main__':
    main()