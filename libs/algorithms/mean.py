import numpy
from PIL import Image

# sostituisce valore di un pixel con il mediano dei livelli di intensità del suo intorno.
# alcuni tipi di rumori casuali hanno capacità di riduzione del rumore, sfocando meno rispetto a quelli di smoothing
# efficaci per rumore a impulsi sia bipolare che unipolare.  Incrementare una finestra si incrementa l'ordine del mediano

# non considero i bordi, li salto completamente


def mean_old(data, H, W):
    I = data
    for i in range(2, W-1):
        for j in range(3, H-1):
            temp = []   # array temporaneo che permette di cercare le statistiche d'ordine

            # kernel 3x3 fisso
            temp.append(I[i-1][j-1])
            temp.append(I[i][j-1])
            temp.append(I[i+1][j-1])
            
            temp.append(I[i-1][j])
            temp.append(I[i][j])
            temp.append(I[i+1][j])

            temp.append(I[i-1][j+1])
            temp.append(I[i][j+1])
            temp.append(I[i+1][j+1])

            I[i][j] = numpy.mean(temp)

    return I

# ritorna un'immagine diversa!!!
# def mean(data, H, W):

#     I = data

#     for i in range(2, W-1):
#         for j in range(3, H-1):
            
#             temp = []   # array temporaneo che permette di cercare le statistiche d'ordine

#             # kernel 3x3 fisso
#             for x in range(i-1, i+1):
#                 for y in range(j-1,j+1):
#                     temp.append(I[x][y])
#             I[i][j] = numpy.mean(temp)

#     return I


def main():

    # IMMAGINI A UN SOLO CANALE (CONVERTITE) CON PILLOW
    
    # img_noisy = Image.open("../../static/images/test.jpg").convert("L") # Converto l'immagine e la rendo a canale unico    
    # img_noisy.show(title="Original")
    # arr = numpy.array(img_noisy)
    # print("shape array 1 ", arr.shape)
    # applico il filtro
    # removed_noise_mean = mean( arr, len(arr), len(arr[0]) )
    # converto l'array in immagine
    # img_filtered_mean = Image.fromarray(removed_noise_mean)
    # img_filtered_mean.show(title="Mean")
    #save image elaborated with cv2
    # cv2.imwrite('../../static/images/edited/mean.png', removed_noise_mean)       ## per salvarlo


    # ******* IMMAGINI A COLORI **************

    # Pillow
    
    img_noisy_color = Image.open("../../static/images/test.png")
    img_noisy_color.show(title="original")

    r, g, b = img_noisy_color.split()

    # r.show()
    # b.show()
    # g.show()

    r = numpy.array(r)
    g = numpy.array(g)
    b = numpy.array(b)
    
    r = Image.fromarray(mean_old(r, len(r), len(r[0])))
    g = Image.fromarray(mean_old(g, len(g), len(g[0])))
    b = Image.fromarray(mean_old(b, len(b), len(b[0])))

    result = Image.merge('RGB', (r, g, b))

    result.show()

    # testa con il vecchio che il for dia lo stesso risultato
    # img_noisy2 = Image.open("../../static/images/test.jpg").convert("L") # Converto l'immagine e la rendo a canale unico    
    # arr2 = numpy.array(img_noisy)
    # removed_noise_mean_old = mean_old( arr2, len(arr2), len(arr2[0]) )
    # img_filtered_mean_old = Image.fromarray(removed_noise_mean_old)
    # img_filtered_mean_old.show(title="mean_old")
    # cv2.imwrite('../../static/images/edited/mean_old.png', removed_noise_mean_old)       ## per salvarlo

    # if list(removed_noise_mean.getdata()) == list(removed_noise_mean_old.getdata()):
    #     print("Identical")
    # else:
    #     print("Different")

main()