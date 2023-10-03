# Project README

## Python3 Development Environment Setup

This project is developed using Python3 and managed with Miniconda. Follow the steps below to set up the development environment:

### 1. Clone the Repository

```bash
git clone [repository_url]
cd [repository_directory]
```

Make sure to replace [repository_url] and [repository_directory] with your actual repository URL and directory.

### 2. Create and Activate Conda Environment
```Miniconda prompt
conda create --name your_environment_name python=input_python_version
conda activate your_environment_name
```
### 3. Install Dependencies

The dependencies for this project include:

**Miniconda**: Download and install Miniconda.

**openpyxl**: A library for reading and writing Excel files.

**scikit-learn**: A machine learning library for data processing, modeling, and evaluation.

**pandas**: A powerful data manipulation and analysis library.
```Miniconda Prompt
conda install package_name
```
### 4. Project Structure
The project follows the structure commonly used in PyCharm and Visual Studio Code for Python projects. Below are key components:

- **main.py**: Main script for processing the MASSIVE Dataset and generating language-specific Excel files.
- **functions.py**: Module containing functions for creating Excel files.
- **generator.sh**: Shell script for running the Python script with specified input and output paths.
### 5. Running the Project
- Place the MASSIVE Dataset JSONL files in the specified input_jsonl_dir directory.
- Run the generator.sh script:
```bash
./generator.sh
```
This command executes the python scripts.



