# Check Info Collector
## About
Project is being designed to collect information from multiple checks and output to an excel file.

## Steps
1. Pass in picture of check
2. Image pre-processing (if needed)
3. OCR extraction
4. Pass words to approximate string matching algorithm to compare with common names in a database
5. extract the amount from words
6. Add columns to dictionary and output final result to excel file