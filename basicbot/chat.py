import nltk
import json
import subprocess
from pkg_resources import resource_filename
package_name = "basicbot"

def get_response(character='default',r=''):
    if(character == 'default'):
        p = import_pairs(character)
    elif(character == 'eliza'):
        p= nltk.chat.eliza.pairs
    elif(character == 'iesha'):
        p= nltk.chat.iesha.pairs
    elif(character == 'rude'):
        p= nltk.chat.rude.pairs
    elif(character == 'suntsu'):
        p= nltk.chat.suntsu.pairs
    elif(character == 'zen'):
        p= nltk.chat.zen.pairs
    c = nltk.chat.util.Chat(p, nltk.chat.util.reflections)
    return c.respond(r)

def converse(character='default'):
    if(character == 'default'):
        p = import_pairs(character)
    elif(character == 'eliza'):
        p= nltk.chat.eliza.pairs
    elif(character == 'iesha'):
        p= nltk.chat.iesha.pairs
    elif(character == 'rude'):
        p= nltk.chat.rude.pairs
    elif(character == 'suntsu'):
        p= nltk.chat.suntsu.pairs
    elif(character == 'zen'):
        p= nltk.chat.zen.pairs
    c = nltk.chat.util.Chat(p, nltk.chat.util.reflections)
    c.converse()

def export_pairs(file_name="chat.json"):
    file_path = resource_filename(package_name, file_name)
    ch=[]
    for p in pairs:
        prompt = p[0]
        content = list(p[1])
        jp = {
          "prompt":prompt,
          "content": content
        }
        ch.append(jp)
    j={}
    j["chat"]=ch
    j={"chat":ch}
    with open(file_path, 'w') as outfile:
        json.dump(j, outfile)

#impor from file and convert to nltk nested tuple format
def import_pairs(character="default"):
    global pairs
    file_name="characters/{}.json".format(character)
    file_path = resource_filename(package_name, file_name)
    ps = []
    with open(file_path, 'r') as infile:
        j = json.load(infile)
        # print(j)
        for p in j["chat"]:
            pair = (r'{}'.format(p["prompt"]),tuple(p["content"]))
            ps.append(pair)
    new_pairs = tuple(ps)
    pairs = new_pairs
    return pairs

def main():
    converse()
    
if __name__ == "__main__":
    main()
else:
    import_pairs()