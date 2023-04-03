FROM python:3.8
# we specify image
WORKDIR /usr/src/app
#we cange our directory and go to app folder - tas ir standarts izmantot app folderi
COPY requirements.txt .
#atrodas saja folderi
COPY run.py .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","run.py"]
