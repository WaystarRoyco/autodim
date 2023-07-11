# autodim

A Python utility for Linux media PCs that adjusts screen brightness and color temperature using a camera.

## Dependencies

- Python 3
- OpenCV
- NumPy
- Redshift

## Installation

```sudo apt update```

```sudo apt install python3 python3-opencv python3-numpy redshift```


To run the script:

```chmod +x autodim.py```

```./autodim.py```

## Configuration

Camera position:

For ideal ambient light capture an external usb camera facing behind or above the veiwing screen(s). This has the added benfit of reducing privacy concerns with activating the camera

You can change the following parameters in the script:

- camera_index: The index of the webcam device (0 for default)
- redshift_command: The template for the redshift command (see [redshift documentation](https://github.com/jonls/redshift/blob/master/README.md) for more options)
- brightness_min: The minimum brightness value for redshift (0.1 to 1)
- brightness_max: The maximum brightness value for redshift (0.1 to 1)
- brightness_threshold: The threshold for ambient light detection (0 to 255)
- time_interval: The time interval for checking ambient light (in seconds)
