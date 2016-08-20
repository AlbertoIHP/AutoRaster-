# Autor : 	   Alberto Herrera Poza
# Estudiante   Universidad de La Frontera
# Comentarios: Antes de la ejecucion del siguiente codigo, es necesario crear tanto en Windows como en linux
#			   variables de entorno que puedan dar acceso a python a todas las librerias de QGIS y sus scripts
#			   en el caso de windows es necesario agregar al path
#			   c:\Program Files\QGIS Essen\bin y c:\Program Files\QGIS Essen\apps\qgis\bin
# 			   En el primer caso, se da el bin de lo que seria OSGEO4W y en el segundo el bin de QGIS para el
#			   acceso a los DLL del sistema. 
#			   Ademas es necesario hacer una nueva variable de entorno con el nombre de PYTHONPATH con lo siguiente
#              C:\Program Files\QGIS Essen\apps\qgis\python\plugins\processing;C:\Program Files\QGIS Essen\apps\qgis\python;C:\Program Files\QGIS Essen\apps\Python27\Lib\site-packages;C:\Program Files\QGIS Essen\apps\qgis\python\plugins
#			   Esta da acceso a python a todos los scripts utilizados por QGIS y sus librerias.

import math
import numpy as np
from numpy import *
import os
import osgeo.gdal as gdal
from stat import *
import struct
import sys

