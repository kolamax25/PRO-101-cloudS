import os
import dropbox
import dropbox.files 
import WriteMode


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        
        for root, dirs, files in os.walk(fileFrom):

            for fileName in files:

                localPath = os.path.join(root, fileName)

                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)

                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overwrite'))

def main():
    accessToken = 'VDRp3rufc9IAAAAAAAAAAXlyiZOC0rWjeDSJ7TXi_0OSRFptoD7QpKpf6iv7Dy0m'
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the folder path to transfer file(s) from: ")
    fileTo = input("Enter the full path to upload to dropbox: ")
    transferData.uploadFile(fileFrom, fileTo)
    print("File has been moved")

main()