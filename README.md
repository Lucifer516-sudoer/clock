<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">CLOCK</h1>
</p>
<p align="center">
    <em>Timekeeping Evolved, Readability Ensured</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=default&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>

<br><!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#overview)
- [ Features](#features)
- [ Repository Structure](#repository-structure)
- [ Modules](#modules)
- [ Getting Started](#getting-started)
  - [ Installation](#installation)
  - [ Usage](#usage)
  - [ Tests](#tests)
- [ Project Roadmap](#project-roadmap)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)
</details>
<hr>

## Overview

Clock is an open-source timekeeping application written in Python, leveraging libraries like Arrow, Rich, Flet, and PyInstaller for precise timing and user-friendly interfaces. The project empowers efficient project management by offering customizable loggers for debugging purposes and providing a seamless development, installation, and deployment experience with tools such as Poetry and Python. The core functionality revolves around creating an intuitive graphical user interface for timekeeping, including theme switching, date-time updates, and about information display. The flexible logging solution ensures enhanced output readability and maintains compatibility with the standard Python logging module. Overall, Clock offers a robust, easy-to-use, and customizable timekeeping solution that caters to a wide range of user requirements.

---

## Features

| Feature          | Description                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ Architecture  | Uses `Python` as the programming language with dependency management via `Poetry`, `pyproject.toml`, and a structured project layout for easy deployment. |
| 🔩 Code Quality  | Consistent code style using `Rich` for output formatting and adheres to the conventions of `Arrow` library.                                               |
| 📄 Documentation | Well-documented with explanations in corresponding Python files for ease of understanding project functionality.                                          |
| 🔌 Integrations  | Leverages the open-source UI development library, `Flet`.                                                                                                 |
| 🧩 Modularity    | Modular architecture with distinct files for different functionalities like API implementation, logging, and user interface.                              |
| 🧪 Testing       | Not explicitly stated in the given codebase details.                                                                                                      |
| ⚡️ Performance   | Utilizes efficient libraries such as `Arrow` for date-time operations; scalability unknown at this time due to limited data.                              |
| 🛡️ Security     | Access controls managed by default Python permissions, but no specific encryption or authentication measures provided in codebase shown.                  |
| 📦 Dependencies  | Uses various dependencies such as `Python`, `pyproject.toml`, `Flet`, `Rich`, `Lock`, and external packages specified in the repository.                  |

---

## Repository Structure

```sh
└── clock/
    ├── README.md
    ├── clock
    │   ├── __init__.py
    │   ├── api.py
    │   ├── app
    │   └── logger
    ├── poetry.lock
    ├── pyproject.toml
    └── tests
        └── __init__.py
```

---

## Modules

<details closed><summary>pyproject.toml</summary>

| File                             | Summary                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pyproject.toml](pyproject.toml) | Empowers efficient project management by providing a well-structured architecture for clock, an open-source timekeeping application. This file, pyproject.toml, facilitates easy dependency management and builds with tools like Poetry, PyInstaller, Python, Arrow, Rich, and Flet. It sets the foundation for a seamless development and installation experience. |

</details>

<details closed><summary>clock</summary>

| File                   | Summary                                                                                                                                                                                          |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [api.py](clock/api.py) | This Python class provides logging facilities while utilizing the Arrow library for precise date-time handling. Enhances the Clock API architecture by enabling customizable timezone settings." |

</details>

<details closed><summary>clock.logger</summary>

| File                                                  | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [_custom_handler.py](clock/logger/_custom_handler.py) | Empower your log management within this clock repository by introducing customizable console and file logging with the RichLogger module. The module features RichConsoleHandler for formatted console logs and RichFileHandler to output rich-formatted entries into a specified file. This flexible logging solution enhances the readability of your app's output while maintaining compatibility with the standard Python logging module. |
| [logger.py](clock/logger/logger.py)                   | Includes customizable loggers for clock", flet, and flet_core.Implements `RichConsoleHandler` and `RichFileHandler` to enhance output readability.Provides a way to configure loggers, ensuring flexible handlers management.                                                                                                                                                                                                                 |

</details>

<details closed><summary>clock.app.gui</summary>

| File                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`__main__`.py](clock/app/gui/__main__.py) | The provided Python script `clock/app/gui/__main__.py` serves as the entrypoint for the graphical user interface (GUI) of our clock repository, automatically executing when `python-m clock.app.gui` is invoked. This script launches the applications main instance through `from clock.app.gui.main import run` and initiates its execution with the `run()` function call. Essentially, this file orchestrates the deployment of our apps visual components on the user's screen for easy timekeeping. |
| [main.py](clock/app/gui/main.py)           | Updates the date-time in the specified UserControl by setting it and refreshing the screen.Sets up loggers to enable debugging for the app and flet libraries.Creates a clock user interface with theme switching and about information display features.Builds and runs the Flet application using the provided main function, which displays the date-time.                                                                                                                                              |

</details>

---

## Getting Started

**System Requirements:**

- **Python**: `version 3.12.4` The version <italic>I used</italic> to develop this. 

### Installation

<h4>From <code>source</code></h4>

> 1. Clone the clock repository:
>  
> ```console
> git clone https://github.com/Lucifer516-sudoer/clock.git
> ```
>
> 2. Change to the project directory:
>
> ```console
> $ cd clock
> ```
>
> 3. Install the dependencies:
> - ### Using Poetry tool
> ```console
> poetry install
> ```
And yeah you need to [google](https://www.google.com) how to install poetry and stuffs.

### Usage

<h4>From <code>source</code></h4>

> Run clock using the command below:
>
> ```console
> python -m clock.app.gui  # runs the flet program
> ```

### Tests

> Run the test suite using the command below:
>
> ```console
> pytest
> ```
Nothing would happen now since, I haven't written any tests for this yet
---

## Project Roadmap

- [x] Create a skeletal boredom clock
- [ ] Add Stop watch functionality
- [ ] Add Timer Functionality
- [ ] Create a world clock (I guess)
- [ ] Modify the UI
- [ ] Think about the packaging and stuffs (Not even thinking about it now)

---

## Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Lucifer516-sudoer/clock/issues)**: Submit bugs found or log feature requests for the `clock` project.
<!-- - **[Submit Pull Requests](https://github.com/Lucifer516-sudoer/clock/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs. -->
- **[Join the Discussions](https://github.com/Lucifer516-sudoer/clock/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Lucifer516-sudoer/clock.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/Lucifer516-sudoer/clock/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=clock">
   </a>
</p>
</details>

---

## License

This project is protected under the **MIT License** License. For more details, refer to the [**LICENSE**](https://choosealicense.com/licenses/mit/#) file.

---

## Acknowledgments

- Have used, some stuffs from the internet, and those stuffs are creditted to the rightful owners
[**Return**](#overview)

---
