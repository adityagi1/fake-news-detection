import urllib.request
from bs4 import BeautifulSoup
import csv
 
url_list = ["http://www.cnn.com/2017/11/23/politics/gop-pollster-memo-republicans-2018/index.html",
			"http://www.cnn.com/2017/11/23/politics/michael-flynn-donald-trump-robert-mueller-new-york-times/index.html",
			"http://www.cnn.com/2017/11/23/politics/joe-barton-image-revenge-porn/index.html",
			"http://www.cnn.com/2017/11/23/health/texas-abortion-law-struck-down/index.html",
			"http://www.cnn.com/2017/11/23/politics/us-navy-seventh-fleet-breaking-point/index.html",
			"http://www.cnn.com/2017/11/23/politics/fugitive-from-justice-fbi-background-check/index.html",
			"http://www.cnn.com/2017/11/23/politics/us-troops-thanksgiving/index.html",
			"http://www.cnn.com/2017/11/22/politics/melanie-sloan-john-conyers-cnn-tv/index.html",
			"http://www.cnn.com/2017/11/23/politics/trump-thanksgiving-teleconference/index.html",
			"http://www.cnn.com/2017/11/23/politics/trump-thanksgiving-mar-a-lago/index.html",
			"http://www.cnn.com/2017/11/22/politics/kellyanne-conway-hatch-act/index.html",
			"http://www.cnn.com/2017/11/22/politics/conyers-lawyer-allegations/index.html",
			"http://www.cnn.com/2017/11/22/politics/thanksgiving-dinner-politics/index.html",
			"http://www.cnn.com/2017/11/22/politics/sebelius-clinton-white-house-behavior/index.html",
			"http://www.cnn.com/2017/11/22/politics/things-president-trump-is-thankful-for/index.html",
			"http://www.cnn.com/2017/11/21/politics/conyers-former-staffer-accuses-harassment/index.html",
			"http://www.cnn.com/2017/11/22/politics/dnc-rnc-fundraising-election-day/index.html",
			"http://www.cnn.com/2017/11/22/politics/tom-carper-gary-cohn-phone-call/index.html",
			"http://www.cnn.com/2017/11/22/politics/trump-thanksgiving-tweets/index.html",
			"http://www.cnn.com/2017/11/21/politics/ivanka-trump-india/index.html",
			"http://www.cnn.com/2017/11/22/politics/trump-convenient-truth-roy-moore/index.html",
			#"http://money.cnn.com/2017/11/22/technology/trump-fcc-policies/index.html",
			"http://www.cnn.com/2017/11/21/politics/zinke-wife-travel/index.html",
			"http://www.cnn.com/2017/11/21/politics/trump-women-accusers/index.html",
			"http://www.cnn.com/2017/11/22/politics/donald-trump-lavar-ball/index.html",
			"http://www.cnn.com/2017/11/21/politics/trump-russia-by-the-numbers/index.html",
			"http://www.cnn.com/2017/11/19/politics/abbe-lowell-kushner-gotcha-games/index.html",
			"http://www.cnn.com/2017/11/15/politics/ivanka-trump-roy-moore/index.html",
			"http://www.cnn.com/2017/11/22/politics/john-conyers-michigan-sexual-harassment-allegations/index.html",
			"http://www.cnn.com/2017/11/22/politics/texas-joe-barton-apology-graphic-picture/index.html",
			"http://www.cnn.com/2017/11/22/politics/democratic-lawmaker-john-conyers-resign/index.html",
			"http://www.cnn.com/2017/11/22/politics/rand-paul-kelley-paul-mystery/index.html",
			"http://www.cnn.com/2017/11/20/politics/travel-ban-supreme-court/index.html",
			"http://www.cnn.com/2017/11/17/politics/trump-supreme-court-list/index.html",
			"http://www.cnn.com/2017/11/17/politics/neil-gorsuch-federalist-society/index.html",
			"http://www.cnn.com/2017/11/14/politics/abortion-first-amendment/index.html",
			"http://www.cnn.com/2017/11/22/politics/justice-department-att-lawsuit-judge/index.html",
			"http://www.cnn.com/2017/11/22/politics/jeff-sessions-background-checks/index.html",
			"http://www.cnn.com/2017/11/22/politics/census-bureau-pick/index.html",
			"http://www.cnn.com/2017/11/22/politics/moore-communications-director-resigns/index.html",
			"http://www.cnn.com/2015/11/24/politics/history-of-the-white-house-turkey-pardon/index.html",
			"http://www.cnn.com/2017/11/21/politics/state-department-tillerson-child-soldiers-protest/index.html",
			"http://www.cnn.com/2017/11/16/politics/jeff-sessions-doj-succession/index.html",
			"http://www.cnn.com/2017/11/20/politics/president-donald-trump-north-korea-terrorism/index.html",
			"http://www.cnn.com/2017/11/22/politics/navy-aircraft-crash/index.html",
			"http://www.cnn.com/2017/11/21/politics/niger-ambush-sgt-la-david-johnson-remains/index.html",
			"http://www.cnn.com/2017/11/21/politics/military-personnel-removed-trump-asia-trip/index.html",
			"http://www.cnn.com/2017/11/21/politics/somalia-us-airstrike-al-shabaab/index.html",
			"http://www.cnn.com/2017/11/20/politics/mueller-interviews-white-house-officials/index.html",
			"http://www.cnn.com/2017/11/17/politics/jared-kushner-july-testimony-did-not-recall-campaign-wikileaks-contact/index.html",
			"http://www.cnn.com/2017/11/15/politics/russia-investigation-fusion-gps-glenn-simpson-dossier/index.html",
			"http://www.cnn.com/2017/11/07/politics/keith-schiller-house-russia-investigation/index.html",
			"http://www.cnn.com/2017/11/08/politics/joseph-mifsud-trump-russia-investigation/index.html",
			"http://www.cnn.com/2017/11/22/politics/tillerson-myanmar-ethnic-cleansing/index.html",
			"http://www.cnn.com/2017/11/22/asia/north-korea-us-terror-provocation/index.html",
			"http://www.cnn.com/2017/11/21/politics/trump-putin-phone-call/index.html",
			#"http://money.cnn.com/2017/11/21/news/economy/treasury-north-korea-sanctions/index.html",
			"http://www.cnn.com/2017/11/12/politics/joe-biden-book-tour/index.html",
			"http://www.cnn.com/2017/11/10/politics/2020-vision-joe-biden-book-tour/index.html",
			"http://www.cnn.com/2017/11/03/politics/2020-vision-elizabeth-warren-rigged/index.html",
			"http://www.cnn.com/2017/11/23/opinions/thanksgiving-troops-opinion-lemmon/index.html",
			"http://www.cnn.com/2017/11/22/opinions/haiti-president-trump-temporary-status-joseph-opinion/index.html",
			"http://www.cnn.com/2017/11/22/opinions/trumps-pathetic-need-for-thanks-misses-this-point-parini/index.html",
			"http://www.cnn.com/2017/11/22/opinions/kelley-paul-since-the-attack-opinion/index.html",
			"http://www.cnn.com/2017/11/21/opinions/companies-think-before-you-tweet-alaimo/index.html",
			"http://www.cnn.com/2017/11/21/opinions/hoboken-mayor-diversity-american-value-bhalla-opinion/index.html",
			"http://www.cnn.com/2017/11/21/politics/murkowski-obamacare-repeal-mandate/index.html",
			#"http://money.cnn.com/2017/11/15/news/economy/obamacare-individual-mandate/index.html",
			#"http://money.cnn.com/2017/11/05/news/economy/tax-reform-bill-house-republicans/index.html",
			"http://www.cnn.com/2017/11/20/politics/dhs-temporary-protected-status-haiti/index.html",
			"http://www.cnn.com/2017/11/21/politics/trump-sanctuary-cities-executive-order-blocked/index.html",
			#"http://money.cnn.com/2017/11/18/news/economy/dreamers-jobs-education-profile/index.html",
			"http://www.cnn.com/2017/11/22/politics/trump-wine-national-park/index.html",
			"http://www.cnn.com/2017/11/17/politics/tax-reform-what-next-senate-bill-republican-plan/index.html",
			"http://www.cnn.com/2017/10/26/politics/trump-voter-commission-gao-investigation/index.html",
			#"http://money.cnn.com/2017/11/21/news/economy/trump-nafta-talks/index.html",
			#"http://money.cnn.com/2017/11/20/news/economy/yellen-submits-resignation/index.html",
			"http://www.cnn.com/2017/11/15/politics/senate-tax-bill-amendments-special-interests-industry-groups/index.html",
			"http://www.cnn.com/2017/11/22/politics/roy-moore-trump-sexual-accusers/index.html",
			"http://www.cnn.com/2017/11/22/us/border-patrol-agent-killed/index.html",
			"http://www.cnn.com/2017/11/21/politics/computer-revolution-us-partisan-politics/index.html",
			"http://www.cnn.com/2017/11/21/politics/roy-moore-campaign-allegations/index.html",
			"http://www.cnn.com/2017/11/21/politics/donald-trump-roy-moore-alabama/index.html",
			"http://www.cnn.com/2017/11/21/politics/puerto-rico-historic-site-reopen/index.html",
			"http://www.cnn.com/2017/11/19/politics/al-franken-minnesota/index.html",
			"http://www.cnn.com/2017/11/20/politics/al-franken-inappropriate-touch-2010/index.html",
			"http://www.cnn.com/2017/11/20/politics/tillerson-rejects-criticism-management-state-department/index.html",
			"http://www.cnn.com/2017/11/14/politics/sexual-harassment-congress/index.html",
			"http://www.cnn.com/2017/11/23/us/white-people-talk-thanksgiving-trnd/index.html",
			"http://www.cnn.com/2017/11/23/africa/libya-reaction-slave-trade/index.html",
			"http://www.cnn.com/2017/11/22/health/baby-receives-kidney-transplant-bn/index.html",
			"http://www.cnn.com/2017/11/23/asia/manus-island-detention-center/index.html",
			"http://www.cnn.com/2017/11/22/us/kate-steinle-murder-trial-jury-deliberations/index.html",
			"http://www.cnn.com/2017/11/22/us/us-gymnastics-doctor-plea-hearing/index.html",
			"http://www.cnn.com/2017/11/22/asia/manus-refugee-police-operation/index.html",
			#"http://www.cnn.com/travel/article/andrew-peacock-expedition-doctor-photographer/index.html",
			"http://www.cnn.com/2017/11/22/africa/french-president-libya-slave-auctions/index.html",
			"http://www.cnn.com/2017/11/22/health/philadelphia-neurologist-guilty-groping-patients/index.html",
			#"http://www.cnn.com/videos/politics/2017/11/20/kellyanne-conway-roy-moore-tax-vote-collins-nr.cnn",
			"http://www.cnn.com/2017/11/22/politics/justice-department-att-lawsuit-judge/index.html",
			"http://www.cnn.com/2017/11/21/asia/north-korea-defector/index.html",
			#"http://www.cnn.com/videos/politics/2017/11/22/gary-cohn-trump-tax-reform-bad-phone-connection-carper-sot-nr.cnn",
			"http://www.cnn.com/2017/11/22/opinions/haiti-president-trump-temporary-status-joseph-opinion/index.html",
			"http://www.cnn.com/2017/11/22/health/jfk-assassination-back-pain/index.html",
			#"http://www.cnn.com/videos/spanish/2017/11/22/cnnee-cafe-vo-tclan-5-ronda.cnn",
			#"http://www.cnn.com/videos/politics/2017/11/22/border-patrol-agent-death-lavandera-ac360-dnt.cnn",
			"http://www.cnn.com/2017/11/21/us/kate-steinle-murder-trial-jury/index.html"
			]
csv_file = open("cnn_articles.csv", "a", newline = '')
writer = csv.writer(csv_file)

for url in url_list:
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	article_url = url
	article_author = soup.find("p", class_ = "metadata__byline").text
	article_title = soup.find("h1", class_ = "pg-headline").text
	article_time = soup.find("p", class_ = "update-time").text
	if ("," in article_author):
		comma_index = article_author.index(",") 
		article_author = article_author[:comma_index]
	article_author = article_author.replace(",","").replace("By","").replace("Analysis by","")
	trimmed_time = article_time[8:]
	print("Article URL:" + article_url + "\n" + "Title:" + article_title + "\n" + 
		"Author:" + article_author + "\n" + "Time:" + trimmed_time + "\n")
	writer.writerow([article_url, article_title, article_author, trimmed_time])

csv_file.close()

	






