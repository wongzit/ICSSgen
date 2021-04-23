# ICSSgen v1.4
![icon_full](https://user-images.githubusercontent.com/41381763/115641810-cb666d80-a354-11eb-8a14-ad0d61f1f7b0.png)
Input file generator for ICSS (2D-NICS) calculation.
**ICSSgen homepage** https://www.wangzhe95.net/program-icssgen

Last update: 2021-04-24

Author: Zhe Wang

## Update history
### v1.4 (2021-04-24)
1. Bug fix: Maximum value of ICSS map range (not displayed in older version)
2. Removed quotes module in Windows version.
3. Executable file for Mac could running on both Intel and Apple M1 chip. (macOS 10.15 or newer)
4. Negative grid quality is allowed.
5. Bug of "0" grid value is fixed.
6. Documents updated.
7. Now all executable files are packaged in *execufiles.zip*.

### v1.3.1 (2021-04-22)
1. Executable program file updated, source code is provided.
2. Now a quote will be displayed before termination.
3. Document is updated.

### v1.2.1 (2021-04-21)
1. Now executable file for all platform is available.
2. ~~Source code is deleted.~~

### v1.2 (2021-04-20)
1. Now you can customize grid quality through program.
2. More stable input file reader was introduced.
3. Running on Linux platform was tested.

### v1.1 (2021-04-20)
1. Program will not be terminated by error inputting when specify the map range.
3. Bug fix.

## Platform
### For all platform
Python source code is provided, if your computer already installed Python IDE, you can run ICSSgen with:

`python3 ICSSgen_v14_source.py`

Executable files for macOS/Linux/Windows are in **execufiles.zip**.

**NOTICE:** Python 3.7 or newer is recommended, ICSSgen may not work normally under Python 2.

### For macOS
Executable file **ICSSgen_v14_mac** has been tested on macOS Catalina 10.15.7 (Intel Mac) and Big Sur 11.2.3 (Intel/M1 Mac).

### For Linux
Before running for the first time, you may need to add permission by:
`chmod +x ./path_to_ICSSgen/ICSSgen_v14_linux`

Add following command to environmental variables (for bash):
`alias icssgen=./path_to_ICSS/ICSSgen_v14_linux`
and you can run ICSSgen by `icssgen`.

### For Microsoft Windows
Executable file **ICSSgen_v14_win.exe** has been tested on Windows 10 Education (x64) with Intel Core i7-10700. Double click to run it.

## How to use
**NOTICE:** ICSSgen only generates input file for Gaussian. More details in program manual.

1. Prepare the input file including calculation route lines, title, charge and spin multiplicity, and Cartesian coordinate.

**EXAMPLE: Input file of benzene on XY plane**
```
%nprocshared=8
%mem=10GB
#p nmr=giao rb3lyp/6-31g(d)

Benzene_opt

0 1
 C                 -1.33923600   -0.39585300    0.00000500
 C                 -0.32668500   -1.35773000    0.00006900
 C                  1.01242100   -0.96187800   -0.00005500
 C                  1.33920200    0.39596500    0.00000800
 C                  0.32679800    1.35770000    0.00006200
 C                 -1.01250100    0.96179800   -0.00005800
 H                 -2.38133000   -0.70401000   -0.00006600
 H                 -0.58108600   -2.41424500    0.00007900
 H                  1.80037500   -1.71023400   -0.00015400
 H                  2.38136700    0.70385800    0.00000700
 H                  0.58095200    2.41426700    0.00001800
 H                 -1.80027600    1.71035300   -0.00006300

```

2. Run ICSSgen.

3. Drag the input file to the program, and press Enter. 
```
Please specify the original input file path:
(eg.: /ICSSgen/example/benzene.gjf)
(user input): /Users/wangzhe/Desktop/ICSSgen/example/benzene.gjf 
```

4. Specify the plane for ICSS calculation, please input "xy", "xz" or "yz" (Not case-sensitive).
```
Please specify the plane for ICSS map (XY, XZ, YZ):
(user input): xy
```

5. Specify the altitude  for ICSS calculation, for on-plane calculation, please input 0. The value is in angstrom.
```
Please input the altitude over the plane (in angstrom):
(user input): 1
```

6. Range specification. Please input two numbers (float is okay) separated by space, eg. -10 10, the range will be set as [-10,10].
```
Please specify the range of X axis (in angstrom, eg. -10 10):
(user input): -5 5

Please specify the range of Y axis (in angstrom, eg. -8 8):
(user input): -5.0 5.0
```

7. Grid quality: smaller value will give you a smoother ICSS map but more expensive calculation cost is needed. The default value is 0.2.
```
Please specify the grid quality (value smaller than 0.25 is recommanded):
(press Enter to use default value 0.2)
(user input): 0.2
ICSSgen will use grid quality of 0.2.
```

8. New input file named with **ICSS_plane_altitude.gjf** would be generated.  You can submit this input file for Gaussian calculation. Enjoy!

## Problem
1. ~~Once you get the input file for ICSS calculation, please open it by text editor before submit to Gaussian calculation. Sometimes the unnecessary line-break in original input file may be remain to the ICSS input file, these line-break will cause error during calculation.~~
This problem has been fixed but I still recommand you to check the input file befor submitting to Gaussian.

**Unnecessary line-break**
```
 H                  2.38136700    0.70385800    0.00000700
 H                  0.58095200    2.41426700    0.00001800
 H                 -1.80027600    1.71035300   -0.00006300
                                                                 # <--- this is unnecessary line-break
 Bq      -3.0      -3.0      1.0
 Bq      -3.0      -2.8      1.0
 Bq      -3.0      -2.6      1.0
```
**No necessary line-break**
```
 H                  2.38136700    0.70385800    0.00000700
 H                  0.58095200    2.41426700    0.00001800
 H                 -1.80027600    1.71035300   -0.00006300 Bq      -3.0      -3.0      1.0     # <--- a line-break needed
 Bq      -3.0      -2.8      1.0
 Bq      -3.0      -2.6      1.0
```

## From author
If you found any bugs, please contact me (wongzit@yahoo.co.jp).

More information about me, please check my [personal website](https://www.wangzhe95.net).

 **Hope you enjoy this program!**
