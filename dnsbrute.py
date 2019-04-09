import dns.resolver
import sys
import style as st

try:
    argumentos = sys.argv
    dominio = sys.argv[1]
    nomearquivo = sys.argv[2]
except:
    print("Argumentos invalidos")
    print ("Usage: dnsbrute.py <dominio> <wordlist>")

try:
    arquivo = open(nomearquivo)
    subdominios = arquivo.read().splitlines()
except:
    print ("Arquivo nao encontrado")
    sys.exit()

try:
    for dominios in subdominios:
        domesub = dominios + '.' + dominio
        resultados = dns.resolver.query(domesub, 'a')
        for resultado in resultados:            
            st.prYellow(domesub)
            st.prCyan(resultado)
            print()
            
            
except:
    pass




