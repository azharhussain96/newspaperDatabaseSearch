#!/usr/bin/python
# newspaperSearch.py
#
# python script that searches the Chronicling America historic newspaper database for a
# keyword and tallies its apperance each year for all provided states. 
# input: startDate, endDate, searchText, state(s)
# output: The script will print a table of counts to stdout
# usage: ./newspaperSearch.py [startYear] [endYear] [searchWord] [state]...
#
# Azhar Hussain, July 18, 2017

import re
import sys
import requests

def searchDatabase(startDate, endDate, searchText, stateArray):

    if len(sys.argv) >= 5:

        if startDate >= 1789 and endDate <= 1924:
            header = '{:>45}| {:>12}| {:>6}| {:>14}|'.format("Historic Newspaper Usage of " + searchText,
                                                             "STATE","YEAR","MATCHES")
            print(header)

            for state in stateArray:

                for year in range(startDate, endDate + 1):

                    url = "http://chroniclingamerica.loc.gov/search/pages/results/?state=" + state + "&date1=" + \
                          str(year) + "&date2=" + str(year) + "&proxtext=" + searchText \
                          + "&x=17&y=16&dateFilterType=yearRange&rows=20&searchType=basic"
                    page = requests.get(url)

                    line = page.text
                    matchObj = re.search('<p class="term">(.*) results', line)

                    if matchObj:
                        year = str(year)
                        matches = matchObj.group(1) + " matches"
                        result = '{:>45}| {:>12}| {:>6}| {:>14}|'.format("",state, year, matches)
                        print(result)
                    else:
                        matches = "0 matches"
                        result = '{:>45}| {:>12}| {:>6}| {:>14}|'.format("",state, year, matches)
                        print(result)

        else:
            sys.stderr.write("error: start date must be >= 1789 AND end date must be <= 1924")
    else:
        sys.stderr.write("usage: newspaperSearch.py startDate endDate searchWord state...")

stateArray = sys.argv[4:]
searchDatabase(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], stateArray)