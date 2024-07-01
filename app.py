# import streamlit as st
# import smartcrop.Generator as smartcrop
# import os
# from PIL import Image

# from sample1 import auto_optimal_smart_crop
# from sample2 import auto_optimal_smart_crop2

# # Set the directory containing images
# img_directory = "images/input"
# output_directory = "images/output"
# output_directory1 = "images/output1"
# output_directory2 = "images/output2"

# # Create the output directories if they don't exist
# for directory in [output_directory, output_directory1, output_directory2]:
#     if not os.path.exists(directory):
#         os.makedirs(directory)

# # List all image files in the directory
# img_files = [f for f in os.listdir(img_directory) if os.path.isfile(os.path.join(img_directory, f))]

# # Dictionary with file names and their dimensions
# image_dimensions = {
#     'image1.jpg': (1448, 869),
#     'image2.jpg': (528, 541),
#     'image3.png': (786, 800),
#     'image4.jpeg': (873, 1161),
#     'image5.png': (1092, 1079),
#     'image6.png': (1193, 1425),
#     'image7.jpg': (1502, 799),
#     'image8.jpg': (1192, 1152),
#     'image9.jpg': (1201, 1171),
#     'output.jpg': (1502, 799)
# }

# html_string = "<br><br><br><br>"

# # Function to perform smart cropping
# def perform_smart_crop(img_input, img_width, img_height, img_output):
#     try:
#         print("img_output: ", img_output)
#         smartcrop.smart_crop(img_input, img_width, img_height, img_output, None)
#         st.write(f"Cropped image saved to: {img_output}")
#     except Exception as e:
#         st.error(f"Error during cropping: {e}")
#         st.error(f"Image input: {img_input}, Image output: {img_output}")

# # Initialize session state
# if 'cropped_images' not in st.session_state:
#     st.session_state.cropped_images = {}
# if 'additional_images1' not in st.session_state:
#     st.session_state.additional_images1 = {}
# if 'additional_images2' not in st.session_state:
#     st.session_state.additional_images2 = {}

# # Layout the Streamlit page
# for img_file in img_files:
#     with st.container():
#         cols = st.columns(5)

#         with cols[0]:
#             # Display original image
#             img_input_path = os.path.join(img_directory, img_file)
#             st.image(img_input_path, use_column_width=True)

#         with cols[1]:
#             # Determine the output file path and ensure the extension is valid
#             img_name, img_ext = os.path.splitext(img_file)
#             valid_extensions = ['.jpg', '.jpeg', '.png']
#             if img_ext.lower() not in valid_extensions:
#                 st.warning(f"Unsupported file format: {img_ext}")
#                 continue
            
#             img_output_path = os.path.join(output_directory, f"output_{img_name}{img_ext}")
#             img_output_path1 = os.path.join(output_directory1, f"output_{img_name}{img_ext}")
#             img_output_path2 = os.path.join(output_directory2, f"output_{img_name}{img_ext}")

#             # Display cropped image if exists
#             if img_file in st.session_state.cropped_images:
#                 if os.path.exists(st.session_state.cropped_images[img_file]):
#                     st.image(st.session_state.cropped_images[img_file], use_column_width=True)
#                 else:
#                     st.warning(f"File {st.session_state.cropped_images[img_file]} not found.")

#         with cols[2]:
#             # Get dimensions from the dictionary
#             img_width, img_height = image_dimensions.get(img_file, (786, 800))

#             # User input for image width and height
#             img_width = st.number_input(f"Width for {img_file} (px)", min_value=1, value=img_width, key=f"width_{img_file}")
#             img_height = st.number_input(f"Height for {img_file} (px)", min_value=1, value=img_height, key=f"height_{img_file}")

#             # Button to trigger the smart crop
#             if st.button(f"Crop {img_file}", key=f"crop_{img_file}"):
#                 perform_smart_crop(img_input_path, img_width, img_height, img_output_path)
                
#                 # Store the cropped image path in session state
#                 st.session_state.cropped_images[img_file] = img_output_path

#                 # Apply additional functions and store results in session state
#                 auto_optimal_smart_crop(img_input_path, img_width, img_height, img_output_path1)
#                 auto_optimal_smart_crop2(img_input_path, img_width, img_height, img_output_path2)

#                 st.session_state.additional_images1[img_file] = img_output_path1
#                 st.session_state.additional_images2[img_file] = img_output_path2

#                 # Verify the cropped image is saved and display it
#                 if os.path.exists(img_output_path):
#                     st.image(img_output_path, use_column_width=True)
#                 st.rerun()
        
#         with cols[3]:
#             # Display additional processed image 1 if exists
#             if img_file in st.session_state.additional_images1:
#                 if os.path.exists(st.session_state.additional_images1[img_file]):
#                     st.image(st.session_state.additional_images1[img_file], use_column_width=True)
#                 else:
#                     st.warning(f"File {st.session_state.additional_images1[img_file]} not found.")

