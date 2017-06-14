//Maya ASCII 2012 scene
//Name: asIcons.ma
//Last modified: Sat, Jun 20, 2015 05:59:58 PM
//Codeset: 1252
requires maya "2008";
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "001200000000-796618";
fileInfo "osv" "Microsoft Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 21.885123374553441 14.533676378597447 24.127572416740133 ;
	setAttr ".r" -type "double3" -25.538352729632635 53.80000000000058 5.385242397488055e-015 ;
	setAttr ".rp" -type "double3" -1.3877787807814457e-017 7.2858385991025898e-017 0 ;
	setAttr ".rpt" -type "double3" 3.0082555163868598e-016 2.7975467232070503e-017 5.6215120816127718e-017 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999979;
	setAttr ".coi" 29.000847948486861;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0 -1.7347234759768071e-016 12 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.21592189422780772 100.75197787864143 -0.12374835693125452 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.59170435747109;
	setAttr ".ow" 7.4944105638274578;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 1.6556714474611969 -0.40000000000000568 5.3840819456707196 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1.4459035162228058 100.31923053878319 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100;
	setAttr ".ow" 12.630774184380186;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.03308855982081 1.3911125197911445 2.8836240962080515 ;
	setAttr ".r" -type "double3" 0 89.999999999999972 0 ;
	setAttr ".rp" -type "double3" -8.8817841970012523e-016 0 -1.4210854715202004e-014 ;
	setAttr ".rpt" -type "double3" -1.3322676295501882e-014 0 1.5099033134902132e-014 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.03308855982081;
	setAttr ".ow" 15.346123053023407;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 3.6123683873968835 5.9188443616198603 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "FKIK_icon";
	setAttr ".t" -type "double3" 0 0 -3 ;
createNode nurbsCurve -n "FKIK_iconShape" -p "FKIK_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 2 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-3.1718117970482555e-017 0.14284570427275867 -1
		-3.1718117970482555e-017 0.14284570427275867 -0.14284570427275867
		-2.2206238405668478e-016 1 -0.14284570427275867
		-2.2206238405668478e-016 1 0.14284570427275867
		-3.1718117970482555e-017 0.14284570427275867 0.14284570427275867
		-3.1718117970482555e-017 0.14284570427275867 1
		3.1718117970482555e-017 -0.14284570427275867 1
		3.1718117970482555e-017 -0.14284570427275867 0.14284570427275867
		2.2206238405668473e-016 -1 0.14284570427275867
		2.2206238405668473e-016 -1 -0.14284570427275867
		3.1718117970482555e-017 -0.14284570427275867 -0.14284570427275867
		3.1718117970482555e-017 -0.14284570427275867 -1
		-3.1718117970482555e-017 0.14284570427275867 -1
		;
createNode transform -n "Pole_icon";
	setAttr ".t" -type "double3" 0 0 3 ;
	setAttr ".smd" 1;
createNode nurbsCurve -n "Pole_iconShape" -p "Pole_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-1 0 0
		1 0 0
		0 0 0
		0 1 0
		0 -1 0
		0 0 0
		0 0 -1
		0 0 1
		;
createNode transform -n "FK_icon";
	setAttr ".t" -type "double3" 0 0 -6 ;
	setAttr ".smd" 2;
createNode nurbsCurve -n "FK_iconShape" -p "FK_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0 -0.78361162489122504 -0.78361162489122382
		0 1.2643394714199588e-016 -1.1081941875543879
		0 0.78361162489122427 -0.78361162489122427
		-4.4408920985006262e-016 1.1081941875543879 -3.4541083832369569e-016
		0 0.78361162489122449 0.78361162489122416
		0 3.7316641393932461e-016 1.1081941875543881
		0 -0.78361162489122393 0.78361162489122438
		4.4408920985006262e-016 -1.1081941875543879 5.9521101886435592e-016
		0 -0.78361162489122504 -0.78361162489122382
		0 1.2643394714199588e-016 -1.1081941875543879
		0 0.78361162489122427 -0.78361162489122427
		;
