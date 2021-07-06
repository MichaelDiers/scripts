'''
  Merge pdf files into a single pdf file.
  Input:
    Name of merged pdf file.
    Directory that contains the pdf files that will be merged.
  The order of the merging process is given by the result of os.listdir(directory).
'''
import os
import sys
from PyPDF4 import PdfFileMerger

def main(mergedFile, inputFiles):
  merger = PdfFileMerger()

  for file in inputFiles:
    merger.append(file)    
  
  merger.write(mergedFile)

  info = os.path.join(os.path.dirname(__file__), 'info.py')
  os.system('python \"{0}\" \"{1}\"'.format(info, mergedFile))

if __name__ == '__main__':
  if (len(sys.argv) != 3):
    print('Usage: python merge.py [merged pdf] [directory]')
  else:
    mergedPdf = sys.argv[1]
    directory = sys.argv[2]
    if os.path.exists(mergedPdf):
      print('File {0} already exists!'.format(mergedPdf))
    elif not os.path.exists(directory):
      print('Directory {0} does not exist!'.format(directory))
    else:
      pdfs = [os.path.join(directory, file) for file in os.listdir(directory) if file[-3:].upper() == 'PDF']
      main(mergedPdf, pdfs)


