Algorithm
		STEP 1) Read client configuration JSON file and set spider name, allowed domain & start urls as per configuration 
		STEP 2) scrap category url for the start url
		STEP 3) for each category
				STEP A) save category url
				STEP B) save category name
				STEP C) scrap items for category url
				STEP D) loop through the items and save each item detail
				STEP E) check if scraped last item of the page, move to next page
				
SOFTWARE SETUP & INSTALL
	Download and setup install anaconda
	Create new environment
	Install scrapy in newly created environment
	
Project Setup
	create an empty folder for scrapy project
	navigate to newly created folder
	open command prompt
	activate newly created environment from command prompt by executing below command
		activate <ScrapyEnvironmentName>
	create new scrapy project by executing below command
		scrapy startproject <ProjectName>
	==========================================
	INITIAL PROJECT STRUCTURE WILL BE AS BELOW
	==========================================
		Sample
			Sample
				items.py
				middlewares.py
				pipelines.py
				settings.py
				__init__.py
				spiders
					__init__.py
			scrapy.cfg
	===========================
	COMPLETED POJECT STRUCTURE
	===========================
		recommender_bot
			recommender_bot
				items.py								=> MODIFY => method[Field()]
				middlewares.py
				pipelines.py
				settings.py								=> MODIFY => property[ROBOTSTXT_OBEY, ITEM_PIPELINES]
				__init__.py
				spiders
					__init__.py		
					product_details_spider.py			=> #####CREATE#####	=> Explained in IDE section below		
				resources								=> CREATE
					client_config.json					=> CREATE
			scrapy.cfg
			requirements.txt							=> CREATE => Added boto3 version
			scrapinghub.yml								=> CREATE => property[stacks, default] => Added scrapy version 
			setup.py									=> CREATE => method[setup(), find_packages()], property[name, version, packages, package_data, entry_points, zip_safe]
			resultset									=> CREATE
				grofers_product_detail_04262018.csv		=> CREATE		
IDE
	open spider with new scrapy environment
	browse for project folder
	open product_details_spider.py
	method => loads(), get_data(), xpath(), extract(), urljoin(), Request(), urlparse()
	property => self, response, Spider, callback, self, url, meta, page, path

Run spider from local using below command
	scrapy crawl <spider name> -o <file.csv>

check-in project to GitHub using below command
	STEP 1) create a repository in GitHub
	STEP 2) git init
	STEP 3) git add .
	STEP 4) git commit -m "<comment>"
	STEP 5) git remote add origin <repository url>
	STEP 6) git push origin master 	
	
	To check in modified project execute step 3,4,6		

Scraping hub integration
	create scrapping hub account 
	create a project and map with github repository
	in settings provide AWS security tokens and s3 bucket location 
References
	https://www.youtube.com/watch?v=yWRkc_E9CYg&list=PLE50-dh6JzC6dHxpAno-a6W7QpWdAFN20
	https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
	https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/
	
	
	

						
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