createNode transform -n "Roll_icon";
createNode nurbsCurve -n "Roll_iconShape" -p "Roll_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 13 0 no 3
		18 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 13 13
		16
		-3.7000062909692977e-016 -0.99839813343704398 0.00012219028690288458
		-2.4329023098109735e-016 -0.98947630420578214 -0.66667891291909531
		6.5611639159099231e-017 -0.06606089591245852 -1.1805163385626853
		3.1793909987926431e-016 0.78361162489122427 -0.78361162489122427
		3.8177870489054318e-016 1.1081941875543879 -3.4541083832369569e-016
		2.2197752240217732e-016 0.78361162489122449 0.78361162489122416
		-6.7855082167406399e-017 -0.10554584149615936 1.147485377304041
		-3.2579115040833995e-016 -0.92538321072514262 0.63464567247479609
		-3.7000062909692977e-016 -0.99839813343704398 0.00012219028690288458
		-3.7000062909692977e-016 -0.99839813343704398 0.00012219028690288458
		-3.7000062909692977e-016 -0.99839813343704398 0.00012219028690288458
		-3.8166879965334855e-016 -1.0758715052462298 0.11260026125536655
		-3.8166879965334855e-016 -1.0758715052462298 0.11260026125536655
		-3.7000062909692977e-016 -0.99839813343704398 0.00012219028690288458
		-3.7000062909692977e-016 -0.99839813343704398 0.00012219028690288458
		-3.5189277740550948e-016 -0.92030481502527717 0.11927041671167145
		;
createNode transform -n "IK_icon";
	setAttr ".t" -type "double3" 0 0 6 ;
createNode nurbsCurve -n "IK_iconShape" -p "IK_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-1 -1 1
		1 -1 1
		1 1 1
		1 1 -1
		1 -1 -1
		-1 -1 -1
		-1 1 -1
		-1 1 1
		-1 -1 1
		-1 -1 -1
		-1 1 -1
		1 1 -1
		0.99586917312289958 -1 -0.99586917312289991
		0.99586917312289958 -1 0.99586917312289991
		1 1 1
		-1 1 1
		;
createNode transform -n "Aim_icon";
	setAttr ".t" -type "double3" 0 0 9 ;
createNode nurbsCurve -n "Aim_iconShape" -p "Aim_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-1 -4.9999999999999989e-013 1
		1 -4.9999999999999989e-013 0.99999999999999967
		9.9999999999999998e-013 4.9999999999999999e-013 9.9999999999999978e-013
		9.9999999999999998e-013 4.9999999999999999e-013 -1.0000000000000002e-012
		1 -5.0000000000000009e-013 -0.99999999999999967
		-1 -5.0000000000000009e-013 -0.99999999999999967
		-9.9999999999999998e-013 4.9999999999999999e-013 -1.0000000000000002e-012
		-9.9999999999999998e-013 4.9999999999999999e-013 9.9999999999999978e-013
		-1 -4.9999999999999989e-013 0.99999999999999967
		-1 -5.0000000000000009e-013 -0.99999999999999967
		-9.9999999999999998e-013 4.9999999999999999e-013 -1.0000000000000002e-012
		9.9999999999999998e-013 4.9999999999999999e-013 -1.0000000000000002e-012
		0.99586917312289958 -5.0000000000000009e-013 -0.99586917312289958
		0.99586917312289958 -4.9999999999999989e-013 0.99586917312289958
		9.9999999999999998e-013 4.9999999999999999e-013 9.9999999999999978e-013
		-9.9999999999999998e-013 4.9999999999999999e-013 9.9999999999999978e-013
		;
createNode transform -n "FaceB_icon";
	setAttr ".t" -type "double3" 0 3 0 ;
