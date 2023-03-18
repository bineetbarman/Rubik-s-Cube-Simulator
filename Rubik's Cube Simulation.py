import tkinter

###FUNDAMENTAL DATA STRUCTURE

##DATA

#to maintain control between rapid keypresses
cont = 0

#location of all points
cube_coordinates = {(-1, 1, 1): {'f': [[-180, 60, 180], [-180, 180, 180], [-60, 180, 180], [-60, 60, 180]], 'l': [[-180, 60, 60], [-180, 60, 180], [-180, 180, 180], [-180, 180, 60]], 'u': [[-180, 180, 180], [-180, 180, 60], [-60, 180, 60], [-60, 180, 180]]},
                    (0, 1, 1): {'f': [[-60, 60, 180], [-60, 180, 180], [60, 180, 180], [60, 60, 180]], 'u': [[-60, 180, 180], [-60, 180, 60], [60, 180, 60], [60, 180, 180]]},
                    (1, 1, 1): {'f': [[60, 60, 180], [60, 180, 180], [180, 180, 180], [180, 60, 180]], 'u': [[60, 180, 180], [60, 180, 60], [180, 180, 60], [180, 180, 180]], 'r': [[180, 60, 180], [180, 180, 180], [180, 180, 60], [180, 60, 60]]},
                    (-1, 0, 1): {'f': [[-180, -60, 180], [-180, 60, 180], [-60, 60, 180], [-60, -60, 180]], 'l': [[-180, -60, 180], [-180, 60, 180], [-180, 60, 60], [-180, -60, 60]]},
                    (0, 0, 1): {'f': [[-60, -60, 180], [-60, 60, 180], [60, 60, 180], [60, -60, 180]]},
                    (1, 0, 1): {'f': [[60, -60, 180], [60, 60, 180], [180, 60, 180], [180, -60, 180]], 'r': [[180, -60, 180], [180, 60, 180], [180, 60, 60], [180, -60, 60]]},
                    (-1, -1, 1): {'f': [[-180, -180, 180], [-180, -60, 180], [-60, -60, 180], [-60, -180, 180]], 'l': [[-180, -180, 180], [-180, -60, 180], [-180, -60, 60], [-180, -180, 60]], 'd': [[-180, -180, 180], [-180, -180, 60], [-60, -180, 60], [-60, -180, 180]]},
                    (0, -1, 1): {'f': [[-60, -180, 180], [-60, -60, 180], [60, -60, 180], [60, -180, 180]], 'd': [[-60, -180, 180], [-60, -180, 60], [60, -180, 60], [60, -180, 180]]},
                    (1, -1, 1): {'f': [[60, -180, 180], [60, -60, 180], [180, -60, 180], [180, -180, 180]], 'd': [[60, -180, 180], [60, -180, 60], [180, -180, 60], [180, -180, 180]], 'r': [[180, -180, 180], [180, -60, 180], [180, -60, 60], [180, -180, 60]]},
                    (-1, 1, 0): {'l': [[-180, 60, 60], [-180, 180, 60], [-180, 180, -60], [-180, 60, -60]], 'u': [[-180, 180, 60], [-180, 180, -60], [-60, 180, -60], [-60, 180, 60]]},
                    (0, 1, 0): {'u': [[-60, 180, 60], [-60, 180, -60], [60, 180, -60], [60, 180, 60]]},
                    (1, 1, 0): {'u': [[60, 180, 60], [60, 180, -60], [180, 180, -60], [180, 180, 60]], 'r': [[180, 60, 60], [180, 180, 60], [180, 180, -60], [180, 60, -60]]},
                    (-1, 0, 0): {'l': [[-180, -60, 60], [-180, 60, 60], [-180, 60, -60], [-180, -60, -60]]},
                    (1, 0, 0): {'r': [[180, -60, 60], [180, 60, 60], [180, 60, -60], [180, -60, -60]]},
                    (-1, -1, 0): {'l': [[-180, -180, 60], [-180, -60, 60], [-180, -60, -60], [-180, -180, -60]], 'd': [[-180, -180, 60], [-180, -180, -60], [-60, -180, -60], [-60, -180, 60]]},
                    (0, -1, 0): {'d': [[-60, -180, 60], [-60, -180, -60], [60, -180, -60], [60, -180, 60]]},
                    (1, -1, 0): {'d': [[60, -180, 60], [60, -180, -60], [180, -180, -60], [180, -180, 60]], 'r': [[180, -180, 60], [180, -60, 60], [180, -60, -60], [180, -180, -60]]},
                    (-1, 1, -1): {'b': [[-180, 60, -180], [-180, 180, -180], [-60, 180, -180], [-60, 60, -180]], 'l': [[-180, 60, -60], [-180, 180, -60], [-180, 180, -180], [-180, 60, -180]], 'u': [[-180, 180, -60], [-180, 180, -180], [-60, 180, -180], [-60, 180, -60]]},
                    (0, 1, -1): {'b': [[-60, 60, -180], [-60, 180, -180], [60, 180, -180], [60, 60, -180]], 'u': [[-60, 180, -60], [-60, 180, -180], [60, 180, -180], [60, 180, -60]]},
                    (1, 1, -1): {'b': [[60, 60, -180], [60, 180, -180], [180, 180, -180], [180, 60, -180]], 'u': [[60, 180, -60], [60, 180, -180], [180, 180, -180], [180, 180, -60]], 'r': [[180, 60, -60], [180, 180, -60], [180, 180, -180], [180, 60, -180]]},
                    (-1, 0, -1): {'b': [[-180, -60, -180], [-180, 60, -180], [-60, 60, -180], [-60, -60, -180]], 'l': [[-180, -60, -60], [-180, 60, -60], [-180, 60, -180], [-180, -60, -180]]},
                    (0, 0, -1): {'b': [[-60, -60, -180], [-60, 60, -180], [60, 60, -180], [60, -60, -180]]},
                    (1, 0, -1): {'b': [[60, -60, -180], [60, 60, -180], [180, 60, -180], [180, -60, -180]], 'r': [[180, -60, -60], [180, 60, -60], [180, 60, -180], [180, -60, -180]]},
                    (-1, -1, -1): {'b': [[-180, -180, -180], [-180, -60, -180], [-60, -60, -180], [-60, -180, -180]], 'l': [[-180, -180, -60], [-180, -60, -60], [-180, -60, -180], [-180, -180, -180]], 'd': [[-180, -180, -60], [-180, -180, -180], [-60, -180, -180], [-60, -180, -60]]},
                    (0, -1, -1): {'b': [[-60, -180, -180], [-60, -60, -180], [60, -60, -180], [60, -180, -180]], 'd': [[-60, -180, -60], [-60, -180, -180], [60, -180, -180], [60, -180, -60]]},
                    (1, -1, -1): {'b': [[60, -180, -180], [60, -60, -180], [180, -60, -180], [180, -180, -180]], 'd': [[60, -180, -60], [60, -180, -180], [180, -180, -180], [180, -180, -60]], 'r': [[180, -180, -60], [180, -60, -60], [180, -60, -180], [180, -180, -180]]}}

