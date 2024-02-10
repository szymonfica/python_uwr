# Szymon Fica 337307
# list 6 task 2

import requests
import time

def find_change(A, B):
    i = 0
    while i < min(len(A), len(B))-1  and A[i] == B[i]:
        i += 1
    j, k = len(A)-1, len(B)-1
    while j >= 0 and k >= 0 and A[j] == B[k]:
        j -= 1
        k -= 1
    return (i, j, k)

websites = []
websites.append('https://www.timeanddate.com/')
websites.append('https://uwr.edu.pl/')

refresh_time = 10

while True:
    websites_text = {}
    for i in websites:
        websites_text[i] = requests.get(i, allow_redirects=False, timeout=10).text
    time.sleep(refresh_time)
    new_websites_text = {}
    for i in websites:
        new_websites_text[i] = requests.get(i, allow_redirects=False, timeout=10).text
        if new_websites_text[i] == websites_text[i]:
            print("Website: " + str(i) + " haven't changed.\n")
        else:
            dif = find_change(websites_text[i], new_websites_text[i])
            print("Website: " + str(i) + " have changed.\n")
            print("Previous version: ")
            print(websites_text[i][dif[0]:dif[1]] + "\n")
            print("New version: ")
            print(new_websites_text[i][dif[0]:dif[2]] + "\n")