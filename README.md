# Basic Credit Card Processing

---

Imagine that you're writing software for a credit card provider. Implement a
program that will add new credit card accounts, process charges and credits
against them, and display summary information.

## Design decisions

Keep it simple!

- going to throw any "gotchas" at you or your submission,
- testing for your ability to suss out edge cases, or
- trying to trick you.

## Why python

- Your program must accept input from two sources: a filename passed in
  command line arguments and STDIN. For example, on Linux or macOS both
  `./myprogram input.txt` and `./myprogram < input.txt` should work. STDIN should read the
  whole input file, which may contain multiple lines.
- Your program must accept the following three input commands passed with space delimited
  arguments:
  - "Add" will create a new credit card for a given name, card number, and limit
    - Card numbers should be validated using Luhn 10

## Requirements

#### Dependencies

- [gnu make](https://www.gnu.org/software/make/) >=3.81

* more details at [core_api readme](https://github.com/QuicketSolutions/core_api)
* [Project Requirements](https://github.com/jack5432109/Basic-Credit-Card-Processing/wiki/Project-Requirements)
* All input will be valid. For example, you don't need to check for or gracefully handle:
  - Illegal characters
  - Malformed commands
  - Capitalization changes
* All input will be space delimited.
* Credit card numbers may vary in length up to 19 characters.
* Credit card numbers will always be numeric.
* Amounts will always be prefixed with "\$" and will be in whole dollars (no
  decimals).

## Input and Output:

```
Lisa: $-93
Quincy: error
Tom: $500
```

## Implementing and Packaging Your Solution:

- An overview of your design decisions
- Why you picked the programming language you used
- How to run your code and tests, including how to compile it if applicable and
  how to install any dependencies your code may have.

Do not include precompiled binaries with your code; we will compile and run
your solution from the source code you provide.