#state of Rubik's Cube
mother_cube_state = {(-1,1,1)  :{'f':'r','l':'y','u':'g'}, (0,1,1)  :{'f':'r','u':'g'}, (1,1,1)  :{'f':'r','u':'g','r':'p'},
             (-1,0,1)  :{'f':'r','l':'y'}        , (0,0,1)  :{'f':'r'}        , (1,0,1)  :{'f':'r','r':'p'}        ,
             (-1,-1,1) :{'f':'r','l':'y','d':'b'}, (0,-1,1) :{'f':'r','d':'b'}, (1,-1,1) :{'f':'r','d':'b','r':'p'},
             
             (-1,1,0)  :{'l':'y','u':'g'}        , (0,1,0)  :{'u':'g'}        , (1,1,0)  :{'u':'g','r':'p'}        ,
             (-1,0,0)  :{'l':'y'}                                             , (1,0,0)  :{'r':'p'}                ,
             (-1,-1,0) :{'l':'y','d':'b'}        , (0,-1,0) :{'d':'b'}        , (1,-1,0) :{'d':'b','r':'p'}        ,
             
             (-1,1,-1) :{'b':'o','l':'y','u':'g'}, (0,1,-1) :{'b':'o','u':'g'}, (1,1,-1) :{'b':'o','u':'g','r':'p'},
             (-1,0,-1) :{'b':'o','l':'y'}        , (0,0,-1) :{'b':'o'}        , (1,0,-1) :{'b':'o','r':'p'}        ,
             (-1,-1,-1):{'b':'o','l':'y','d':'b'}, (0,-1,-1):{'b':'o','d':'b'}, (1,-1,-1):{'b':'o','d':'b','r':'p'}}

