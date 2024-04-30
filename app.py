import streamlit as st
from PIL import Image
import numpy as np
import cv2
from ultralytics import YOLO  # Assuming ultralytics is installed

# Install Plotly if not already installed
import plotly.graph_objects as go

st.set_page_config(
    page_title="Berries Classifier",
    page_icon="🍓",
    layout="wide"
)

modelpath = r"best.pt"


@st.cache_resource()
def load_model(modelpath):
    """Loads the YOLO model from the specified path."""
    return YOLO(modelpath)


def display_results(predictions):
    """Displays the uploaded image and prediction details."""
      # Stretch image to fill column

    if predictions is not None:

        # Get class names and probabilities
        class_names = {0: 'Blackberry', 1: 'Blueberry', 2: 'Raspberry', 3: 'Seaberry', 4: 'Strawberry'}
        probs = predictions[0].probs.data.numpy()

        # Create the horizontal bar chart with Plotly
        data = [go.Bar(
            x=probs,
            y=[f"{class_names[i]}" for i in range(len(class_names))],
            orientation='h',
            marker=dict(color='royalblue'),
        )]

        layout = go.Layout(
            xaxis=dict(title=''),
            yaxis=dict(title=''),
            margin=dict(t=20, l=10, r=10, b=10),
        )

        fig = go.Figure(data=data, layout=layout)

        fig.update_layout(width=400, height=300)
        st.plotly_chart(fig)

        prediction = np.argmax(predictions[0].probs.data.numpy())



st.title("🍓Berries Classifier")

image_file = st.file_uploader('Upload image', type=['png', 'jpg', 'jpeg', 'gif'])

col1, col2 = st.columns(2)

with col1: 
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image=image, use_column_width=True)

with col2:
    if image_file is not None:
        # Load the model using caching
        model = load_model(modelpath)

        # Perform prediction and handle potential errors
        try:
            result = model(image)
            predictions = result if result is not None else None
            display_results(predictions)

        except Exception as e:
            st.error(f"An error occurred: {e}")


def funnyquote(predictions):
  prediction = np.argmax(predictions[0].probs.data.numpy())
  if prediction == 0:
    st.success("Looks like a raccoon's midnight snack! It's a blackberry ")
  elif prediction == 1:
    st.success("This berry's so blue, even the raccoon's feeling it! It's a blueberry ")
  elif prediction == 2:
    st.success("A berry fit for a raccoon feast! It's a raspberry ")
  elif prediction == 3:
    st.success("A berry from the raccoon's secret stash! It's a sea berry ")
  elif prediction == 4:
    st.success("Raccoon-approved sweetness! It's a strawberry ")
  else:
    st.error("Lenny doesn't classify it")


if image_file is not None:
        # Load the model using caching
        model = load_model(modelpath)

        # Perform prediction and handle potential errors
        try:
            result = model(image)
            predictions = result if result is not None else None
            funnyquote(predictions)

        except Exception as e:
            st.error(f"An error occurred: {e}")