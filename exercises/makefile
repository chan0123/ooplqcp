FILES :=           \
    IsPrime1T      \
    IsPrime2T      \
    RMSET          \
    FactorialT     \
    MapT           \
    ReduceT        \
    CollatzT       \
    Collatz2T      \
    RangeIteratorT \
    AllOfT         \
    RangeT         \
    DecoratorsT    \
    SelectT        \
    ProjectT       \
    CrossJoinT     \
    ThetaJoinT     \
    NaturalJoinT

%.pyx: %.py
	./$<

%.pyy: %.py
	coverage run --branch ./$<
	coverage report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

testx: $(FILES:=.pyx)

testy: $(FILES:=.pyy)