cube_state = {(-1,1,1)  :{'f':'r','l':'y','u':'g'}, (0,1,1)  :{'f':'r','u':'g'}, (1,1,1)  :{'f':'r','u':'g','r':'p'},
             (-1,0,1)  :{'f':'r','l':'y'}        , (0,0,1)  :{'f':'r'}        , (1,0,1)  :{'f':'r','r':'p'}        ,
             (-1,-1,1) :{'f':'r','l':'y','d':'b'}, (0,-1,1) :{'f':'r','d':'b'}, (1,-1,1) :{'f':'r','d':'b','r':'p'},
             
             (-1,1,0)  :{'l':'y','u':'g'}        , (0,1,0)  :{'u':'g'}        , (1,1,0)  :{'u':'g','r':'p'}        ,
             (-1,0,0)  :{'l':'y'}                                             , (1,0,0)  :{'r':'p'}                ,
             (-1,-1,0) :{'l':'y','d':'b'}        , (0,-1,0) :{'d':'b'}        , (1,-1,0) :{'d':'b','r':'p'}        ,
             
             (-1,1,-1) :{'b':'o','l':'y','u':'g'}, (0,1,-1) :{'b':'o','u':'g'}, (1,1,-1) :{'b':'o','u':'g','r':'p'},
             (-1,0,-1) :{'b':'o','l':'y'}        , (0,0,-1) :{'b':'o'}        , (1,0,-1) :{'b':'o','r':'p'}        ,
             (-1,-1,-1):{'b':'o','l':'y','d':'b'}, (0,-1,-1):{'b':'o','d':'b'}, (1,-1,-1):{'b':'o','d':'b','r':'p'}}
#faces
cube_face = {'u' : ((-1,1,1),(0,1,1),(1,1,1),(-1,1,0),(0,1,0),(1,1,0),(-1,1,-1),(0,1,-1),(1,1,-1)),
             'f' : ((-1,1,1),(0,1,1),(1,1,1),(-1,0,1),(0,0,1),(1,0,1),(-1,-1,1),(0,-1,1),(1,-1,1)),
             'r' : ((1,1,1),(1,0,1),(1,-1,1),(1,1,0),(1,0,0),(1,-1,0),(1,1,-1),(1,0,-1),(1,-1,-1)),
             'd' : ((-1,-1,1),(0,-1,1),(1,-1,1),(-1,-1,0),(0,-1,0),(1,-1,0),(-1,-1,-1),(0,-1,-1),(1,-1,-1)),
             'b' : ((-1,1,-1),(0,1,-1),(1,1,-1),(-1,0,-1),(0,0,-1),(1,0,-1),(-1,-1,-1),(0,-1,-1),(1,-1,-1)),
             'l' : ((-1,1,1),(-1,0,1),(-1,-1,1),(-1,1,0),(-1,0,0),(-1,-1,0),(-1,1,-1),(-1,0,-1),(-1,-1,-1)),
             'e' : ((-1,0,1),(0,0,1),(1,0,1),(-1,0,0),(1,0,0),(-1,0,-1),(0,0,-1),(1,0,-1)),
             'm' : ((0,1,1),(0,0,1),(0,-1,1),(0,1,0),(0,-1,0),(0,1,-1),(0,0,-1),(0,-1,-1)),
             's' : ((-1,1,0),(0,1,0),(1,1,0),(-1,0,0),(1,0,0),(-1,-1,0),(0,-1,0),(1,-1,0))}

abbre = {'f':'Front', 'b':'Back', 'u':'Upper',
         'd':'Down', 'r':'Right', 'l':'Left',
         's':'Standing', 'e':'Equatorial', 'm':'Middle'}
#antenna(towards right, upper, front face respectively)
arrow_r = [[10],[0],[0]]
arrow_u = [[0],[10],[0]]
arrow_f = [[0],[0],[10]]

#inner plates
#important (in CLOCKWISE order)
#for function 'inner_render'
inner = {'r':((60,180,180),(60,180,-180),(60,-180,-180),(60,-180,180)),
         'u':((-180,60,180),(-180,60,-180),(180,60,-180),(180,60,180)),
         'f':((-180,180,60),(180,180,60),(180,-180,60),(-180,-180,60)),
         'l':((-60,180,180),(-60,180,-180),(-60,-180,-180),(-60,-180,180)),
         'd':((-180,-60,180),(-180,-60,-180),(180,-60,-180),(180,-60,180)),
         'b':((-180,180,-60),(180,180,-60),(180,-180,-60),(-180,-180,-60))}

#how position of face sticker changes with a certain turn
#some faces are excluded
#Eg: when turning Front face (clockwise),
#stickers on front remain on front while those on down come at left
x_order = ('d','b','u','f')
y_order = ('r','b','l','f')
z_order = ('l','d','r','u')

