'''
Hi! I'm @LocCodE and one of my friends asked me to make a simple script in Python
which may help him to work with Hunter.io website.

I started to practise programming in Python and as a result,
I want to present this non-official CLI version of Hunter.io.

All you need is to get the API-key from Hunter.io at put it into the hunter_io variable,
check the requirements.txt file, then run this script with parameters:
E.g.: -d domain.com -l 100

After that, you will get a .txt file with 100 emails for the website domain.com.

Thank you for reading and using this,
With best regards @LocCodE!
'''

import sys
import requests
from datetime import datetime
from pyhunter import PyHunter


# Checking the params -d and -l
arguments_len = len(sys.argv) - 1

if arguments_len == 4:
    if sys.argv[1] == '-d' and sys.argv[3] == '-l':
        # Do not forget to put your API-key in PyHunter()!
        hunter_api = PyHunter('')
        domain = sys.argv[2]
        limit = sys.argv[4]
        # Trying to connect to Hunter.io and get the list of emails for the given domain
        try:
            hunter_resp = hunter_api.domain_search(domain, limit=limit)
            emails_len = len(hunter_resp['emails'])
            filename_output = 'email_results_' + str(datetime.now().strftime("%H-%M-%S_%d-%m-%y")) + '.txt'
            file_output = open(filename_output, "w+")
            for x in range(emails_len):
                file_output.write(str(hunter_resp['emails'][x]['value']) + "\r\n")
            file_output.close()
        # Catching errors into the error log .txt file
        except requests.exceptions.HTTPError as e:
            filename_output = 'error_log_' + str(datetime.now().strftime("%H-%M-%S_%d-%m-%y")) + '.txt'
            file_output = open(filename_output, "w")
            file_output.write(str(e) + "\r\n")
            file_output.close()
            print('HTTP-connection error. Maybe you are out of the limit? '
                  'Or you have forgotten to put your API-key in hunter_api variable. Please check the error log.')
    else:
        print('Wrong arguments. Please recheck the example: -d domain.com -l 100')
else:
    print('Wrong or no arguments at all. Please recheck the example: -d domain.com -l 100')



