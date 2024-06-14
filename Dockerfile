FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y python3-tk xvfb

# Copy application files
COPY app.py /ERIC/
COPY chat.py /ERIC/
COPY chatdata.json /ERIC/
COPY data.pth /ERIC/
COPY model.py /ERIC/
COPY nltk_preprocessing.py /ERIC/
COPY training.py /ERIC/

WORKDIR /ERIC

# Install Python dependencies
RUN pip install nltk numpy torch

# Set up Xvfb
ENV DISPLAY=:99
RUN Xvfb $DISPLAY -screen 0 1024x768x24 -ac +extension GLX +render -noreset &

# Expose the port if necessary
EXPOSE 5000

CMD ["python", "app.py"]
