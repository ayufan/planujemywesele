COMMAND := scrapy runspider -s USER_AGENT='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

all: zespoly.csv

zespoly.csv: zespoly.py
		$(COMMAND) zespoly.py -o zespoly.csv -t csv
