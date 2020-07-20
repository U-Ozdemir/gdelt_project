
# What is the GDELT DB?
- GDELT monitors tens of thousands of news websites around the globe and automatically extracts entities, themes, quotes, sentiment, images, and events present in articles posted on these sites. Article metadata is archived at 15-minute time intervals 24 hours a day.
- In addition to analyzing text content from monitored sites, GDELT transcribes video and audio broadcasts from monitored sites, and translates them from 65 different languages into English text. Further, the database currently contains over a quarter of a billion unique event references and adds over three quarters of a trillion sentiment assessments, 1.5 billion location references, and 70 billion images on a yearly basis, made possible by the overall global increase in the capacity to store, communicate, and compute information. 
- GDELT was designed to serve as a “passive crowdsourcing” platform (Leetaru, 2011), providing a dashboard that keeps a pulse on global events and news reporting by assessing linkages between communication processes and societal-scale physical behavior. GDELT’s main database can be divided into three interrelated sub-datasets: the Global Knowledge Graph (GKG), Events, and Special Collections.

GDELT website: https://www.gdeltproject.org

## GKG (Global Knowledge Graph)
- GDELT’s Global Knowledge Graph (GKG) serves as the main database for storing metadata extracted from print, broadcast, and news web portals. Once a news report appears online, GDELT scrapes and computationally analyzes its content by relying on various image recognition and natural language processing techniques.
- On each obtained textual news report, GDELT employs more than 40 content-analytic dictionaries to extract over 2,230 identified emotions, topics, themes, and named entities. These dictionary-based content analysis pipelines draw on a preselected list of keywords (i.e., the dictionary) that are assumed to reflect a construct of interest. The respective goal of these dictionaries is to measure “the rate at which keywords appear in a text to classify a document into categories or to measure the extent to which documents belong to particular categories”

## Events
- The main purpose of GDELT’s EVENT database is to store geopolitical events that are recorded in news articles. To computationally extract a mentioned event from a news report, GDELT relies on the CAMEO code- book (Gerner, et al., 2002). CAMEO consists of manually predefined and extensively validated verb phrases to detect up to twenty different types of event occurrences concerned with international and domes- tic conflict, ranging from diplomatic event categories (e.g., "APPEAL", or "AGREE") to conflict categories (e.g., "REDUCE RELATIONS", or "USE CONVENTIONAL FORCE"). Each event type is then attributed one of the twenty EventRootCodes that specify its type, as well as a more de- tailed EventCode that specify the event type in a more fine-grained fash- ion. For example, EventRootCode 14 reflects any PROTEST event, whereas EventRootCode 1422 reflects a hunger strike for policy change.
- Finally, all event types are ultimately organized under four primary classifications: Verbal Cooperation, Material Cooperation, Verbal Conflict, and Material Conflict. This Quadclass variable supports the analysis of event types at the highest level of aggregation and is less prone to GDELT’s automated coding errors in the underlying events data (Wang et al., 2016), due to the higher levels of aggregation in mapping event types to symbols.
- Beyond assessing the event type, CAMEO also extracts the two main actors that characterize an event. Accordingly, CAMEO assesses actions where actor 1 performs a respective action (the event type) on actor 2. Hence, ad- ditional information about these actors is provided, for example, whether the actors belong to a certain country, ethnic/religious group, or are part of a governmental, military, or educational institution. 

## Special Collections
- GDELT applies its automated GKG content-analytic pipeline on a selection of “special collections” spanning American television, academic literature discussing the Middle East and Africa, human rights reports, and historical American books.

