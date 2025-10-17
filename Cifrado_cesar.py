ALFABETO = "abcdefghijklmnñopqrstuvwxyz ,."

texto_cifrado = ("l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm "
"k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm "
"xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw "
"gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm "
",puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf "
"mfkwu .tizifsif.uplilh")

caracteres = ALFABETO
longitud = len(caracteres)
minus = {ch: i for i, ch in enumerate(caracteres)}

PALABRAS_COMUNES = [" que ", " de ", " la ", " el ", " y ", " en ", " para ", " con ", " su ", " del ", " las ", " los "]

mejor = None  
for movimiento in range(1, longitud):
    caracteres_salida = []
    for ch in texto_cifrado:
        if ch in minus:
            idx = minus[ch]
            caracteres_salida.append(caracteres[(idx - movimiento) % longitud])
        else:
            caracteres_salida.append(ch)
    candidato = ''.join(caracteres_salida)
    puntuacion = sum(candidato.lower().count(w) for w in PALABRAS_COMUNES)
    if mejor is None or puntuacion > mejor[0]:
        mejor = (puntuacion, movimiento, candidato)

if mejor:
    puntuacion, movimiento, texto = mejor
    print(f"se mueve = {movimiento}   (puntuación = {puntuacion})")
    print()
    print(texto)
