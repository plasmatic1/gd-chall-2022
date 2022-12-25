# gd-chall-2022

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

## Building the Levels

There are three recipes that you should run:

* `release` (the default): Generates the level for the full expression used for the challenge (in `gates.txt`)
* `debug`: Generates the level for the example expression for debugging purposes (in `gates_example.txt`)
* `dry`: Performs a dry run on the example expression

## Generating Expression

.... TBD ...

# Notes

* `backup-1` and `backup-2` are older versions of spwn code and 