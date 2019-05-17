jtitles=[]
emp=[]
loc=[]
sal=[]
summ=[]
dat=[]

# Initialize all variables for the while loop
page = 0
page_url = 'https://au.indeed.com/jobs?q=data+scientist&l=Australia&start={}'.format(page)
source = requests.get(page_url).text
soup = BeautifulSoup(source, 'lxml')

# Each page has a unique Previous and "Next button
# Except for first page has no Previous and last page has no Next button
# Loop through pages until the Next button cannot be found in the soup

# Next button for first page
next_button_text = soup.find_all('span', attrs={'class': 'np'})[0].getText()

while 'Next' in next_button_text:
    
    for jobs in soup.find_all(class_='result'):

        try:
            job_title = jobs.a.text.strip()
        except Exception as e:
            job_title = None
        jtitles.append(job_title)

        try:
            employer = jobs.span.text.strip()
        except Exception as e:
            employer = None
        emp.append(employer)

        try:
            location = jobs.find('span', class_='location').text.strip()
        except Exception as e:
            location = None
        loc.append(location)

        try:
            salary = jobs.find('span', class_='salary no-wrap').text.strip()
        except Exception as e:
            salary = None
        sal.append(salary)

        try:
            summary = jobs.find('div', class_='summary').text.strip()
        except Exception as e:
            summary = None
        summ.append(summary)

        try:
            date = jobs.find('span', class_='date').text.strip()
        except Exception as e:
            date = None
        dat.append(date)       
    
    # Update url and soup object
    page += 10
    page_url = 'https://au.indeed.com/jobs?q=data+scientist&l=Australia&start={}'.format(page)
    source = requests.get(page_url).text
    soup = BeautifulSoup(source, 'lxml')
    
    # For page two until the loop completes the Next button is the second
    # value in the find_all list
    try:    
        next_button_text = soup.find_all('span', attrs={'class': 'np'})[1].getText()
    except:
        # Need to update variable to another string to stop the while loop
        next_button_text = 'Finished'
        print('Final page of results is: ' + str(page))
        
df = pd.DataFrame({'jobtitle': jtitles,
                   'employer': emp,
                   'location': loc,
                   'salary': sal,
                   'summary': summ,
                   'date': dat})
