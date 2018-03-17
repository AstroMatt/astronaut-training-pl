build:
    rm -fr _book/
    sphinx-build -j 4 -b singlehtml . _book/

rebuild:
    sphinx-build -j 4 -b singlehtml . _book/

clean:
    -rm -fr _book/
