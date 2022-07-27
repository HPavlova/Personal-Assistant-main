FROM python:3.10
COPY . .
RUN pip install -r requirements.txt
SHELL ["powershell", "-command"]
CMD [ "python", "Personal_assistant/main.py" ]