createNode nurbsCurve -n "FaceB_iconShape" -p "FaceB_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		53
		0 1.0000012199999999 0
		2.6553999739999999e-017 0.9238811267 0.38268346670000003
		4.9065464349999998e-017 0.7071078623 0.7071078623
		6.4107131180000003e-017 0.38268346670000003 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		6.4107131180000003e-017 -0.38268346670000003 0.9238811267
		4.9065464349999998e-017 -0.7071078623 0.7071078623
		2.6553999739999999e-017 -0.9238811267 0.38268346670000003
		0 -1.0000012199999999 0
		-2.6553999739999999e-017 -0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 -0.7071078623 -0.7071078623
		-6.4107131180000003e-017 -0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		0 1.0000012199999999 0
		0.38268346670000003 0.9238811267 -2.6553999739999999e-017
		0.7071078623 0.7071078623 -4.9065464349999998e-017
		0.9238811267 0.38268346670000003 -6.4107131180000003e-017
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 -0.38268346670000003 -6.4107131180000003e-017
		0.7071078623 -0.7071078623 -4.9065464349999998e-017
		0.38268346670000003 -0.9238811267 -2.6553999739999999e-017
		0 -1.0000012199999999 0
		-0.38268346670000003 -0.9238811267 2.6553999739999999e-017
		-0.7071078623 -0.7071078623 4.9065464349999998e-017
		-0.9238811267 -0.38268346670000003 6.4107131180000003e-017
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0.38268346670000003 6.4107131180000003e-017
		-0.7071078623 0.7071078623 4.9065464349999998e-017
		-0.38268346670000003 0.9238811267 2.6553999739999999e-017
		0 1.0000012199999999 0
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-0.38268346670000003 0 -0.9238811267
		-0.7071078623 0 -0.7071078623
		-0.9238811267 0 -0.38268346670000003
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0 0.38268346670000003
		-0.7071078623 0 0.7071078623
		-0.38268346670000003 0 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		0.38268346670000003 0 0.9238811267
		0.7071078623 0 0.7071078623
		0.9238811267 0 0.38268346670000003
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 0 -0.38268346670000003
		0.7071078623 0 -0.7071078623
		0.38268346670000003 0 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		;
createNode transform -n "FaceA_icon";
	setAttr ".t" -type "double3" 0 3 3 ;
createNode nurbsCurve -n "FaceA_iconShape" -p "FaceA_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		53
		0 1.0000012199999999 0
		2.6553999739999999e-017 0.9238811267 0.38268346670000003
		4.9065464349999998e-017 0.7071078623 0.7071078623
		6.4107131180000003e-017 0.38268346670000003 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		6.4107131180000003e-017 -0.38268346670000003 0.9238811267
		4.9065464349999998e-017 -0.7071078623 0.7071078623
		2.6553999739999999e-017 -0.9238811267 0.38268346670000003
		0 -1.0000012199999999 0
		-2.6553999739999999e-017 -0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 -0.7071078623 -0.7071078623
		-6.4107131180000003e-017 -0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		0 1.0000012199999999 0
		0.38268346670000003 0.9238811267 -2.6553999739999999e-017
		0.7071078623 0.7071078623 -4.9065464349999998e-017
		0.9238811267 0.38268346670000003 -6.4107131180000003e-017
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 -0.38268346670000003 -6.4107131180000003e-017
		0.7071078623 -0.7071078623 -4.9065464349999998e-017
		0.38268346670000003 -0.9238811267 -2.6553999739999999e-017
		0 -1.0000012199999999 0
		-0.38268346670000003 -0.9238811267 2.6553999739999999e-017
		-0.7071078623 -0.7071078623 4.9065464349999998e-017
		-0.9238811267 -0.38268346670000003 6.4107131180000003e-017
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0.38268346670000003 6.4107131180000003e-017
		-0.7071078623 0.7071078623 4.9065464349999998e-017
		-0.38268346670000003 0.9238811267 2.6553999739999999e-017
		0 1.0000012199999999 0
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-0.38268346670000003 0 -0.9238811267
		-0.7071078623 0 -0.7071078623
		-0.9238811267 0 -0.38268346670000003
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0 0.38268346670000003
		-0.7071078623 0 0.7071078623
		-0.38268346670000003 0 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		0.38268346670000003 0 0.9238811267
		0.7071078623 0 0.7071078623
		0.9238811267 0 0.38268346670000003
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 0 -0.38268346670000003
		0.7071078623 0 -0.7071078623
		0.38268346670000003 0 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		;
createNode transform -n "FaceC_icon";
	setAttr ".t" -type "double3" 0 3 -3 ;
