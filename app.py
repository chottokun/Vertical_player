from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# カレントディレクトリを静的ファイルのルートに設定
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    import webbrowser
    url = "http://127.0.0.1:9000/window_view.html"
    webbrowser.open(url)
    uvicorn.run(app, host="127.0.0.1", port=9000)
