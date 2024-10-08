# intellisense by theScriptingEngineer (www.theScriptingEngineer.com)
# Created by theScriptingEngineer
import math
import NXOpen


theSession  = NXOpen.Session.GetSession()
workPart = theSession.Parts.Work
displayPart = theSession.Parts.Display


def create_string_attribute(nx_object: NXOpen.NXObject, title: str, value: str) -> None:
    objects1 = [NXOpen.NXObject.Null] * 1 
    objects1[0] = nx_object
    attribute_manager: NXOpen.AttributeManager = theSession.AttributeManager
    attributePropertiesBuilder1 = attribute_manager.CreateAttributePropertiesBuilder(workPart, objects1, NXOpen.AttributePropertiesBuilder.OperationType.NotSet) # type: ignore
    
    attributePropertiesBuilder1.IsArray = False
    
    attributePropertiesBuilder1.DataType = NXOpen.AttributePropertiesBaseBuilder.DataTypeOptions.String
    
    attributePropertiesBuilder1.Title = title
    
    attributePropertiesBuilder1.StringValue = value
    
    nXObject1 = attributePropertiesBuilder1.Commit()
    
    id1 = theSession.GetNewestUndoMark(NXOpen.Session.MarkVisibility.Visible)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(id1)
    
    attributePropertiesBuilder1.Destroy()    


def main():
    # Method-1: Using the builder
    for item in workPart.Bodies: # type: ignore
        create_string_attribute(item, "Test", "HelloAgain") # Body (workPart), Attribute title (name), Attribute value 
    

    # Method-2: Seting directly (Instead of using the builder)
    for item in workPart.Bodies: # type: ignore
        item.SetUserAttribute('my_attribute_direct', -1, 'my_value', NXOpen.Update.Option.Now)

    
if __name__ == '__main__':
    main()
