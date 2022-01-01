import numpy
import box
from binpackp import NumberBin, Fit
import math

def del_input_boxes(possibility, input_box):
    input_possiblity = [0 for x in range(14)]
    for x in range(len(possibility)):
        arr2_index = x
        if x > 6:
            arr2_index -= 6
        if possibility[x] > 0:
                for _ in range(int(possibility[x] / 100)):
                    #101
                    if x == 0:
                        if input_box[4] > 0:
                            input_possiblity[x] += 1
                        input_box[4] -= 2
                    #102
                    elif x == 1:
                        if input_box[5] > 0:
                            input_possiblity[x] += 1
                        input_box[5] -= 3
                    #103
                    elif x == 2:
                        if input_box[6] > 0:
                            input_possiblity[x] += 1
                        input_box[6] -= 4 
                    #104                    
                    elif x == 3:
                        if input_box[0] > 0:
                            input_possiblity[x] += 1
                        input_box[0] -= 2   
                    #105
                    elif x == 4:
                        if input_box[1] > 0:
                            input_possiblity[x] += 1   
                        input_box[1] -= 3
                    #106
                    elif x == 5:
                        if input_box[3] > 0:
                            input_possiblity[x] += 1 
                        input_box[3] -= 3  
                    #201
                    elif x == 6:
                        if input_box[4] > 0 and input_box[6] > 0:
                            input_possiblity[x] += 1  
                        input_box[4] -= 1
                        input_box[6] -= 2 
                    #202
                    elif x == 7:
                        if input_box[5] > 0 and input_box[7] > 0:
                            input_possiblity[x] += 1
                        input_box[5] -= 1
                        input_box[7] -= 1   
                    #203
                    elif x == 8:
                        if input_box[6] > 0 and input_box[7] > 0:
                            input_possiblity[x] += 1
                        input_box[6] -= 1
                        input_box[7] -= 1 
                    #204  
                    elif x == 9:
                        if input_box[6] > 0 and input_box[5] > 0:
                            input_possiblity[x] += 1
                        input_box[2] -= 1
                        input_box[7] -= 1  
                    #205 
                    elif x == 10:
                        if input_box[1] > 0 and input_box[4] > 0:
                            input_possiblity[x] += 1
                        input_box[1] -= 1
                        input_box[4] -= 3 
                    #206  
                    elif x == 11:
                        if input_box[5] > 0 and input_box[1] > 0:
                            input_possiblity[x] += 1   
                        input_box[5] -= 6
                        input_box[1] -= 1
                    #207
                    elif x == 12:
                        if input_box[2] > 0 and input_box[3] > 0:
                            input_possiblity[x] += 1  
                        input_box[3] -= 2
                        input_box[2] -= 1 
                    #208
                    elif x == 13:
                        if input_box[0] > 0 and input_box[6] > 0:
                            input_possiblity[x] += 1 
                        input_box[0] -= 6
                        input_box[6] -= 1  

    return input_possiblity, input_box


def add_0():
    print(cal)
    L76_112_152_180[0] += cal
def add_1():
    print(cal)
    L76_112_152_180[0] += cal
def add_1():
    print(cal)
    L76_112_152_180[0] += cal
def add_1():
    print(cal)
    L76_112_152_180[0] += cal



if __name__ == '__main__':
#                   2HUL 2UL WUL01 WUL03 HU   U  MU   ETC
     input_boxess = [20, 300, 300, 300, 200, 300, 300, 20]
     print('2HUL :',input_boxess[0])
     print('2UL :',input_boxess[1])
     print('WUL01 :',input_boxess[2])
     print('WUL03 :',input_boxess[3])
     print('HU :',input_boxess[4])
     print('U :',input_boxess[5])
     print('MU :',input_boxess[6])
     print('ETC :',input_boxess[7])
     print()
     calculation = box.calculation()
     possibility = calculation.calculate_possibility(input_boxess)
     possibility, boxes_cnt = del_input_boxes(possibility=possibility, input_box=input_boxess)
     box = box.pattern()
     pattern_keys = list(box.get_pattern("get_all").keys())
     L76_112_152_180=[0,0,0,0]

     for j in range(len(possibility)):
         print(f"Type {pattern_keys[j]} : {possibility[j]}")

         if pattern_keys[j] == 101 :
             cal = possibility[j]*0.5
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal

         elif pattern_keys[j] == 102 :
             cal = possibility[j]*0.5
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal

         elif pattern_keys[j] == 103 :
             cal = possibility[j]*0.5
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal

         elif pattern_keys[j] == 104 :
             cal = possibility[j]*0.5
             print('input to stack type : ',(cal))
             L76_112_152_180[3] += cal

         elif pattern_keys[j] == 105 :
             cal = possibility[j]*0.5
             print('input to stack type : ',(cal))
             L76_112_152_180[3] += cal

         elif pattern_keys[j] == 106 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal
             print()

         elif pattern_keys[j] == 201 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal

         elif pattern_keys[j] == 202 :
             cal = possibility[j]*0.5
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal

         elif pattern_keys[j] == 203 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[0] += cal

         elif pattern_keys[j] == 204 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[2] += cal

         elif pattern_keys[j] == 205 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[1] += cal

         elif pattern_keys[j] == 206 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[1] += cal
            
         elif pattern_keys[j] == 207 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[2] += cal
        
         elif pattern_keys[j] == 208 :
             cal = possibility[j]
             print('input to stack type : ',(cal))
             L76_112_152_180[1] += cal



