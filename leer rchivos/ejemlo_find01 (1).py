

def leer_archivo(archivo, modo):            #        **** Reading files in Python  ****
    infile  = open(archivo, modo)           # Pointer to a file
    lista = []                              # Create an empty list
    with infile:                            # Handle the file
        for linea in infile:                #     Go through all the lines
            linea = linea.replace("\n","")  #     Delete line break "\n"
            lista.append(linea)             #     Append line to list
    infile.close()                          # Free resource
    return (lista)                          # Return list


def escribir_archivo(archivo, modo, lista): #        ****  Writing files in Python  ****
    outfile =  open(archivo, modo)          # Pointer to a file
    lstln = len(lista)                      # Number of elements in list
    for i in range(0, lstln-1):             
        linea_out = lista[i] + '\n'         #     Adds line  plus line break "\n"
        outfile.write(linea_out)            #     Write line to the output file
    i+= 1                                   # Write last line without line break
    linea_out = lista[i]                    #     
    outfile.write(linea_out)                #     
    outfile.close()                         # Free resource
    return                                  # Return

def color_asig(color):                      #        **** Assign a color to each word for highlighting  ****
    color = color % 8                       # There are only eight available colors. 
    if (color == 0):                        #
        return ('00FFBF', 'Red')            # Set color 1
    elif(color == 1):                       #
        return ('00BFFF', 'Fuchsia')        # Set color 2
    elif(color == 2):                       #
        return ('BF00BF', 'Navy')           # Set color 3
    elif(color == 3):                       #
        return ('FF00FF', 'Green')          # Set color 4
    elif(color == 4):                       #
        return ('000F0F', 'Lime')           # Set color 5
    elif(color == 5):                       #
        return ('00FFFF', 'Blue')           # Set color 6
    elif(color == 6):                       #
        return ('EFEF00', 'Purple')         # Set color 7
    elif(color == 7):                       #
        return ('FFFF00', 'Yello')          # Set color 8
    else:
        return ('FFFF00', 'Teal')

def mostrar_lista(lista, title):            #        **** Show list  ****
    print('\n')
    if (title != ''):                       # Display title
        print('\n    ********  ', \
              title, '  ********\n')
    for linea in lista:                     # Display list items 
        print(linea)

def ordenar_lista_size(lista):                                               #        **** Sort list by size  ****
    m = len(lista)                                                           # Rows?
    lista_sz = []                                                            # Size list
    for i in range(m):                                                       # Get size searched words
        lista_sz.append(len(lista[i][0]))                                    #     Get size of each word
    for i in range(m-1):                                                     # Find "m-1" biggers
        for j in range(m-1- i):                                              #     Find the  biggest in this set
            if (lista_sz[j] < lista_sz[j+1]):                                #     if order is incorrect, swap
                lista_sz[j], lista_sz[j+1], = lista_sz[j+1], lista_sz[j]     #         word size list
                lista[j], lista[j+1] = lista[j+1], lista[j]                  #         lista list
    return(lista)




'''
    ********  main  ********
'''

#infile_name = 'C:/python_ejemplos/strings/texto_target.txt'              #........Working Files
infile_name   = 'texto_target.txt'                                        # Input file name               ./
infile_mode   = 'r'                                                       # input file mode               ./
listword_name = 'lista_palabras.txt'                                      # Input file name               ./
listword_mode = 'r'                                                       # input file mode               ./
outfile_name  = '_find'                                                   # Output file name              ./
outfile_mode  = 'w'                                                       # Output file mode              ./
dm  = infile_name.find('.')                                               #     Get dot position
outfile_name = infile_name[0:dm] + outfile_name + '.html'                 # Set the output file name

                                                                          #........Open files
infile_name = 'texto_target.txt'
infile_mode = 'r'
listword_name = 'lista_palabras.txt'
listword_mode = 'r'
outfile_mode= 'w'
dm = infile_name.find('.')
outfile_name = infile_name[0:dm]+outfile_name + '.html'

