from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field, PositiveInt


app = FastAPI()


class Transaction(BaseModel):
    valor: PositiveInt
    tipo: Literal["c", "d"]
    descricao: str = Field(max_length=10)


@app.post("/clientes/{client_id}/transacoes")
def create_transaction(client_id: int, transaction: Transaction):
    return {"limite": 0, "saldo": 0}


@app.get("/clientes/{client_id}/extrato")
def read_statement(client_id: int):
    return {
            "saldo": {
                      "total": 0,
                      "data_extrato": "",
                      "limite": 0
                      },
            "ultimas_transacoes": [
                {
                    "valor": 0,
                    "tipo": "c",
                    "descricao": "",
                    "realizada_em": ""
                    }
                ]
            }
