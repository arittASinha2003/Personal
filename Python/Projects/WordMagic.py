print("-"*20)
print("Welcome to word magic")
print("       - Aritta Sinha")
print("-"*20)
count = 0
name = input("Enter your name : ")
print("\n")
if name == " " or name == "":
  print("Your name can't be empty\nSorry! Closing the program... ")
else:
  for i in name:
    if i == 'a' or i == 'A':
      print("\n      A\n     A A\n    A   A\n   AAAAAAA\n  A       A\n A         A\nA           A")
    elif i == 'b' or i == 'B':
      print("\nBBBBBBB\nB     B\nB     B\nBBBBBBB\nB     B\nB     B\nBBBBBBB ")
    elif i == 'c' or i == 'C':
      print("\nCCCCCCCCC\nC\nC\nC\nC\nC\nCCCCCCCCC")
    elif i == 'd' or i == 'D':
      print("\nDDDDD\nD    D\nD     D\nD      D\nD     D\nD    D\nDDDDD")
    elif i == 'e' or i == 'E':
      print("\nEEEEEEE\nE\nE\nEEEEEEE\nE\nE\nEEEEEEE")
    elif i == 'f' or i == 'F':
      print("\nFFFFFFF\nF\nF\nFFFFFFF\nF\nF\nF")
    elif i == 'g' or i == 'G':
      print("\nGGGGGGGG\nG\nG\nG  GGGG\nG  G  G\nG  G  G\nGGGG  G")
    elif i == 'h' or i == 'H':
      print("\nH     H\nH     H\nH     H\nHHHHHHH\nH     H\nH     H\nH     H")
    elif i == 'i' or i == 'I':
      print("\nIIIIIII\n   I\n   I\n   I\n   I\n   I\nIIIIIII")
    elif i == 'j' or i == 'J':
      print("\nJJJJJJJJ\n    J\n    J\nJ   J\n J  J\n  J J\n   JJ\n    J")
    elif i == 'k' or i == 'K':
      print("\nK  K\nK K\nKK\nK\nKK\nK K\nK  K")
    elif i == 'l' or i == 'L':
      print("\nL\nL\nL\nL\nL\nL\nLLLLLLL")
    elif i == 'm' or i == 'M':
      print("\nM     M\nMM   MM\nM M M M\nM  M  M\nM     M\nM     M\nM     M")
    elif i == 'n' or i == 'N':
      print("\nN     N\nNN    N\nN N   N\nN  N  N\nN   N N\nN    NN\nN     N")
    elif i == 'o' or i == 'O':
      print("\nOOOOOOO\nO     O\nO     O\nO     O\nO     O\nOOOOOOO")
    elif i == 'p' or i == 'P':
      print("\nPPPPP\nP   P\nP   P\nPPPPP\nP\nP\nP")
    elif i == 'q' or i == 'Q':
      print("\nQQQQQQQ\nQ     Q\nQ     Q\nQ     Q\nQ Q   Q\nQ  Q  Q\nQQQQQQQ\n     Q")
    elif i == 'r' or i == 'R':
      print("\nRRRRR\nR   R\nR   R\nRRRRR\nRR\nR R\nR  R\nR   R")
    elif i == 's' or i == 'S':
      print("\nSSSSSS\nS\nS\nSSSSSS\n     S\n     S\nSSSSSS")
    elif i == 't' or i == 'T':
      print("\nTTTTTTT\n   T\n   T\n   T\n   T\n   T\n   T")
    elif i == 'u' or i == 'U':
      print("\nU     U\nU     U\nU     U\nU     U\nU     U\nU     U\nUUUUUUU")
    elif i == 'v' or i == 'V':
      print("\nV         V\n V       V\n  V     V\n   V   V\n    V V\n     V")
    elif i == 'w' or i == 'W':
      print("\nW     W\nW     W\nW     W\nW  W  W\nW W W W\nWW   WW\nW     W")
    elif i == 'x' or i == 'X':
      print("\nX     X\n X   X\n  X X\n   X\n  X X\n X   X\nX     X")
    elif i == 'y' or i == 'Y':
      print("\nY     Y\n Y   Y\n  Y Y\n   Y\n   Y\n   Y\n   Y")
    elif i == 'z' or i == 'Z':
      print("\nZZZZZZZ\n     Z\n    Z\n   Z\n  Z\n Z\nZZZZZZZ")
    elif i == " ":
      print("\n\n\n\n\n")
    else:
      count += 1
      
  if count > 0:
    print(f"\nYour name contains {count} unknown characters\nSo, I skipped it")
  print("\nThanks for using word magic!\nHope you like it")
    
    
     
     
    
  