color_code = {'r':'red','o':'lightpink','y':'yellow',
              'g':'lightgreen','b':'blue','p':'indigo'}

#how position of cubelet changes with turn
clock_order = {-1:{(-1,1):(1,1) ,(0,1)  :(1,0) ,(1,1) :(1,-1),
                   (1,0) :(0,-1),               (1,-1):(-1,-1),
                   (0,-1):(-1,0),(-1,-1):(-1,1),(-1,0):(0,1)},
               1:{(1,1) :(-1,1), (1,0):(0,1), (1,-1):(1,1),
                  (0,-1):(1,0),              (-1,-1):(1,-1),
                  (-1,0):(0,-1), (-1,1):(-1,-1), (0,1):(-1,0)}}

#faces on same axis in order
same_axis = {'x':('r','m','l'),'-x':('l','m','r'),'y':('u','e','d'),'-y':('d','e','u'),'z':('f','s','b'),'-z':('b','s','f')}
num_axis = {1:{1:'r',0:'m',-1:'l'},2:{1:'u',0:'e',-1:'d'},3:{1:'f',0:'s',-1:'b'}}

#rotation matrices
angle_turn = {15:(0.9659258262890683, 0.25881904510252074),
              30:(0.8660254037844387, 0.49999999999999994),
              45:(0.7071067811865476, 0.7071067811865476),
              60:(0.5000000000000001, 0.8660254037844386),
              75:(0.25881904510252074, 0.9659258262890683),
              -15:(0.9659258262890683, -0.25881904510252074),
              -30:(0.8660254037844387, -0.49999999999999994),
              -45:(0.7071067811865476, -0.7071067811865476),
              -60:(0.5000000000000001, -0.8660254037844386),
              -75:(0.25881904510252074, -0.9659258262890683)}

cos_15 = 0.9659258262890683
sin_15 = 0.25881904510252074

x_mat = ((1,       0,      0),
         (0,  cos_15,-sin_15),
         (0,  sin_15, cos_15))

y_mat = (( cos_15, 0,  sin_15),
         (      0, 1,       0),
         (-sin_15, 0,  cos_15))

z_mat = (( cos_15,-sin_15, 0),
         ( sin_15, cos_15, 0),
         (      0,      0, 1))

xc_mat = ((1,       0,      0),
         (0,  cos_15,sin_15),
         (0,  -sin_15, cos_15))

yc_mat = (( cos_15, 0,  -sin_15),
         (      0, 1,       0),
         (sin_15, 0,  cos_15))

zc_mat = (( cos_15,sin_15, 0),
         ( -sin_15, cos_15, 0),
         (      0,      0, 1))

cur_mat = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]

rot_code = {1:x_mat, 2:y_mat, 3:z_mat, 4:xc_mat, 5:yc_mat, 6:zc_mat}

##FUNCTIONS

#matrix multiplication
def mat_mul(left, right):
    cols_right = len(right[0])
    rows_right = len(right)
    new = []
    for row in left:
        new.append([])
        for column in range(cols_right):
            new_ele = 0
            for ele in range(rows_right):
                new_ele += row[ele]*right[ele][column]
            new[-1].append(new_ele)
    return new

#matrix creater
def mat_cre(axis, angle):
    cos = angle_turn[angle][0]
    sin = angle_turn[angle][1]
    if axis == 'x':
        return ((1,   0,    0),
                (0, cos, -sin),
                (0, sin,  cos))
    elif axis == 'y':
        return (( cos, 0, sin),
                (   0, 1,   0),
                (-sin, 0, cos))
    else:
        return ((cos, -sin, 0),
                (sin,  cos, 0),
                (  0,    0, 1))

#x = -1(left), 0(middle), 1(right)
#n = 1(anti_clockwise), -1(clockwise) 
def x_turn(x,n):
    global cube_state
    temp_x = {}
    for y,z in clock_order[n]:
        #changing a cubelet's position
        new_position = (x,)+clock_order[n][y,z]
        temp_x[new_position] = {}
        cubelet_info = cube_state[x,y,z]
        for sticker in cubelet_info:
            #sticker = face direction
            if sticker in x_order:
                new_sticker = x_order[(x_order.index(sticker) + n)%4]
                temp_x[new_position][new_sticker] = cubelet_info[sticker]
            else:
                temp_x[new_position][sticker] = cubelet_info[sticker]
    cube_state.update(temp_x)

