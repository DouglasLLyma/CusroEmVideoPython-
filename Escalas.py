escala = str(input('Digite o I da escala desejada: '))
if escala == 'C':
    CampoHarmonico = 'C, Dm, Em, F, G, Am, Bm(b5)'
    if escala == 'G':
        CampoHarmonico = 'G, Am, Bm, C, D, Em, F#m(b5)'
        if escala == 'D':
            CampoHarmonico = 'D, Em, F#m, G, A, Bm, C#m(b5),'
            if escala == 'A':
                CampoHarmonico = 'A, Bm, C#m, D, E, F#m, G#m(b5)'
else:
    CampoHarmonico = 'não existe'
print(CampoHarmonico)
        