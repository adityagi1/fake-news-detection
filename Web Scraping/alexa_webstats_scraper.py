from bs4 import BeautifulSoup
import csv
import urllib.request
import time

#information to scrape from webpage: global rank, USrank, country, top 5 countries, bouncerate, daily pageviews per visitor,
#daily time on site, percentage search visits, total sites linking in 

#open and initialize necessary csv files
csv_file = open("alexa_webstats.csv", "w", newline = '')
writer = csv.writer(csv_file)

#write the header/field names to the csv file
writer.writerow(["site_url", "global_rank", "US_rank", "website_country", "top1_country",
	"top2_country", "top3_country", "top4_country", "top5_country", "bounce_rate", "daily_pageviews_per_visitor", "daily_time_on_site",
	"percentage_search_visits", "number_sites_linking_in"])



#a variable to count which website is being processed
count = 1;

#list of domains to query from Alexa Webstats
domain_list = ["100percentfedup.com", "abcnews.com.co", "abovetopsecret.com", "activistpost.com", "allnewspipeline.com",
"americannews.com", "americasfreedomfighters.com", "amren.com", "anonhq.com", "antiwar.com", 
"barenakedislam.com", "beforeitsnews.com", "bipartisanreport.com", "blacklistednews.com", "breitbart.com",                 
"collective-evolution.com" , "conservativetribune.com", "counterpunch.org" , "dailystormer.com", "dailywire.com",              
"davidstockmanscontracorner.com", "dcclothesline.com", "der-postillon.com", "educateinspirechange.org", "elmundotoday.com",               
"freedomoutpost.com", "frontpagemag.com", "globalresearch.ca", "godlikeproductions.com", "gomerblog.com",                 
"guardianlv.com", "healthimpactnews.com", "humansarefree.com", "ifyouonlynews.com", "ihavethetruth.com",              
"informationclearinghouse.info", "infowars.com", "investmentwatchblog.com", "jewsnews.co.il", "journal-neo.org",      
 "kingworldnews.com", "lewrockwell.com", "liberalamerica.org", "madworldnews.com", "mintpressnews.com",             
 "morningnewsusa.com", "nakedcapitalism.com", "naturalnews.com", "newstarget.com", "newsthump.com", 
 "nutritionfacts.org", "occupydemocrats.com", "opednews.com", "paulcraigroberts.org", "politicususa.com",
 "presstv.com", "prisonplanet.com", "rbth.com", "realfarmacy.com", "redflagnews.com",               
  "reductress.com", "rense.com", "returnofkings.com", "rt.com", "russia-insider.com",
  "shtfplan.com", "silverdoctors.com", "southfront.org", "survivopedia.com", "theantimedia.org", 
  "thecommonsenseshow.com", "thedailysheeple.com", "thedailywtf.com", "theeconomiccollapseblog.com", "theeventchronicle.com",         
  "thefederalistpapers.org",        "thefreethoughtproject.com",      "thenewamerican.com",            
  "theonion.com", "thepoke.co.uk", "theunrealtimes.com", "toprightnews.com", "trueactivist.com",
  "truthdig.com", "twitchy.com", "unz.com", "usuncut.com", "vdare.com",
  "veteranstoday.com", "vigilantcitizen.com", "voltairenet.org", "wakingtimes.com", "washingtonsblog.com",           
  "waterfordwhispersnews.com", "whatreallyhappened.com", "whydontyoutrythis.com", "wikileaks.org", "winningdemocrats.com",           
  "wnd.com", "worldtruth.tv", "yournewswire.com", "zerohedge.com", "nytimes.com", "foxnews.com", "cnn.com"]

#loop through each website in the list
for domain in domain_list:
	print("Website No.: ", str(count))
	
	target_url = "https://www.alexa.com/siteinfo/" + domain
	page = urllib.request.urlopen(target_url)
	soup = BeautifulSoup(page, 'html.parser')
	try:
		global_rank =soup.find_all("strong", class_ = "metrics-data align-vmiddle")[0].text.strip()
	except AttributeError:
		global_rank = ""
	try:	
		US_rank = soup.find_all("strong", class_ = "metrics-data align-vmiddle")[1].text.strip()
	except AttributeError:
		US_rank = ""
	try:	
		website_country = soup.find("span", class_ = "text-inline").text.strip()
	except AttributeError:
		website_country = ""
	try:	
		top1_country = soup.find("tr", attrs = {"data-count":"1", "class" : " "}).contents[1].text.strip()
	except AttributeError:
		top1_country = ""
	try:	
		top2_country = soup.find("tr", attrs = {"data-count":"2","class" : " "}).contents[1].text.strip()
	except AttributeError:
		top2_country = ""
	try:	
		top3_country = soup.find("tr", attrs = {"data-count":"3", "class" : " "}).contents[1].text.strip()
	except AttributeError:
		top3_country = ""
	try:
		top4_country = soup.find("tr", attrs = {"data-count":"4", "class" : " "}).contents[1].text.strip()
	except AttributeError:
		top4_country = ""
	try:	
		top5_country = soup.find("tr", attrs = {"data-count":"5", "class" : " "}).contents[1].text.strip()
	except AttributeError:
		top5_country = ""
	try:	
		bounce_rate = soup.find_all("strong", class_ = "metrics-data align-vmiddle")[2].text.strip()
	except AttributeError:
		bounce_rate = ""
	try:	
		daily_pageviews_visitor = soup.find_all("strong", class_ = "metrics-data align-vmiddle")[3].text.strip()
	except AttributeError:
		daily_pageviews_visitor = ""
	try:	
		daily_site_time = soup.find_all("strong", class_ = "metrics-data align-vmiddle")[4].text.strip()
	except AttributeError:
		daily_site_time = ""
	try:	
		percentage_search_traffic = soup.find_all("strong", class_ = "metrics-data align-vmiddle")[5].text.strip()
	except:
		percentage_search_traffic = ""
	try:	
		num_sites_linking_in = soup.find("span", class_ = "font-4 box1-r").text.strip()
	except AttributeError:
		num_sites_linking_in = ""
	writer.writerow([domain, global_rank, US_rank, website_country, top1_country, top2_country, top3_country, top4_country,
		top5_country, bounce_rate, daily_pageviews_visitor, daily_site_time, percentage_search_traffic, num_sites_linking_in])
	count+=1
	time.sleep(2)


csv_file.close()