#y = -1(down), 0(equatorial), 1(top)
def y_turn(y, n):
    global cube_state
    temp_y = {}
    for z,x in clock_order[n]:
        new_position = clock_order[n][z,x][1],y,clock_order[n][z,x][0]
        temp_y[new_position] = {}
        cubelet_info = cube_state[x,y,z]
        for sticker in cubelet_info:
            if sticker in y_order:
                new_sticker = y_order[(y_order.index(sticker) + n)%4]
                temp_y[new_position][new_sticker] = cubelet_info[sticker]
            else:
                temp_y[new_position][sticker] = cubelet_info[sticker]
    cube_state.update(temp_y)

#z = -1(back), 0(standing), 1(front)
def z_turn(z, n):
    global cube_state
    temp_z = {}
    for x,y in clock_order[n]:
        new_position = clock_order[n][x,y]+(z,)
        temp_z[new_position] = {}
        cubelet_info = cube_state[x,y,z]
        for sticker in cubelet_info:
            if sticker in z_order:
                new_sticker = z_order[(z_order.index(sticker) + n)%4]
                temp_z[new_position][new_sticker] = cubelet_info[sticker]
            else:
                temp_z[new_position][sticker] = cubelet_info[sticker]
    cube_state.update(temp_z)

#dictionery of turn
f_turn = {1:x_turn, 2:y_turn, 3:z_turn}

#to rotate view by 15°
#n = key for specific matrix
def rot(n):
    global cur_mat
    cur_mat = mat_mul(rot_code[n], cur_mat)

#changing orientation
def orient(a):
    for i in (1,0,-1):
        f_turn[a[0]](i,a[1])
    coloring()

###GRAPHIC RENDER

##BASE WIDGETS
    
#main application window               
wn = tkinter.Tk()
wn.title("Rubik's Cube Simulator")
wn.rowconfigure(0, weight = 1, minsize = 700)
wn.columnconfigure(0, weight = 1, minsize = 700)

#frame for canvas
#its minsize + 2*bd = minsize of canvas (to compensate for border)
fra_canvas = tkinter.Frame(bg = 'white', relief = 'sunken', bd = 10)

#this panel will show the cube in 3-D
view = tkinter.Canvas(master = fra_canvas, width = 700, height = 700,
                      bg='white', bd = 0, highlightthickness = 0)
view.grid(row = 0, column = 0)
fra_canvas.grid(row = 0, column = 0, sticky = 'nsew')
fra_canvas.rowconfigure(0, weight = 1, minsize = 680)
fra_canvas.columnconfigure(0, weight = 1, minsize = 700)

##FUNCTIONS

#collects default proper input for function 'nearest'
def feed():
    arrows = dict(zip(('a_r', 'a_u', 'a_f'),(arrow_r, arrow_u, arrow_f)))
    for i in arrows:
        x,y,z = arrows[i]
        n1,n2,n3 = mat_mul(cur_mat, (x,y,z))
        arrows[i] = (n1,n2,n3)
    return arrows

#finds nearest point
def nearest(a_r, a_u, a_f):
    near = ''
    d = {1:a_r, 2:a_u, 3:a_f}
    for i in d:
        if d[i][-1][-1] >= 0:
            near += num_axis[i][1]
        else:
            near += num_axis[i][-1]
    return near

#finds farthest face to nearest point along turning axis
def farthest(layer):
    near = nearest(**feed())
    for axis in same_axis:
        if layer in same_axis[axis]:
            for face in near:
                if face in same_axis[axis][-1]:
                    n1,n2,n3 = same_axis[axis]
                    return n1+n2+n3
                
#draws specified sides of cubelets (but does not update)
def draw(keys, faces, coor):
    for key in keys:
        for face in faces:
            if face in cube_state[key]:
                n1,n2,n3,n4 = coor[key][face]
                view.create_polygon(n1[0]+350,-n1[1]+350,n2[0]+350,-n2[1]+350,
                                    n3[0]+350,-n3[1]+350,n4[0]+350,-n4[1]+350,
                                    fill = color_code[cube_state[key][face]], outline = 'black', width = 8)

#draws in_between layer
def inner_render(layer, near, mat):
    if layer in ['e','s','m']:
        for i in 'xyz':
            for j in near:
                if layer in same_axis[i] and j in same_axis[i]:
                    d = j
                    break
        t = []
        for p in inner[d]:
            x,y,z = p
            n1,n2,n3 = mat_mul(mat, ([x],[y],[z]))
            t.extend((n1[0],n2[0]))
        view.create_polygon(t[0]+350,-t[1]+350,t[2]+350,-t[3]+350,t[4]+350,-t[5]+350,t[6]+350,-t[7]+350,
                        fill = 'black', outline = 'black', width = 8)
    elif layer not in near:
        t = []
        for p in inner[layer]:
            x,y,z = p
            n1,n2,n3 = mat_mul(mat, ([x],[y],[z]))
            t.extend((n1[0],n2[0]))
        view.create_polygon(t[0]+350,-t[1]+350,t[2]+350,-t[3]+350,t[4]+350,-t[5]+350,t[6]+350,-t[7]+350,
                        fill = 'black', outline = 'black', width = 8)

