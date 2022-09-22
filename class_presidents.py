#tallies votes for presidents of two school classes. Somehow the vote tallies for sophomore and junior class presidents got mixed up! 
#Your function should accept as its parameter a string representing a filename of vote results. 
#It should output the next sophomore and junior class presidents. The file format looks like the following:
#Jared s 25 Sophie j 12 Tom j 44 Isaac s 30 Emily s 60 Russ s 23 Madison j 20

def class_presidents(x):
    with open(x, "r") as file:
        innit = file.read().split()
        sv = []
        jv = []
        sn = []
        jn = []
        for i in range(0, len(innit),3):
            if innit[i+1] == "s" :
                sv.append(innit[i+2])
                sn.append(innit[i])
            elif innit[i+1] == "j" :
                jv.append(innit[i+2])
                jn.append(innit[i])
        in_sv = sv.index(max(sv))
        in_jv = jv.index(max(jv))
        print(f"Sophomore Class President: {sn[in_sv]} ({max(sv)} votes)")
        print(f"Junior Class President: {jn[in_jv]} ({max(jv)} votes)")