## Access to GDELT
- GDELT’s data has been integrated into Google BigQuery, a web service designed to store and provide access to large-scale datasets through standard SQL queries.
(https://console.cloud.google.com/bigquery?project=gdelt-bq&redirect_from_classic=true&p=gdelt-bq&d=covid19&t=onlinenewsgeo&page=table)
- While Google BigQuery provides unprecedented querying speed, it is a fee-based service that can quickly become expensive with increasingly data-heavy operations. Likewise, relying on independently developed scripts necessitates knowledge and details about their execution and the specific purpose, preprocessing, and analysis steps undertaken to obtain the data from GDELT.

## use cases:
- ???


## Three primary data streams are created:
- one codifying physical activities around the world in over 300 categories,
- one recording the people, places, organizations, millions of themes and thousands of emotions underlying those events and their interconnections and 
- one codifying the visual narratives of the world's news imagery.

## Why is GDELT created?
- GDELT is designed to help support new theories and descriptive understandings of the behaviors and driving forces of global-scale social systems from the micro-level of the individual through the macro-level of the entire planet by offering realtime synthesis of global societal-scale behavior into a rich quantitative database allowing realtime monitoring and analytical exploration of those trends.
- By quantitatively codifying human society's events, dreams and fears, can we map happiness and conflict, provide insight to vulnerable populations and even potentially forecast global conflict in ways that allow us as a society to come together to deescalate tensions, counter extremism, and break down cultural barriers? 


## What are the sources they extract from?
- from hundreds of thousands of global media outlets to special collections like 215 years of digitized books, 21 billion words of academic literature spanning 70 years, human rights archives and even saturation processing of the raw closed captioning stream of almost 100 television stations across the US in collaboration with the Internet Archive's Television News Archive.
- Finally, also in collaboration with the Internet Archive, the Archive captures nearly all worldwide online news coverage monitored by GDELT each day into its permanent archive to ensure its availability for future generations even in the face of repressive forces that continue to erode press freedoms around the world.

## How reliable are these sources?
- GDELT extracts from new articles, so I assume if the articles are biased or of bad quality, then so is the source. 

# Questions:
1. What kind of storage is GDELT? (data lake etc.)
    - ???
2. How can you connect to this DB?
    - There is a python package called gdeltPyR, but it is outdated (doesn't work for me)
    - Use gdelt python package, see code below this document.

3. How do you get the data out of this DB?
    - google BigQuery platform (the API calls are limited, after certain amount need to pay), it uses SQL queries


4. How do they get their data?
    - tabari software
    - The data are based on news reports from a variety of international news sources coded using the Tabari system for events and additional software for location and tone. (Read abstract: http://data.gdeltproject.org/documentation/ISA.2013.GDELT.pdf)

5. How do they process their data?
    - ???

6. Which data sources do they have?
    - GDELT’s Global Knowledge Graph (GKG): serves as the main database for storing metadata extracted from print, broadcast, and news web portals. Once a news report appears online, GDELT scrapes and computationally analyzes its content by relying on various image recognition and natural language processing techniques. (paper: iCoRe: The GDELT Interface for the Advancement of Communication Research)

    - mentions
    - event database: They use Tabari software code event categories. The software reads the keywords and puts them in the associates category. They use dictionairies for this.



## Tabari software:
- The Tabari system has very extensive open-source dictionaries for the identification of political actors.
- Location and tone: The raw Tabari output files are geolocated by a post-processing system. The first system
takes the verb and actor word sentence offsets (that is, the identity of the word in the sentence
that was the start of each actor and verb mention) and converts them back into their locations
in the original article. This is then cross-walked against the list of all geographic locations
found in the text, and the closest location to each of the actor and verb mentions is assigned
to it.
- The “tone” of each article is measured using the tonal algorithm from Shook et al. [2012].

## Pipeline:
- Pre-processing: First the article is cleaned up, any textual URLs, phone numbers, email addresses, non-ASCII characters, and other material is removed.
> How is it cleaned up?

> Which other material is removed?
- The article is then run through full-text geocoding that automatically identifies and disambiguates all geographic references in the text, resolving them to their centroid lat/long coordinates, using Leetaru (2012).
- The article then goes through a preprocessing pipeline that creates four versions of the text:
    - RAW: The text is kept as-is with no change.
    - CITY TOCOUNTRY NOPERSON: All mentions of cities and other geographic landmarks are replaced with the name of the country the city/landmark is lo- cated in. Thus, “Soldiers marched in Cairo today” will be replaced with “Soldiers marched in Egypt today.” While the Tabari .actors dictionary contains major city names, it contains only the largest cities, and a mention of soldiers attacking a small village will cause Tabari not to find a country affiliation for the victim ac- tors, while this interpolation will replace that small village with its corresponding country name, causing Tabari to find a match. Person names remain as-is.
    - PERSONTOCOUNTRY : For each person’s name found in the text, the closest location to the first mention of the person’s name is then assigned to that person and all mentions of the person’s name are then replaced with that location’s coun- try name. Thus, a mention of “Egyptian Minister of Foreign Affairs Mohamed Orabi attended the summit yesterday. While he was there, Orabi pledged support for...” the second sentence would be rewritten to “While he was there, Egypt pledged support for. . . ” This is essentially a special geographically-centered form of entity dereferencing. This version dramatically improves matching of diplo- matic events in which a political leader is referred to throughout an article, but the leader is not significant enough to have his or her own entry in the Tabari .actors list. In addition, all mentions of cities and other geographic landmarks are replaced with “CityName, CountryName.”
    - FULL: In this version, each person name is associated with its corresponding location as in PERSONTOCOUNTRY, but all mentions of the person’s name are replaced with the form of “PersonName of CountryName” (adding the coun- try name and inserting the word “of” between the person’s name and the country name). All mentions of cities or landmarks are converted to the format “City- Name, CountryName.”



# Sources:
- CAMEO CODES: http://data.gdeltproject.org/documentation/CAMEO.Manual.1.1b3.pdf
- all GDELT files: http://data.gdeltproject.org/events/
- GDELT author paper(2013): http://data.gdeltproject.org/documentation/ISA.2013.GDELT.pdf
- python package: https://github.com/linwoodc3/gdeltPyR/blob/master/examples/gdeltPyR_basic_use.md
- GDELT summary: https://api.gdeltproject.org/api/v2/summary/summary?d=web&t=summary&k=%22coronavirus%22+%22protest%22&ts=custom&sdt=20200101000000&edt=20200714235959&svt=zoom&stc=yes&sta=list&c=1
- master file list: http://data.gdeltproject.org/gdeltv2/masterfilelist.txt
- paper 2019 (pdf in github): iCoRe: The GDELT Interface for the Advancement of Communication Research
- UK government on GDELT: https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/methodologies/explorationoftheglobaldatabaseofeventslanguageandtonegdeltwithspecificapplicationtodisasterreporting

# Code to pull data from GDELT

With code below you can pull some data from the GDELT database. You might need to do **pip3 install gdelt** if it cannot find the package.

In the table you can pull from 3 sources: events, gkg, mentions.



```
import gdelt

gd2 = gdelt.gdelt(version=2)

results = gd2.Search(date=['2020 Jul 16'],  table='events', output='df', coverage=False)

print(results.info())

```