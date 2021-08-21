from fuzzywuzzy import fuzz
import pytesseract
import cv2

FNAMES_FILE_PATH = 'data/names-lists/firstnames.txt'
LNAMES_FILE_PATH = 'data/names-lists/lastnames.txt'
IMAGE_PATH = 'data/check1.jpg'

class CheckOCR:

    def read_names(self, filepath):
        with open(filepath) as names:
            res = [name[:-1] for name in names]
        return res

    def get_name(self, words: list, fnames: list, lnames:list):
        first_name = last_name = words[0]
        fname_found = lname_found = False
        fmax_score = lmax_score =-1
        
        # compare each word to each 
        # name in the first and last names list
        for word in words:

            if not fname_found:                 
                for fname in fnames:
                    score = fuzz.ratio(word.lower(), fname.lower())
                    if score > fmax_score:
                        fmax_score = score
                        first_name = fname
                        fmatch = word
                        if score == 100:
                            fname_found = True

            if not lname_found:
                for lname in lnames:
                    score = fuzz.ratio(word.lower(), lname.lower())
                    if score > lmax_score:
                        lmax_score = score
                        last_name = lname
                        lmatch = word
                        if score == 100:
                            lname_found = True

        print(f'''Confidence levels:\nfname matched {fmatch}~{first_name} with confidence: {fmax_score}%\nlname matched {lmatch}~{last_name} with confidence: {lmax_score}%''')
        return first_name, last_name
    
    def get_amount(self, words:list):
        specifiers = [str(i) for i in range(10)] + [',', '.', '$']
        amt = None
        max_score = -1
        for word in words:
            all_digits = True
            for c in word:
                if c not in specifiers:
                    all_digits = False
                    break
            if not all_digits: continue
            score = 1 # all chars are specifiers
            if 2 < len(word.replace('$','').replace(',', '').replace('.','')) < 7: score += 7
            if '.' in word: score += 3
            if '$' in word: score += 2
            if ',' in word: score += 1

            if score > max_score:
                max_score = score
                match = word
                amt = word.replace('$','').replace(',', '')
 
        print(f'Score {max_score} was acheived with {match} to create {amt}')
        return amt

ocr = CheckOCR()
FNAMES = ocr.read_names(FNAMES_FILE_PATH)
LNAMES = ocr.read_names(LNAMES_FILE_PATH)
# FNAMES.append('John')
# LNAMES.append('Smith')
print('+++++++++++++++ PROGRAM STARTED +++++++++++++++++++')

# Adding custom options
custom_config = r'--psm 11'
output = pytesseract.image_to_string(
    cv2.imread(IMAGE_PATH),
    config=custom_config
    )

words = output.split()
print(words)
print(ocr.get_name(words, FNAMES, LNAMES))
print(ocr.get_amount(words))