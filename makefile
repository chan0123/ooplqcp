clean:
	cd examples; make clean
	@echo
	cd exercises; make clean

config:
	git config -l

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/ooplqcp.git
	git push -u origin master

pull:
	@rsync -r -t -u -v --delete             \
    --include "Hello.py"                    \
    --include "Assertions.py"               \
    --include "UnitTests1.py"               \
    --include "UnitTests2.py"               \
    --include "UnitTests3.py"               \
    --include "Exceptions.py"               \
    --include "Types.py"                    \
    --include "Operators.py"                \
    --include "Variables.py"                \
    --include "Iteration.py"                \
    --include "Yield.py"                    \
    --include "Lambda.py"                   \
    --include "Comprehensions.py"           \
    --include "Iterables.py"                \
    --include "GlobalVariables.py"          \
    --include "ClassVariables.py"           \
    --include "InstanceVariables.py"        \
    --include "Methods.py"                  \
    --include "Sequences.py"                \
    --include "Lists.py"                    \
    --include "Strings.py"                  \
    --include "Sets.py"                     \
    --include "Dicts.py"                    \
    --include "FunctionKeywords.py"         \
    --include "FunctionDefaults.py"         \
    --include "FunctionUnpacking.py"        \
    --include "FunctionTuple.py"            \
    --include "FunctionDict.py"             \
    --exclude "*"                           \
    ../../../examples/python/ examples
	@rsync -r -t -u -v --delete             \
    --include "IsPrime1.py"                 \
    --include "IsPrime1T.py"                \
    --include "IsPrime2.py"                 \
    --include "IsPrime2T.py"                \
    --include "Factorial.py"                \
    --include "FactorialT.py"               \
    --include "Reduce.py"                   \
    --include "ReduceT.py"                  \
    --include "Map.py"                      \
    --include "MapT.py"                     \
    --include "RangeIterator.py"            \
    --include "RangeIteratorT.py"           \
    --include "Range.py"                    \
    --include "RangeT.py"                   \
    --include "Reduce2T.py"                 \
    --exclude "*"                           \
    ../../../exercises/python/ exercises

push:
	make clean
	@echo
	git add .travis.yml
	git add examples
	git add exercises
	git add makefile
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

testx:
	cd examples; make testx
	@echo
	cd exercises; make testx

testy:
	cd examples; make testy
	@echo
	cd exercises; make testy
