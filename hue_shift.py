import argparse
from PIL import Image
import numpy as np
import colorsys
import os

def apply_hue_shift(image_path, hue_shift, output_path):
    img = Image.open(image_path).convert("RGBA")
    img_np = np.array(img)
    rgb_img, alpha_channel = img_np[..., :3], img_np[..., 3]

    hsv_img = np.apply_along_axis(lambda rgb: colorsys.rgb_to_hsv(*(rgb / 255.0)), -1, rgb_img)
    hsv_img[..., 0] = (hsv_img[..., 0] + hue_shift / 360.0) % 1.0
    new_rgb_img = np.apply_along_axis(lambda hsv: np.array(colorsys.hsv_to_rgb(*hsv)) * 255, -1, hsv_img).astype(np.uint8)

    Image.fromarray(np.dstack((new_rgb_img, alpha_channel)), "RGBA").save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Applies a hue shift to an image.")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("hue_shift", type=float, help="Value of the hue shift in degrees (0 to 360)")
    parser.add_argument("-o", "--output_path", dest="output_path", help="Optional: Path to the output image")

    args = parser.parse_args()
        
    base_name, ext = os.path.splitext(args.image_path)
    output_file = args.output_path or f"{base_name}_{args.hue_shift}{ext}"
    
    apply_hue_shift(args.image_path, args.hue_shift, output_file)
    print(f"Hue-Shift von {args.hue_shift} angewendet: {output_file}")

if __name__ == "__main__":
    main()
