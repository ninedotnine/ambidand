default: test

.PHONY: test clean doc

test:
	@python -t -m ambidand_tests

clean:
	rm -rf __pycache__

doc: doc/ambidand.txt doc/ambidand.html

doc/ambidand.txt: ambidand.py
	@mkdir -p doc
	@pydoc ambidand > doc/ambidand.txt

doc/ambidand.html: ambidand.py
	@mkdir -p doc
	@pydoc -w ambidand > /dev/null
	@echo "" >> ambidand.html # add a newline at the eof because pydoc doesn't
	@mv ambidand.html doc/
