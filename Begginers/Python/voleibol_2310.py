num_jogadores = int(input())
total_saques = 0
total_bloqueios = 0
total_ataques = 0
total_acertos_saques = 0
total_acertos_bloqueios = 0
total_acertos_ataques = 0

while num_jogadores > 0:
      nome_jogador = input()
      tentativas = input().split()
      acertos = input().split()

      total_saques += int(tentativas[0])
      total_acertos_saques += int(acertos[0])

      total_bloqueios += int(tentativas[1])
      total_acertos_bloqueios += int(acertos[1])
                  
      total_ataques += int(tentativas[2])
      total_acertos_ataques += int(acertos[2])
                                    
      percentual_saque = (total_acertos_saques / total_saques) * 100
                                                
      percentual_bloqueio = (total_acertos_bloqueios / total_bloqueios) * 100
                                                            
      percentual_ataque = (total_acertos_ataques / total_ataques) * 100

      num_jogadores -= 1
            
print(f"Pontos de Saque: {percentual_saque:.2f} %.")
print(f"Pontos de Bloqueio: {percentual_bloqueio:.2f} %.")
print(f"Pontos de Ataque: {percentual_ataque:.2f} %.")
