# gd-chall-2022

Source code for the challenge "Hardest Demon Bloodbath by Riot" used in [idekCTF 2022](https://ctf.idek.team/).

# Installation and Usage

## Requirements

* [spwn](https://github.com/Spu7Nix/SPWN-language/)
    * Install SPWN from [github](https://github.com/Spu7Nix/SPWN-language/releases)
    * GD is built for Windows, so it's recommended to use the Windows isntaller
* [python with pip](https://www.python.org/)
    * Used for formatting the circuit inputs into a more friendly format for spwn as it is not as powerful a scripting language as python
* [GNU make](https://www.gnu.org/software/make/)
    * Used to build and export the level
    * Recommended to install using [chocolatey](https://chocolatey.org/) for windows
    * Run `choco install make` in an admin Powershell terminal

## Solutions

Here are the solutions to each expression.  See `Converting Solution to Text` for more details on how this works.

|File|ASCII|Binary/Gate Input|
|-|-|-|
|gates_8.txt|Hex value `AA`|`10101010`|
|gates_32.txt|`susy`|`01110011 01110101 01110011 01111001`|
|gates_64.txt|`mosussss`|`01101101 01101111 01110011 01110101 01110011 01110011 01110011 01110011`|
|gates_128.txt|`mosus_is_sussy!!`|`01101101 01101111 01110011 01110101 01110011 01011111 01101001 01110011 01011111 01110011 01110101 01110011 01110011 01111001 00100001 00100001`|
|gates_256.txt|`unban_cursed_from_demonlist!1!!1`|`01110101 01101110 01100010 01100001 01101110 01011111 01100011 01110101 01110010 01110011 01100101 01100100 01011111 01100110 01110010 01101111 01101101 01011111 01100100 01100101 01101101 01101111 01101110 01101100 01101001 01110011 01110100 00100001 00110001 00100001 00100001 00110001`|

* I believe the intended flag should have underscores instead of spaces due to a communication error, but I'm not exactly sure and haven't gone through the `sympy` work to figure that out.

You can convert the ascii representations of each solution into binary using the following command:

```
python -c "print(*map(lambda c: bin(ord(c))[2:].rjust(8, '0'), input()))"
```

Binary inputs are separated by spaces every 8 chars for aesthetic purposes.

## Building the Levels

Before running `make`, you must first create the following blank levels in your geometry dash save file as Spwn cannot create new levels:

* CTFCHALL2022
* CTFCHALL2022DEBUG

which should correspond to the relevant variable names in the Makefile.

Then, there are three recipes that you can run (along with a `clean` recipe to cleanup temporary files):

* `release` (the default): Generates the level for the full expression used for the challenge (in `gates.txt`)
* `debug`: Generates the level for the example expression for debugging purposes (in `gates_example.txt`)
* `dry`: Performs a dry run on the example expression

A more detailed explanation is given below:

### Generating the Expression

.... TBD ...

#### Converting Solution to Text

Since the flag is in the form `idek{<ascii>}`, we must be able to convert our solution into a valid flag for the user.  In this case, the flag is encoded as:

```
like
say hello
01101000 + 01100101 + ... 
first is h
then is e
and so on
```

... TBD ...

### Generating the Level

When generating the level, there are some invariants from the converted gates format that are assumed, such as:

* The inputs for a gate will always show up before a gate itself, so we can process them left-right

.... TBD ...

# Notes

* `backup-1` and `backup-2` are older versions of the spwn code for this challenge
