'''
  Read the document info of a pdf file.
'''
import os
import sys
from PyPDF4 import PdfFileReader

def main(path):
  reader = PdfFileReader(path)
  info = reader.getDocumentInfo()
  pages = reader.getNumPages()
    
  print('Pdf Info')
  if info:
    for (key, value) in info.items():
      print('{0: <20}: {1}'.format(key[1:], value))
  if pages:
    print('{0: <20}: {1}'.format('Pages', pages))
  if not info and not pages:
    print('no info available')

if __name__ == '__main__':
  if (len(sys.argv) != 2):
    print('Usage: python {0} [pdf]'.format(os.path.basename(__file__)))
  else:
    pdf = sys.argv[1]
    main(pdf)
