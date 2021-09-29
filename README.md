# Bold_Join

Script allows for specimens data retrieval from BOLD, using its Public API.

In order for the data to be extracted Minimum Data Threshold needs to be met by individual BOLD records. Threshold requirments: 
- Taxonomic information available (at least Phylum, Classs and Order) 
- Specified BIN (Barcode Index Number) 
- Country of collection and collection site coordinates. 

Retrieved data is curated: 
- duplicates are removed;
- for given BIN, if specimen taxonomy is missing, results are compared with each other in order to establish taxonomic template;
- process_id values (unique to BOLD)  and collectors names of duplicates are appended to first result and combined into single result;
- only results with geolocation info are saved;
- total number of results from Bold is specified;
- total number of results, which passes thresholds is specified;

![Diagram](https://user-images.githubusercontent.com/69317662/134813923-50f61eb4-a351-4c23-9984-3593a09bf8ce.jpg)




Output file is composed of following information: 
- Process_id (unique BOLD reference number)
- Institution storing
- BIN
- Taxonomic information
- Collected by
- Identification provided by
- Country
- Latitude and Longitude 
- Date


# Usage Information:
Please run all the scripts in following order: 
  - For simplified .csv output: module_1 -> module_2 -> module_3
  - For .json output: module_1 -> module_2 -> module_4_parsing_json

Module 1 requires user input (one or more taxa of interest, separated by '|') - for example: Clitellata|Collembola.
All other modules will use output files from previous modules as their input. 

# Additional Information:
Scripts were run and tested using Python 3.9.6 and use almost only build-in packages.

Required package to install:
- BeautifulSoup4; Installation instruction can be find here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

# Project information 
This project was performed as part of the EUdaphobase COST Action (CA18237) www.EUdaphobase.org.
