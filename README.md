#FreeGPT-Py
is a ChatGPT API without any limit and API Key and this is completely free

#How to Run
1. Clone this repo
```
git clone https://github.com/jokosantosi/FreeGPT-Py.git
```
2. Change to workdir
```
cd FreeGPT-Py
```
3. Install Depedency
```
pip install -r requirement.txt
```
4. Run the App
```
python3 app.py
```
5. Run the Example
```
python3 example.py
```

or you can using a docker
1. Clone this repo
```
git clone https://github.com/jokosantosi/FreeGPT-Py.git
```
2. Change to workdir
```
cd FreeGPT-Py
```
3. Build a image Docker
```
docker build -t jokosantosi/freegpt-py .
```
4. Run the Docker image
```
docker run -p 8000:8000 jokosantosi/freegpt-py
```