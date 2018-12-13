#import necessary libraries
import requests
import csv

#initialize variables
endpoint = "https://api.sharedcount.com/v1.0/"
api_key = "3802555cf5b82fba0c2709e934d139654dd91aff"
stem_list = ["100percentfedup.com", "abcnews.com.co", "abovetopsecret.com", "activistpost.com", "allnewspipeline.com",
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
count = 1

#create output csv file
csv_file = open("socialmedia_data.csv", "w", newline = '')
writer = csv.writer(csv_file)




#get the social media information for each website
for stem in stem_list: 
	website = "https://" + stem
	params_dict = {"url": website, "apikey": api_key}
	result = requests.get(endpoint, params = params_dict)
	data = result.json()
	su = data["StumbleUpon"]
	pi = data["Pinterest"]
	li = data["LinkedIn"]
	fb_total = data["Facebook"]["total_count"]
	fb_comment = data["Facebook"]["comment_count"]
	fb_reaction = data["Facebook"]["reaction_count"]
	fb_share = data["Facebook"]["share_count"]
	fb_comment_plugin = data["Facebook"]["comment_plugin_count"]
	gpo = data["GooglePlusOne"]
	#print information about the website currently being processed
	print("Website No. ", count , "\n" , 
		"Website: " , stem , "\n" , 
		"Data: ",su , pi , li , fb_total , fb_comment, fb_reaction, fb_share, fb_comment_plugin, gpo)
	writer.writerow([stem, su, pi, li, fb_total, fb_comment, fb_reaction, fb_share, fb_comment_plugin, gpo])
	count+=1



csv_file.close()




