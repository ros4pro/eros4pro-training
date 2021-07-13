# eros4pro-training
>Study materials of the eROS4Pro training by the University of Tartu

## Introduction
The source code of the instructions for the eROS4Pro training can be found under the source directory. An RST markup language ise used. The generated html is placed under the html directory. The html is also published via gh-pages at:

<https://ros4pro.github.io/eros4pro-training>

## Build instructions

To build the sources in this repository, you need to have the following prerequisites installed:

```
pip3 install --user sphinx
pip3 install --user sphinx_rtd_theme
pip3 install --user sphinxcontrib-contentui
pip3 install --user sphinx-copybutton
pip3 install --user recommonmark
```

Then obtain a copy of this repository:

```
git clone https://github.com/ros4pro/eros4pro-training.git
```

Navigate into the cloned directory

```
cd eros4pro-training
```

And run the following command to build an html version of the materials:

```
make html
```


