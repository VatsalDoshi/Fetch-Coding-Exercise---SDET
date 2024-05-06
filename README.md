# Fake Gold Bar Finder

## Overview
This project automates the process of identifying a fake gold bar from a set of nine bars using a minimal number of weighings. It utilizes Selenium for browser automation to interact with a specified web page designed to simulate the weighing process.

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://your-repository-url.com
   ```

2. Navigate to the project directory:
   ```bash
   cd your_project_name
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Edit the `config/config.py` file to change the URL or any other settings related to WebDriver configurations.

## Running the Project
To run the main automation script, execute the following command from the project root directory:
```bash
python src/main.py
```

## Algorithm
The algorithm for finding the fake gold bar involves strategically weighing subsets of bars to minimize the total number of weighings needed. It uses a divide and conquer approach, testing groups of bars against each other to quickly isolate the lighter, fake bar.

## Testing
To execute the test cases, run the following command:
```bash
pytest tests/
```
This will invoke the tests defined in `tests/test_find_the_fake.py`, which ensure that the algorithm correctly identifies the fake bar under controlled conditions.

## Project Structure
```
your_project_name/
│
├── src/                     # Source code directory
│   ├── main.py              # Main script to run the automation
│   ├── helpers.py           # Helper functions for Selenium interactions
│   └── algorithm.py         # Logic to determine the fake gold bar
│
├── tests/                   # Test cases directory
│   └── test_find_the_fake.py# Test script for the algorithm and Selenium interactions
│
├── config/                  # Configuration files
│   └── config.py            # Configuration settings for the project
│
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Contributing
If you'd like to contribute to the project, please fork the repository and submit a pull request.

## Contact
For any additional questions or feedback, please contact me on 
doshi.va@northeastern.edu or on https://www.linkedin.com/in/vatsal-v-doshi/
