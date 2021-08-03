import os

def compile_passages(path, w, out):
    outfile = open(out, 'w')
    doc_id = 0
    
    outfile.write('id\ttext\ttitle\n')

    for (dirname, _, fnames) in os.walk(path):
        for fname in fnames:
            print(dirname, fname)
            file_path = os.path.join(dirname, fname)
            chapter_name = os.path.splitext(fname)[0]
            with open(file_path, 'r') as chapter:
                all_words = chapter.read().strip().split()
                for i in range(0, len(all_words), w):
                    words = ' '.join(all_words[i:i+w])
                    title = ' '.join((dirname, chapter_name)).title()
                    line = str(doc_id) + '\t' + words + '\t' + title + '\n'
                    outfile.write(line)
                    doc_id += 1
    
    outfile.close()

if __name__ == '__main__':
    import sys
    compile_passages(
        path = sys.argv[1],
        w = int(sys.argv[2]),
        out = sys.argv[3],
    )
