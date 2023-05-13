# image_Caption_Generator

This is a simple interactive web application built with Streamlit that generates captions for uploaded images. 
The model used is a pre-trained ViT-GPT2-COCO-EN architecture, which combines the ViT (Vision Transformer) and GPT-2 (Generative Pre-trained Transformer 2) architectures.

## Getting Started

To get started with the image caption generator, you will need to install the following dependencies:
- `torch`
- `streamlit`
- `transformers`
- `Pillow`

or install requirement as follows:
- `pip install -r requirements.txt`

## How to Use
1. Upload an image of type JPG, JPEG, or PNG.
2. Click on the "Generate Captions" button.
3. The model will generate up to 10 captions for the uploaded image.
4. The predicted captions will be displayed below the image.
## Model Details
The image caption generator is based on the ViT-GPT2-COCO-EN model from Hugging Face. 
This model is a combination of the Vision Transformer (ViT) and Generative Pre-trained Transformer 2 (GPT-2) architectures, and has been trained on the COCO dataset for image captioning.


