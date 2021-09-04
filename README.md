# CSS Minifier

**_Not just any other minfier. This is something special._**

This is targetted towards [CSS Battle](https://cssbattle.dev/). Length of the code is one of the metrics in [CSS Battle](https://cssbattle.dev/). This CSS Minifier tries to reduce the length of code by renaming class names and id names.

## Usage

Have your source code at [source.html](source.html). Run [main.py](main.py) script.

```bash
python3 main.py # generates optimized_source.html
```

[optimized_source.html](optimized_source.html) contains Optimized Source :)

## Why this project exists

[CSS Battle](https://cssbattle.dev/) is a CSS code-golfing game. Participants are given an image, they're ranked based on following metrics.

- Percentage match between the Output of CSS and given image
- Size of source code (in number of characters). The lesser the size, the better the rank.

So, Even our percentage match is 100%, Due to opponents lesser size, our rank may fall behind. This project is an attempt to squeeze the characters out of the source code.

## Logic

Some websites minify source code ([like this](https://www.willpeavy.com/tools/minifier/)). The problem is, they do not change anything in source code. We can replace looong class names and ids with short classnames. This is what I did. Below is the rough breakdown of the process.

- Parse Classes and Ids (seperately).
  - Keep track of frequencies of each selector.
- Sort the selectors based on their frequency, in descending order.
  - Because, We need to assign shorter class to most occuring selector.
- Generate short classes with 26 alphabets and map to existing selectors.
- Replace the existing selectors with short versions of them.

And, Pass this source to any of the above websites. That's the boring job :)

### Example

Check [source.html](source.html) and [optimized_source.html](optimized_source.html).
