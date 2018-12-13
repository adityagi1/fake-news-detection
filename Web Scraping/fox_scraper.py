import urllib.request
from bs4 import BeautifulSoup
import csv
import numpy as np

url_list = ["http://www.foxnews.com/politics/2017/11/23/new-manafort-travel-docs-reveal-closer-ties-to-russia-report.html",
 			"http://www.foxnews.com/politics/2017/11/23/michael-flynn-lawyers-cut-ties-with-trump-legal-team-reports-say.html",
 			"http://www.foxnews.com/politics/2017/11/23/al-franken-admits-crossed-line-after-groping-allegations.html",
 			"http://www.foxnews.com/politics/2017/11/23/ex-rep-hinchey-who-pushed-to-protect-environment-dies.html",
 			"http://www.foxnews.com/politics/2017/11/23/new-manafort-travel-docs-reveal-closer-ties-to-russia-report.html",
 			"http://www.foxnews.com/politics/2017/11/23/despite-blue-laws-customers-line-up-for-black-friday-deals.html",
 			"http://www.foxnews.com/politics/2017/11/23/gop-committees-moore-remain-at-odds-as-alabama-election-nears.html",
 			"http://www.foxnews.com/politics/2017/11/23/congressional-russia-probes-likely-to-head-into-2018.html",
 			"http://www.foxnews.com/politics/2017/11/23/trump-visits-coast-guard-station-in-florida-touts-own-accomplishments-in-thanksgiving-tweets.html",
 			"http://www.foxnews.com/politics/2017/11/23/during-thanksgiving-politics-takes-back-seat-polls.html",
 			"http://www.foxnews.com/health/2017/11/23/abortion-rates-in-us-hit-historic-low-cdc-report-finds.html",
 			"http://www.foxnews.com/us/2017/11/23/north-dakota-university-walks-back-email-urging-opposition-to-gop-tax-legislation.html",
 			"http://www.foxnews.com/politics/2017/11/23/federal-judge-blocks-texas-law-banning-barbaric-second-trimester-abortion-procedure.html",
 			"http://www.foxnews.com/opinion/2017/11/23/trump-is-right-america-and-russia-need-to-work-together-to-lower-tensions.html",
 			"http://www.foxnews.com/opinion/2017/11/23/judge-napolitano-should-government-guarantee-higher-taxes-for-your-children-in-return-for-lower-taxes-for.html",
 			"http://www.foxnews.com/politics/2017/11/22/rep-joe-barton-warned-woman-hed-tell-police-if-shared-explicit-photos-and-messages-report-says.html",
 			"http://www.foxnews.com/politics/2017/11/22/al-franken-accused-inappropriate-touching-by-two-more-women.html",
 			"http://www.foxnews.com/politics/2017/11/22/sessions-orders-review-federal-background-check-system-for-gun-buyers.html",
 			"http://www.foxnews.com/politics/2017/11/22/john-conyers-has-no-plans-to-resign-amid-sexual-harassment-scandal-lawyer-says.html",
 			"http://www.foxnews.com/politics/2017/11/22/presenting-your-2017-turkey-bowl-winners.html",
 			"http://www.foxnews.com/politics/2017/11/22/education-department-considers-narrowing-civil-rights-work.html",
 			"http://www.foxnews.com/politics/2017/11/22/lovers-inadvertently-featured-on-rob-gronkowski-erotica-book-lose-lawsuit.html",
 			"http://www.foxnews.com/politics/2017/11/22/doug-jones-hammers-roy-moore-over-sexual-misconduct-allegations-in-new-ad.html",
 			"http://www.foxnews.com/politics/2017/11/22/republican-rep-joe-barton-apologizes-after-lewd-photo-surfaces.html",
 			"http://www.foxnews.com/opinion/2017/11/22/liberals-throw-bill-clinton-under-bus-to-cover-for-25-years-taking-wrong-stand-on-sexual-abuse.html",
 			"http://www.foxnews.com/politics/2017/11/22/rand-pauls-wife-speaks-out-on-attack-says-media-victimized-her-husband.html",
 			"http://www.foxnews.com/opinion/2017/11/22/exposing-sexual-misconduct-is-necessary-to-change-horrible-behavior-not-to-score-political-points.html",
 			"http://www.foxnews.com/politics/2017/11/22/john-conyers-hometown-newspaper-calls-for-resignation-after-public-betrayal.html",
 			"http://www.foxnews.com/entertainment/2017/11/22/reading-rainbow-host-levar-burton-mistaken-for-lavar-ball-on-twitter.html",
 			"http://www.foxnews.com/politics/2017/11/22/homeless-people-defecating-on-la-streets-fuels-horror-hepatitis-outbreak-as-city-faulted.html",
 			"http://www.foxnews.com/politics/2017/11/22/violence-against-rohingya-muslims-in-burma-is-ethnic-cleansing-us-declares.html",
 			"http://www.foxnews.com/politics/2017/11/22/alabama-senate-hopeful-doug-jones-defended-man-with-ties-to-kkk-holocaust-deniers.html",
 			"http://www.foxnews.com/politics/2017/11/22/storm-sexual-harassment-claims-engulfs-capitol-hill.html",
 			"http://www.foxnews.com/politics/2017/11/22/hillary-clinton-obamas-record-made-it-hard-to-run-on-agenda-change.html",
 			"http://www.foxnews.com/politics/2017/11/22/poor-mans-don-king-trump-takes-aim-at-hoops-dad-lavar-ball-as-feud-escalates.html",
 			"http://www.foxnews.com/politics/2017/11/22/trump-nfl-may-keep-teams-in-locker-rooms-during-national-anthem-next-year.html",
 			"http://www.foxnews.com/politics/2017/11/22/after-trump-remarks-alabama-senate-hopefuls-make-latest-pitches-to-voters.html",
 			"http://www.foxnews.com/politics/2017/11/22/anti-trump-sticker-sales-grow-after-texas-controversy.html",
 			"http://www.foxnews.com/politics/2017/11/22/alaskas-murkowski-says-backs-repeal-obamacare-individual-mandate.html",
 			"http://www.foxnews.com/opinion/2017/11/22/erick-erickson-this-thanksgiving-should-all-be-thankful-for-trump-know-am.html",
 			"http://www.foxnews.com/opinion/2017/11/22/newt-gingrich-trumps-historic-impact-on-federal-court-system-will-help-our-nation-prosper-for-decades-to-come.html",
 			"http://www.foxnews.com/politics/2017/11/22/american-freed-from-north-korea-by-president-carter-found-burned-to-death.html",
 			"http://www.foxnews.com/politics/2017/11/21/fusion-gps-paid-journalists-court-papers-confirm.html",
 			"http://www.foxnews.com/politics/2017/11/21/military-members-reassigned-after-having-inappropriate-contact-during-trump-s-asia-trip.html",
 			#"http://video.foxnews.com/v/5654414590001/?#sp=show-clips",
 			"http://www.foxnews.com/politics/2017/11/21/fbi-investigating-democratic-rep-over-payments-to-primary-challenger.html",
 			"http://www.foxnews.com/politics/2017/11/21/ethics-panel-probes-conyers-allegations-as-dem-leaders-call-claims-disturbing.html",
 			"http://www.foxnews.com/opinion/2017/11/21/it-s-time-for-congressional-hispanic-caucus-to-realize-that-being-latino-is-not-partisan-issue.html",
 			"http://www.foxnews.com/politics/2017/11/21/trump-plays-down-roy-moore-allegations-blasts-liberal-rival-in-alabama-race.html",
 			"http://www.foxnews.com/tech/2017/11/21/how-fccs-move-on-net-neutrality-could-impact-consumers.html",
 			"http://www.foxnews.com/opinion/2017/11/21/trump-is-not-crazy-despite-claims-some-mental-health-professionals.html",
 			"http://www.foxnews.com/politics/2017/11/21/us-slaps-new-sanctions-on-north-korea-after-designating-it-sponsor-terror.html",
 			"http://www.foxnews.com/politics/2017/11/21/judge-grants-manafort-thanksgiving-travel-but-no-boozing.html",
 			"http://www.foxnews.com/politics/2017/11/21/trump-pardons-turkey-look-at-white-houses-thanksgiving-tradition.html",
 			"http://www.foxnews.com/politics/2017/11/21/doj-moves-to-strip-citizenship-for-immigrant-child-sex-abusers.html",
 			"http://www.foxnews.com/politics/2017/11/21/trump-pardons-thanksgiving-turkeys-drumstick-has-bright-future.html",
 			"http://www.foxnews.com/politics/2017/11/21/fcc-chairman-moves-to-dismantle-obama-net-neutrality-rules.html",
 			"http://www.foxnews.com/politics/2017/11/21/melania-trump-son-barron-receive-white-house-christmas-tree.html",
 			"http://www.foxnews.com/opinion/2017/11/21/newt-gingrich-house-and-senate-gop-must-stay-united-to-enact-tax-cuts.html",
 			"http://www.foxnews.com/politics/2017/11/21/white-house-trump-and-putin-spoke-by-phone-syria-on-agenda.html",
 			"http://www.foxnews.com/politics/2017/11/21/conyers-admits-settlement-after-report-on-sexual-conduct-with-ex-staffers-but-denies-allegations.html",
 			"http://www.foxnews.com/opinion/2017/11/21/gregg-jarrett-roy-moore-is-not-fit-to-serve-in-us-senate-and-voters-should-reject-him.html",
 			"http://www.foxnews.com/politics/2017/11/21/roy-moore-allegations-leave-alabama-pastors-divided-as-election-looms.html",
 			"http://www.foxnews.com/us/2017/11/21/bikini-baristas-turn-men-into-harvey-weinsteins-washington-city-claims.html",
 			"http://www.foxnews.com/politics/2017/11/21/al-frankens-resignation-sought-by-prominent-liberal-groups-as-new-claims-emerge.html",
 			"http://www.foxnews.com/world/2017/11/21/china-jails-prominent-human-rights-lawyer-for-2-years-for-inciting-subversion.html",
 			"http://www.foxnews.com/us/2017/11/21/virginia-calls-on-limited-crowd-size-bans-guns-at-robert-e-lee-statue.html",
 			"http://www.foxnews.com/politics/2017/11/21/charlie-rose-al-franken-and-roy-moore-harassment-allegations-continue.html",
 			"http://www.foxnews.com/opinion/2017/11/21/juan-williams-democrats-and-politics-impeaching-trump.html",
 			"http://www.foxnews.com/opinion/2017/11/21/common-ground-is-pretty-barren-right-now-in-america-except-at-buzzys.html",
 			"http://www.foxnews.com/opinion/2017/11/21/hey-kirsten-gillibrand-lot-us-knew-what-bill-clinton-did-was-wrong-back-in-1990s.html",
 			"http://www.foxnews.com/opinion/2017/11/21/marc-thiessen-yes-clintons-should-be-investigated.html",
 			"http://www.foxnews.com/politics/2017/11/21/trump-crackdown-on-sanctuary-cities-permanently-blocked-by-federal-judge.html",
 			"http://www.foxnews.com/politics/2017/11/20/us-general-says-nuclear-launch-order-can-be-refused-sparking-debate.html",
 			"http://www.foxnews.com/politics/2017/11/20/trump-order-on-sanctuary-cities-permanently-blocked-by-federal-judge.html",
 			"http://www.foxnews.com/politics/2017/11/20/exclusive-lawmakers-call-on-trump-administration-to-outlaw-muslim-brotherhood-with-new-strategy.html",
 			"http://www.foxnews.com/politics/2017/11/20/trump-administration-ends-protected-status-for-haitians-living-in-us-after-quake.html",
 			"http://www.foxnews.com/politics/2017/11/20/trumps-foundation-stepped-up-2016-giving-amid-campaign-scrutiny.html",
 			"http://www.foxnews.com/politics/2017/11/20/from-trump-to-clinton-how-us-presidents-have-dealt-with-north-korea.html",
 			"http://www.foxnews.com/opinion/2017/11/20/hillary-is-toast-scandals-finally-catch-up-with-clintons.html",
 			"http://www.foxnews.com/politics/2017/11/20/lois-lerner-wants-irs-testimony-sealed-forever-fearing-death-threats.html",
 			"http://www.foxnews.com/us/2017/11/20/nc-fire-department-loses-funds-over-confederate-flag.html",
 			"http://www.foxnews.com/politics/2017/11/20/trumps-nicknames-for-rivals-from-rocket-man-to-crooked-hillary.html",
 			"http://www.foxnews.com/politics/2017/11/20/al-franken-hit-with-groping-allegation-from-second-woman.html",
 			"http://www.foxnews.com/politics/2017/11/20/race-for-2020-democratic-nomination-already-getting-started-in-new-hampshire.html",
 			"http://www.foxnews.com/politics/2017/11/20/trump-hits-raiders-marshawn-lynch-for-standing-only-for-mexican-anthem-suggests-suspension.html",
 			"http://www.foxnews.com/politics/2017/11/20/steve-bannon-gillibrand-s-clinton-criticism-earthquake-in-democratic-party.html",
 			"http://www.foxnews.com/opinion/2017/11/20/elephant-trophies-seriously-this-is-what-washington-is-spending-its-time-on.html",
 			"http://www.foxnews.com/opinion/2017/11/20/trump-should-welcome-zimbabwes-mugabe-ouster-as-opportunity-for-human-rights.html",
 			"http://www.foxnews.com/politics/2017/11/19/trump-reignites-feud-with-flake-predicts-hell-vote-no-on-tax-cuts.html",
 			"http://www.foxnews.com/opinion/2017/11/19/does-your-gas-and-electricity-cost-too-much-can-thank-liberals-for-that.html",
 			"http://www.foxnews.com/politics/2017/11/19/franken-reportedly-wont-resign-amid-more-congressional-calls-to-deal-with-allegations-against-him-and-roy-moore.html",
 			"http://www.foxnews.com/world/2017/11/19/us-nuclear-general-says-would-resist-illegal-trump-strike-order.html",
 			"http://www.foxnews.com/politics/2017/11/19/trump-dunks-on-ucla-stars-controversial-father-says-should-have-left-players-in-jail.html",
 			"http://www.foxnews.com/politics/2017/11/19/mnuchin-denies-tax-plans-favor-big-biz-says-bond-villain-comparison-compliment.html",
 			"http://www.foxnews.com/opinion/2017/11/19/health-care-plan-from-2000-years-ago-could-help-america-today.html",
 			"http://www.foxnews.com/politics/2017/11/19/zimbabwes-mugabe-army-commander-to-negotiate-leaders-exit.html",
 			"http://www.foxnews.com/politics/2017/11/19/community-organizer-elected-new-orleans-first-woman-mayor.html",
 			"http://www.foxnews.com/politics/2017/11/18/ex-dmv-worker-new-york-gov-cuomo-ignored-sex-assault-claims.html",
 			"http://www.foxnews.com/politics/2017/11/18/jeff-flake-gop-is-toast-if-it-becomes-party-trump-moore.html",
 			"http://www.foxnews.com/politics/2017/11/18/alabama-democrat-doug-jones-denies-being-ultra-liberal-says-opposes-trumps-border-wall.html",
 			"http://www.foxnews.com/politics/2017/11/18/palestinians-vow-to-cut-off-israeli-peace-talks-if-trump-closes-groups-washington-post.html",
 			"http://www.foxnews.com/politics/2017/11/18/congress-has-paid-nearly-1-million-in-settlements-after-workplace-complaints-this-year.html",
 			"http://www.foxnews.com/opinion/2017/11/18/moore-franken-creepy-biden-and-other-horrendous-media-fiascos.html",
 			"http://www.foxnews.com/politics/2017/11/18/gop-official-in-nh-urges-bill-clinton-s-name-be-dropped-from-state-democratic-dinner.html",
 			"http://www.foxnews.com/us/2017/11/18/wisconsin-bill-seeks-to-lower-drinking-age-to-19.html",
 			"http://www.foxnews.com/opinion/2017/11/18/dear-taylor-swift-thanks-for-not-telling-me-about-your-politics.html",
 			"http://www.foxnews.com/politics/2017/11/17/sessions-jokes-about-russia-probe-at-federalist-society-event.html",
 			"http://www.foxnews.com/politics/2017/11/17/kushner-told-trump-campaign-staff-to-avoid-meeting-foreigners-lawyer-claims.html",
 			"http://www.foxnews.com/politics/2017/11/17/trump-holds-off-reversing-ban-on-elephant-trophy-imports.html",
 			"http://www.foxnews.com/politics/2017/11/17/clinton-aide-false-comparison-to-equate-bill-with-weinstein-moore.html",
 			"http://www.foxnews.com/politics/2017/11/17/alabama-gov-kay-ivey-to-vote-for-roy-moore-in-senate-race-despite-sex-allegations.html",
 			"http://www.foxnews.com/politics/2017/11/17/liberal-views-roy-moores-democratic-rival-could-pose-pitfall-amid-scandal.html",
 			"http://www.foxnews.com/politics/2017/11/17/cynics-history-politicized-sex-scandals.html",
 			"http://www.foxnews.com/opinion/2017/11/17/hey-al-franken-no-joke-need-to-resign.html",
 			"http://www.foxnews.com/politics/2017/11/17/senate-ethics-committee-could-soon-be-busy-with-franken-menendez-heres-what-it-does.html",
 			"http://www.foxnews.com/opinion/2017/11/17/preventive-war-with-north-korea-would-be-total-hell-heres-why.html",
 			"http://www.foxnews.com/politics/2017/11/17/hillary-clinton-questions-legitimacy-trumps-victory-in-2016-election.html",
 			"http://www.foxnews.com/politics/2017/11/17/if-roy-moore-is-expelled-from-senate-hed-be-first-since-civil-war-era.html",
 			"http://www.foxnews.com/politics/2017/11/17/japan-bolstering-defenses-against-north-korea-threat-abe-says.html",
 			"http://www.foxnews.com/us/2017/11/17/rev-jesse-jackson-reveals-parkinsons-disease-diagnosis.html",
 			"http://www.foxnews.com/politics/2017/11/17/as-roy-moore-battles-accusations-wife-kayla-emerges-as-top-defender.html",
 			"http://www.foxnews.com/world/2017/11/17/tillerson-calls-on-zimbabwe-to-return-to-civilian-rule-following-military-takeover.html",
 			"http://www.foxnews.com/entertainment/2017/11/17/al-franken-mocked-by-late-night-hosts-for-sexual-misconduct-allegations.html",
 			"http://www.foxnews.com/politics/2017/11/17/jared-kushners-ties-to-white-house-link-to-russia-investigation.html",
 			]
