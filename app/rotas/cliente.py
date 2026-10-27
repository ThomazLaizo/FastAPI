from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Cliente

router = APIRouter(
    prefix = "/clientes"
)

CLIENTES_LIST = [Cliente(id_ = 1, nome = "Thomaz", email = "thomazlaizo@gmail.com", telefone = "11951349043"),
                Cliente(id_ = 2, nome = "Isabella", email = "isabellacosta@gmail.com", telefone = "11381920568"),
                Cliente(id_ = 3, nome = "Mikael", email = "mikael2009@gmail.com", telefone = "12859203980")]

@router.get("/", response_model = list[Cliente])
async def listar_clientes():
    return CLIENTES_LIST

@router.get("/{cliente_id}", response_model = Cliente)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENTES_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")