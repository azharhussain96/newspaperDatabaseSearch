**newspaperDatabaseSearch**

A python script that searches Chronicling America newspaper database for a keyword and tallies its 
apperance each year for all provided states.

usage: ./newspaperDatabaseSearch [startDate] [endDate] [searchWord] [state]...

The program prints to stdout but can be redirected to a file. 
The script requires the *re*, *sys*, and *requests* module.
*re* and *sys* are bundled in the standard libaries.
*requests* can be installed with `sudo pip install requests`


