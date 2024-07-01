import smartcrop.Generator as Generator


img_output = "images\output\output.jpg"
img_input = "images\input\image5.png"
img_width = 600
img_height = 1300
Generator.smart_crop(img_input, img_width, img_height, img_output, None)