lista_texto = leer_archivo(infile_name, infile_mode)
mostrar_lista(lista_texto, infile_name)
palabras = leer_archivo(listword_name, listword_mode)
mostrar_lista(palabras, listword_name)

lista_palabras = []
for i in range (len(palabras)):
    lista_palabras.append([])
    lista_palabras[i].append(palabras[i])
    c1 , c2 = color_asig(i)
    lista_palabras[i].append(c1)
    lista_palabras[i].append(c2)
mostrar_lista(lista_palabras, ' sin ordenar')
lista_palabras = ordenar_lista_size(lista_palabras)
mostrar_lista(lista_palabras, ' ordenada ordenar')

                                                                           # Open input file with text to analyze
                                                                          #     Show input file contents
                                                                          # Open input file with words to search
                                                                          #     Show list words

                                                                          #........Define highlight: word + format
                                                                          # New list
                                                                          # Go through all previous list
                                                                          #     this item is a list
                                                                          #     Set 
                                                                          #     Get highlighting colors
                                                                          #         Set highlighting color_1
                                                                          #         Set highlighting color_2
                                                                          #
                                                                          # . . . .Sort list by size


#........Start Output list
lista_out = []
lista_out.append('<HTML>\n<HEAD>\n<TITLE> ejemplo_find01 </TITLE>\n</HEAD>\n\n')    # . . . .Set headers for a html file
lista_out.append('<BODY  BGCOLOR=\"#FFFFFF\"  BACKGROUND=\"./images/ITESMwatermark.png\">\n<BR><P>\n<BR><P>\n\n\n\n\n')

for linea in lista_texto:
    j = -1
    resaltar = []
    pos_fin = len(linea)
    for i in range(0, len(lista_palabras)):
        pos_ini = 0
        while(1):
            encontrada = linea.find(lista_palabras[i][0],pos_ini,pos_fin)
            if( encontrada == -1):
                pos_ini = pos_fin
            else:
                pos_ini = encontrada + len(lista_palabras[i][0])
                encontrada_i = encontrada
                encontrada_f = pos_ini
                c1 = lista_palabras[i][1]
                c2 = lista_palabras[i][2]
                add_item= 1
                b = len(resaltar)
                for a in range(0,b):
                    if( (encontrada_i > resaltar [a][0] ) and (encontrada_i < resaltar [a][1])):
                        add_item = 0
                        break
                if (add_item):
                    resaltar.append([])
                    j += 1
                    resaltar[j].append(encontrada_i)
                    resaltar[j].append(encontrada_f)
                    resaltar[j].append(c1)
                    resaltar[j].append(c2)
                    
                
            if(pos_fin<=pos_ini):
                break
                #else
                #nothing
                
    if(resaltar):
        pos_ini = 0
        linea_out = ""
        resaltar.sort(key=lambda resaltar: resaltar [:][0])
        for i in range (0,len(resaltar)):
            linea_out= linea_out + linea[pos_ini: resaltar[i][0]]
                    
            linea_out = linea_out + "<span style=\"background-color: #" + resaltar[i][2] + "\"><b><font color=\"" + resaltar[i][3] + "\">"
            linea_out = linea_out + linea[resaltar[i][0] : resaltar[i][1]]
            linea_out = linea_out + "</font></b></span>"
            pos_ini = resaltar[i][1];
                    
        if(pos_ini < len(linea)):
            linea_out= linea_out + linea[pos_ini : len(linea)]
                    
    else:
        linea_out=linea
                
    linea_out= linea_out + "<br>"
    lista_out.append(linea_out)
            
            
        
                                                                          #         If  there is some original text add itwithout highlight
                 
        
                                                                          #         if no word was found, add line without highlight any words
        
    
                                                                          #     Add line break
                                                                          #     Add parsed text to output list


lista_out.append('<BR>\n')                                                # . . . .Set footers for a html file
lista_out.append('\n\n\n\n<BR><P></BODY></HTML>')


escribir_archivo(outfile_name, outfile_mode, lista_out)
# Write output list to the output file