createNode nurbsCurve -n "FaceC_iconShape" -p "FaceC_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 24;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		53
		0 1.0000012199999999 0
		2.6553999739999999e-017 0.9238811267 0.38268346670000003
		4.9065464349999998e-017 0.7071078623 0.7071078623
		6.4107131180000003e-017 0.38268346670000003 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		6.4107131180000003e-017 -0.38268346670000003 0.9238811267
		4.9065464349999998e-017 -0.7071078623 0.7071078623
		2.6553999739999999e-017 -0.9238811267 0.38268346670000003
		0 -1.0000012199999999 0
		-2.6553999739999999e-017 -0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 -0.7071078623 -0.7071078623
		-6.4107131180000003e-017 -0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		0 1.0000012199999999 0
		0.38268346670000003 0.9238811267 -2.6553999739999999e-017
		0.7071078623 0.7071078623 -4.9065464349999998e-017
		0.9238811267 0.38268346670000003 -6.4107131180000003e-017
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 -0.38268346670000003 -6.4107131180000003e-017
		0.7071078623 -0.7071078623 -4.9065464349999998e-017
		0.38268346670000003 -0.9238811267 -2.6553999739999999e-017
		0 -1.0000012199999999 0
		-0.38268346670000003 -0.9238811267 2.6553999739999999e-017
		-0.7071078623 -0.7071078623 4.9065464349999998e-017
		-0.9238811267 -0.38268346670000003 6.4107131180000003e-017
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0.38268346670000003 6.4107131180000003e-017
		-0.7071078623 0.7071078623 4.9065464349999998e-017
		-0.38268346670000003 0.9238811267 2.6553999739999999e-017
		0 1.0000012199999999 0
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-0.38268346670000003 0 -0.9238811267
		-0.7071078623 0 -0.7071078623
		-0.9238811267 0 -0.38268346670000003
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0 0.38268346670000003
		-0.7071078623 0 0.7071078623
		-0.38268346670000003 0 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		0.38268346670000003 0 0.9238811267
		0.7071078623 0 0.7071078623
		0.9238811267 0 0.38268346670000003
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 0 -0.38268346670000003
		0.7071078623 0 -0.7071078623
		0.38268346670000003 0 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		;
createNode transform -n "FaceD_icon";
	setAttr ".t" -type "double3" 0 3 -6 ;
createNode nurbsCurve -n "FaceD_iconShape" -p "FaceD_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		53
		0 1.0000012199999999 0
		2.6553999739999999e-017 0.9238811267 0.38268346670000003
		4.9065464349999998e-017 0.7071078623 0.7071078623
		6.4107131180000003e-017 0.38268346670000003 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		6.4107131180000003e-017 -0.38268346670000003 0.9238811267
		4.9065464349999998e-017 -0.7071078623 0.7071078623
		2.6553999739999999e-017 -0.9238811267 0.38268346670000003
		0 -1.0000012199999999 0
		-2.6553999739999999e-017 -0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 -0.7071078623 -0.7071078623
		-6.4107131180000003e-017 -0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		0 1.0000012199999999 0
		0.38268346670000003 0.9238811267 -2.6553999739999999e-017
		0.7071078623 0.7071078623 -4.9065464349999998e-017
		0.9238811267 0.38268346670000003 -6.4107131180000003e-017
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 -0.38268346670000003 -6.4107131180000003e-017
		0.7071078623 -0.7071078623 -4.9065464349999998e-017
		0.38268346670000003 -0.9238811267 -2.6553999739999999e-017
		0 -1.0000012199999999 0
		-0.38268346670000003 -0.9238811267 2.6553999739999999e-017
		-0.7071078623 -0.7071078623 4.9065464349999998e-017
		-0.9238811267 -0.38268346670000003 6.4107131180000003e-017
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0.38268346670000003 6.4107131180000003e-017
		-0.7071078623 0.7071078623 4.9065464349999998e-017
		-0.38268346670000003 0.9238811267 2.6553999739999999e-017
		0 1.0000012199999999 0
		-2.6553999739999999e-017 0.9238811267 -0.38268346670000003
		-4.9065464349999998e-017 0.7071078623 -0.7071078623
		-6.4107131180000003e-017 0.38268346670000003 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		-0.38268346670000003 0 -0.9238811267
		-0.7071078623 0 -0.7071078623
		-0.9238811267 0 -0.38268346670000003
		-1.0000012199999999 0 6.9389023660000001e-017
		-0.9238811267 0 0.38268346670000003
		-0.7071078623 0 0.7071078623
		-0.38268346670000003 0 0.9238811267
		6.9389023660000001e-017 0 1.0000012199999999
		0.38268346670000003 0 0.9238811267
		0.7071078623 0 0.7071078623
		0.9238811267 0 0.38268346670000003
		1.0000012199999999 0 -6.9389023660000001e-017
		0.9238811267 0 -0.38268346670000003
		0.7071078623 0 -0.7071078623
		0.38268346670000003 0 -0.9238811267
		-6.9389023660000001e-017 0 -1.0000012199999999
		;
