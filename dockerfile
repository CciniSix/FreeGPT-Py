FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip install asyncio aiohttp uuid fastapi 'uvicorn[standard]'
EXPOSE 8000
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0"]
