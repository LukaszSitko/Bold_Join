# Bold_Join

Script allows for specimens data retrieval from BOLD, using its Public API.

Retrieved data needs to contain following information, which were set as thresholds (user can modify required values in the source code - please refer to modify.txt (will be available soon) file for more information): 
- Taxonomy 
- BIN (Barcode Index Number) 
- Country of collection
- Collectors information 
- Identification information
- Geolocation: longitude and lattitude 
- Collection date (if possible)

Retrieved data is curated: 
- duplicates are removed;
- for given BIN, if specimen taxonomy is missing, results are compared with each other in order to establish taxonomic template;
- process_id values (unique to BOLD) of duplicates is appended to first result;
- only results with geolocation info are saved;
- total number of results from Bold is specified;
- total number of results, which passes thresholds is specified;

![Diagram](https://user-images.githubusercontent.com/69317662/134813923-50f61eb4-a351-4c23-9984-3593a09bf8ce.jpg)








# Usage Information:
Please run all the scripts in following order: 
  For simplified .csv output: module_1 -> module_2 -> module_3
  For .json output: module_1 -> module_2 -> module_4_parsing_json

Module 1 requires requires user input (one or more taxa of interest, separated by '|') - for example: Clitellata|Collembola.
All other modules will use output files from previous modules as their input. 

