from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelos.cliente import Cliente
from fastapi import HTTPException


class ClienteRepositorio:
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
        self.db = banco_de_dados

    async def listar_clientes(self) -> list[Cliente]:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, email, telefone FROM clientes")
            linhas = cursor.fetchall()
            clientes = [Cliente(id_ = linha[0], nome = linha[1], email = linha[2], telefone = linha[3]) for linha in linhas]
            return clientes

    async def obter_cliente(self, cliente_id: int) -> Cliente:
      with self.db.conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute("SELECT id, nome, email, telefone FROM clientes WHERE id = ?", (cliente_id,))
                linha = cursor.fetchone()
                if linha:
                    return Cliente(id_ = linha[0], nome = linha[1], email = linha[2], telefone = linha[3])
                raise HTTPException(status_code=404, detail="Cliente não encontrado")