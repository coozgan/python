import requests
import argparse
from bs4 import BeautifulSoup
import json
import re
from csv import writer
from colorama import Fore, Style

def main():
    parser = argparse.ArgumentParser(description="Jobstreet.sg Job Web Scraping")
    parser.add_argument('-c', '--country',
                        help="Insert the country code e.g. ph, sg, my etc., By Default it's code is SG")
    parser.add_argument('-n', '--noagency', help='Search without Agency', action='store_true')
    parser.add_argument('-k', '--keyword', help='Search Job Keyword', required=True, type=str)
    parser.add_argument('-r', '--sortbyrelevance', help='Sort by relevance, Default is sort by Date',
                        action='store_true')

    args = parser.parse_args()
    relevance = False
    agency = True
    country = 'sg'
    if args.country:
        country = args.country
    if args.sortbyrelevance:
        relevance = True
    if args.noagency:
        agency = False
    process(args.keyword, relevance, agency, country)


def process(keyword='', byrelevance=False, noAgency=True, country='sg'):
    max_page = 50  # The number of pages that we will surf
    BASE_URL = 'https://www.jobstreet.com.{}/en/job-search/{}-jobs/'.format(country, keyword)
    BASE_URL_POST_FIX = '' if byrelevance else '/?sort=createdAt'
    with open('jobstreet.csv', mode='a') as csv_file:
        csv_writer = writer(csv_file)
        header = ['URL', 'JOB TITLE', 'COMPANY']
        csv_writer.writerow(header)
        for page_number in range(1, max_page):
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
            page = requests.get(BASE_URL + str(page_number) +
                                BASE_URL_POST_FIX, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            tag = soup.find("script", text=re.compile(
                ".*window\.REDUX_STATE.*"))
            try:
                text = str(tag.contents[0])
                text = text.strip('window.REDUX_STATE = ')[:-1]
                myjson = json.loads(text)
                the_jobs = myjson['result']['jobs']
                # Job list
                for joblist in the_jobs:
                    company = joblist['companyMeta']['name']
                    if noAgency:
                        if not isAgency(str(company)):
                            job_title = joblist['jobTitle']
                            job_url = joblist['jobUrl']
                            csv_writer.writerow([job_url, job_title, company])
                    else:
                        job_title = joblist['jobTitle']
                        job_url = joblist['jobUrl']
                        csv_writer.writerow([job_url, job_title, company])
                    print(Fore.GREEN + "A Job of {} from {}".format(job_title, company))
                    print(Fore.RED)
                print(Fore.WHITE + "{:.2f}/100.00".format(100 * (page_number / max_page)))

            except:
                print("Something went wrong\n100.00/100.00 DONE")
        print(Fore.GREEN + "100.00/100.00 DONE")
        print(Style.RESET_ALL)


# Block known Agency from scraping

def isAgency(compnyName):
    blocked = ['Oaktree Consulting', 'Goldtech Resources Pte Ltd', 'JMC Talent Search Pte. Ltd.',
               'TRUST RECRUIT PTE. LTD.', 'Shell Infotech Pte Ltd', 'PeopleSearch Pte Ltd', 'Hawksford Singapore',
               'Seacare Manpower Services Pte Ltd', 'COLLABERA SEARCH PTE. LTD.', 'Xcellink Pte Ltd',
               'Inter Island Manpower Pte Ltd', 'Helius Technologies Pte Ltd', 'BGC Group (Recruitment)',
               'P-Serv Pte Ltd', 'Cadmus Resources', 'Corestaff Pte Ltd', 'Recruit Haus Pte Ltd',
               'Global Search Partners Pte Ltd', 'Mars Consulting Pte. Ltd.', 'Prestige Professions Pte Ltd',
               'ITCAN PTE. LIMITED', 'Achieve Talents Pte Ltd', 'RRECRUITER PTE. LTD.', 'Adecco Personnel',
               'Career Edge Asia Pte', 'Resource Selection Pte Ltd', 'APBA TG Human Resource Pte Ltd',
               'Kerry Consulting Pte Ltd', 'EBC CONNECT PTE. LTD.', 'Mass Power Services Pte Ltd',
               'Protemps Employment Services Pte Ltd', 'HR Business Partners International Pte Ltd',
               'Talentvis Singapore Pte Ltd', 'Talent Trader Group Pte Ltd - Engineering',
               'Talent Trader Group Pte Ltd', 'EMBER RECRUITMENT PTE. LTD', 'CVista HR Consulting Pte Ltd',
               'JOBEE PTE LTD', 'JOBEE PTE LTD', 'Softenger (Singapore`) Pte Ltd', 'Ideals Recruitment Pte Ltd',
               'Capital Human Resource Management', 'SEARCH STAFFING SERVICES PTE. LTD',
               'Masters Career Consultancy Pte Ltd', 'HPS Partners Pte Ltd', 'Source Solutions HR Pte Ltd',
               'CA SEARCH PTE LTD', 'NEXTWAVE PARTNERS PTE. LTD.', 'BGC Group Singapore', 'Page Personnel',
               'Robert Walters (S) Pte Ltd', 'Globesoft Services Pte Ltd', 'Hudson Global Resources',
               'Allegis Group Singapore Pte Ltd', 'Smart Recruitment', 'CELECTI PTE. LTD.',
               'Continental Technology Solutions Pte Ltd', 'Forte Employment Services Pte Ltd', 'SEARCH ALLY PTE. LTD.',
               'JOINTHIRE SINGAPORE PTE. LTD.', 'GMP Technologies ', '3TOP CONSULTING PTE LTD', 'RMA Contracts Pte Ltd',
               'Manfield Employment Services Pte Ltd', 'Maestro Human Resource Pte Ltd', 'GMP Technologies',
               'ScienTec Personnel', 'Search Personnel Pte Ltd', 'HTZ RESOURCES', 'MTC Staffing Pte. Ltd.',
               'Nala Employment Pte Ltd', 'Ambition Group Singapore Pte. Ltd. (SG)', 'TODAY\'S CAREER PTE. LTD.',
               'Accellion Pte Ltd', 'Allegis Group Singapore Pte Ltd', 'Integrity Partners Pte. Ltd.',
               'Robert Half International Pte Ltd', 'TempServ Pte Ltd', 'HRLinked Asia Search & Consultancy Pte. Ltd.',
               'Ad Astra Consultants Private Ltd', 'RecruitPlus Consulting Pte Ltd', 'Michael Page',
               'Integrity Partners Pte. Ltd.', 'Robert Half International', 'TempServ Pte Ltd', 'RecruitFlash Pte. Ltd',
               'Dynamic Human Capital Pte Ltd', 'The Supreme HR Advisory Pte. Ltd', 'GATEWAY SEARCH PTE LTD',
               'PRIMESTAFF MANAGEMENT SERVICES PTE LTD', 'ARYAN SOLUTIONS PTE. LTD', 'WE GOT THIS PTE. LTD',
               'Good Job Creations (Singapore) Pte Ltd', 'Reeracoen Singapore Pte Ltd', 'JAC Recruitment Pte. Ltd',
               'MCI Career Services Pte Ltd', 'EPS Consultants Pte Ltd', 'JOBSTUDIO PTE LTD',
               'Cobalt Consulting (Asia) Pte. Ltd', 'Cornerstone Global Partners', 'CTC Global Pte. Ltd',
               'People Profilers Pte Ltd', 'Quinnox Solutions Pte Ltd', 'RECRUIT EXPRESS', 'U3 Infotech Pte Ltd',
               'VOLT', 'Kelly Services (S) Pte Ltd', 'PERSOL Singapore', 'FSK Advisory Pte Ltd',
               'Pearson Frank International', 'Search Index Pte Ltd', 'JTE Recruit Pte Ltd', 'Recruitment Hub Asia',
               'JonDavidson Pte Ltd', 'Achieve Career Consultant Pte Ltd', 'Faststream Recruitment Pte Ltd',
               'Manpower Staffing Services (S) Pte Ltd', 'Hays Specialist Recruitment Pte Ltd', 'U3 Infotech Pte Ltd',
               'RecruitFirst Pte. Ltd', 'Achieve Career Consultant Pte Ltd', 'Capita Pte Ltd',
               'BGC Group (Outsourcing)', 'Avensys Consulting Pte Ltd', 'Stafflink Services Pte Ltd',
               'Optimum Solutions (S) Pte Ltd']
    for block in blocked:
        if block in compnyName:
            return True


if __name__ == '__main__':
    main()
