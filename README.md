# Basic Credit Card Processing

---

This program contains code for a basic credit card provider. It can add new credit card accounts, process charges and credits against them, and displays a summarry after completion.


## Design decisions

The design decisions I made resemble Facade Design pattern. I created three files each containing a class: 
- `main.py`: main class that runs the program, reads input and forwards the command to credit card processor 
- `user.py`: records User information
- `credit_card_processor.py`: the Credit Card Processor, that processes the commands and manipulates user information. 

## Why python

Python helps me focus on the program requirements, by having me deal with lesser idiosyncracies that comes with any programming language. In my opinion, I am able to achieve more in fewer steps or lines of code than many other programming languages.

## Requirements

- [python](https://www.python.org/) >=3
- [pip](https://pip.pypa.io/en/stable/)
- [pytest](https://docs.pytest.org/en/stable/)
- [pyinstaller](https://www.pyinstaller.org/)

## Usage

- `$ pytest`
  - runs tests
- `

`pip install pytest`
`pip install pyinstaller`
`pyinstaller --onefile main.py`

## Implementing and Packaging Your Solution:

- An overview of your design decisions
- Why you picked the programming language you used
- How to run your code and tests, including how to compile it if applicable and
  how to install any dependencies your code may have.

Do not include precompiled binaries with your code; we will compile and run
your solution from the source code you provide.
