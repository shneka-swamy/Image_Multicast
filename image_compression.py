import cv2
import base64
import io
from PIL import Image
import numpy as np


def save(path, image, jpg_quality=None, png_compression=None):
    if jpg_quality:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
    elif png_compression:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
    else:
        cv2.imwrite(path, image)


def main():
    # img_path = "png_compression.png"
    img_path = "sample_image.jpg"
    image = cv2.imread(img_path)
    #cv2.imshow('Original Image', image)

    # Convert the image to a string
    with open("sample_image.jpg", "rb") as img:
        b64string = base64.b64encode(img.read())
        print(len(b64string))

    # Save the image with lesser quality
    out_jpeg = "Modified_jpeg.jpg"
    save(out_jpeg, image, jpg_quality=10)
    img_jpeg = cv2.imread(out_jpeg)

    with open("Modified_jpeg.jpg", "rb") as img:
        b64string = base64.b64encode(img.read())
        print(b64string)

    # Convert back to the required image
    b64_string = b64string.decode()
    img = Image.open(io.BytesIO(base64.b64decode(b64_string)))
    cv2_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imwrite("reconstructed.jpg", cv2_img)
    cv2.imshow('Reconstructed Image', cv2.imread("reconstructed.jpg"))


    # Save the image with more compression
    out_png = "Modified_png.png"
    save(out_png, image, png_compression=9)
    img_png = cv2.imread(out_png)

    with open("Modified_png.png", "rb") as img:
        b64string = base64.b64encode(img.read())
        print(len(b64string))

    cv2.waitKey(0)
    cv2.destroyWindow('Original Image')


if __name__ == '__main__':
    main()
