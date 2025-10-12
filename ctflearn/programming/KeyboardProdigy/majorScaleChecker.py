
scale = ["C", "C#", 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
pattern = [2, 2, 1, 2, 2, 2, 1]

def get_mojor_scale(key):
    ind = scale.index(key)
    major_scale = [key]
    for i in pattern:
        ind = (ind + i) % 12
        major_scale.append(scale[ind])
    return major_scale

def convert_enharmonics(input_scale):
    for key in range(len(input_scale)):
        if input_scale[key] not in scale:
            ind = scale.index(input_scale[key][0])
            if input_scale[key][1]=='b':
                ind = (ind - 1) % 12
            if input_scale[key][1] == '#':
                ind = (ind + 1) % 12
            input_scale[key] = scale[ind]
    return input_scale

def check_mojor_scale(inp_scale):
    inp_scale = inp_scale.strip().replace('\t', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')
    print("formated : ", inp_scale)
    inp_scale = convert_enharmonics(inp_scale)
    print("enharmonic converted", inp_scale)
    major_of_key = ''
    for k in inp_scale:
        if inp_scale.count(k)==2 and major_of_key=='':
            major_of_key = k
        elif inp_scale.count(k)==2 and major_of_key!=k:
            print(f"False : 2 major scale indicator {major_of_key} and {k}")
            return False
        elif inp_scale.count(k)>2:
            print(f"False: key {k} appeared {inp_scale.count(k)} times")
            return False
    if major_of_key=='':
        print("False: no major scale for any key found")
        return False
    major_scale = get_mojor_scale(major_of_key)
    print(f"the right major scal for key {major_of_key} is {major_scale}")
    for key in inp_scale:
        if key in major_scale:
            major_scale.remove(key)
        else:
            print(f"False: {key} is not in {major_scale}")
            return False
    return True

if __name__== "__main__":
    input_scales = open("notes", 'r').readlines()
    count = 0
    for scales in input_scales:
        if check_mojor_scale(scales):
            count +=1
    print(f"total {count} valid major scales found")