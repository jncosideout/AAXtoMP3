import sys
import json

def flatten_chapters(y):
    out = []
 
    def flatten(x, level=0):
 
        for a in x:
            if 'chapters' in a:
                sub_chapters = a["chapters"] 
                del a["chapters"]
                if level>0:
                    a["title"] = '*' * level + ' ' + a["title"]
                out.append(a)
                flatten(sub_chapters, level+1)

            else:
                if level>0:
                    a["title"] = '*' * level + ' ' + a["title"]
                out.append(a)
            
    flatten(y)
    return out

if len(sys.argv) != 2:
    print("usage: python flatten_chapters.py filename")
    sys.exit(2)

data = json.load(open(sys.argv[1]));

data["content_metadata"]["chapter_info"]["chapters"] = flatten_chapters(data["content_metadata"]["chapter_info"]["chapters"])

print(json.dumps(data, indent=4, sort_keys=False));



