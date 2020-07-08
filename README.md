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

- [python](https://www.python.org/) >=3.0
- [pip](https://pip.pypa.io/en/stable/)
- [pytest](https://docs.pytest.org/en/stable/)
  - `pip install pytest`
- [pyinstaller](https://www.pyinstaller.org/)
  - `pip install pyinstaller`
  
## Usage

### Test
```
$ pytest
```
To run tests, use the above command in the root directory of this program.

### Build
```
$ pyinstaller --onefile main.py
```
This will generate the executable in a subdirectory called `dist` that can be used with the input files.