#         with cols[4]:
#             # Display additional processed image 2 if exists
#             if img_file in st.session_state.additional_images2:
#                 if os.path.exists(st.session_state.additional_images2[img_file]):
#                     st.image(st.session_state.additional_images2[img_file], use_column_width=True)
#                 else:
#                     st.warning(f"File {st.session_state.additional_images2[img_file]} not found.")

#     st.markdown(html_string, unsafe_allow_html=True)
import streamlit as st
import smartcrop.Generator as smartcrop
import os
from PIL import Image

from sample1 import auto_optimal_smart_crop
from sample2 import auto_optimal_smart_crop2

# Set the directory containing images
img_directory = "images/input"
output_directory = "images/output"
output_directory1 = "images/output1"
output_directory2 = "images/output2"

# Create the output directories if they don't exist
for directory in [output_directory, output_directory1, output_directory2]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# List all image files in the directory
img_files = [f for f in os.listdir(img_directory) if os.path.isfile(os.path.join(img_directory, f))]

html_string = "<br><br><br><br>"

# Function to perform smart cropping
def perform_smart_crop(img_input, img_width, img_height, img_output):
    try:
        print("img_output: ", img_output)
        smartcrop.smart_crop(img_input, img_width, img_height, img_output, None)
        st.write(f"Cropped image saved to: {img_output}")
    except Exception as e:
        st.error(f"Error during cropping: {e}")
        st.error(f"Image input: {img_input}, Image output: {img_output}")

# Initialize session state
if 'cropped_images' not in st.session_state:
    st.session_state.cropped_images = {}
if 'additional_images1' not in st.session_state:
    st.session_state.additional_images1 = {}
if 'additional_images2' not in st.session_state:
    st.session_state.additional_images2 = {}

# User input for image width and height
img_width = st.number_input(f"Width for all images (px)", min_value=1, value=786)
img_height = st.number_input(f"Height for all images (px)", min_value=1, value=800)

# Button to trigger the smart crop for all images
if st.button("Crop all images"):
    for img_file in img_files:
        img_input_path = os.path.join(img_directory, img_file)
        img_name, img_ext = os.path.splitext(img_file)
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if img_ext.lower() not in valid_extensions:
            st.warning(f"Unsupported file format: {img_ext}")
            continue

        img_output_path = os.path.join(output_directory, f"output_{img_name}{img_ext}")
        img_output_path1 = os.path.join(output_directory1, f"output_{img_name}{img_ext}")
        img_output_path2 = os.path.join(output_directory2, f"output_{img_name}{img_ext}")

        perform_smart_crop(img_input_path, img_width, img_height, img_output_path)

        # Store the cropped image path in session state
        st.session_state.cropped_images[img_file] = img_output_path

        # Apply additional functions and store results in session state
        auto_optimal_smart_crop(img_input_path, img_width, img_height, img_output_path1)
        auto_optimal_smart_crop2(img_input_path, img_width, img_height, img_output_path2)

        st.session_state.additional_images1[img_file] = img_output_path1
        st.session_state.additional_images2[img_file] = img_output_path2

        # Verify the cropped image is saved
        if not os.path.exists(img_output_path):
            st.error(f"File {img_output_path} not found.")
        if not os.path.exists(img_output_path1):
            st.error(f"File {img_output_path1} not found.")
        if not os.path.exists(img_output_path2):
            st.error(f"File {img_output_path2} not found.")
    st.rerun()

# Layout the Streamlit page
for img_file in img_files:
    with st.container():
        cols = st.columns(4)

        with cols[0]:
            # Display original image
            img_input_path = os.path.join(img_directory, img_file)
            st.image(img_input_path, use_column_width=True, caption=f"Original {img_file}")

        with cols[1]:
            # Display cropped image if exists
            if img_file in st.session_state.cropped_images:
                if os.path.exists(st.session_state.cropped_images[img_file]):
                    st.image(st.session_state.cropped_images[img_file], use_column_width=True, caption=f"Cropped {img_file}")
                else:
                    st.warning(f"File {st.session_state.cropped_images[img_file]} not found.")

        with cols[2]:
            # Display additional processed image 1 if exists
            if img_file in st.session_state.additional_images1:
                if os.path.exists(st.session_state.additional_images1[img_file]):
                    st.image(st.session_state.additional_images1[img_file], use_column_width=True, caption=f"Optimal Crop 1 {img_file}")
                else:
                    st.warning(f"File {st.session_state.additional_images1[img_file]} not found.")

        with cols[3]:
            # Display additional processed image 2 if exists
            if img_file in st.session_state.additional_images2:
                if os.path.exists(st.session_state.additional_images2[img_file]):
                    st.image(st.session_state.additional_images2[img_file], use_column_width=True, caption=f"Optimal Crop 2 {img_file}")
                else:
                    st.warning(f"File {st.session_state.additional_images2[img_file]} not found.")

    st.markdown(html_string, unsafe_allow_html=True)

