import cv2
import math
import numpy as np
from settings import *

def pixelArea(image):
    return np.sum( image ) / 255

def approxDistance(image):
    return DISTANCE_FACTOR / pixelArea( image )

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt( abs( x1 - x2 )**2 + abs( y1 - y2 )**2 )

def lines(edges, original):
    #find lines
    lines = cv2.HoughLinesP( edges, LINE_POSITION_RESOLUTION, LINE_ANGLE_RESOLUTION, LINE_THRESHOLD, minLineLength = LINE_MINIMUM_LENGTH, maxLineGap = LINE_MAXIMUM_GAP )

    #draw lines
    number = 1
    for line in lines:
        x1, y1, x2, y2 = line[0]

        angle = math.atan2( abs( x1 - x2 ), abs( y1 - y2 ) )

        #check if the lines are similar to each other
        isSimilar = False
        for i in range(number):
            x1_2, y1_2, x2_2, y2_2 = lines[i][0]

            angle_2 = math.atan2( abs( x1_2 - x2_2 ), abs( y1_2 - y2_2 ) )

            print('a1:', angle, 'a2:', angle_2)

            print('diff:', abs( angle - angle_2 ), 'vs', LINE_ANGLE_THRESHOLD)

            if abs( angle - angle_2 ) < LINE_ANGLE_THRESHOLD:
                print('bad angle')
                if distance( (x1, y1), (x1_2, y1_2) ) or distance( (x2, y2), (x2_2, y2_2) ):
                    print('and too close')
                    #isSimilar = True

        #if the lines are not similar, proceed
        if not isSimilar:
            cv2.line( original, (x1, y1), (x2, y2), (255, 0, 0), 2 )
            print( number, ': (', x1, ',', y1, ') -> (', x2, ',', y2, ')' )
            number += 1

def main():
    #read image
    original = cv2.imread( FILE_NAME )

    #convert colors to HSV
    converted = cv2.cvtColor( original, cv2.COLOR_BGR2HSV )

    #detect object
    object = cv2.inRange( converted, OBJECT_MINIMUM_HSV, OBJECT_MAXIMUM_HSV )

    print('Pixel area:', pixelArea( object ))
    print('Approx distance:', approxDistance( object ))

    #erode away random blobs
    eroded = cv2.erode( object, cv2.getStructuringElement( cv2.MORPH_RECT, (EROSION_SIZE, EROSION_SIZE) ) )

    #soften
    softened = cv2.blur( eroded, (SOFTENING, SOFTENING) )

    #get all non black
    expanded = cv2.inRange( softened, np.array( [5] ), np.array( [255] ) )

    #get edges
    edges = cv2.Canny( expanded, EDGE_THRESHOLD, EDGE_THRESHOLD * EDGE_RATIO )

    #detect lines
    lines( edges, original )

    #show images
    cv2.imshow( 'original', original )
    cv2.imshow( 'object', object )
    cv2.imshow( 'eroded', eroded )
    cv2.imshow( 'softened', softened )
    cv2.imshow( 'expanded', expanded )
    cv2.imshow( 'edges', edges )

    #wait to close
    cv2.waitKey()

main()