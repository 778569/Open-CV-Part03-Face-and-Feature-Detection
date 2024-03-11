# Open-CV-Part03-Face-and-Feature-Detection
Detect faces and features with precision using OpenCV in this GitHub repository. Implement robust algorithms for facial recognition, eye detection, and more, with comprehensive documentation and easy-to-follow examples for seamless integration into projects.


## Qualites of features 

* Features are qualities of an object
* Salient attribute or components of an object within an image scence
* ideally invariant to transformations
* May be identified by classifiers<br><br>

![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/bdfc3189-3d36-4901-992c-0e0c0efa4e82)

## Detection vs Recognition

Detection is often a step prior ti recognition
Example - The image at the right detects faces .A postdetection process might be to try and recognize a face matching a database of classifiers.
in this case features such as distance between eyes in an image, may be use both for the detection process to see whether or not a face actually exists, but also used as a classifire for the recognition process to see which face is specifically matchs with.

in here there will two algorithms 
1. Template maching for general object recognition
2. Haar cascading as mean for face detection

## Template matching 

* Search a smimiler pattern between two images<br><br>
![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/30a607eb-257d-4c42-859e-98208db0217f)<br><br>

* taking a referance image call tempate and sliding it around the other comparison image taking difference every position.
* result - black and whie gray scale image with varying intensities showing how well match each position.

# Template matching : 2D Example

![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/1f000964-7506-4ff2-bb38-be7498f701d9) <br><br>
![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/ba33457c-9fc9-4edb-9599-8ef053e6abe3)<br><br>


# Limitations

![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/be2e1167-cb3c-412b-8465-0c96b86a3e82) <br><br>