## Clase que representa el archivo de metadatos de una imagen raster, y que en sus metodos tiene la posibilidad de obtener cualquier dato de estos.
## This class represent all from a metada file from a raster image, their method allows obtain any value from it.
class metaData(object):

    def __init__(self, filepath, band):
        self.filepath = filepath + "_MTL.txt"
        archi = open(self.filepath, 'r')
        self.data = archi.readlines()
        self.band = band
	
    def getFilepath(self):
        return self.filepath
	
    def getMetaData(self):
        return self.data
	
    def getFilepath(self):
        return self.filepath
		
    def getValue(self, indexOf):
        value = self.data[indexOf]
        value = value.split("= ")
        value = value[1]
        return float(value)
	
    #GROUP = MIN_MAX_REFLECTANCE
    def getMinReflectance(self):
        if(self.band == "B1"):
            return self.getValue(91)
        else:
            if(self.band == "B2"):
                return self.getValue(93)
            else:
                if(self.band == "B3"):
                    return self.getValue(95)
                else:
                    if(self.band == "B4"):
                        return self.getValue(97)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(99)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(101)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(103)
                                else:
                                    print "The band " + self.band + " dont have this parameter at the metadata File"
													
    def getMaxReflectance(self):
        if(self.band == "B1"):
            return self.getValue(90)
        else:
            if(self.band == "B2"):
                return self.getValue(92)
            else:
                if(self.band == "B3"):
                    return self.getValue(94)
                else:
                    if(self.band == "B4"):
                        return self.getValue(96)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(98)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(100)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(102)
                                else:
                                    print "The band " + self.band + " dont have this parameter at the metadata File"
	
    #GROUP = MIN_MAX_RADIANCE
    def getMinRadiance(self):
        if(self.band == "B1"):
            return self.getValue(71)
        else:
            if(self.band == "B2"):
                return self.getValue(73)
            else:
                if(self.band == "B3"):
                    return self.getValue(75)
                else:
                    if(self.band == "B4"):
                        return self.getValue(77)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(79)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(85)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(87)
                                else:
                                    if(self.band == "B61"):
                                        return self.getValue(81)
                                    else:
                                        if(self.band == "B62"):
                                            return self.getValue(83)
                                        else:
                                            print "The band " + self.band + " dont have this parameter at the metadata File"
		
    def getMaxRadiance(self):
        if(self.band == "B1"):
            return self.getValue(70)
        else:
            if(self.band == "B2"):
                return self.getValue(72)
            else:
                if(self.band == "B3"):
                    return self.getValue(74)
                else:
                    if(self.band == "B4"):
                        return self.getValue(76)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(78)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(84)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(86)
                                else:
                                    if(self.band == "B61"):
                                        return self.getValue(80)
                                    else:
                                        if(self.band == "B62"):
                                            return self.getValue(82)
                                        else:
                                            print "The band " + self.band + " dont have this parameter at the metadata File"
		
    
    #GROUP = IMAGE_ATTRIBUTES
    def getSunAzimuth(self):
        return self.getValue(60)
	
    def getSunElevation(self):
        return self.getValue(61)
		
    def getEarthDistance(self):
        return self.getValue(62)
	
    def getCloudCover(self):
        return self.getValue(58)
	
    #GROUP = MIN_MAX_PIXEL_VALUE
    def getMinQuantizeCal(self):
        if(self.band == "B1"):
            return self.getValue(107)
        else:
            if(self.band == "B2"):
                return self.getValue(109)
            else:
                if(self.band == "B3"):
                    return self.getValue(111)
                else:
                    if(self.band == "B4"):
                        return self.getValue(113)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(115)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(121)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(123)
                                else:
                                    if(self.band == "B61"):
                                        return self.getValue(117)
                                    else:
                                        if(self.band == "B62"):
                                            return self.getValue(119)
                                        else:
                                            print "The band " + self.band + " dont have this parameter at the metadata File"
	
    def getMaxQuantizeCal(self):
        if(self.band == "B1"):
            return self.getValue(106)
        else:
            if(self.band == "B2"):
                return self.getValue(108)
            else:
                if(self.band == "B3"):
                    return self.getValue(110)
                else:
                    if(self.band == "B4"):
                        return self.getValue(112)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(114)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(120)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(122)
                                else:
                                    if(self.band == "B61"):
                                        return self.getValue(116)
                                    else:
                                        if(self.band == "B62"):
                                            return self.getValue(118)
                                        else:
                                            print "The band " + self.band + " dont have this parameter at the metadata File"
	
    #GROUP = RADIOMETRIC_RESCALING
    def getRadianceMult(self):
        if(self.band == "B1"):
            return self.getValue(173)
        else:
            if(self.band == "B2"):
                return self.getValue(174)
            else:
                if(self.band == "B3"):
                    return self.getValue(175)
                else:
                    if(self.band == "B4"):
                        return self.getValue(176)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(177)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(180)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(181)
                                else:
                                    if(self.band == "B61"):
                                        return self.getValue(178)
                                    else:
                                        if(self.band == "B62"):
                                            return self.getValue(179)
                                        else:
                                            print "The band " + self.band + " dont have this parameter at the metadata File"

    def getRadianceAdd(self):
        if(self.band == "B1"):
            return self.getValue(182)
        else:
            if(self.band == "B2"):
                return self.getValue(183)
            else:
                if(self.band == "B3"):
                    return self.getValue(184)
                else:
                    if(self.band == "B4"):
                        return self.getValue(185)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(186)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(189)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(190)
                                else:
                                    if(self.band == "B61"):
                                        return self.getValue(187)
                                    else:
                                        if(self.band == "B62"):
                                            return self.getValue(188)
                                        else:
                                            print "The band " + self.band + " dont have this parameter at the metadata File"

    def getReflectanceMult(self):
        if(self.band == "B1"):
            return self.getValue(191)
        else:
            if(self.band == "B2"):
                return self.getValue(192)
            else:
                if(self.band == "B3"):
                    return self.getValue(193)
                else:
                    if(self.band == "B4"):
                        return self.getValue(194)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(195)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(196)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(197)
                                else:
                                    print "The band " + self.band + " dont have this parameter at the metadata File"
								
    def getReflectanceAdd(self):
        if(self.band == "B1"):
            return self.getValue(198)
        else:
            if(self.band == "B2"):
                return self.getValue(199)
            else:
                if(self.band == "B3"):
                    return self.getValue(200)
                else:
                    if(self.band == "B4"):
                        return self.getValue(201)
                    else:
                        if(self.band == "B5"):
                            return self.getValue(202)
                        else:
                            if(self.band == "B7"):
                                return self.getValue(203)
                            else:
                                if(self.band == "B8"):
                                    return self.getValue(204)
                                else:
                                    print "The band " + self.band + " dont have this parameter at the metadata File"
									
									
									