createNode transform -n "Main_icon";
createNode nurbsCurve -n "Main_iconShape" -p "Main_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		5.4852813742385749 3.3587661386919276e-016 -5.4852813742385669
		-8.8502194254805285e-016 4.7500126261776391e-016 -7.7573593128807152
		-5.4852813742385695 3.35876613869193e-016 -5.4852813742385695
		-7.7573593128807152 1.37643482313315e-031 -2.247888655066061e-015
		-5.4852813742385713 -3.3587661386919285e-016 5.4852813742385687
		-2.3374437545133636e-015 -4.7500126261776401e-016 7.757359312880717
		5.4852813742385669 -3.3587661386919305e-016 5.4852813742385704
		7.7573593128807152 -2.5512410475333544e-031 4.16649281949641e-015
		5.4852813742385749 3.3587661386919276e-016 -5.4852813742385669
		-8.8502194254805285e-016 4.7500126261776391e-016 -7.7573593128807152
		-5.4852813742385695 3.35876613869193e-016 -5.4852813742385695
		;
createNode transform -n "Root_icon";
createNode nurbsCurve -n "curveShape1" -p "Root_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 2 no 3
		8 0 1 2 3 4 5 6 7
		8
		-4.9182671052726707 0 -0.47774735047241618
		-5.6110276386982285 0 -0.47774735047241662
		-5.6110276386982285 0 -1.3332483861290205
		-6.9442760248272482 0 0
		-5.6110276386982294 0 1.3332483861290194
		-5.6110276386982285 0 0.47774735047241473
		-4.9182671052726707 0 0.47774735047241607
		-4.9182671052726707 0 -0.47774735047241618
		;
createNode nurbsCurve -n "curveShape2" -p "Root_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 2 no 3
		8 0 1 2 3 4 5 6 7
		8
		-0.47774735047241718 0 4.9182671052726707
		-0.47774735047241784 0 5.6110276386982285
		-1.3332483861290219 0 5.6110276386982285
		-1.5419390264231332e-015 0 6.9442760248272482
		1.3332483861290181 0 5.6110276386982294
		0.47774735047241351 0 5.6110276386982285
		0.47774735047241507 0 4.9182671052726707
		-0.47774735047241718 0 4.9182671052726707
		;
createNode nurbsCurve -n "curveShape3" -p "Root_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 2 no 3
		8 0 1 2 3 4 5 6 7
		8
		4.9182671052726707 0 0.47774735047241818
		5.6110276386982285 0 0.47774735047241906
		5.6110276386982285 0 1.3332483861290232
		6.9442760248272482 0 3.0838780528462664e-015
		5.6110276386982294 0 -1.3332483861290167
		5.6110276386982285 0 -0.47774735047241229
		4.9182671052726707 0 -0.47774735047241407
		4.9182671052726707 0 0.47774735047241818
		;
createNode nurbsCurve -n "curveShape4" -p "Root_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 2 no 3
		8 0 1 2 3 4 5 6 7
		8
		0.47774735047241917 0 -4.9182671052726707
		0.47774735047242028 0 -5.6110276386982285
		1.3332483861290245 0 -5.6110276386982285
		4.6258170792694001e-015 0 -6.9442760248272482
		-1.3332483861290154 0 -5.6110276386982294
		-0.47774735047241107 0 -5.6110276386982285
		-0.47774735047241307 0 -4.9182671052726707
		0.47774735047241917 0 -4.9182671052726707
		;
createNode transform -n "Bend_icon";
	setAttr ".t" -type "double3" 0 0 -9 ;
