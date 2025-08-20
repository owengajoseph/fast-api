from fastapi import FastAPI


app = FastAPI()


@app.get('/ blog')
def blog():
    return "creating"