#calculates coordinates for partial turn
#sign = 1(anti_clockwise), -1(clockwise)
def partial_turn(layer, angle, sign):
    for ax in same_axis:
        if layer in same_axis[ax] and ax[0] != '-':
            axis = ax
            break

    matri = mat_cre(axis, angle*sign)
    temp = dict()
    for cube in cube_face[layer]:
        temp[cube] = dict()
        for sticker in cube_state[cube]:
            temp[cube][sticker] = []
            for po in cube_coordinates[cube][sticker]:
                x,y,z = po
                x,y,z = mat_mul(cur_mat, mat_mul(matri,([x],[y],[z])))
                temp[cube][sticker].append((x[0],y[0],z[0]))

    arrows = dict(zip(('a_r', 'a_u', 'a_f'),(arrow_r, arrow_u, arrow_f)))
    for i in arrows:
        x,y,z = arrows[i]
        n1,n2,n3 = mat_mul(cur_mat, mat_mul(matri,(x,y,z)))
        arrows[i] = (n1,n2,n3)

    near = nearest(**arrows)
    draw(cube_face[layer], near, temp)
    inner_render(layer, near, mat_mul(cur_mat, matri))

#updates for orientation
def main_render(near_point):
    for face in near_point:
        for cube in cube_face[face]:
            for st in cube_state[cube]:
                t = []
                if st in near_point:
                    for coor in cube_coordinates[cube][st]:
                        x,y,z = coor
                        n1,n2,n3 = mat_mul(cur_mat, ([x],[y],[z]))
                        t.extend((n1[0],n2[0]))
                    view.create_polygon(t[0]+350,-t[1]+350,t[2]+350,-t[3]+350,t[4]+350,-t[5]+350,t[6]+350,-t[7]+350,
                                    fill = color_code[cube_state[cube][st]], outline = 'black', width = 8)
    view.update()

#updates screen for each frame of turning
#layer = [axis_number, along_axis_number, sense_of_rotation]
def turn_render(layer, turn_func):
    near = nearest(**feed())
    seq = farthest(num_axis[layer[0]][layer[1]])
    view.delete('all')
    for frame in range(5):
        for i in seq:
            if i == num_axis[layer[0]][layer[1]]:
                partial_turn(i, 15*(1+frame), layer[2])
            else:
                inner_render(i, near, cur_mat)
                temp = dict()
                for j in cube_coordinates:
                    temp[j] = dict()
                    for k in cube_coordinates[j]:
                        temp[j][k] = []
                        for coor in cube_coordinates[j][k]:
                            x,y,z = coor
                            n1,n2,n3 = mat_mul(cur_mat, ([x],[y],[z]))
                            temp[j][k].append((n1[0],n2[0],n3[0]))
                draw(cube_face[i], near, temp)
        view.after(20)
        view.update()
        view.delete('all')
    turn_func(layer[1], layer[2])
    view.after(20)
    main_render(near)


###USER INTERFACE

## FUNCTIONS

#colors panel of face layer with color of centrepiece
def coloring():
    for i in (1,-1):
        fra_dic[num_axis[1][i]]['fra'].configure(bg = color_code[cube_state[i,0,0][num_axis[1][i]]])
    for i in (1,-1):
        fra_dic[num_axis[2][i]]['fra'].configure(bg = color_code[cube_state[0,i,0][num_axis[2][i]]])
    for i in (1,-1):
        fra_dic[num_axis[3][i]]['fra'].configure(bg = color_code[cube_state[0,0,i][num_axis[3][i]]])
    fra_fra.update()

#combines functions with render functions
def comb(func,layer):
    def n(x = 0):
        global cont
        if cont == 0:
            cont = 1
            if func in (rot, orient):
                view.delete('all')
                func(layer)
                main_render(nearest(**feed()))
            else:
                turn_render(layer, func)
                coloring()
                check()
            cont = 0
    return n

#saving
def save():
    import pickle
    fiob = open('rubik_stash', 'wb')
    pickle.dump(cube_state, fiob)
    print('File saved.')

#    
def open_f():
    global cube_state
    try:
        import pickle
        global cube_state
        fiob = open('rubik_stash', 'rb')
        cube_state = pickle.load(fiob)
        print('File loaded.')
    except:
        print('Some error occured. Opening with default settings.')
        reset()