csv_file = open("fox_articles.csv", "w", newline = '')
writer = csv.writer(csv_file)


#base_page = urllib.request.urlopen("http://www.foxnews.com/politics.html")
#base_soup = BeautifulSoup(base_page, 'html.parser')
#h2_tag_list = base_soup.find_all("h2", class_ = "title")
#print(len(h2_tag_list))
#for i in np.arange(1,len(h2_tag_list)):
#	print(h2_tag_list[i].contents[1]["href"]) 

for article_url in url_list: 
	article_page = urllib.request.urlopen(article_url) 
	article_soup = BeautifulSoup(article_page, "html.parser")
	article_author = article_soup.find("meta", attrs = {"name": "dc.creator"})["content"]
	article_title = article_soup.find("meta", attrs = {"name":"dc.title"})["content"]
	article_time = article_soup.find("meta", attrs = {"name":"dc.date"})["content"] 
	#if ("," in article_author):
	#	comma_index = article_author.index(",") 
	#	article_author = article_author[:comma_index]
	#article_author = article_author.replace(",","").replace("By","").replace("Analysis by","")
	#trimmed_time = article_time[8:]
	print("Article URL:" + article_url + "\n" + "Title:" + article_title + "\n" + 
	"Author:" + article_author + "\n" + "Time:" + article_time + "\n")
	writer.writerow([article_url, article_title, article_author, article_time])
#print(article_title, article_author, article_time)


csv_file.close()

