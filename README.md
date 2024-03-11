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

## Haar Cascade Method

* A form of features-based machine learning
* Uses pretrain images of labeled positives and negatives
* Runs through thousands of classifires in a cascaded manner
* Used case : Detect faces in the image and draw bounding boxes.

# Process of cascading
![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/f8870626-39b6-4db6-a9dc-564eacb5ffd7) <br><br>

![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/c90ff463-987a-4ffd-90f3-9f9daf89d409) <br><br>

## QR reading algorithm

![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/6ee741d9-9d6d-4495-ad82-f1456cb7a3f2)

## QR code Generator

![image](https://github.com/778569/Open-CV-Part03-Face-and-Feature-Detection/assets/52319671/c69bdae4-4783-43ab-b1f0-d690d6f58900)




