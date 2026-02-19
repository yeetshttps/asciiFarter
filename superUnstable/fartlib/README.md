# Fartlib for AsciiFarter
#### Version 1.1
Fartlib is a Python module designed specifically for AsciiFarter. It includes all the basic functions such as getting and printing ascii arts, and allows for less headache-inducing development.

Fartlib is designed to allow easy integration of AsciiFarter's features to any Python 3 based scripts/programs.

## Getting fartlib set up
Fartlib needs the following modules to work:

`bs4` - [BeatifulSoup](https://pypi.org/project/beautifulsoup4/) is a library for parsing XML and HTML.

`lxml` - [lxml](https://pypi.org/project/lxml/) binds XML related libraries to python and gives `bs4` better XML parsing functionality.

installing these modules should be as simple as running:
```bash
pip3 install bs4 lxml
```
But, if you run into problems, try following the installation steps on the respective module's webpage, which is usually linked on the pypi page.

To make it so fartlib doesnt have to be manually copied to the directory your project is in, copy the `fartlib` folder to your lib/python folder:

On Linux, it's usually as simple as running this command from this folder:
```bash
cp -r ../fartlib $(realpath /usr/lib/python3.*)
```

> Note that the folder you need to copy fartlib to may differ from system to system, and that this command may not work for all linux distros. 

In the future, a script will be made that does this automatically for you.

## Using fartlib
For examples on how fartlib can be used in your code, see '`./example1.py`' and '`example2.py`'.

Documentation is available in `fartlib/docs/`. 
Documentation is currently limited to API references and may be outdated.

## Credits

Fartlib's author(s) takes no liability or responsibility for security flaws or fartlib destroying your codebase, use it at your own risk.
Licensed under GPL-3.0:
```
        AsciiFarter: make your terminal shart™
        Copyright (C) 2024-2026 Jacob Haché(mangolover1899, itsyeetsup)
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
See `LICENSE.md` in the root of this repository for the full license.

All external software(`bs4`, `lxml`) is property of their respective author(s) and are licensed under their respective software licenses.
