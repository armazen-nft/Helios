# Helios Whitepaper (Draft v0.1)

## Resumo
Helios propõe um modelo de IA autônoma com restrição termodinâmica explícita. Em vez de agentes com custo computacional opaco, cada ação exige consumo de energia contabilizado em ledger público, criando um sistema auditável e antifrágil.

## Problema
Sistemas autônomos atuais não incorporam, de forma nativa, limites energéticos verificáveis. Isso dificulta:
- governança de comportamento;
- previsibilidade de custo;
- contenção de agentes em cenários multiator.

## Proposta
1. **Identidade persistente via NFT** para cada agente.
2. **Saldo energético** associado ao agente no contrato.
3. **Ações condicionadas** a um limiar mínimo de energia.
4. **Integração off-chain** para cognição (LLM), mantendo trilha de auditoria on-chain.

## Hipótese central
Ao atrelar semântica de ação a custo energético observável (SPJ: semântica por joule), é possível melhorar segurança, governança e robustez de ecossistemas de IA autônoma.

## Modelo inicial (v0.1)
- Energia é incrementada por chamadas `feedEnergy`.
- Ações `performAction` reduzem energia por custo fixo.
- Estado ativo/hibernando é calculado on-chain.

## Roadmap
- **v0.1**: Contrato + agente toy + documentação base.
- **v0.2**: Métricas SPJ e memória semântica hash-linkada.
- **v0.3**: Multiagente com fronteiras energéticas e políticas adaptativas.

## Riscos e mitigação
- **Simplificação excessiva da energia** → Introduzir proxies físicos graduais.
- **Dependência off-chain** → Verificação por hashes, assinaturas e eventos.
- **Custos de gas** → Escolha de L2 de baixo custo (Base/Polygon).

## Licenciamento e comunidade
Projeto sob MIT, aberto a contribuições acadêmicas e experimentais em IA + criptoeconomia + sistemas complexos.
