

ANTLR=/usr/local/lib/antlr-4.9.2-complete.jar

PARSER_FILES=\
	SCV.interp\
	SCVLexer.py\
	SCVParser.py\
	SCV.tokens\
	SCVLexer.tokens\
	SCVLexer.interp\
	SCVListener.py

all: $(PARSER_FILES)
	#python3 main.py test.scv
	#python3 main.py test2.scv
	python3 main.py example1.scv

$(PARSER_FILES): SCV.g4
	java -jar $(ANTLR) SCV.g4 -Dlanguage=Python3

clean:
	rm -fr $(PARSER_FILES) __pycache__
