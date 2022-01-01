import numpy as np
class box_info:
    def __init__(self, box_name=None) -> None:
        self.BOX_INFO = [[76, 109, 112], [76, 73, 112], [76, 54, 112], [110, 73, 180], [152, 73, 222], [152, 85, 222], [110, -99, 150], [110, 109, 180]]
        self.BOX_NAME = ['HU', 'U', 'MU', '2UL', 'WUL03', 'WUL01', 'ETC', '2HUL']
        self.BOXES = self.make_obj()
    def find_info(self, box_name=None):
        index = 0
        for name in self.BOX_NAME:
            if name.upper() == box_name:
                index = self.BOX_NAME.index(name)
        width = self.BOX_INFO[index][0]
        height = self.BOX_INFO[index][1]
        length = self.BOX_INFO[index][2]
        return [width, height, length]
    def make_obj(self):
        boxes_obj = []
        for index, info in enumerate(self.BOX_INFO):
            boxes_obj.append(box(info[0], info[1], info[2], self.BOX_NAME[index]))
        return boxes_obj
    def get_box_name(self):
        return self.BOX_NAME

class box:
    def __init__(self, width, height, length, name) -> None:
        self.width = width
        self.height = height
        self.length = length
        self.name = name
    def get_info(self):
        return [self.width, self.height, self.length, self.name]

class pattern:
    def __init__(self) -> None:
        pass
    def get_pattern(self, type):
        same_type_stacking = {
            101 : [["HU"], ["HU"]],
            102 : [["U"], ["U"], ["U"]],
            103 : [["MU"], ["MU"], ["MU"], ["MU"]],
            104 : [["2HUL"], ["2HUL"]], 
            105 : [["2UL"], ["2UL"], ["2UL"]],
            106 : [["WUL03"], ["WUL03"], ["WUL03"]] 
        }
        mix_type_stacking = {
            201 : [["HU"], ["MU"], ["MU"]],
            202 : [["ETC"], ["U"]],
            203 : [["ETC"], ["MU"]],
            204 : [["WUL01"], ["ETC"]],
            205 : [['2HUL'], ["HU", "HU", "HU"]],
            206 : [["2UL"], ["U", "U", "U"], ["U", "U", "U"]],
            207 : [["WUL03"], ["WUL03"], ["WUL01"]], 
            208 : [["2HUL"], ["MU", "MU", "MU"], ["MU", "MU", "MU"]]
        }  
        return_thing = None
        if type == "same_type":
            return_thing = same_type_stacking
        elif type == "get_all" :
            return_thing = {**same_type_stacking, **mix_type_stacking}
        else :
            return_thing = mix_type_stacking
        return return_thing
    def get_info(self, type, id):
        # w h l
        same_type_stacking = {
            101 : [76 / 1000, 109*2 /1000, 112 / 1000],
            102 : [76 / 1000, 73*3 / 1000, 112 / 1000],
            103 : [76 / 1000, 54 * 4 / 1000, 112 / 1000],
            104 : [110 / 1000, 109 * 2 / 1000, 180 / 1000], 
            105 : [110 / 1000, 73 * 2 / 1000, 180 / 1000],
            106 : [152 / 1000, 73 * 3 / 1000, 222 / 1000] 
        }
        mix_type_stacking = {
            201 : [76 / 1000, ((54 * 2) + 109) / 1000, 112 / 1000],
            202 : [76 / 1000, (73 + 100) / 1000, 112 / 1000],
            203 : [76 / 1000, (100 + 54) / 1000, 112 / 1000],
            204 : [(110+110) / 1000, (100 + 85) / 1000, 150 / 1000],
            205 : [(76 + 76 + 76) / 1000, (109 + 109) / 1000, 112 / 1000],
            206 : [(76 + 76 + 76) / 1000, (54 + 54 + 73) / 1000, 112 / 1000 ],
            207 : [152 / 1000, (85 + 73 + 73) / 1000, 222 / 1000], 
            208 : [(76 + 76 + 76) / 1000, (54 + 54 + 109) / 1000, + 112 / 1000]
        }
        if type == 'same_type':
            return same_type_stacking[id]
        else :
            return mix_type_stacking[id]
class calculation:
    def __init__(self) -> None:
        self.pattern_arr = np.zeros((14, 8))
        self.pattern = pattern()
    def calculate_possibility(self, input_box):
        stackable_info = np.zeros((14, 8))
        stackable_info[0][0] = 2
        stackable_info[1][1] = 3
        stackable_info[2][2] = 4
        stackable_info[3][6] = 2
        stackable_info[4][3] = 3
        stackable_info[5][4] = 3
        stackable_info[6][0] = 1
        stackable_info[6][2] = 2
        stackable_info[7][7] = 1
        stackable_info[7][1] = 1
        stackable_info[8][7] = 1
        stackable_info[8][2] = 1
        stackable_info[9][5] = 1
        stackable_info[9][7] = 1
        stackable_info[10][0] = 3
        stackable_info[10][6] = 1
        stackable_info[11][3] = 1
        stackable_info[11][1] = 6
        stackable_info[12][4] = 2
        stackable_info[12][5] = 1
        stackable_info[13][2] = 6
        stackable_info[13][6] = 1
        self.pattern_arr = stackable_info
        pos_arr = []
        for item in stackable_info:
            truly_have = 0
            for idx, box in enumerate(input_box):
                if item[idx] != 0:
                    if box >= item[idx] :
                        truly_have += box
                    else :
                        truly_have -= 99
            pos_arr.append((truly_have * 100) / np.sum(item)) 
        stackable_name_n_pattern = self.pattern.get_pattern("get_all")
        cnt = 0
        # for key in stackable_name_n_pattern.keys():
        #     print(f"Type {key} : {int(pos_arr[cnt])} | Possible counted number of this type to be made : {int(pos_arr[cnt] / 100)}")
        #     cnt += 1
        return pos_arr
    def get_pattern(self):
        return self.pattern_arr
