import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from loguru import logger
from modules.fileworker import generate_xlsx


logger.add("data.log", rotation="100 MB", enqueue=True)
app = FastAPI()


@app.post('/create_excel', response_class=FileResponse)
async def create_excel(file: UploadFile):
    content = await file.read()
    result, name = generate_xlsx(content, file.filename)
    if result:
        headers = {'Content-Disposition': f'attachment; filename="{name}.xlsx"'}
        return FileResponse(f'{name}.xlsx', headers=headers)
    else:
        return 'example/empty.txt'


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
