from fastapi import FastAPI
from router.qr_code import router_qr
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="qr-code")


origins = [
    "https://qr-code-front-three.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=[ "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "accept","Content-Type" ]
)

app.include_router(router_qr)


