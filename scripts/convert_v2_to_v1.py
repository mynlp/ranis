#!/usr/bin/python                                                                         
# coding: utf-8

import sys;
import glob;
import os;
import re;


#### #### #### #### ####
#フォルダを指定すれば、対象の拡張子のファイルを重複なく取ってくる
def all_files( pat, file_path):
  for match in glob.glob( os.path.join( file_path, pat ) ):
    yield match
#####jterm関数
def jterm(x):
  
  if x in ("DATA-ITEM",
           "PLAN",
           "PROCESS",
           "PLAN-OR-PROCESS",
           "PERSON",
           "INTELLIGENT-AGENT",
           "ARTIFACT",
           "LANGUAGE",
           "TIME",
           "LOCATION",
           "QUALITY",
           "REFERENCE",
           "EXTERNAL-REFERENCE",
           "FORMULA",
           "OTHER-SPAN",
           "DOMAIN",
           "ORGANIZATION",
           0):
    return "TERM"

  elif x == "QUANTITY" or x == "MODALITY":
    return "MEASURE"

  elif x == "APPLY-TO":
    return "TRIGGER:APPLY_TO" #-が_に変わるのでここは必要

  else:
    return "TRIGGER:"+x

#####jrelation関数
def jrelation(x,y,z):
  x=x.upper() #big letter
  if x == "ATTRIBUTE":

    if tclass[z] == "MEASURE":
      return ("EVALUATE",y,z)

    else:
      return ("ATTRIBUTE",z,y)

  elif x == "APPLY-TO":
    return ("APPLY_TO", y,z)

  elif x == "COREFERENCE":
    return ("EQUIVALENCE",y,z)

  elif x in ("IS-A","MEMBER-COLLECTION","COMPONENT-OBJECT"):
    return("SUBCONCEPT",y,z)

  elif x == "AGENT":
    return ("PERFORM",z,y)

  elif x in ("INPUT","OUTPUT","IN_OUT",
             "ORIGIN", "DESTINATION", "ORI_DEST",
             "TARGET", "CONDITION",0):

    return(x,z,y)

  elif x =="OTHER-REL":
    if tclass[z] == "MEASURE":
      return ("EVALUATE",y,z)
    else:
      return (x,y,z)

  else:
    return (x,y,z)
######################################
#引数でフォルダを指定する

argvs = sys.argv;
argc = len(argvs);

if argc != 2:
  print ('Usage: # python %s file_path' % argvs[0])
  quit();

file_path = argvs[1]
################################
#１ファイルずつ取ってきて一行ずつ読む
for file in sorted(all_files('*.split.ann', file_path )):
  f_name=os.path.basename(file)
  f=open(f_name,"w")
#  print (f_name)

  tclass={}
  tspan={}
  ttext={}

  rclass={}
  rfrom={}
  rto={}

  aclass={}
  attribid={}


  
  for line in open(file):
      #先頭にID来るのは既知なのでmatch使用
    id=re.match("((\w).*?)\t(.+)",line)
     
    if id:
        if id.group(2)=="T":
              tid=id.group(1)#+":tid"
              
              tnakami=id.group(3).split("\t")
              t_class=tnakami[0].split(" ")[0]
              t_spans=tnakami[0].split(" ")[1]
              t_spang=tnakami[0].split(" ")[2]
              t_text=tnakami[1]
              ####### ######

              tclass[tid]=t_class
              tspan[tid]=t_spans+" "+t_spang
              ttext[tid]=t_text

        elif id.group(2)=="R":
              rid=id.group(1)#+":rid"
              
              r_nakami=id.group(3).split(" ")
              r_class=r_nakami[0]
              r_from=r_nakami[1].split(":")[1]
              r_to=r_nakami[2].split(":")[1].rstrip("\t")

              #### ####
              rclass[rid]=r_class
              rfrom[rid]=r_from
              rto[rid]=r_to


        elif id.group(2)=="A":
             aid=id.group(1)

             a_nakami=id.group(3).split(" ")
             a_class=a_nakami[0]
             a_span=a_nakami[1]

             #### ####
             aclass[aid]=a_class
             attribid[aid]=a_span

        else:
        
            print (line.rstrip("\n")+"元データ異常:要チェック")

