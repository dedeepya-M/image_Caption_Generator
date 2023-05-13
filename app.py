# importing required libraries
import streamlit as st # using streamlit to make a simple interactive web application
from PIL import Image # useing PILLOW for opening images
#  importing necessary HuggingFace libraries      
from transformers import ViTFeatureExtractor, AutoTokenizer, VisionEncoderDecoderModel
# using ViTFeatureExtractor for extracting image features from an image .
# using AutoTokenizer for for loading a tokenizer class from the transformers library based 
# on the model name or model path provided.
# using VisionEncoderDecoderModel for raining, fine-tuning and generating predictions from 
# an encoder-decoder architecture, which can be used for image captioning or text-to-image generation.
import torch # used as a deep learning framework to execute the computations for the ViT-GPT2-COCO-EN model

# refers to a pre-trained model that combines the ViT (Vision Transformer) 
# and GPT-2 (Generative Pre-trained Transformer 2) architectures 
loc = "ydshieh/vit-gpt2-coco-en" 

# load the pre-trained feature extractor, tokenizer, and model 
# from the specified location
feature_extractor = ViTFeatureExtractor.from_pretrained(loc)
tokenizer = AutoTokenizer.from_pretrained(loc)
model = VisionEncoderDecoderModel.from_pretrained(loc)
model.eval()

# prediction function 
def predict(image, num_captions=10):
    # extract features from the input image using the pre-trained feature extractor
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    # generate captions using the pre-trained model
    with torch.no_grad():
        output_ids = model.generate(pixel_values, 
                                     max_length=16, 
                                     num_beams=10, 
                                     num_return_sequences=num_captions, 
                                     return_dict_in_generate=True).sequences
    # decode the predicted output IDs into text using the pre-trained tokenizer    
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds

# streamlit application 
def main():
    # title of streamlit application
    st.title("Image Caption Generator")
    st.write("Upload an image and generate captions!") # prpmpt 
    # upload image of required types only
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"]) 

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # display uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Generate Captions'):
            # initiate prediction function 
            captions = predict(image, num_captions=10)
            # display captions
            st.write("Predicted Captions:")
            for caption in captions:
                st.write("- " + caption)

# starting point of execution
if __name__ == "__main__":
    main()
