# Advent of Code 2021

All the solutions are written in Python using only packages from the standard library.
This year i am focusing on type hinting, the challenges do not lend themselves to any deep dive into the typing library, but the volume of tasks does build familiarity with the tools and will hopefully establish typehinting as a default for me when i write code. My second goal is to only use standart library packages, and to use them wherever possible. I will not reimplement any standard lib functionality where i can avoid it.

Thank you to [Eric Wastl](http://was.tl/) for making this wonderful challenge.

## Usage

The tools to fetch and run the challenges have third party requirements, see `requirements.txt`.


To run a challenge:
```sh
$ ./run.py --day 15
```

To fetch the `input.txt` for a day:
```sh
$ ./fetch_input.py --day 15
```

Fetching will require a fresh session token from [Advent of Code](https://adventofcode.com). Create a `.env` file and set the variable `AOC_SESSION` to your session token:

```sh
AOC_SESSION = xyz
```
