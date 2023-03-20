import docx2txt
import glob

directory = glob.glob(r'E:\2023\NER\Medical speciality\docs\entretiens/*.docx')

for file_name in directory:

    with open(file_name, 'rb') as infile:
        outfile = open(file_name[:-5]+'.txt', 'w', encoding='utf-8')
        doc = docx2txt.process(infile)

        outfile.write(doc)

    outfile.close()
    infile.close()

print("=========")
print("All done!")