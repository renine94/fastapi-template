FROM --platform=linux/amd64 riiid.azurecr.io/quizium-backend-b2b:base-0.0.1

COPY . /var/app

RUN python3.11 -m pip install --upgrade pip && \
    python3.11 -m pip --no-cache-dir install -r requirements/prod.txt

CMD sh -c "uvicorn src.main:app --host 0.0.0.0 --port 8000"