createNode nurbsCurve -n "Bend_iconShape" -p "Bend_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 10;
	setAttr ".cc" -type "nurbsCurve" 
		1 8 0 no 3
		9 0 1 2 3 4 5 6 7 8
		9
		0 0 1.2461054241411718
		0 0.23161895894243972 0.23161895894243983
		0 1.2461054241411709 0
		0 0.23161895894243972 -0.23161895894243983
		0 0 -1.2461054241411718
		0 -0.23161895894243972 -0.23161895894243983
		0 -1.2461054241411709 0
		0 -0.23161895894243972 0.23161895894243983
		0 0 1.2461054241411718
		;
createNode transform -n "Scapula_icon";
	setAttr ".t" -type "double3" 0 3 6 ;
createNode nurbsCurve -n "Scapula_iconShape" -p "Scapula_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 18 0 no 3
		23 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 18 18
		21
		-0.10000000000000006 -1 3.223048243472635e-016
		-0.10000000000000012 -1 0.25512228824339356
		-0.10000000000000023 -0.78361162489122471 0.78665241825139887
		-0.10000000000000026 -1.1020249310612287e-016 1.106673790874301
		-0.10000000000000014 0.78361162489122449 0.7866524182513982
		-0.10000000000000001 0.99999999999999989 0.25512228824339334
		-0.09999999999999995 1 7.7375464517792861e-017
		-0.09999999999999995 1 7.7375464517792861e-017
		-0.09999999999999995 1 7.7375464517792861e-017
		0.10000000000000006 1 1.2178438550279914e-016
		0.10000000000000006 1 1.2178438550279914e-016
		0.10000000000000006 1 1.2178438550279914e-016
		0.10000000000000001 0.99999999999999989 0.25512228824339334
		0.099999999999999881 0.78361162489122449 0.7866524182513982
		0.099999999999999756 -1.1020249310612287e-016 1.106673790874301
		0.09999999999999977 -0.78361162489122471 0.78665241825139887
		0.099999999999999895 -1 0.25512228824339356
		0.09999999999999995 -1 3.667137453322698e-016
		0.09999999999999995 -1 3.667137453322698e-016
		0.09999999999999995 -1 3.667137453322698e-016
		-0.10000000000000006 -1 3.223048243472635e-016
		;
createNode transform -n "HipSwinger_icon";
	setAttr ".t" -type "double3" 0 3 9 ;
createNode nurbsCurve -n "HipSwinger_iconShape" -p "HipSwinger_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.62688929991297959 -3.8385898727907598e-017 0.62688929991298004
		-1.2643170607829326e-016 6.7857323231109134e-017 -1.1081941875543879
		0.62688929991297959 -3.8385898727907616e-017 0.62688929991298004
		-1.1081941875543879 1.9663354616187859e-032 -3.2112695072372299e-016
		0.62688929991297959 3.8385898727907573e-017 -0.62688929991298004
		-3.3392053635905195e-016 -6.7857323231109146e-017 1.1081941875543881
		-0.62688929991298004 3.8385898727907672e-017 -0.6268892999129797
		1.1081941875543879 -3.6446300679047921e-032 5.9521325992805852e-016
		-0.62688929991297959 -3.8385898727907598e-017 0.62688929991298004
		-1.2643170607829326e-016 6.7857323231109134e-017 -1.1081941875543879
		0.62688929991297959 -3.8385898727907616e-017 0.62688929991298004
		;
createNode transform -n "IKLocal_icon";
	setAttr ".t" -type "double3" 0 0 12 ;
	setAttr ".smd" 2;
createNode nurbsCurve -n "IKLocal_iconShape" -p "IKLocal_icon";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0 -1.260955009782782 -1.2609550097827817
		0 1.2643394714199588e-016 -1.1081941875543879
		0 1.2609550097827822 -1.260955009782782
		-4.4408920985006262e-016 1.1081941875543879 -3.4541083832369569e-016
		0 1.2609550097827822 1.260955009782782
		0 3.7316641393932461e-016 1.1081941875543881
		0 -1.260955009782782 1.260955009782782
		4.4408920985006262e-016 -1.1081941875543879 5.9521101886435592e-016
		0 -1.260955009782782 -1.2609550097827817
		0 1.2643394714199588e-016 -1.1081941875543879
		0 1.2609550097827822 -1.260955009782782
		;


// End of asIcons.ma
