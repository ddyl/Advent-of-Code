# Advent of Code Solutions

This project contains my attempts at solving the [Advent of Code Challenges](https://adventofcode.com/). Currently, only solutions for 2022 puzzles are in this project.

Since I was playing around with [click](https://click.palletsprojects.com/en/8.1.x/) at the time I thought I'd try to build a CLI to run any Advent of Code challenge that I've solved. Although, it's still a work in progress! Please see the "Future Implementations" section for more details.

Although I haven't forked from the repository, this project is heavily based on the [cookiecutter](https://github.com/cookiecutter/cookiecutter) template and the [hypermodern python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) article series from Claudio Jolowicz.

## Usage

[Poetry](https://python-poetry.org/) and Python (version 3.10 or up) are required for this project. I recommend configuring poetry to create virtual environments in the project with:

```
poetry config virtualenvs.in-project true
```

After setting this option, you should be able to use the following to get started:

```bash
poetry shell # To create virtual environment
poetry install # To install project dependencies
poetry run aoc --help  # To view all available commands
```

### CLI Options

This project gets the Advent of Code puzzle data (inputs, puzzle texts) via https requests to the website. For this purpose, the site's cookie is required. Please run the command below, [copy your cookie session](https://github.com/wimglenn/advent-of-code-wim/issues/1), and paste when prompted:

```bash
poetry run aoc set-cookie
```

This will save your cookie into your current working directory under `/.conf/cookie/cookie`.

Once you have set your cookie, you can run the following command to get a solution for a particular year and day:

```bash
poetry run aoc get-solution -y 2022 -d 1 # To get the solutions for year 2022, day 1
poetry run aoc get-solution # To enter year and day interactively
```

Any date that is invalid (ex. year 3000) or any day where I have not included a solution (which, sadly, is most of them) will return an error code.

## Additional information:

### SSL Error

Many organizations use some form of SSL/TLS inspection to bolster their security on the web. However, this also means that anything using the python requests library may have issues accessing any website.

In order to solve this, export the entire certificate chain from the Advent of Code website. In Google Chrome as of December 2022, the steps to do this are (and this is subject to change):

- Click on "Padlock" in the URL bar
- Click "Connection is secure"
- Click "Certificate is valid"
- Click "Details", then "Export" on the bottom right
- When the File Save dialog comes up, ensure you have the "certificate chain" selected, instead of "single certificate"

And copy its contents to the **end** of the file identified with:

```bash
poetry run print-cacert-loc
```

## Future Implementations

Here are a list of things I want to implement for this project in the future:

- Get the problem description for each day from the website
- Move my solutions for prior years (stored in other repositories) into this one
- Include an option to copy and paste outputs directly in the CLI, for folks who don't want to use cookies
- Include a command to list which solutions are available
- Submit answers through this project (instead of copy-pasting on the website)
