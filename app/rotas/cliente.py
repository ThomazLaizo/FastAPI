from fastapi import Depends
from typing import Annotated

from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Cliente
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio

router = APIRouter(
    prefix = "/clientes"
)

CLIENTES_LIST = [Cliente(id_ = 1, nome = "Thomaz", email = "thomazlaizo@gmail.com", telefone = "11951349043"),
                Cliente(id_ = 2, nome = "Isabella", email = "isabellacosta@gmail.com", telefone = "11381920568"),
                Cliente(id_ = 3, nome = "Mikael", email = "mikael2009@gmail.com", telefone = "12859203980")]

@router.get("/", response_model = list[Cliente])
async def listar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()

@router.get("/{cliente_id}", response_model=Cliente)
async def obter_cliente(
    cliente_id: int,
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)

    if not cliente:
        raise HTTPException(status_code = 404, detail = "Cliente Não Encontrado!")
    return cliente