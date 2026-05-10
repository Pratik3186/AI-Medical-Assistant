from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.middlewares.exceptions_handlers import catch_exceptions_middleware
from server.modules.routes.upload_pdf import router as upload_router
from server.modules.routes.ask_question import router as ask_router


app = FastAPI(title="Medical Assistant API",description="API for AI Medical Assistant Chatbot")

@app.get("/")
def home():
    return {
        "message": "Medical Assistant API is running"
    }

#CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

#middleware exceptions handlers 

app.middleware("http")(catch_exceptions_middleware)


#routers

#1. upload pdfs document
app.include_router(upload_router)

#2. asking query
app.include_router(ask_router)


