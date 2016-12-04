COMMAND := scrapy runspider -s USER_AGENT='Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

all: wodzireje.csv zespoly.csv

%.csv: %.py
		$(COMMAND) $< -o $@ -t csv
