# basic_agent.py
# Requer: pip install web3 requests

from web3 import Web3
import json
import time

# Config (substitua com sua testnet)
RPC_URL = "https://sepolia.base.org"  # Exemplo Base Sepolia
PRIVATE_KEY = "SUA_PRIVATE_KEY_AQUI_NUNCA_COMMIT"
CONTRACT_ADDRESS = "0x... (após deploy)"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

# ABI mínima (copie do compilado)
ABI = [...]  # Cole o ABI gerado pelo Remix/compilador

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)


def feed_energy(token_id: int, amount: int = 200_000):
    tx = contract.functions.feedEnergy(token_id, amount).build_transaction(
        {
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gas": 200000,
            "gasPrice": w3.to_wei("0.1", "gwei"),
        }
    )
    signed = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(f"Energia alimentada: {tx_hash.hex()}")


# Loop simples de "vida" do agente
token_id = 0  # Seu primeiro agente
while True:
    energy, active = contract.functions.getAgentStatus(token_id).call()
    print(f"Agente {token_id} | Energia: {energy} | Ativo: {active}")

    if not active:
        print("Alimentando energia...")
        feed_energy(token_id)

    # Simula ação
    if active:
        data = b"acao_simulada_" + str(time.time()).encode()
        tx = contract.functions.performAction(token_id, data).build_transaction({...})  # similar acima
        # Envie tx...

    time.sleep(60)  # 1 min
