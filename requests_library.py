from bs4 import BeautifulSoup
import requests
import time

print('Put the skill that You are not familiar with')
unfamiliar_skill=input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #gets html text from a website
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text #Gets the text from inside span
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','') #replace removes the white space
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href'] #we need to get link from a tag in h2 tag which is present in header tag
            if unfamiliar_skill not in skills:
                with open(f'Jobs/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n") #strip removes f.extra space
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f'More Info: {more_info} \n')

                print(f'File saved: {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)