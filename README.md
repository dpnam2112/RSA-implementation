# My Awesome Project

a RSA implementation for the assignment of Cryptography and Cybersecurity course at Ho Chi Minh City
University of technology - semester 241.


## Table of Contents

- [Installation](#installation)
- [Activating the Environment](#activating-the-environment)
- [Installing Packages](#installing-packages)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, you'll need to have Poetry installed. Follow the steps below:

### Install Poetry

You can install Poetry globally using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Alternatively, if you prefer to use `pip`, you can install it via:

```bash
pip install poetry
```

### Verify Installation

After installation, verify that Poetry is installed correctly by checking the version:

```bash
poetry --version
```

## Activating the Environment

Once you have installed Poetry, navigate to your project directory:

```bash
cd path/to/your/project
```

Then run:

```bash
poetry shell
```

This command activates the virtual environment that Poetry manages for your project. You will see the environment name in your terminal prompt, indicating that you are now working within the project's virtual environment.

## Installing Packages

To install packages for your project, use the following command:

```bash
poetry add requests
```

Replace `requests` with the name of the package you wish to install. This command will update your `pyproject.toml` file and install the package in your virtual environment.

### Installing Development Dependencies

If you need to install packages that are only required for development (like testing frameworks), you can add them as follows:

```bash
poetry add --dev pytest
```

### Installing from `pyproject.toml`

If you have a `pyproject.toml` file that specifies your dependencies, you can install all the required packages with:

```bash
poetry install
```

This will set up your environment according to the specifications in `pyproject.toml`.

## Usage

To run the application, make sure your virtual environment is activated. Then execute:

```bash
python main.py
```

Replace `main.py` with the entry point of your application. You can add specific command line arguments or configurations here based on your project needs.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Instructions for Use
- Replace the project name, description, and usage instructions with specifics about your project.
- Adjust any commands or package names based on what your project requires.
- If applicable, include any additional sections that may be relevant to your project, such as testing instructions or configuration settings.
