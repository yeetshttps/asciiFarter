# fartlib reference
This document outlines all the functions, objects and classes included in `fartlib`.
Innaccurate information? Make an [issue on GitHub](https://github.com/yeetshttps/asciiFarter/issues).

---

## `getfart`
`getfart` is the main module used by `fartlib`. It includes functions and classes to receive art files over the internet such as `random_art` or `newest_art`.

### `.random_art()`
```python3
class getfart.random_art()
```
Gets a randomly selected ascii art.

#### Attributes
###### `random_art.name`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The filename of the randomly selected art.

###### `random_art.File`
[`urllib.request.Request()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) - The art as a file-like object.

###### `random_art.text`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The text of the randomly selected art, equalvilant to "`random_art.File.read().decode('utf-8')`".

#### Methods
###### `random_art.poop()`
```python3
def random_art.poop(line_delay=0.000001)
```
Prints the art in AsciiFarter style, replaceable using [`stdout`](https://docs.python.org/3/library/sys.html#sys.stdout) and [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep).

###### Arguments:
`line_delay`: [`float`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. Responsible for the scrolling effect output by AsciiFarter.


---

### `.newest_art()`
```python3
class getfart.newest_art()
```
Get the newest art, pulled from the `<newestAscii>` element in [`status.xml`](https://yeetshttps.github.io/asciiFarter/status.xml).

#### Attributes
###### `newest_art.name`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The filename of the selected art.

###### `newest_art.File`
[`urllib.request.Request()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) - The art as a file-like object.

###### `newest_art.text`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The text of the selected art, equalvilant to "`newest_art.File.read().decode('utf-8')`".

#### Methods
###### `newest_art.poop()`
```python3
def newest_art.poop(line_delay=0.000001)
```
Prints the art in AsciiFarter style, replaceable using [`stdout`](https://docs.python.org/3/library/sys.html#sys.stdout) and [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep).

###### Arguments:
`line_delay`: [`float`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. Responsible for the scrolling effect output by AsciiFarter.