#    
def reset():
    global cube_state
    for i in mother_cube_state:
        for j in mother_cube_state[i]:
            cube_state[i][j]=mother_cube_state[i][j]
    main_render(nearest(**feed()))
    coloring()
    check()

#
def scram():
    from random import choice
    for i in range(20):
        choice((x_turn,y_turn,z_turn))(choice((1,0,-1)),1)
    main_render(nearest(**feed()))
    coloring()
    check()

#
def check():
    found = 0
    for face in ('r','u','f','l','d','b'):
        cubes = tuple(cube_face[face])
        color_check = cube_state[cubes[0]][face]
        for cube in cubes[1:]:
            if color_check != cube_state[cube][face]:
                found = 1
                break
        if found == 1:
            wn.title("Rubik's Cube Simulator")
            break
    else:
        wn.title("Rubik's Cube Simulator [SOLVED!]")

##WIDGETS

#frame containing frame containing buttons
fra_fra = tkinter.Frame(bg = 'white', relief = 'sunken', bd = 10)
fra_fra.grid(row = 0, column = 1, sticky = 'nsew')
fra_fra.rowconfigure(3, weight = 1)

fra_dic = {}
#frames containing buttons
for axis in num_axis:
    for layer, sense in zip(num_axis[axis], (-1,-1,1)):
        layer_name = abbre[num_axis[axis][layer]]
        fra_dic[num_axis[axis][layer]] = dict()
        fra_dic[num_axis[axis][layer]]['fra'] = tkinter.Frame(master = fra_fra,
                                                       bg = 'white',
                                                       relief = 'raised',
                                                       bd = 20)
        fra_dic[num_axis[axis][layer]]['fra'].grid(row = axis-1,
                                                   column = 1-layer,
                                                   sticky = 'nsew')

        fra_axis = fra_dic[num_axis[axis][layer]]['fra']

        fra_axis_but = tkinter.Frame(master = fra_axis,
                                   bg = 'white',
                                   relief = 'groove',
                                   bd = 10)
        fra_axis_but.grid(row = 0, column = 0, sticky = 'nsew')

        label = tkinter.Label(master = fra_axis,
                              font = ('Courier New',11,'italic'),
                              text = layer_name,bg = 'white',
                              relief = 'sunken',bd = 6)
        label.grid(row = 1, column = 0, sticky = 'nsew')

        btn = tkinter.Button(fra_axis_but, text='↻',bg = 'black',fg = 'white',
                             command = comb(f_turn[axis],[axis,layer,sense]),
                             bd = 5, width = 3, height =1,
                             font = ('Calibri',20, 'bold'),
                             activebackground = 'silver')
        btn.grid(row = 0, column = 0, sticky = 'nsew')
        btn = tkinter.Button(fra_axis_but, text='↺',bg = 'black',fg = 'white',
                             command = comb(f_turn[axis],[axis,layer,-sense]),
                             bd = 5, width = 3, height =1,
                             font = ('Calibri',20, 'bold'),
                             activebackground = 'silver')
        btn.grid(row = 0, column = 1, sticky = 'nsew')

#frame containing buttons for rotation for full cube
fra_rot = tkinter.Frame(master = fra_fra, bg = 'silver', relief = 'raised', bd = 10)
fra_rot.grid(row = 3, column = 0, sticky = 'nsew')
fra_rot.rowconfigure([0,1,2], weight = 1)
fra_rot.columnconfigure([0,1,2], weight = 1)

for i in zip('xyz',(1,2,3), ('PITCH','YAW','ROLL')):
    label = tkinter.Label(master = fra_rot,
                      font = ('Courier New',10,'italic'),
                      width = 7, height = 3,
                      text = i[2],bg = 'white',
                      relief = 'raised',bd = 6)
    label.grid(row = i[1]-1, column = 0, sticky = 'nsew')

    btn = tkinter.Button(fra_rot, text='↻',bg = 'black',fg = 'white',
                         command = comb(rot, i[1]+3 ),
                         bd = 5,
                         font = ('Calibri',10, 'bold'),
                         activebackground = 'silver')
    btn.grid(row = i[1]-1, column = 1, sticky = 'nsew')

    btn = tkinter.Button(fra_rot, text='↺',bg = 'black',fg = 'white',
                         command = comb(rot, i[1] ),
                         bd = 5,
                         font = ('Calibri',10, 'bold'),
                         activebackground = 'silver')
    btn.grid(row = i[1]-1, column = 2, sticky = 'nsew')


