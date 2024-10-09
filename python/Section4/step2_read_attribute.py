# Simcenter 3D 2306
# Journal created by Frederik on Thu Jan 11 15:35:26 2024 W. Europe Standard Time
#
import math
import NXOpen


theSession  = NXOpen.Session.GetSession()
the_lw: NXOpen.ListingWindow = theSession.ListingWindow
workPart = theSession.Parts.Work
displayPart = theSession.Parts.Display


def main():
    the_lw.Open()
    for item in workPart.Bodies: # type: ignore
        the_lw.WriteFullline(item.JournalIdentifier + ':')
        value: str = item.GetStringAttribute('my_attribute')
        the_lw.WriteFullline('\t' + value)
        my_attribute_information: NXOpen.NXObject.NXObjectAttributeInformation = item.GetUserAttribute('my_attribute', NXOpen.NXObject.AttributeType.String, -1)
        the_lw.WriteFullline('\t' + my_attribute_information.StringValue)

        for attr in item.GetUserAttributes(): # GetUserAttributes returns a so called iterable, this is why we can loop using this syntax
            # attr is of type NXOpen.NXObject.NXObjectAttributeInformation
            the_lw.WriteFullline('These are all properities of ' + attr.Title + ': ')
            the_lw.WriteFullline(str(attr))

    
if __name__ == '__main__':
    main()