############################################################################################################################################################

#Clase que representa una imagen raster, que permite obtener todos sus datos y crearla si fuera necesario.
#This class represent all from a raster picture, allows receives all data or create it.
class rasterFile(object):
	
    #Metodo constructor, el cual recibe como parametro la direccion del fichero raster en cuestion.
    #Constructor method, who receives the raster filepath at issue.
    def __init__(self, filepath):
        #En caso que se trabaje a nivel de directorios (NO PROBADO)
        auxDirectoryList = filepath.split("\\")
        self.name = auxDirectoryList[(auxDirectoryList.__len__() - 1)].split("_")[0]
        self.band = auxDirectoryList[(auxDirectoryList.__len__() - 1)].split("_")[1].split(".")[0]
		
        if (auxDirectoryList.__len__() > 1):
            i = 0
            namePath = ""
            while(i <= (auxDirectoryList.__len__() - 2)):
                if(i == 0):
                    namePath = auxDirectoryList[i]
                else:
                    namePath = namePath + "\\" + auxDirectoryList[i]
                i = i + 1
            namePath = namePath + "\\" + self.name
        else:
            namePath = self.name
        self.filepath = filepath
        self.dataset = gdal.Open(self.filepath, gdal.GA_ReadOnly)
        try:
            if(self.band == "B6"):
                self.band = auxDirectoryList[(auxDirectoryList.__len__() - 1)].split("_")[1] + auxDirectoryList[(auxDirectoryList.__len__() - 1)].split("_")[3].split(".")[0]
            else:
                self.band = self.band
            self.metadata = metaData(namePath, self.band)
        except IOError:
            print "This raster dont have metadata"
        self.completePath = namePath
	
    #Metodo que devuelve el formato de imagen del fichero raster.
    #This method returns the format of our raster file.
    def getDriver(self):
        if(self.dataset is None):
            print "This raster file do not exist, you can create it by using createRaster() function"
        else:
            return self.dataset.GetDriver().ShortName
	
    #Este metodo recibe un parametro que puede ser x, y o count. El primero retorna el numero de pixeles en el eje X 
    #el segundo retorna el numero de pixeles en el eje Y, y el tercero el numero de bandas con el que esta compuesto
    #el raster.
    #This method, receives three parameters, could be x, y or count. First one returns pixel number on the X axis, 
    #second one returns pixel number on the Y axis, at last the count returns band number present on the raster file.
    def getSize(self, infoType):
        if(self.dataset is None):
            print "This raster file do not exist, you can create it by using createRaster() function"
        else:
            if(infoType == "x"):
                return self.dataset.RasterXSize
            else:
                if(infoType == "y"):
                    return self.dataset.RasterYSize
                else:
                    if(infoType == "count"):
                        return self.dataset.RasterCount
                    else:
                        return "ERROR1: Your infoType parameter is not valid"
	
    #Este metodo retorna la proyeccion del archivo raster en cuestion.
    #This method returns projection raster file at issue.
    def getProjection(self):
        if(self.dataset is None):
            print "This raster file do not exist, you can create it by using createRaster() function"
        else:
            return self.dataset.GetProjection()
    
    #Este metodo retorna la transformacion geografica del archivo raster en cuestion.
    #This method returns the Geo transform of our raster file at issue.
    def getGeoTransform(self):
        if(self.dataset is None):
            print "This raster file do not exist, you can create it by using createRaster() function"
        else:
            return self.dataset.GetGeoTransform()
	
    #Este metodo devuelve el tipo de variable utilizado en la matriz que compone la imagen raster.
    #This method returns the variable type used by raster file at issue.
    def getDataType(self):
        return getSize("count").DataType
	
        ## FALTA AGREGAR EL DATA TYPE COMO PARAMETRO VARIABLE
			
############################################################################################################################################################

