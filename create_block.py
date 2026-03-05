import #########
import ######
from ######## import ######
#The project is being explored for further development, hence the code has been hashed. however, if interested please reachout.

##########################

# Get dimensions from command-line (mm to meters)
length = float(sys.argv[1]) / 1000
width = float(sys.argv[2]) / 1000
height = float(sys.argv[3]) / 1000

# Start SolidWorks
######## = ###########################
###################### = ########

# Template path (update if needed)
template = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2025\templates\Part.prtdot"

# Open new part with dummy vars for errors/warnings
errors = ############################# | ################, 0)
warnings = ######################## | #################, 0)

part = ###############(template, 1, 0, "", errors, warnings)

if part is None:
    raise Exception("Failed to create new part.")

# Select Top Plane
callout = #######################
selected = part.##########################("Top Plane", "PLANE", 0, 0, 0, False, 0, callout, 0)
if not selected:
    raise Exception("Failed to select Top Plane.")

# Start sketch
part.SketchManager.InsertSketch(True)

# Draw rectangle
part.#######################(0, 0, 0, length/2, width/2, 0)

# Exit sketch
part.ClearSelection2(True)
part.####################

# Extrude feature
####### = ########################(
    True, False, False, 0, 0,
    height, 0,
    False, False, False, False,
    0, 0, False, False,
    False, False, True, True, True, 0, 0, False
)

if feat is None:
    raise Exception("Extrusion failed.")

print("✅ Solid block created successfully.")
