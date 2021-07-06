'''
  Delete the document info of a pdf file.
'''
import os
import sys
from PyPDF4 import PdfFileMerger

def main(input, output):  
  merger = PdfFileMerger()
  merger.append(input)
  merger.write(output)

  info = os.path.join(os.path.dirname(__file__), 'info.py')
  os.system('python \"{0}\" \"{1}\"'.format(info, output))

if __name__ == '__main__':
  if (len(sys.argv) != 3):
    print('Usage: python {0} [input] [output]'.format(os.path.basename(__file__)))
  else:
    inPdf = sys.argv[1]
    outPdf = sys.argv[2]
    if inPdf == outPdf:
      print('Choose different names for input and output file!')
    elif not os.path.exists(inPdf):
      print('File {0} does not exist!'.format(inPdf))  
    elif os.path.exists(outPdf):
      print('File {0} already exisits!'.format(outPdf))    
    else:
      main(inPdf, outPdf)
