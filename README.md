**newspaperDatabaseSearch**

A python script that searches Chronicling America newspaper database for a keyword and tallies its 
apperance each year for all provided states.

usage: ./newspaperDatabaseSearch [startDate] [endDate] [searchWord] [state]...

The program prints to stdout but can be redirected to a file. 
The script requires the *re*, *sys*, and *requests* module.
*re* and *sys* are bundled in the standard libaries.
*requests* can be installed with `sudo pip install requests`

**Sample Output**

---------------------------------------------
|      Newspaper Usage of Term: drugs       | 
---------------------------------------------
|          STATE|     YEAR|          MATCHES|
---------------------------------------------
|       New York|     1890|     1292 matches|
|       New York|     1891|     1697 matches|
|       New York|     1892|     1855 matches|
|       New York|     1893|     2478 matches|
|       New York|     1894|     3427 matches|
|       New York|     1895|     1271 matches|
|       New York|     1896|     1049 matches|
|       New York|     1897|     1207 matches|
|       New York|     1898|      955 matches|
|       New York|     1899|     1032 matches|
|       New York|     1900|     1583 matches|
|       New York|     1901|     1269 matches|
|       New York|     1902|     1449 matches|
|       New York|     1903|     1890 matches|
|       New York|     1904|     2027 matches|
|       New York|     1905|     1970 matches|
---------------------------------------------
|          Texas|     1890|     1257 matches|
|          Texas|     1891|     1121 matches|
|          Texas|     1892|     1420 matches|
|          Texas|     1893|     2579 matches|
|          Texas|     1894|     2061 matches|
|          Texas|     1895|     1656 matches|
|          Texas|     1896|     1844 matches|
|          Texas|     1897|     2348 matches|
|          Texas|     1898|     1975 matches|
|          Texas|     1899|     2686 matches|
|          Texas|     1900|     2668 matches|
|          Texas|     1901|     2655 matches|
|          Texas|     1902|     2805 matches|
|          Texas|     1903|     1632 matches|
|          Texas|     1904|     1768 matches|
|          Texas|     1905|     2529 matches|
---------------------------------------------
|        Arizona|     1890|     1146 matches|
|        Arizona|     1891|     1116 matches|
|        Arizona|     1892|     1156 matches|
|        Arizona|     1893|     1146 matches|
|        Arizona|     1894|     1684 matches|
|        Arizona|     1895|     1500 matches|
|        Arizona|     1896|     1986 matches|
|        Arizona|     1897|     1667 matches|
|        Arizona|     1898|     2171 matches|
|        Arizona|     1899|     3501 matches|
|        Arizona|     1900|     2503 matches|
|        Arizona|     1901|     3128 matches|
|        Arizona|     1902|     3632 matches|
|        Arizona|     1903|     3573 matches|
|        Arizona|     1904|     3553 matches|
|        Arizona|     1905|     3715 matches|
---------------------------------------------

