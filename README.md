# bamboo :bamboo: :panda_face: :bamboo:
A simple tool for creating visualization of pandas's data frame in html. It accepts a dictionary of dataframes and produces a web page showing all the df's in separated tabs. You can also use the pandas' own visualization tools for producing fancy dfs and embed them in the page.

##

```
import numpy as np
import pandas as pd
df1 = pd.DataFrame(np.random.random((4,4)), columns = ["A", "B", "C", "D"])
df2 = pd.DataFrame(np.random.random((4,4)), columns = ["E", "F", "G", "H"])

# We put both df in a dictionary and use pandas' styler object to add captions
dic_pandas={"first":df1.style.set_caption("first"), "second": df2.style.set_caption("second")}

a = View();a.output("My first example", dic_pandas, "output.html")
```

## Prerequisites
It's necessary to use the library [freezeheader](https://github.com/laertejjunior/freezeheader) for freezing the header of the table.

## TODO
- Improve the overall layout
- Add some tools like a search bar, simple row/column statistics
- Can we make the header's freeze in a simpler way? (i'd like to do so without using a third party library)

## Authors

* **Rafael Soares Pinto** rsoaresp at gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
