# GIFMaker
A simple GUI for Making GIF and timelapse video

## Installation

```bash
pip install -r requirements.txt
```
## Docker

1. Build the docker image
```bash
docker build -t makegif .
```
1.1. or pull the docker image from dockerhub
```bash
docker pull kaorikaori/makegif
```
2. Deploy the docker container
```bash
docker run -d -p 7860:7860 makegif 
```
3. Start the server at http://localhost:7860/

## Usage

```bash
python main.py
```