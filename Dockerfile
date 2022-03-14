# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR .

# copy the dependencies file to the working directory
COPY requirements.txt .


# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY chromedriver .
COPY data_saved/domain.txt ./data_saved/domain.txt
COPY data_saved/exact_country_log.xlsx ./data_saved/exact_country_log.xlsx
COPY data_saved/log.xlsx ./data_saved/log.xlsx
COPY data_saved/new.txt ./data_saved/new.txt
COPY data_saved/url.txt ./data_saved/url.txt
COPY whois_lookup .
COPY adReported.py .
COPY exact_country_solver.py .
COPY exact_country_scrapper.py .
COPY get_domain.py .
COPY main.py .
COPY randomize_user_agent.py .
COPY reader.py .
COPY report.py .
COPY report_handsha.py .
COPY reporter.py .
COPY saver.py .
COPY scrapper.py .
COPY tester.py .



# command to run on container start
CMD [ "python", "main.py" ]