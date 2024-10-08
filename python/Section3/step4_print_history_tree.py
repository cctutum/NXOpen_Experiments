# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Created by theScriptingEngineer
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.Layer
from typing import List

theSession  = NXOpen.Session.GetSession()
the_lw: NXOpen.ListingWindow = theSession.ListingWindow
workPart = theSession.Parts.Work
displayPart = theSession.Parts.Display


def get_all_features() -> List[NXOpen.Features.Feature]:
    """
    Get all the features in the work part.

    Returns:
        List[NXOpen.Features.Feature]: A list of all the features in the work part.
    """
    all_features: List[NXOpen.Features.Feature] = []
    for item in workPart.Features:
        all_features.append(item)
    return all_features


def main() : 
    """
    Main function to print the history tree of features.

    Prints the journal identifier, name, and type of each feature in the work part,
    along with the journal identifier, name, and type of each child feature.
    """
    the_lw.Open()

    all_features: List[NXOpen.Features.Feature] = get_all_features()
    for i in range(len(all_features)):
        the_lw.WriteFullline(all_features[i].JournalIdentifier + " with name " + all_features[i].GetFeatureName() + " of type " + str(type(all_features[i])))
        all_children: List[NXOpen.Features.Feature] = all_features[i].GetChildren()
        for j in range(len(all_children)):
            the_lw.WriteFullline("\t" + all_children[j].JournalIdentifier + " with name " + all_children[j].GetFeatureName() + " of type " + str(type(all_children[j])))


if __name__ == '__main__':
    main()