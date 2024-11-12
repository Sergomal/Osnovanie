from PIL import Image
import stepic


def encode_text(image_path, text, output_path):
    image = Image.open(image_path)
    encoded_image = stepic.encode(image, text.encode())
    encoded_image.save(output_path)


encode_text(
    "D:\\My_Py\\to_encode.jpg",
    "QwErTy!@",
    "encoded.png",
)  # to_encode.jpg

print("The text is hidden in the image")


def decode_text(image_path):
    image = Image.open(image_path)
    decoded_text = stepic.decode(image)
    return decoded_text


secret_text = decode_text("encoded.png")
print(secret_text)
