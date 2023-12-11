FROM continuumio/miniconda3:latest
 
# Create app directory
WORKDIR /app
 
# Install app dependencies
COPY requirements.txt ./
 
RUN pip install -r requirements.txt
 
# Bundle app source
COPY . .
 
EXPOSE 5000

CMD [ "flask", "run"]