#Clase que representa todo lo que se puede realizar con un conjunto de imagenes raster, ya sea el calculo de NDVI, reproyecciones, calculos, etc. (En construccion).
#This class represents all actions that we could do with raster files, it could be NDVI, reproject, calculator, etc. (Not ready yet).
class rasterCalculator(object):
	
    def createRaster(self, type, sizeX, sizeY, bandNumber, projection, geoTransform, filepath):
        if(self.checkMetadata(type)):
            data = gdal.GetDriverByName(type).Create(filepath, sizeX, sizeY, bandNumber, gdal.GDT_Float32)
            data.SetProjection(projection)
            data.SetGeoTransform(geoTransform)
            return data
        else:
            print "Driver ", type, " is not supported by Create method"
            return None
				
    #Este metodo permite verificar la metada de una imagen raster, o al menos la que viene en la imagen.
    #This method allows verify the raster file metada, or the metada existing on the picture at least.
    def checkMetadata(self, type):
        driver = gdal.GetDriverByName(type)
        metadata = driver.GetMetadata()
        if metadata.has_key(gdal.DCAP_CREATE) and metadata[gdal.DCAP_CREATE] == 'YES':
            #'Driver GTiff supports Create() method.'
            driver = None
            metadata = None
            return True
        else:
            # 'Driver GTIFF does not support Create()'
            driver = None
            metadata = None
            return False
			
	
    #Este metodo calcula el ndvi
    def ndvi(self, redBand, nearRedBand, outFile):
		
        #Cargamos ambas bandas, en este caso se pone 1 por que estas imagenes solo poseen 1 banda
        #We load the both bands, in this case we put 1 because those pictures have only 1 band
        red_band = redBand.dataset.GetRasterBand(1) # RED BAND
        nir_band = nearRedBand.dataset.GetRasterBand(1) # NIR BAND
		
        #Creamos el archivo de salida donde guardaremos el resultado del calculo del indice NDVI.
        #We create the output file, wich we'll use to save our result from NDVI calculus.
        dst_ds = self.createRaster(redBand.getDriver(), redBand.getSize("x"), redBand.getSize("y"), 1, redBand.getProjection(), redBand.getGeoTransform(), outFile)
        # Obtenemos el numero de lineas en el eje Y.
        # Retrieve the number of lines within the image.
        numLines = red_band.YSize
		
		
        # Recorremeremos linea por linea la matriz, de manera que podamos ir pixel por pixel.
        # Will walk through all Y axis lines, so we could take pixel by pixel.
        for line in range(numLines):
			
            # Definimos un acumulador de lineas para ir agregando al final de cada secuencia del loop (step by step)
            # Define variable for output line.
            outputLine = ''
            # Los datos se leen como una cadena que contiene una representacion binaria de los valores de la imagen, estos deben
            # ser convertidos a los valores de numero, en este caso los valores de punto flotante. En este caso usaremos el Struct packet.
			
			
            # Leemos la informacion de la linea actual de la banda roja con el fin de poder desempaquetarla para utilizarla como punto flotante.
            # Read in data for the current line from the image band representing the red wavelength.
            red_scanline = red_band.ReadRaster(0, line, red_band.XSize, 1, red_band.XSize, 1, gdal.GDT_Float32)
			
            # Desempaquetamos la linea de datos para ser leidas como informacion de punto flotante.
            # Unpack the line of data to be read as floating point data
            red_tuple = struct.unpack('f' * red_band.XSize, red_scanline)

            # Lo mismo con la banda infraroja cercana.
            # The same with the NIR band.
            nir_scanline = nir_band.ReadRaster(0, line, nir_band.XSize, 1, nir_band.XSize, 1, gdal.GDT_Float32)
            nir_tuple = struct.unpack('f' * nir_band.XSize, nir_scanline)
			
            # Una tupla es similar a una lista en el modo de acceso a los datos, pero los datos no pueden ser editados.
            # Ahora recorremos cada columna de la linea en cuestion, para poder hacer uso de la ecuacion pixel por pixel.
            # En este caso se utilizo la tupla de la banda roja, pero podia utilziarse la de la infraroja cercana da igual.
			
            for i in range(len(red_tuple)):
                #Calculamos pixel por pixel.
                ndvi_lower = (nir_tuple[i] + red_tuple[i])
                ndvi_upper = (nir_tuple[i] - red_tuple[i])
                ndvi = 0
                #Nos fijamos en la division por cero.
                if ndvi_lower == 0:
                    ndvi = 0
                else:
                    ndvi = ndvi_upper / ndvi_lower
                    # Vamos agregando de a poco en la linea de salida (como acumulador)
                    # lo que se vaya calculando del ndvi y se empaqueta devuelta a datos binarios.
                outputLine = outputLine + struct.pack('f', ndvi)
            # Una vez recorrida toda la primera linea se escribe en el fichero raster de salida
            # y se prosigue con la siguiente linea y asi se itera hasta terminar el proceso.
            dst_ds.GetRasterBand(1).WriteRaster(0, line, red_band.XSize, 1, outputLine, buf_xsize=red_band.XSize, buf_ysize=1, buf_type=gdal.GDT_Float32)
			
			
			
    def toa(self, raster, outFile):
		
        x_band = raster.dataset.GetRasterBand(1) # Raster
        dst_ds = self.createRaster(raster.getDriver(), raster.getSize("x"), raster.getSize("y"), 1, raster.getProjection(), raster.getGeoTransform(), outFile)
        numLines = x_band.YSize
		
        for line in range(numLines):
			
            outputLine = ''
            x_scanline = x_band.ReadRaster(0, line, x_band.XSize, 1, x_band.XSize, 1, gdal.GDT_Float32)
            x_tuple = struct.unpack('f' * x_band.XSize, x_scanline)

            for i in range(len(x_tuple)):
                pixelDN = x_tuple[i]
                radian_sun_elevation = (math.pi) / (raster.metadata.getSunElevation())
                TOA_upper = raster.metadata.getReflectanceMult() * pixelDN  + raster.metadata.getReflectanceAdd()
                TOA_lower = math.sin(radian_sun_elevation)
                TOA = 0
                if pixelDN == 0:
                    TOA = 0
                else:
                    TOA = TOA_upper / TOA_lower
                outputLine = outputLine + struct.pack('f', TOA)
            dst_ds.GetRasterBand(1).WriteRaster(0, line, x_band.XSize, 1, outputLine, buf_xsize=x_band.XSize, buf_ysize=1, buf_type=gdal.GDT_Float32)
			
	
    def ndii(self, nirBand, swir1Band, outFile):
		
        nir_band = nirBand.dataset.GetRasterBand(1) 
        swir1_band = swir1Band.dataset.GetRasterBand(1) 
		
        dst_ds = self.createRaster(nirBand.getDriver(), nirBand.getSize("x"), nirBand.getSize("y"), 1, nirBand.getProjection(), nirBand.getGeoTransform(), outFile)
        numLines = nir_band.YSize
		
        for line in range(numLines):
			
            outputLine = ''
            nir_scanline = nir_band.ReadRaster(0, line, nir_band.XSize, 1, nir_band.XSize, 1, gdal.GDT_Float32)
			
            nir_tuple = struct.unpack('f' * nir_band.XSize, nir_scanline)

            swir1_scanline = swir1_band.ReadRaster(0, line, swir1_band.XSize, 1, swir1_band.XSize, 1, gdal.GDT_Float32)
            swir1_tuple = struct.unpack('f' * swir1_band.XSize, swir1_scanline)
			
            for i in range(len(nir_tuple)):
                #Calculamos pixel por pixel.
                ndii_lower = (nir_tuple[i] + swir1_tuple[i])
                ndii_upper = (nir_tuple[i] - swir1_tuple[i])
                ndii = 0
                if ndii_lower == 0:
                    ndii = 0
                else:
                    ndii = ndii_upper / ndii_lower
                outputLine = outputLine + struct.pack('f', ndii)
            dst_ds.GetRasterBand(1).WriteRaster(0, line, nir_band.XSize, 1, outputLine, buf_xsize=nir_band.XSize, buf_ysize=1, buf_type=gdal.GDT_Float32)
	
