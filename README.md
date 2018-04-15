# Marking with MarkDown

## To get started 

`chmod u+x *.py`

## To mark a student

`./mark.py [student id without u]`

Change `subl` inside mark.py to your own preferred editor.

## To compile 

`./read.py [nolatex] [no of scripts]`

If nolatex is specified then weasyprint will be used instead. Obtain from [http://weasyprint.org/](http://weasyprint.org/).

If n = no of script is specified only the n latest (alphabetically largest) will be regenerated. results.csv and breakdown.csv are always rebuilt for the whole directory.



## Dependencies

* Pandoc
* pypandoc
* Either:
	* pdflatex
	* weasyprint
