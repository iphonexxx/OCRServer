#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from restapi import ExtractImage2, Ocr2, CompressImage, DetectType2, DetectType3, recognize
#from tornado.wsgi import WSGIContainer
#from tornado.httpserver import HTTPServer
#from tornado.ioloop import IOLoop
import logging
import os

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)-5s %(name)-8s - %(message)s")
recognize.loadConfig()

app = Flask(__name__)


@app.route('/health')
def heath_check():
    return 'OK'


api = Api(app)

api.add_resource(DetectType2.DetectType2Api, '/api/detect_invoice')
api.add_resource(ExtractImage2.ExtractImage2Api, '/api/extract_image')
api.add_resource(Ocr2.OCR2Api, '/api/ocr')
api.add_resource(CompressImage.CompressImageApi, '/api/compress_image')

logging.debug('Load Recongize Config: %s' % str(recognize.getConfig()))

def getVaildImgFileList():
    rootDir = r"/home/hello/work/OCRServer/inv_img/"
    lstValidImgFile = []
    bExitLoop = False
    for parent, dirnames, filenames in os.walk(rootDir):
        for filename in filenames:
            if filename.endswith(".jpg"):
                imgFile = os.path.join(parent,filename)
                lstValidImgFile.append(imgFile)
                #if len(lstValidImgFile) > 50:
                #    bExitLoop = True;
                #    break;
        if bExitLoop:
            break;

    return lstValidImgFile;
    pass
    
def get_filePath_fileName(filename):  
    (filepath,tempfilename) = os.path.split(filename);  
    (shotname,extension) = os.path.splitext(tempfilename);  
    return shotname

def main():
    lstVaildImgFiles = getVaildImgFileList()
    
    obj = DetectType3.DetectType3Api()
    #obj.post()
    nIndex = 0
    for imgFile in lstVaildImgFiles:
        print(imgFile)
        #if os.path.exists(imgFile)
        #    continue;
        nIndex = nIndex + 1
        if nIndex >= 20:
            break;

        strJobID = get_filePath_fileName(imgFile)
        print(strJobID)
        strFilePath = imgFile
        obj.post2(strJobID, strFilePath)
    pass

def test():
    obj = DetectType3.DetectType3Api()
    strJobID = "f4f87396eece404131ff119bd181ee3a"
    print(strJobID)
    strFilePath = "/home/hello/work/OCRServer/inv_img/f4f87396eece404131ff119bd181ee3a.jpg"
    obj.post2(strJobID, strFilePath)
    pass


if __name__ == '__main__':
    main();
    #test();
