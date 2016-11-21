# Physical-distance-between-Objects
Thr objects are assumed to be chess piece
The two primary parts of the code are 
Detecting the chess piece which has the most lines of code.
Measuring the distance between chess piece.


Detecting chess piece
“cv2.cvtColor(image, cv2.COLOR_BGR2HSV)” -Image converted to HSV color model 
“Gra[:,:,2]” - Converted to black and white. The 2 signifies black and white.
“v2.GaussianBlur(gray, (7,7), 0)” - Blur the image in order to better detect image.
“cv2.inRange(gray, 0, 70)” Select black pixels denoted by range from 0 to 70. This is the background of chess piece. The chess piece is in white color.
The gaps in the background need to be filled. This is done by repeating dilation and erosion. In Dilation, the value of the output pixel is the maximum value of all the pixels in the input pixel's neighborhood. In a binary image, if any of the pixels is set to the value 1, the output pixel is set to 1. In Erosion, the value of the output pixel is the minimum value of all the pixels in the input pixel's neighborhood. In a binary image, if any of the pixels is set to 0, the output pixel is set to 0.
“np.where(edged>50)”-Select the chess piece by selecting all white pixels




Measuring distance between Chess piece.
 In the variable ‘ff’ all pixels of the detected chess piece are stored.
 The average of all pixels of chess piece is found by using the mean function to find the centre of the chess piece
 The distance is found by using Euclidian distance formula. 
               dist((x, y), (a, b)) = Squareroot((x - a)² + (y - b)²)
            Where x,y are x and y coordinates of centre of first chess piece. Similarly a,b are x and y coordinates of centre of second chess piece.




Executing the file
In the first line of newCalibrate file , you will need to set the distance between chess pieces of two images. This is needed to calibrate the camera each time camera position is changed
When you calibrate , new file called donotdelete.txt will be generated.
Then run calculate file. The distance will be shown :)
