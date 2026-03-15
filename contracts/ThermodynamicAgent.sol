// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ThermodynamicAgent is ERC721, Ownable {
    uint256 private _nextTokenId;
    mapping(uint256 => uint256) public accumulatedEnergy; // Energia dissipada (unidades virtuais)
    uint256 public constant MIN_ENERGY_THRESHOLD = 100_000; // Threshold para ações
    uint256 public energyPerAction = 50_000; // Custo base por ação simples

    event EnergySpent(uint256 indexed tokenId, uint256 amount);
    event ActionPerformed(uint256 indexed tokenId, bytes data);

    constructor() ERC721("HeliosAgent", "HLSA") Ownable(msg.sender) {}

    // Mint um novo agente (NFT) com energia inicial zero
    function mintAgent(address to) external onlyOwner {
        uint256 tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        accumulatedEnergy[tokenId] = 0; // Começa sem energia → precisa "alimentar"
    }

    // Função para "alimentar" energia (simula dissipação, pode vir de PoW/PoE futuro)
    function feedEnergy(uint256 tokenId, uint256 amount) external {
        require(_ownerOf(tokenId) == msg.sender, "Not owner");
        accumulatedEnergy[tokenId] += amount;
        emit EnergySpent(tokenId, amount);
    }

    // Ação custosa: só executa se tiver energia suficiente
    function performAction(uint256 tokenId, bytes calldata data) external {
        require(_ownerOf(tokenId) == msg.sender, "Not owner");
        require(accumulatedEnergy[tokenId] >= MIN_ENERGY_THRESHOLD, "Insufficient energy - agent hibernating");

        // Deduz custo
        accumulatedEnergy[tokenId] -= energyPerAction;
        emit ActionPerformed(tokenId, data);

        // Aqui futuro: call para LLM off-chain, store hash de memória, etc.
    }

    // View: status termodinâmico
    function getAgentStatus(uint256 tokenId) external view returns (uint256 energy, bool active) {
        energy = accumulatedEnergy[tokenId];
        active = energy >= MIN_ENERGY_THRESHOLD;
    }
}
