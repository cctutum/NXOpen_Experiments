﻿# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Created by theScriptingEngineer
#
import NXOpen
from typing import List

def main() : 
    theSession  = NXOpen.Session.GetSession()
    workPart: NXOpen.Part = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    all_bodies: List[NXOpen.Body] = []
    for item in workPart.Bodies:
        all_bodies.append(item)

    for body in all_bodies:
        displayModification1 = theSession.DisplayManager.NewDisplayModification()
        displayModification1.ApplyToAllFaces = True
        displayModification1.ApplyToOwningParts = False
        displayModification1.NewColor = 42
        
        objects1 = [NXOpen.DisplayableObject.Null] * 1 
        # body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
        objects1[0] = body
        displayModification1.Apply(objects1)
        
        markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
        nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
        
        displayModification1.Dispose()
    
if __name__ == '__main__':
    main()