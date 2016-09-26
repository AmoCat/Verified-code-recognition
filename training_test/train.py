import os


for i in range(1,10):
	os.popen('tesseract '+str(i)+'.tif '+str(i)+'.exp2 batch.nochop makebox')
	os.popen('tesseract '+str(i)+'tif '+str(i)+'.exp1 nobatch box.train.stderr')

os.popen('unicharset_extractor *.box')
os.popen('shapeclustering -F font_properties -U unicharset *.tr')
os.popen('mftraining -F font_properties  -U unicharset *.tr')
os.popen('mv inttemp  newfont.inttemp')
os.popen('mv normproto  newfont.normproto')
os.popen('mv pffmtable newfont.pffmtable')
os.popen('mv shapetable  newfont.shapetable')
os.popen('combine_tessdata newfont.')
os.popen('cp newfont.traineddata  /usr/local/opt/tessdata/')