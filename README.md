# autodim

A Python utility that automatically adjusts screen brightness and color temperature based on the ambient light detected by a webcam.

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
```./autodimv0.1.py```

## Configuration

You can change the following parameters in the script:

- camera_index: The index of the webcam device (0 for default)
- redshift_command: The template for the redshift command (see [redshift documentation](https://github.com/jonls/redshift/blob/master/README.md) for more options)
- brightness_min: The minimum brightness value for redshift (0.1 to 1)
- brightness_max: The maximum brightness value for redshift (0.1 to 1)
- brightness_threshold: The threshold for ambient light detection (0 to 255)
- time_interval: The time interval for checking ambient light (in seconds)
