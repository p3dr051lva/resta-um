import itertools
import string
# as proximas 6 linhas sao variaveis que irao ser util mais para frente, no codigo
SPACE = ' ' * 3
PIN = ' o '
SIZE = 7
aux = 32
keys = list(itertools.product(string.digits[:7], string.ascii_lowercase[:7]))
values = []
for i in range(SIZE):
   for j in range(SIZE):
      if (i >= 2 and i <= 4) or (j >= 2 and j <= 4):
         values.append(PIN)
      else:
         values.append(SPACE)
values[(SIZE * SIZE) // 2] = '   '
print('Ola este eh o jogo resta um, o objetivo do jogo eh voce deixar apenas uma peca no tabuleiro, voce so pode mover as pecas para uma casa vazia caso '
      'o meio esteja livre, nao pode pular mais de uma casa por vez, e so pode se mover dentro do limite das casas, bom jogo!!')
#printa o tabuleiro atualizado a cada jogada                 
def print_tab(tab):
   print('''         a   b   c   d   e   f   g
       +---+---+---+---+---+---+---+
      1|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+
      2|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+
      3|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+
      4|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+
      5|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+
      6|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+
      7|%s|%s|%s|%s|%s|%s|%s|
       +---+---+---+---+---+---+---+''' % tuple(tab.values()))
# define se a jogada eh valida 
def valida_jogada(tab, i_o, j_o, i_d, j_d):
   if i_o > 7 or i_d > 7 or j_o > 7 or j_d > 7: return False
   if tab[i_o * 7 + j_o] != PIN: return False
   if tab[((i_o + i_d)//2) * 7 + (j_o + j_d)//2] != PIN: return False
   if tab[i_d * 7 + j_d] != SPACE: False
   if i_d == i_o and j_d != (j_o + 2) and j_o != (j_o - 2): return False
   elif j_d == j_o and i_d != (i_o + 2) and i_d != (i_o - 2): return False
   return True
    
   
   
# faz o loop das jogadas 
jogada=(True)
while jogada == True:
     
   print_tab(tab = dict(zip(keys, values)))
   x = input("digite a jogada (xx-xx) ex 3c-4a : ")
   z = x.split('-')
   i_o = int(z[0][0]) - 1
   j_o = ord(z[0][1]) - ord('a')
   i_d = int(z[1][0]) - 1
   j_d = ord(z[1][1]) - ord('a')
   if valida_jogada(values, i_o, j_o, i_d, j_d):
     i_m = (i_o + i_d) // 2
     j_m = (j_o + j_d) // 2
     values[i_d * 7 + j_d] = PIN
     values[i_m * 7 + j_m] = SPACE
     values[i_o * 7 + j_o] = SPACE
     aux -= 1
   else:
      print("jogada invalida!!")
# serve para quando o usuario deixar apenas uma peca no tabuleiro
if aux == 1:
   print('parabens voce conseguiu')


   

      
