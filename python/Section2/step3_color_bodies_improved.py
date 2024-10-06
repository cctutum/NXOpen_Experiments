# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Created by theScriptingEngineer
#
import NXOpen
from typing import List


theSession  = NXOpen.Session.GetSession()
workPart: NXOpen.Part = theSession.Parts.Work
displayPart = theSession.Parts.Display


def get_all_bodies() -> List[NXOpen.Body]:
    all_bodies: List[NXOpen.Body] = []
    for item in workPart.Bodies:
        all_bodies.append(item)
    return all_bodies


def color_body(body: NXOpen.Body, color: int = 42) -> None:
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    displayModification1.ApplyToAllFaces = True
    displayModification1.ApplyToOwningParts = False
    displayModification1.NewColor = color
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    # body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    objects1[0] = body
    displayModification1.Apply(objects1)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    displayModification1.Dispose()


def main() :
    all_bodies: List[NXOpen.Body] = get_all_bodies()

    for index, body in enumerate(all_bodies):
        color_body(body, (index * 10) % 216 + 1)

    
if __name__ == '__main__':
    main()