Steps to run scrapers:

1)Download anaconda
2)Install scrapy in anaconda prompt by typing -
            conda install -c conda-forge scrapy
            (https://www.accordbox.com/blog/scrapy-tutorial-4-how-install-scrapy-windows/)
3)Once scrapy is installed, change the directory to the directory where you have the project (In anaconda prompt)
4)Then navigate to the spiders directory and run the spider using the following command -
            scrapy runspider spider1.py


How to create a new project:

1) Once you are in the directory where you want to create the project (through anaconda prompt), type the following command - 
            scrapy startproject name_of_project  
            [where name_of_project is the name you want to give for your project, rest of the statement is part of syntax]
2) Once the project is created, change the contents of the file according to your needs
3) To create a new spider - 
            scrapy genspider spider_name domain_name
            [where spider_name is the name you want to give for the spider and domain_name is the domain of the website you want to scrape/crawl etc]