print('')
print('type 76 : ',L76_112_152_180[0],' stack')
print('type 112 : ',L76_112_152_180[1],' stack')
print('type 152 : ',L76_112_152_180[2],' stack')
print('type 180 : ',L76_112_152_180[3],' stack')
print('')


def print_result(fit_name, fit_result):
    print(fit_name + " Result: ", fit_result, 'Length:', len(fit_result.bins))
    for bin in fit_result.bins:
        used_volume = bin.volume - bin.available_volume
        used_percentage = used_volume / bin.volume
        print(used_volume,'/', bin.volume, bin.items, used_percentage, '%')
        # print(bin.total_bins)

# bin_size = random.randint(10,100)
# fit_these = [random.randint(1, bin_size) for _ in range(1000)]

# print(fit_these)
x76=L76_112_152_180[0]
x112=L76_112_152_180[1]
x152=L76_112_152_180[2]
x180=L76_112_152_180[3]

math.ceil(x76)
math.ceil(x112)
math.ceil(x152)
math.ceil(x180)

print('use type76',math.ceil(x76))
print('use type112',math.ceil(x112))
print('use type152',math.ceil(x152))
print('use type180',math.ceil(x180))
print()

#to con

bin_size = 1200
fit_these = []

for i in range(math.ceil(x76)): 
    fit_these.append(76)

for i in range(math.ceil(x112)): 
    fit_these.append(112)

for i in range(math.ceil(x152)): 
    fit_these.append(152)

for i in range(math.ceil(x180)): 
    fit_these.append(180)
    

# for i in range(100): 
#     fit_these.append(76)

# for i in range(0): 
#     fit_these.append(112)

# for i in range(152): 
#     fit_these.append(152)

# for i in range(55): 
#     fit_these.append(180)


print(fit_these)

# # generic_results = Fit.fit(NumberBin, bin_size, fit_these)
# next_fit_results = Fit.nf(NumberBin, bin_size, fit_these)
# first_fit_results = Fit.ff(NumberBin, bin_size, fit_these)

worst_fit_result = Fit.wf(NumberBin, bin_size, fit_these)
best_fit_result = Fit.bf(NumberBin, bin_size, fit_these)


# sorted_next_fit_results = Fit.nfd(NumberBin, bin_size, fit_these) # not implemented
# sorted_first_fit_results = Fit.ffd(NumberBin, bin_size, fit_these)

sorted_worst_fit_result = Fit.wfd(NumberBin, bin_size, fit_these)
sorted_best_fit_result = Fit.bfd(NumberBin, bin_size, fit_these)


# print_result("Next Fit", next_fit_results)
# print_result("First Fit", first_fit_results)
# print()
# print_result("Worst Fit", worst_fit_result)
# print()
# print_result("Best Fit", best_fit_result)
# print()
# print_result("Next Fit With Sort", next_fit_results) # not implemented
# print_result("First Fit With Sort", sorted_first_fit_results)
print()
print_result("Worst Fit With Sort", sorted_worst_fit_result)
print()
print_result("Best Fit With Sort", sorted_best_fit_result)
print()

# if type(L76_112_152_180[0]%1) == 0 : 
#     print('type 76 -0.5')



if L76_112_152_180[0]-(math.ceil(x76)) < 0:
    print('type 76 -0.5')

if L76_112_152_180[1]-(math.ceil(x112)) < 0:
    print('type 112 -0.5')

if L76_112_152_180[2]-(math.ceil(x152)) < 0:
    print('type 152 -0.5')

if L76_112_152_180[3]-(math.ceil(x180)) < 0:
    print('type 180 -0.5')


