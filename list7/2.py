# Szymon Fica 337307
# list 7 task 2

import requests
import time
import threading

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

refresh_time = 5

def main_f(url):
    website_text = requests.get(url, allow_redirects=False, timeout=10).text
    time.sleep(refresh_time)
    new_website_text = requests.get(url, allow_redirects=False, timeout=10).text
    if new_website_text == website_text:
        print("Website: " + str(url) + " haven't changed.\n")
    else:
        dif = find_change(website_text, new_website_text)
        print("Website: " + str(url) + " have changed.\n")
        print("Previous version: ")
        print(website_text[dif[0]:dif[1]] + "\n")
        print("New version: ")
        print(new_website_text[dif[0]:dif[2]] + "\n")

while True:
    threads = []
    for i in websites:
        t = threading.Thread(target=main_f, args=[i])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
        