FROM continuumio/miniconda3:latest

LABEL maintainer="ameen@gmail.com"

# Create app directory
WORKDIR /app
 
# Install app dependencies
COPY requirements.txt ./
 
RUN pip install -r requirements.txt
 
# Bundle app source
COPY . .
 
EXPOSE 5000

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]