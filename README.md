# Push-Up and Pull-Up Counter

## Description

The Push-Up and Pull-Up Counter is a computer vision application that uses a webcam to automatically detect and count push-up and pull-up repetitions in real-time. The program utilizes deep learning techniques, specifically object detection models, to identify human body poses and track movements for both push-ups and pull-ups.

## Table of Contents

Installation
Usage
Requirements
Configuration
Contributing
License

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/SAHITHV/push-up-pull-up-counter.git
```

2. Change into the project directory:

```bash
cd push-up-pull-up-counter
```

3. Install any required dependencies (if any) by running:

```bash
pip install -r requirements.txt
```

4. Download the pre-trained object detection model (e.g., YOLO, SSD) by following the instructions in the `models/README.md` file.

## Usage

To use the Push-Up and Pull-Up Counter, follow these steps:

1. Make sure you have Python and a compatible webcam connected to your machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `push_up_pull_up_counter.py` script:

```bash
python push_up_pull_up_counter.py
```

4. The webcam feed will appear with bounding boxes around detected human body poses, and a push-up and pull-up counter will be displayed on the screen.

5. Perform push-ups and pull-ups within the webcam's view, and the detector will track and count each repetition accordingly.

6. Press the `q` key to exit the program.

## Requirements

The Push-Up and Pull-Up Counter requires the following:

- Python (version >= 3.x)
- Webcam (built-in or external)

## Configuration

The Push-Up and Pull-Up Counter allows for some basic configuration options. These options can be modified in the `config.json` file. The available configurations are as follows:

- `push_up_threshold`: An integer representing the distance (in pixels) between the nose and the floor, used to determine a valid push-up repetition.
- `pull_up_threshold`: An integer representing the distance (in pixels) between the hands and the bar (or any suitable reference point), used to determine a valid pull-up repetition.
- `show_video`: A boolean indicating whether to display the webcam feed with bounding boxes and push-up/pull-up count.

## Contributing

Contributions to this project are welcome! If you find any bugs, have feature requests, or want to improve the code, feel free to open an issue or submit a pull request.

When contributing, please follow the existing coding style, and make sure to thoroughly test your changes.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as you see fit. See the [LICENSE](LICENSE) file for more details.

## Credits

The Push-Up and Pull-Up Counter was developed by SAHITH(https://github.com/SAHITHV). If you have any questions or need assistance, feel free to reach out to me. Happy counting!# push-up-pull-up-with-no-push-up-condition
