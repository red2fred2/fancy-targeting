import numpy as np

FILE_NAME                   = 'images/image0.jpg'   # image to read

OBJECT_MINIMUM_HSV = np.array( [50, 25, 25] )       # object color range min
OBJECT_MAXIMUM_HSV = np.array( [70, 255, 255] )     # object color range max

EROSION_SIZE                = 3                     # how much to erode away random blobs

SOFTENING                   = 9                     # how many pixel blur to soften

EDGE_THRESHOLD              = 100                   # ???
EDGE_RATIO                  = 2                     # ???

LINE_POSITION_RESOLUTION    = 2                     # how precise the position of pixels on a line must be
LINE_ANGLE_RESOLUTION       = np.pi / 90            # how precise the angle of the line must be
LINE_THRESHOLD              = 5                     # how many votes does this "line" need to be considered a line
LINE_MINIMUM_LENGTH         = 20                    # minimum length of what is considered a line
LINE_MAXIMUM_GAP            = 15                    # maximum space between parts of a line
MAX_LINES                   = 4                     # maximum number of lines to detect
LINE_DISTANCE_THRESHOLD     = 10                    # how far apart lines have to be to be considered unique
LINE_ANGLE_THRESHOLD        = np.pi/6

DISTANCE_FACTOR             = 113700                # some "magic" number turns number of pixels into distance
