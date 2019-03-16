# Purpose: 😄

> |               Folder 📂               |               Description |
> | :-----------------------------------: | ------------------------: |
> | [Face Detection](<./Face detection/>) |     Face Detection folder |
> |      [TF-retrain](./TF-retrain/)      | Retrain google classifier |

    This is annoying to have multiple pictures from multiple camera, sorted all a different way.
    It would be simpler to sort photos by person, place, date, camera, landscape, portrait, etc ...
    Photos.app from  already does all of that but i wanted to use Machine Learning to try it myself with python.

![logo-Python](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

### First step:

##### Face Detection

On the web some tutorials are very poor and useless, however i found this one <https://realpython.com/face-recognition-with-python/#want-to-know-more>.

Thank you - `Shantnu Tiwari` - ❤️

This one is very clear, short and well-written.
The programme use the famous open librarie OpenCV.
<img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" alt="logo-OpenCV" width="240" height="180" />

OpenCV uses machine learning algorithms to search for faces within a picture. OpenCV use cascade classification and more precisely Haar Feature-based Cascade Classifier for Object Detection.
Therefore the Classifier is train with tons of data and pretty quickly, resulting in a XML file.
Since face detection is such a common case, OpenCV comes with a number of built-in cascades for detecting everything from faces to eyes to hands to legs.

You can use the first programme as follow:

```python
python3 face_detect.py myPhoto.png haarcascade_frontalface_default.xml
```

The result are good with a high detection rate. However time to time, i will or will not detect face. To get around this problem, you can adjust the _scaleFactor_ parameter.

This face detection option is native in numerous of devices as camera, computer, phone, etc...
My next goal is to detect and **recognise**.

### Second step

##### Recognise

<https://www.tensorflow.org/hub/tutorials/image_retraining>

Tensorflow is an open source machine learning framework developped by Google. The one resource, i will use is _How to Retrain an Image Classifier for New Categories_ in the TF Hub section.

First of:

```python
pip install tensorflow-hub
```

Then the you need some photos of whatever you need to be recognise. In my case, i chose Harry Potter, Hermione, Ron from the Harry Potter saga. To download all pictures (~100 per personages), i used a script named [googleimagesdownload](https://github.com/hardikvasa/google-images-download). This was the best way i found to get photos, api for Bing or Google was to laborious for this simple purpose.

Once you have all pictures, make sure to order the different folder correctly.

ex: ~/downloaded
      \|
      |-Harrypotter ~100
      |-Hermione    ~100
      |-Ron         ~100

Some pictures downloaded was awful so sort out bad picture or unrelated photos.

    curl -LO https://github.com/tensorflow/hub/raw/master/examples/image_retraining/retrain.py

Or you can find the script in the TF-retrain/retrain.py

Run **python retrain.py -h** for all options.

However in a simple way you can run: ~20 minutes

    python retrain.py --image_dir ~/downloaded

The script will write out the new model trained on your categories to /tmp/output_graph.pb, and a text file containing the labels to /tmp/output_labels.txt

Now the model is train to recognise and sort a picture between the 3 folders (or numbers of folder you have).

We need to tell the classifier to use our model:

    curl -LO https://github.com/tensorflow/tensorflow/raw/master/tensorflow/examples/label_image/label_image.py
    python label_image.py \
    --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt \
    --input_layer=Placeholder \
    --output_layer=final_result \
    --image=IMAGE_TO_SORT

For some details, refer to this video from channel "google developers": <https://www.youtube.com/watch?v=cSKfRcEDGUs>

I do recommand you to read this article [coding-robin.de/train-your-own-opencv-haar-classifier](https://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html) which use a different approach.
