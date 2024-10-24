# Hue Shift Image Processor

This script applies a hue shift to an image and saves the modified images with altered hues.

## Requirements
To run the script, you need the following Python packages:
- `Pillow`: For image processing
- `numpy`: For numerical computations

You can install these packages using `pip`:
```bash
python -m venv .venv

.\.venv\bin\activate # Linux
.\.venv\Scripts\Activate.ps1 # Windows

pip install -r requirments.txt
```

## Usage
The script is executed via the command line. The basic syntax is:
```bash
python hue_shift.py <image_path> <hue_shift> [-o <output_path>]
```

### Arguments
- ```image_path```: (Required) The path to the input image to be processed.
- ```hue_shift```: (Required) The value of the hue shift in degrees (0 to 360). If no value is provided, default values will be used.
- ```-o```, ```--output_path```: (Optional) The path to the output image or folder. If no output path is specified, the image will be saved with default names.

## Example
To apply a hue shift of 100 degrees to an image named ```input_image.png``` and save the result as ```output_image.png```, run the following command:
``` bash
python hue_shift.py input_image.png 100 -o output_image.png
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

> Feel free to copy and modify as needed!
