import re

line_in = ' the numbers are:  650-804-0778 , (650)-(804)-0778 , ' \
          '(650)-804-0778 , 650 804 0778 , (acv) (pcb) uyth'


"""
Return the phone numbers from the line_in
"""

# print(re.findall(r'\w{3}-\w{3}-\w{4}','650-804-0778'))
#
# print(re.findall(r'\(\w{3}\)-\w{3}-\w{4}','(650)-804-0778'))
# print(re.findall(r'\(?\w{3}\)?-\w{3}-\w{4}','650-804-0778'))
# print(re.findall(r'\w{3}\D+\w{3}\D+\w{4}','650 804 0778'))
#
# print(re.findall(r'\(?\w{3}\)?\D+\(?\w{3}\)?\D+\(?\w{4}\)?',line_in))

print(re.findall(r'\(?\d{3}\)?\D+\(?\d{3}\)?\D+\(?\d{4}\)?',line_in))