import nltk
import json
import subprocess

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

def export_pairs(file="chat.json"):
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
    with open(file, 'w') as outfile:
        json.dump(j, outfile)

#impor from file and convert to nltk nested tuple format
def import_pairs(character="default"):
    global pairs
    file="characters/{}.json".format(character)
    ps = []
    # cmd = "pwd"
    # returns output as byte string
    # print("Current directory: "+str(subprocess.check_output(cmd)))
    # try:
    with open(file, 'r') as infile:
        j = json.load(infile)
        # print(j)
        for p in j["chat"]:
            pair = (r'{}'.format(p["prompt"]),tuple(p["content"]))
            ps.append(pair)
    # except:
    #     with open("./seqbot/"+file, 'r') as infile:
    #         j = json.load(infile)
    #         for p in j["chat"]:
    #             pair = (r'{}'.format(p["prompt"]),tuple(p["content"]))
    #             ps.append(pair)
    new_pairs = tuple(ps)
    pairs = new_pairs
    return pairs

def main():
    converse()
    
if __name__ == "__main__":
    main()
else:
    import_pairs()