############################################################################################################################################################
class listDirMaker(object):
	
    def __init__(self, path):
        self.dirList = []
        self.walktree(path, self.visitfile)
		
 
    def walktree(self, top, callback):
        '''recursively descend the directory tree rooted at top,
		  calling the callback function for each regular file'''
	 
        for f in os.listdir(top):
            pathname = os.path.join(top, f)
            mode = os.stat(pathname)[ST_MODE]
            if S_ISDIR(mode):
                # It's a directory, recurse into it
                self.walktree(pathname, callback)
            elif S_ISREG(mode):
                # It's a file, call the callback function
                callback(pathname, f, top)
            else:
                # Unknown file type, print a message
                print 'Skipping %s' % pathname
 
    def visitfile(self, fullname, file, path):
        format = fullname.split(".")
        if(format[format.__len__()-1] == "TIF"):
            self.dirList.append(fullname)
			
    def getdirList(self):
        return self.dirList
		
    def getIndexOf(self):
        return self.dirList.__len__()
		
############################################################################################################################################################
if __name__ == '__main__':

    #listDirmaker es una clase que permite recorrer un arbol de directorios y buscar imagenes TIF, solo necesitamos el directorio tope
    #y con eso se generara un arreglo de direcciones de cada uno de los archivos tiff encontrados desde el directorio tope
    #en este caso asigne directamente getdirList para obtener la lista.
    try:
        totalArchivos = listDirMaker("D:\IMAGENES LANDSAT\Imagenes").getdirList()
        print "Se encontraron ", totalArchivos.__len__(), "imagenes raster."
        lastRaster = ""
        currentRaster = ""
        calculadora = rasterCalculator()
		
        for indice in range(len(totalArchivos)):
            currentRaster = rasterFile(totalArchivos[indice])
            #En el indice cero el primero es igual al ultimo, y se crea el directorio respectivo 
            if(indice == 0):
                newDir = "C:\Users\Public\imagenes" + "\\" + currentRaster.name
                try:
                    lastRaster = currentRaster
                    os.makedirs(newDir)
                    print "Los resultados para las imagenes " + currentRaster.name + " se guardaran en " + newDir 
                except OSError:
                    pass
            #Despues se rigue esta norma para la creacion de directorios, si el raster actual tiene distinto nombre que el anterior
            #Entonces hay que crear un nuevo directorio para el actual raster trabajado
            if(currentRaster.name != lastRaster.name):
                newDir = "C:\Users\Public\imagenes" + "\\" + currentRaster.name
                try:
                    os.makedirs(newDir)
                    print "Los resultados para las imagenes " + currentRaster.name + " se guardaran en " + newDir
                except OSError:
                    pass
            print "Se ha cargado " + currentRaster.name + ", en la banda " + currentRaster.band
			
            if(currentRaster.band == "B61" or currentRaster.band == "B62"):
                print "Esta es la banda B61 o la banda B62, no se procesaran"
            else:
                print "Calculando TOA para la banda " + currentRaster.band + " de la imagen " + currentRaster.name
                calculadora.toa(currentRaster, newDir + "\\" + currentRaster.name + "_" + currentRaster.band + "_TOA.TIF")
                currentRaster = rasterFile(newDir + "\\" + currentRaster.name + "_" + currentRaster.band + "_TOA.TIF")
                if(indice == 0):
                    lastRaster = currentRaster
				
            if(lastRaster.band == "B3" and currentRaster.band == "B4" and lastRaster.name == currentRaster.name):
                print "Calculando NDVI para el archivo " + currentRaster.name
                calculadora.ndvi(lastRaster, currentRaster, newDir + "\\" + currentRaster.name + "_NDVI.TIF")
            else:
                if(lastRaster.band == "B4" and currentRaster.band == "B5" and lastRaster.name == currentRaster.name):
                    print "Calculando NDII para el archivo " + currentRaster.name
                    calculadora.ndii(lastRaster, currentRaster, newDir + "\\" + currentRaster.name + "_NDII.TIF")
				
            print indice, " de ", totalArchivos.__len__(), " completados"	
			lastRaster = currentRaster
			#print totalArchivos[indice]
		
		
	except OSError:
		print "Ni idea man"
	
	raw_input()
	

	
