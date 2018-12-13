from nytimesarticle import articleAPI
import csv
import numpy as np
import time


api_caller = articleAPI("d18acaee460d4e0b8dd46ba0acc5d67a")
csv_file = open("NYT_articles.csv", "w", newline = '')
writer = csv.writer(csv_file)
for pg_num in np.arange(0,200,1):
	results = api_caller.search(begin_date = 20151115, end_date = 20161115, page = pg_num)
	# Is the API trying to communicate something? (rate exceeded??)
	if "message" in results.keys():
		print(results.get("message"))
	#Did the API call fail?
	if results is None or results.get("response") is None:
		print("API Call Failed!")
	for article_num in range(9):
		print("Page No.: " + str(pg_num) + "	" + "Article No.: " + str(article_num) + "\n")
		article_dict = results.get("response").get("docs")[article_num]
		web_url = article_dict.get("web_url", "empty")
		snippet = article_dict.get("snippet", "empty")
		source = article_dict.get("source", "empty")
		headline = article_dict.get("headline").get("main")
		print_headline = article_dict.get("headline").get("print_headline")
		#insert logic for getting keywords
		pub_date = article_dict.get("pub_date")
		document_type = article_dict.get("document_type")
		#check if news_desk is misspelt - check if "new_desk" key is in the dict?
		if "new_desk" in article_dict.keys():
			news_desk = article_dict["new_desk"]
		#the regular case (no misspelling!) - check if "news_desk" key is in the dict? 
		elif "news_desk" in article_dict.keys():
			news_desk = article_dict["news_desk"]
		else:
			news_desk = "empty"
		#insert logic for getting individual author's names? not required
		if "byline" in article_dict.keys() and "original" in article_dict["byline"].keys():
			author = article_dict.get("byline").get("original", "empty")
		else:
			author = "empty"
		type_of_material = article_dict.get("type_of_material", "empty")
		#print("web_url: " + web_url)
		#print("author: " + author)
		#print("headline: " + headline)
		#print("pub_date: " + pub_date) 
		#print("source: " + source)
		#if (print_headline != None):
		#	print("print_headline: " + print_headline)
		#print("news_desk: " + news_desk)
		#print("snippet: " + snippet)
		#print("type_of_material: " + type_of_material)
		#print("document_type: " + document_type)	 
		#now just need to write to a csv!
		# surpress any character encoding warnings
		try:
			writer.writerow([web_url, author, headline, pub_date, source, print_headline, news_desk, snippet, type_of_material, document_type])
		except UnicodeEncodeError:
			pass
	# the API has a 1 call per second rate limit.
	time.sleep(3)

csv_file.close()

#things to get: (web_url, snippet, source, headline, print_headline, keywords, pub_date, document_type,news_desk, byline/author, type_of_material)