###Entityの変換

  for ti, tc in sorted(tclass.items()):
    tclass[ti]=jterm(tc) #属性によるものはTERMと元perlにある。

###属性の処理
  for ai,ac in sorted(aclass.items()):
    tmpid = attribid[ai]

    if ac == "Name":
       tclass[tmpid]="OBJECT"
      
    elif ac == "Judgment":
      tclass[tmpid]="MEASURE"


####reactionの変換
   #
  for ri,rc in sorted(rclass.items()):
     A1=rfrom[ri]
     A2=rto[ri]

     (rclass[ri],rfrom[ri],rto[ri])=jrelation(rc, A1, A2)#変換して入れなおす


################################################################
#TRIGGERの処理
  i=1
  for rkey,rc2 in sorted(rclass.items()):
    if rc2 =="FROM":
      rx=rfrom[rkey]
      ry=rto[rkey]
      
      if tclass[rx] in ("TERM", "MEASURE","OBJECT"):
        
        del rclass[rkey]
        del rfrom[rkey]
        del rto[rkey]
        
      else:
        prefix, trigger=tclass[rx].split(":")#TRIGGER:INPUT を　：前後にわける
###################################
        #toを探しに行く
        new_rclass=rclass.copy()
        new_rfrom=rfrom.copy()
        new_rto=rto.copy()

        for new_key, new_c in sorted(new_rclass.items()):

          newx = new_rfrom[new_key]
          newy = new_rto[new_key]
          gkey ="G"+str(i)#元のperlではint(rkey[1:])*10000
          
          if new_c =="TO" and newx == rx :
            new_id=gkey
            (rclass[new_id],rfrom[new_id],rto[new_id]) =jrelation(trigger,ry,newy)
            i +=1 

      del rclass[rkey],rfrom[rkey],rto[rkey]
##############################
#to:上で処理されているはずなので全部消してしまってよい
  for a, b in sorted(rclass.items()):
    if b=="TO":
      del rclass[a],rfrom[a],rto[a]

      #ここまででfrom/toは消えてしまっている
#TRIGGERをかかり先・かかり元とする, from/to以外の関係を消す
  for c in sorted(rclass.keys()):
    rxx=rfrom[c]
    ryy=rto[c]

    if "TRIGGER" in tclass[rxx] or "TRIGGER" in tclass[ryy]:

      del rclass[c]
      del rfrom[c]
      del rto[c]

###何も関係のないEntityの除去
  for ttkey, ttclass in sorted(tclass.items()):
    unused = 1

    for relkey, relfrom in sorted(rfrom.items()):
      if relfrom == ttkey:
        unused = 0
        
    for rel_key, relto in sorted(rto.items()):
      if relto ==ttkey:
        unused =0

    if unused:
      del tclass[ttkey]
      del tspan[ttkey]
      del ttext[ttkey]



################
# result print #
################


  for t3_key, t3_class in sorted(tclass.items(), key=lambda x: int(x[0][1:])):
    span=tspan[t3_key]
    text=ttext[t3_key]
    tmatch=re.match("TRIGGER:(.+?)", t3_class)
    
    if tmatch:
     t3_class =tmatch.group()

    f.write(t3_key+"\t"+t3_class+" "+span+"\t"+text+"\n")
 
  for rrkey, rrclass in sorted(rclass.items(), key=lambda x: int(x[0][1:])):
    last_x=rfrom[rrkey]
    last_y=rto[rrkey]

    f.write(rrkey+"\t"+rrclass+" x:"+last_x+" y:"+last_y+"\n")

  f.close()
