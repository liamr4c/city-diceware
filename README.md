# city-diceware: Diceware with city names
Make diceware passwords with a wordlist of all cities with more than 1000 people (142283).

## Usage
1. (Optionally) generate `cities.txt` with up-to-date information with `make -f wordlist.Makefile`
2 Run `./diceware.py`. Use `./diceware.py -h` for a list of options.

## Security
diceware.py uses python3's `secrets` module to get cryptographically-secure randomness. It is 28 lines of python, easily auditable by you. This is assuming that you accually want to use this, it was made "because I can" and does not attempt to be especially useful.