#frame for orientations
fra_ori = tkinter.Frame(master = fra_fra, bg = 'silver', relief = 'raised', bd = 10)
fra_ori.grid(row = 3, column = 1, sticky = 'nsew')
fra_ori.rowconfigure([0,1,2], weight = 1)
fra_ori.columnconfigure([0,1,2], weight = 1)

for i in zip('xyz',(0,1,2)):
    label = tkinter.Label(master = fra_ori,
                      font = ('Courier New',10,'italic'),
                      width = 7, height = 3,
                      text = i[0], bg = 'white',
                      relief = 'raised',bd = 6)
    label.grid(row = i[1], column = 0, sticky = 'nsew')

    btn = tkinter.Button(fra_ori, text='↻',bg = 'black',fg = 'white',
                         command = comb(orient, [ i[1]+1, -1]),
                         bd = 5,
                         font = ('Calibri',10, 'bold'),
                         activebackground = 'silver')
    btn.grid(row = i[1], column = 1, sticky = 'nsew')

    btn = tkinter.Button(fra_ori, text='↺',bg = 'black',fg = 'white',
                         command = comb(orient, [ i[1]+1, 1]),
                         bd = 5,
                         font = ('Calibri',10, 'bold'),
                         activebackground = 'silver')
    btn.grid(row = i[1], column = 2, sticky = 'nsew')

#frame for options
fra_opt = tkinter.Frame(master = fra_fra, bg = 'silver', relief = 'raised', bd = 10)
fra_opt.grid(row = 3, column = 2, sticky = 'nsew')
fra_opt.rowconfigure([0,1,2], weight = 1)
fra_opt.columnconfigure(0, weight = 1)

#button for reset
btn_reset = tkinter.Button(fra_opt, text='RESET',bg = 'black',fg = 'white',
                         command = reset,
                         bd = 10,
                         font = ('Courier New',15, 'bold'),
                         activebackground = 'silver')
btn_reset.grid(row = 1, column = 0, sticky = 'nsew')

#button for saving
btn_save = tkinter.Button(fra_opt, text='SAVE',bg = 'black',fg = 'white',
                         command = save,
                         bd = 10,
                         font = ('Courier New',15, 'bold'),
                         activebackground = 'silver')
btn_save.grid(row = 0, column = 0, sticky = 'nsew')

#button for scrambling
btn_scram = tkinter.Button(fra_opt, text='SCRAMBLE',bg = 'black',fg = 'white',
                         command = scram,
                         bd = 10,
                         font = ('Courier New',15, 'bold'),
                         activebackground = 'silver')
btn_scram.grid(row = 2, column = 0, sticky = 'nsew')

open_f()
main_render(nearest(**feed()))
coloring()
check()

wn.bind('u',comb(y_turn,[2,1,-1]))
wn.bind('h',comb(x_turn,[1,-1,1]))
wn.bind('j',comb(z_turn,[3,1,-1]))
wn.bind('k',comb(x_turn,[1,1,-1]))
wn.bind('i',comb(z_turn,[3,-1,1]))
wn.bind('n',comb(y_turn,[2,-1,1]))

wn.bind('U',comb(y_turn,[2,1,1]))
wn.bind('H',comb(x_turn,[1,-1,-1]))
wn.bind('J',comb(z_turn,[3,1,1]))
wn.bind('K',comb(x_turn,[1,1,1]))
wn.bind('I',comb(z_turn,[3,-1,-1]))
wn.bind('N',comb(y_turn,[2,-1,-1]))

wn.bind('y',comb(x_turn,[1,0,-1]))
wn.bind('b',comb(z_turn,[3,0,-1]))
wn.bind('m',comb(y_turn,[2,0,1]))

#while checking key bindings, check if Caps Lock is off or on
wn.bind('Y',comb(x_turn,[1,0,1]))
wn.bind('B',comb(z_turn,[3,0,1]))
wn.bind('M',comb(y_turn,[2,0,-1]))

wn.bind('7',comb(rot,3))
wn.bind('9',comb(rot,6))
wn.bind('4',comb(rot,2))
wn.bind('6',comb(rot,5))
wn.bind('8',comb(rot,1))
wn.bind('5',comb(rot,4))

wn.bind('o',comb(orient,(1,-1)))
wn.bind('p',comb(orient,(2,-1)))
wn.bind('l',comb(orient,(3,-1)))

wn.bind('O',comb(orient,(1,1)))
wn.bind('P',comb(orient,(2,1)))
wn.bind('L',comb(orient,(3,1)))

wn.mainloop()
