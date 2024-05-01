# 🍓[Berry Whisperer L1](https://berries-classifier.streamlit.app/): Berries Classifier

This little gem (pun intended) is a web app that helps you identify your mystery berries using the power of image classification!

## What can it do?

- Upload a picture of your berry.
- Image classifier will analyze the image and tell you the kind of berry it is (hopefully with 99% accuracy, but hey, even squirrels mess up sometimes).
- Get a fun fact about your berry, courtesy of Lenny the raccoon (our resident quality assurance tester... with a questionable sweet tooth).

## How to use it:

1.  Click "Upload image" and choose a picture of your berry. Make sure it's a clear shot for best results (blurry berries are hard to identify, even for AIs).
2.  Sit back, relax, and watch the magic happen! The berry whisperer will show you the image and tell you its berry destiny (or inform you if it's having an existential crisis and can't decide).

## Things to keep in mind:

- This berry whisperer can only classify blackberries, blueberries, raspberries, seaberries, and strawberries. If you have something more exotic, you might need to consult a real (human) expert.
- Errors happen (even to AIs). If something goes wrong, you'll see an error message. Don't worry, it's not your fault (probably).

**We hope you enjoy using the Berry Whisperer L1! If you have any questions or feedback, feel free to send a carrier pigeon our way**



https://github.com/lennytheracoon/Berries-classifier/assets/166391256/08e7df79-6cce-4a1d-9090-bd31e42ba0ea



## Installation:

This web app is built using Python libraries. To run it locally, you'll need to have the following installed:

- Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- Streamlit ([https://streamlit.io/](https://streamlit.io/))
- Pillow (fork of PIL) ([https://pillow.readthedocs.io/](https://pillow.readthedocs.io/))
- NumPy ([https://numpy.org/](https://numpy.org/))
- OpenCV (optional) ([https://opencv.org/](https://opencv.org/))
- Ultralytics for YOLO ([https://www.ultralytics.com/](https://www.ultralytics.com/))
- Plotly ([https://plotly.com/python/](https://plotly.com/python/))

**Install requirements**

```Python
pip install -r requirements.txt
```

**Once you have the libraries installed, you can run the app using the following command:**

```Python
streamlit run app.py
```

Use code [with caution.](/faq#coding)

**Make sure you have a pre-trained YOLO model file (e.g., `best.pt`) trained on a dataset of berry images.** You'll need to update the `modelpath` variable in the code to point to the location of your model file.

## Acknowledgments

We'd like to express our gratitude to the following for their contributions to this project:

- **Ultralytics for YOLO ([https://www.ultralytics.com/](https://www.ultralytics.com/))**: Their open-source framework provided the foundation for our image classification model.
- **Roboflow ([https://roboflow.com/](https://roboflow.com/))**: This platform be helpful for training a custom YOLO model on a dataset of berry images.

## License:
The source code for this web app is distributed under an open-source license (to be determined).
