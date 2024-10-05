import NXOpen
import NXOpen.Features

def main():
    # Initialize the session and work part
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work

    # Define cylinder parameters
    origin = NXOpen.Point3d(0.0, 0.0, 0.0)
    axis = NXOpen.Vector3d(0.0, 0.0, 1.0)
    radius = 5.0
    height = 10.0

    # Create a cylinder feature
    cylinderBuilder = workPart.Features.CreateCylinderBuilder(None)
    cylinderBuilder.Diameter.RightHandSide = str(2 * radius)
    cylinderBuilder.Height.RightHandSide = str(height)
    cylinderBuilder.SetOriginAndDirection(origin, axis)

    # Commit the feature to create the cylinder
    cylinderFeature = cylinderBuilder.CommitFeature()
    cylinderBuilder.Destroy()

if __name__ == '__main__':
    main()