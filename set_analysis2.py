import pandas as pd
import numpy as np

#-----------------------------------------------------------
#前回データのクリアプログラム

cl_sheet = pd.read_excel('C:/Users/fun-f/Desktop/myfile/クリアBOOK.xlsx')#クリアデータ読み込み


for i in range(31) :
  path = ("C:/Users/fun-f/Desktop/myfile/basket-analysis/" + str(i) +".xlsx")
  
  cl_sheet.to_excel(path)
  
  
print("SUCCESSFULL")  

print("0 or 1 or 2  の条件指数を入力して下さい！")
print("0 = Ranking Key Item ")#売れ筋点数順
print("1 = Select Key Item ")#キーアイテムを指定
print("2 =  Rnking Key CategoryItems ")#アイテムカテゴリーをキーアイテムに検索
#print("3 =  Select Key Item ")#用途別アイテムカテゴリーをキーアイテムに検索

swich = input()


request_list = []

#キーワード入力
#data_8 = 0 を入力
#df_sarch_list = 1を入力
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#サーチリスト読み込み
data_sarch_list = pd.read_excel('C:/Users/fun-f/Desktop/myfile/basket-analysis/sarch-list.xlsx')#サーチアイテムがある場合のプログラム
df_sarch_list = pd.DataFrame(data_sarch_list)

#--------------------------------------------------------
#アイテム別売上ランキングベスト５のキー設定

category1 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_1.xlsx")

df_category1 = pd.DataFrame(category1)#OP

category2 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_2.xlsx")

df_category2 = pd.DataFrame(category2)#CD

category3 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_3.xlsx")

df_category3 = pd.DataFrame(category3)#JK

category4 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_4.xlsx")

df_category4 = pd.DataFrame(category4)#KT

category5 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_5.xlsx")

df_category5 = pd.DataFrame(category5)#CS

#category6 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_6.xlsx")

#df_category6 = pd.DataFrame(category6)#CT

category7 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_7.xlsx")

df_category7 = pd.DataFrame(category7)#BL


category8 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_8.xlsx")

df_category8 = pd.DataFrame(category8)#SK


category9 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_9.xlsx")

df_category9 = pd.DataFrame(category9)#PT

#category10 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_10.xlsx")

#df_category10 = pd.DataFrame(category10)#

#category11 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_11.xlsx")

#df_category11 = pd.DataFrame(category11)#INN

category12 = pd.read_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/key_item_12.xlsx")

df_category12 = pd.DataFrame(category12)#SET UP

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

df_itemcategory_list =  pd.concat([df_category1, df_category2,df_category5,df_category7,df_category8,df_category9],axis=0)#1
#
#df_itemcategory_list =  pd.concat([df_category4, df_category8,df_category9,df_category3,df_category8,df_category9],axis=0)#2
#df_itemcategory_list =  pd.concat([df_category12],axis=0)#3 df_category11,df_category10,df_category3,df_category8,df_category9

#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#任意のアイテムカテゴリーセレクト(※最大30品番)

#-----------------------------------------------------------------------------------------------

if swich == str(2) :
  df_lists = df_itemcategory_list["商品名"].values
  df_lists_values = df_itemcategory_list["点数"].values
  
  df_category = pd.DataFrame({"商品名" :df_lists,"合計数量" :df_lists_values})
  df_category.to_excel('C:/Users/fun-f/Desktop/myfile/basket-analysis/Key-Item-List.xlsx')
    
#---------------------------------------------------------------------------------------------------    
#要素１
#全体客数

data1 = pd.read_csv('C:/Users/fun-f/Desktop/myfile/basket-analysis/data-folder/売上集計データ.csv',encoding='SHIFT-JIS')#ok


df_data1 = pd.DataFrame(data1)

cust_values = df_data1['売上客数'].values
n = np.sum(cust_values) #対象期間客数
print(n)
#----------------------------------------------------------
#売上合計数量
data2 = pd.read_csv('C:/Users/fun-f/Desktop/myfile/basket-analysis/data-folder/品番売上集計データ.csv',encoding='SHIFT-JIS')#ok

data2_df = pd.DataFrame(data2)
#------------------------------------------------------------
#ここから追加
item_cd = pd.DataFrame(data2_df['商品コード'].astype('str').str.zfill(10).values,columns=["商品CD"])
item_category = pd.DataFrame(data2_df['商品コード'].astype('str').str.zfill(10).str[2:4].values,columns=["アイテムCD"])
item_name = pd.DataFrame(data2_df['商品名'].values,columns=["商品名"])
item_t = pd.DataFrame(data2_df['合計数量'].values,columns=["合計数量"])
item_m = pd.DataFrame(data2_df['合計金額'].values,columns=["合計金額"])

df_data2 = pd.concat([item_cd,item_category,item_name,item_t,item_m],axis=1)
#ここまで追加
#------------------------------------------------------------

#df_data2 = pd.DataFrame(data2) #ここが元々のデータ

xname_values = df_data2['商品名'].values

x_values = df_data2['合計数量'].values


#print(xname_values)
#print(df_data2)
#-----------------------------------------------------------
del_1 = 'ｼｮｯﾋﾟﾝｸﾞﾊﾞｯｸﾞS'#除外品番
del_2 = "ｼｮｯﾋﾟﾝｸﾞﾊﾞｯｸﾞM"#除外品番
del_3 = "ｼｮｯﾋﾟﾝｸﾞﾊﾞｯｸﾞL"#除外品番
del_4 = "ｼｮｯﾋﾟﾝｸﾞﾊﾞｯｸﾞLL"#除外品番
del_5 = "ﾊﾝﾄﾞｸﾘｰﾝｼﾞｪﾙ"#除外品番
del_6 = "ｷﾚｲﾏｽｸ"#除外品番
del_7 = "ｼｮｯﾋﾟﾝｸﾞﾊﾞｯｸﾞLL＊"#除外品番
del_8 = "わけあり"#除外品番
del_9 = "ｷﾞﾌﾄS"
del_10 = "ｷﾞﾌﾄM"
del_11 = "ｷﾞﾌﾄL"
#検証対象品番
sample_failes = []
del_failes = []

if swich == str(0) :
  
  for i in df_data2["商品名"]:
    if i == del_1:
      del_failes.append(i)
      
    elif i == del_2:
      del_failes.append(i)
      
      
    elif i == del_3:
      del_failes.append(i)
      
      
    elif i == del_4:
      del_failes.append(i)
      
      
    elif i == del_5:
      del_failes.append(i)
      
      
    elif i == del_6:
      del_failes.append(i)
      
      
    elif i == del_7:
      del_failes.append(i)
      
      
    elif i == del_8:
      del_failes.append(i)
      
      
    elif i == del_9:
      del_failes.append(i)  
      
    elif i == del_10:
      del_failes.append(i)
      
    elif i == del_11:
      del_failes.append(i)
        
    else :
      for x in df_data2["商品名"]:
        
        if x == i :
          l_dt = df_data2[df_data2["商品名"] == i]
          l_dt_v = l_dt['合計数量'].values
          i_data = pd.DataFrame({"商品名":i,"合計数量":l_dt_v})        
          sample_failes.append(i_data)

  data_7 = pd.concat(sample_failes)
  data_8 = data_7.sort_values(by="合計数量" ,ascending=False).head(20)#検証品番リスト
  print(data_7)
  data_8.to_excel('C:/Users/fun-f/Desktop/myfile/sample.xlsx')
  print(data_8)      
  data_8.to_excel('C:/Users/fun-f/Desktop/myfile/basket-analysis/Key-Item-List.xlsx')
  
elif swich == str(1) :
  for i in df_sarch_list['商品名'] :
    print(i)
    sch_1 = df_data2[df_data2['商品名'].values == i]
    sch_2 = sch_1['合計数量'].values
    sdh_2_cat = sch_1['アイテムCD'].values#7/8追加コード⓵
    
    #sdh_2_cat = sch_1['商品CD'].values#7/8追加コード⓶

    
    #sch_3 = pd.DataFrame({"アイテムCD" : sch_2_cat, "商品名" : [i] , "合計数量" : sch_2})
    
    sch_3 = pd.DataFrame({"商品名" : [i] , "合計数量" : sch_2})
    
    request_list.append(sch_3)
      
    
    print(sch_3)
      
  sch_lists = pd.concat(request_list)    
  print(sch_lists)
  sch_lists.to_excel('C:/Users/fun-f/Desktop/myfile/basket-analysis/Key-Item-List.xlsx')
  

#ーーーーーーー検証リスト【サンプルA】ーーーーーーーー
#　
#　★サンプルリストA【data_8】売上点数順上位20品番

#  ★サーチリストA【df_sarch_list】任意アイテムリスト

#-----------------------------------------------------------
#顧客データ抽出
data = pd.read_csv('C:/Users/fun-f/Desktop/myfile/basket-analysis/data-folder/顧客データ.csv',encoding='SHIFT-JIS')

df_1 = pd.DataFrame(data)


#ーーーーーーー顧客データ生成ーーーーーーーーー

df_1_no = pd.DataFrame(df_1['伝票番号'].values,columns=['伝票番号'])
df_1_itcd = pd.DataFrame(df_1['商品コード'].astype('str').str.zfill(10).values,columns=['商品コード'])
df_1_itnm = pd.DataFrame(df_1['商品名'].values,columns=['商品名'])
df_1_mon = pd.DataFrame(df_1['標準金額'].values,columns=['標準金額'])
df_1_itemcd = pd.DataFrame(df_1['商品コード'].astype('str').str.zfill(10).str[2:4].values, columns=['アイテムCD'])
cont = df_1['商品名'].values
cont_1 = np.unique(cont)
#---------------------------------------------------------------------------------------
#                          ここから変更

#cust_dt = pd.concat([df_1_no,df_1_itemcd,df_1_itcd,df_1_itnm,df_1_mon],axis=1)#変更前

cust_dt = pd.concat([df_1_no,df_1_itemcd,df_1_itcd,df_1_itnm,df_1_mon,df_1_mon,df_1_itemcd],axis=1)#変更後
print(cust_dt)
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#サンプルリストBを生成
sample_b = []
sample_0 = []
sample_1 = []
sample_2 = []
sample_3 = []
sample_4 = []
sample_5 = []
sample_6 = []
sample_7 = []
sample_8 = []
sample_9 = []
sample_10 = []
sample_11 = []
sample_12 = []
sample_13 = []
sample_14 = []
sample_15 = []
sample_16 = []
sample_17 = []
sample_18 = []
sample_19 = []
sample_20 = []
sample_21 = []#ここから追加
sample_22 = []
sample_23 = []
sample_24 = []
sample_25 = []
sample_26 = []
sample_27 = []
sample_28 = []
sample_29 = []
sample_30 = []


#----------------------------------------ここから変更箇所　↓　↓　↓

c = 0

if swich == str(0) :
  sarch_data = data_8
  
elif swich == str(1) :
  sarch_data = df_sarch_list  

  
elif swich == str(2) :
  sarch_data = df_itemcategory_list  

  
  
else:
  print("0 or 1 を入力して下さい")
  
  
#for i in data_8["商品名"]:
for i in sarch_data["商品名"]:
  print(i)
  c += 1
  data_9 = cust_dt[cust_dt["商品名"] == i]
  data_10 = data_9['伝票番号'].values
  data_11 = np.unique(data_10)#対象品番の顧客データ
  data_12 = len(data_11)
  #print(data_12)#SET件数
  for n in data_11:
    data_13 = cust_dt[cust_dt["伝票番号"] == n]
    data_14 = data_13["商品名"].values
    print(data_14)
    #print(data_14)
    data_15 = np.unique(data_14)
    data_16 = pd.DataFrame(data_14)
    #print(data_15)
    
#---------------------------------ここまで変更    
    for x in data_15 :
      #print(x)
      if x == del_1:
        del_failes.append(x)
        
      elif x == del_2:
        del_failes.append(x)
        
        
      elif x == del_3:
        del_failes.append(x)
        
        
      elif x == del_4:
        del_failes.append(x)
        
        
      elif x == del_5:
        del_failes.append(x)
        
        
      elif x == del_6:
        del_failes.append(x)
        
        
      elif x == del_7:
        del_failes.append(x)
        
        
      elif x == del_8:
        del_failes.append(x)
        
      else :
        list_name = str("sample_") + str(c)
        #print(list_name)
        #for l in faile_lists :
        if c == 0:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_0.append(x_1)
          
        elif c == 1:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_1.append(x_1)
          
        elif c == 2:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_2.append(x_1)
          
        elif c == 3:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_3.append(x_1)  
      
        elif c == 4:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_4.append(x_1)
          
        elif c == 5:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_5.append(x_1)  
          
        elif c == 6:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_6.append(x_1)  

        elif c == 7:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_7.append(x_1)  
      
        elif c == 8:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_8.append(x_1)
          
        elif c == 9:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_9.append(x_1)  
          
        elif c == 10:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_10.append(x_1)
           
        elif c == 11:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_11.append(x_1)  
      
        elif c == 12:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_12.append(x_1)
          
        elif c == 13:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_13.append(x_1)  
          
        elif c == 14:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_14.append(x_1)  
                    
        elif c == 15:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_15.append(x_1)  
      
        elif c == 16:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_16.append(x_1)
          
        elif c == 17:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_17.append(x_1)  
          
        elif c == 18:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_18.append(x_1)   
            
        elif c == 19:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_19.append(x_1)  
      
        elif c == 20:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_20.append(x_1)
          
        elif c == 21:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_21.append(x_1)  
      
        elif c == 22:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_22.append(x_1)
          
        elif c == 23:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_23.append(x_1)  
          
        elif c == 24:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_24.append(x_1)  
                    
        elif c == 25:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_25.append(x_1)  
      
        elif c == 26:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_26.append(x_1)
          
        elif c == 27:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_27.append(x_1)  
          
        elif c == 28:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_28.append(x_1)   
            
        elif c == 29:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_29.append(x_1)  
      
        elif c == 30:
          x_1 = pd.DataFrame({"商品名" :[x]})
          sample_30.append(x_1)  
          
        else:
          del_failes.append(x)

print(sample_0)    
#ーーーーーーーーーーーー データセット数を算出 ーーーーーーーーーーーーーーーー   

#ここでデータのセット数を演算する
#ーーーーー リスト一覧 ーーーーーーーー

sample_0x = []
sample_1x = []
sample_2x = []
sample_3x = []
sample_4x = []
sample_5x = []
sample_6x = []
sample_7x = []
sample_8x = []
sample_9x = []
sample_10x = []
sample_11x = []
sample_12x = []
sample_13x = []
sample_14x = []
sample_15x = []
sample_16x = []
sample_17x = []
sample_18x = []
sample_19x = []
sample_20x = [] 
sample_21x = []#ここから追加
sample_22x = []
sample_23x = []
sample_24x = []
sample_25x = []
sample_26x = []
sample_27x = []
sample_28x = []
sample_29x = []
sample_30x = [] 

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#print(sample_1) 
unq_0 = np.unique(sample_0) 
unq_1 = np.unique(sample_1)
unq_2 = np.unique(sample_2)
unq_3 = np.unique(sample_3)
unq_4 = np.unique(sample_4)
unq_5 = np.unique(sample_5)
unq_6 = np.unique(sample_6)
unq_7 = np.unique(sample_7)
unq_8 = np.unique(sample_8)
unq_9 = np.unique(sample_9)
unq_10 = np.unique(sample_10) 
unq_11 = np.unique(sample_11)
unq_12 = np.unique(sample_12)
unq_13 = np.unique(sample_13)
unq_14 = np.unique(sample_14)
unq_15 = np.unique(sample_15)
unq_16 = np.unique(sample_16)
unq_17 = np.unique(sample_17)
unq_18 = np.unique(sample_18)
unq_19 = np.unique(sample_19)
unq_20 = np.unique(sample_20)
unq_21 = np.unique(sample_21)#ここから追加
unq_22 = np.unique(sample_22)
unq_23 = np.unique(sample_23)
unq_24 = np.unique(sample_24)
unq_25 = np.unique(sample_25)
unq_26 = np.unique(sample_26)
unq_27 = np.unique(sample_27)
unq_28 = np.unique(sample_28)
unq_29 = np.unique(sample_29)
unq_30 = np.unique(sample_30)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
keyitem = sarch_data['商品名'].values 
#keyitem = data_8['商品名'].values 
print(keyitem)

for i in unq_1 :
  #print(i)
  if i == keyitem[0]:
    del_failes.append(i)  
    
  else:
    sample_1_in = pd.concat(sample_1)
    take1 = sample_1_in[sample_1_in["商品名"] == i]
    take2 = len(take1)
    take2_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    
    take2_2 = take2_1["アイテムCD"].values #
    print(take2_2)
    #take2_2_1 = take2_2[0].values
    print(take2_2)
    
    take3 = pd.DataFrame({"アイテムCD" : [take2_2],"商品名":[i],"SET数":[take2]})
    sample_1x.append(take3)
    
  take4 = pd.concat(sample_1x)
  take5 = pd.DataFrame(take4)
  take6 = take5.sort_values(by="SET数" ,ascending=False)
  take6.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/1.xlsx")
#print(take4)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

for i in unq_2 :
  #print(i)
  if i == keyitem[1]:
    del_failes.append(i)  
    
  else:
    sample_2_in = pd.concat(sample_2)
    take7 = sample_2_in[sample_2_in["商品名"] == i]
    take8 = len(take7)
    
    take8_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take8_2 = take8_1["アイテムCD"].values#追加項目2
    take9 = pd.DataFrame({"アイテムCD" : [take8_2],"商品名":[i],"SET数":[take8]})
    #take3 = pd.DataFrame({"アイテムCD" : [take2_2,"商品名":[i],"SET数":[take2]})
    sample_2x.append(take9)
    
  take10 = pd.concat(sample_2x)
  take11 = pd.DataFrame(take10)
  take12 = take11.sort_values(by="SET数" ,ascending=False)
  take12.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/2.xlsx")
#print(take10)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー12

for i in unq_3 :
  #print(i)
  if i == keyitem[2]:
    
    del_failes.append(i)  
    
  else:
    sample_3_in = pd.concat(sample_3)
    take13 = sample_3_in[sample_3_in["商品名"] == i]
    take14 = len(take13)
    take14_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take14_2 = take14_1["アイテムCD"].values#追加項目2
    take15 = pd.DataFrame({"アイテムCD":[take14_2],"商品名":[i],"SET数":[take14]})

    sample_3x.append(take15)
    
  take16 = pd.concat(sample_3x)
  take17 = pd.DataFrame(take16)
  take18 = take17.sort_values(by="SET数" ,ascending=False)
  take18.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/3.xlsx")
#print(take16)

  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー18


for i in unq_4 :
  #print(i)
  if i == keyitem[3]:
    del_failes.append(i)  
    
  else:
    sample_4_in = pd.concat(sample_4)
    take19 = sample_4_in[sample_4_in["商品名"] == i]
    take20 = len(take19)
    take20_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take20_2 = take20_1["アイテムCD"].values#追加項目2
    take21 = pd.DataFrame({"アイテムCD":[take20_2],"商品名":[i],"SET数":[take20]})
   
    sample_4x.append(take21)
    
take22 = pd.concat(sample_4x)
take23 = pd.DataFrame(take22)
take24 = take23.sort_values(by="SET数" ,ascending=False)
take24.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/4.xlsx")
#print(take22)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー24


for i in unq_5 :
  #print(i)
  if i == keyitem[4]:
    del_failes.append(i)  
    
  else:
    sample_5_in = pd.concat(sample_5)
    take25 = sample_5_in[sample_5_in["商品名"] == i]
    take26 = len(take25)
    take26_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take26_2 = take26_1["アイテムCD"].values#追加項目2
    take27 = pd.DataFrame({"アイテムCD":[take26_2],"商品名":[i],"SET数":[take26]})
    
    sample_5x.append(take27)
    
take28 = pd.concat(sample_5x)
take29 = pd.DataFrame(take28)
take30 = take29.sort_values(by="SET数" ,ascending=False)
take30.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/5.xlsx")
#print(take28)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー30


for i in unq_6 :
  #print(i)
  if i == keyitem[5]:
    del_failes.append(i)  
    
  else:
    sample_6_in = pd.concat(sample_6)
    take31 = sample_6_in[sample_6_in["商品名"] == i]
    take32 = len(take31)
    take32_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take32_2 = take32_1["アイテムCD"].values#追加項目2
    take33 = pd.DataFrame({"アイテムCD":[take32_2],"商品名":[i],"SET数":[take32]})
    
    sample_6x.append(take33)
    
take34 = pd.concat(sample_6x)
take35 = pd.DataFrame(take34)
take36 = take35.sort_values(by="SET数" ,ascending=False)
take36.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/6.xlsx")
#print(take34)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー36


for i in unq_7 :
  #print(i)
  if i == keyitem[6]:
    del_failes.append(i)  
    
  else:
    sample_7_in = pd.concat(sample_7)
    take37 = sample_7_in[sample_7_in["商品名"] == i]
    take38 = len(take37)
    take38_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take38_2 = take38_1["アイテムCD"].values#追加項目2
    take39 = pd.DataFrame({"アイテムCD":[take38_2],"商品名":[i],"SET数":[take38]})

    sample_7x.append(take39)
    
take40 = pd.concat(sample_7x)
take41 = pd.DataFrame(take40)
take42 = take41.sort_values(by="SET数" ,ascending=False)
take42.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/7.xlsx")
#print(take40)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー42


for i in unq_8 :
  #print(i)
  if i == keyitem[7]:
    del_failes.append(i)  
    
  else:
    sample_8_in = pd.concat(sample_8)
    take43 = sample_8_in[sample_8_in["商品名"] == i]
    take44 = len(take43)
    take44_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take44_2 = take44_1["アイテムCD"].values#追加項目2
    take45 = pd.DataFrame({"アイテムCD":[take44_2],"商品名":[i],"SET数":[take44]})
   
    sample_8x.append(take45)

    
take46 = pd.concat(sample_8x)
take47 = pd.DataFrame(take46)
take48 = take47.sort_values(by="SET数" ,ascending=False)
take48.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/8.xlsx")
#print(take46)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー48


for i in unq_9 :
  #print(i)
  if i == keyitem[8]:
    del_failes.append(i)  
    
  else:
    sample_9_in = pd.concat(sample_9)
    take49 = sample_9_in[sample_9_in["商品名"] == i]
    take50 = len(take49)
    take50_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take50_2 = take50_1["アイテムCD"].values#追加項目2
    take51 = pd.DataFrame({"アイテムCD":[take50_2],"商品名":[i],"SET数":[take50]})
    
    sample_9x.append(take51)
    
take52 = pd.concat(sample_9x)
take53 = pd.DataFrame(take52)
take54 = take53.sort_values(by="SET数" ,ascending=False)
take54.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/9.xlsx")
#print(take52)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー54


for i in unq_10 :
  #print(i)
  if i == keyitem[9]:
    del_failes.append(i)  
    
  else:
    sample_10_in = pd.concat(sample_10)
    take55 = sample_10_in[sample_10_in["商品名"] == i]
    take56 = len(take55)
    take56_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take56_2 = take56_1["アイテムCD"].values#追加項目2
    take57 = pd.DataFrame({"アイテムCD":[take56_2],"商品名":[i],"SET数":[take56]})

    sample_10x.append(take57)
    
take58 = pd.concat(sample_10x)
take59 = pd.DataFrame(take58)
take60 = take59.sort_values(by="SET数" ,ascending=False)
take60.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/10.xlsx")
#print(take58)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー60


for i in unq_11 :
  #print(i)
  if i == keyitem[10]:
    del_failes.append(i)  
    
  else:
    sample_11_in = pd.concat(sample_11)
    take61 = sample_11_in[sample_11_in["商品名"] == i]
    take62 = len(take61)
    take62_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take62_2 = take62_1["アイテムCD"].values#追加項目2
    take63 = pd.DataFrame({"アイテムCD":[take62_2],"商品名":[i],"SET数":[take62]})
   
    sample_11x.append(take63)
    
take64 = pd.concat(sample_11x)
take65 = pd.DataFrame(take64)
take66 = take65.sort_values(by="SET数" ,ascending=False)
take66.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/11.xlsx")
#print(take64)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー66


for i in unq_12 :
  #print(i)
  if i == keyitem[11]:
    del_failes.append(i)  
    
  else:
    sample_12_in = pd.concat(sample_12)
    take67 = sample_12_in[sample_12_in["商品名"] == i]
    take68 = len(take67)
    take68_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take68_2 = take68_1["アイテムCD"].values#追加項目2
    take69 = pd.DataFrame({"アイテムCD":[take68_2],"商品名":[i],"SET数":[take68]})
    
    sample_12x.append(take69)
    
take70 = pd.concat(sample_12x)
take71 = pd.DataFrame(take70)
take72 = take71.sort_values(by="SET数" ,ascending=False)
take72.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/12.xlsx")
#print(take70)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー72


for i in unq_13 :
  #print(i)
  if i == keyitem[12]:
    del_failes.append(i)  
    
  else:
    sample_13_in = pd.concat(sample_13)
    take73 = sample_13_in[sample_13_in["商品名"] == i]
    take74 = len(take73)
    take74_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take74_2 = take74_1["アイテムCD"].values#追加項目2
    take75 = pd.DataFrame({"アイテムCD":[take74_2],"商品名":[i],"SET数":[take74]})
   
    sample_13x.append(take75)
    
take76 = pd.concat(sample_13x)
take77 = pd.DataFrame(take76)
take78 = take77.sort_values(by="SET数" ,ascending=False)
take78.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/13.xlsx")
#print(take76)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー78


for i in unq_14 :
  #print(i)
  if i == keyitem[13]:
    del_failes.append(i)  
    
  else:
    sample_14_in = pd.concat(sample_14)
    take79 = sample_14_in[sample_14_in["商品名"] == i]
    take80 = len(take79)
    take80_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take80_2 = take80_1["アイテムCD"].values#追加項目2
    take81 = pd.DataFrame({"アイテムCD":[take80_2],"商品名":[i],"SET数":[take80]})
    
    sample_14x.append(take81)
    
take82 = pd.concat(sample_14x)
take83 = pd.DataFrame(take82)
take84 = take83.sort_values(by="SET数" ,ascending=False)
take84.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/14.xlsx")
#print(take82)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー84


for i in unq_15 :
  #print(i)
  if i == keyitem[14]:
    del_failes.append(i)  
    
  else:
    sample_15_in = pd.concat(sample_15)
    take85 = sample_15_in[sample_15_in["商品名"] == i]
    take86 = len(take85)
    take86_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take86_2 = take86_1["アイテムCD"].values#追加項目2
    take87 = pd.DataFrame({"アイテムCD":[take86_2],"商品名":[i],"SET数":[take86]})
    
    sample_15x.append(take87)
    
take88 = pd.concat(sample_15x)
take89 = pd.DataFrame(take88)
take90 = take89.sort_values(by="SET数" ,ascending=False)
take90.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/15.xlsx")
#print(take88)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー90


for i in unq_16 :
  #print(i)
  if i == keyitem[15]:
    del_failes.append(i)  
    
  else:
    sample_16_in = pd.concat(sample_16)
    take91 = sample_16_in[sample_16_in["商品名"] == i]
    take92 = len(take91)
    take92_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take92_2 = take92_1["アイテムCD"].values#追加項目2
    take93 = pd.DataFrame({"アイテムCD":[take92_2],"商品名":[i],"SET数":[take92]})
    
    sample_16x.append(take93)
    
take94 = pd.concat(sample_16x)
take95 = pd.DataFrame(take94)
take96 = take95.sort_values(by="SET数" ,ascending=False)
take96.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/16.xlsx")
#print(take94)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー96


for i in unq_17 :
  #print(i)
  if i == keyitem[16]:
    del_failes.append(i)  
    
  else:
    sample_17_in = pd.concat(sample_17)
    take97 = sample_17_in[sample_17_in["商品名"] == i]
    take98 = len(take97)
    take98_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take98_2 = take98_1["アイテムCD"].values#追加項目2
    take99 = pd.DataFrame({"アイテムCD":[take98_2],"商品名":[i],"SET数":[take98]})
    
    sample_17x.append(take99)
    
take100 = pd.concat(sample_17x)
take101 = pd.DataFrame(take100)
take102 = take101.sort_values(by="SET数" ,ascending=False)
take102.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/17.xlsx")
#print(take100)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー102


for i in unq_18 :
  #print(i)
  if i == keyitem[17]:
    del_failes.append(i)  
    
  else:
    sample_18_in = pd.concat(sample_18)
    take103 = sample_18_in[sample_18_in["商品名"] == i]
    take104 = len(take103)
    take104_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take104_2 = take104_1["アイテムCD"].values#追加項目2
    take105 = pd.DataFrame({"アイテムCD":[take104_2],"商品名":[i],"SET数":[take104]})
   
    sample_18x.append(take105)
    
take106 = pd.concat(sample_18x)
take107 = pd.DataFrame(take106)
take108 = take107.sort_values(by="SET数" ,ascending=False)
take108.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/18.xlsx")
#print(take106)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー108


for i in unq_19 :
  #print(i)
  if i == keyitem[18]:
    del_failes.append(i)  
    
  else:
    sample_19_in = pd.concat(sample_19)
    take109 = sample_19_in[sample_19_in["商品名"] == i]
    take110 = len(take109)
    take110_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take110_2 = take110_1["アイテムCD"].values#追加項目2
    take111 = pd.DataFrame({"アイテムCD":[take110_2],"商品名":[i],"SET数":[take110]})

    sample_19x.append(take111)
    
take112 = pd.concat(sample_19x)
take113 = pd.DataFrame(take112)
take114 = take113.sort_values(by="SET数" ,ascending=False)
take114.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/19.xlsx")
#print(take112)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー114


for i in unq_20 :
  #print(i)
  if i == keyitem[19]:
    del_failes.append(i)  
    
  else:
    sample_20_in = pd.concat(sample_20)
    take115 = sample_20_in[sample_20_in["商品名"] == i]
    take116 = len(take115)
    take116_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take116_2 = take116_1["アイテムCD"].values#追加項目2
    take117 = pd.DataFrame({"アイテムCD":[take116_2],"商品名":[i],"SET数":[take116]})
   
    sample_20x.append(take117)
    
take118 = pd.concat(sample_20x)
take119 = pd.DataFrame(take118)
take120 = take119.sort_values(by="SET数" ,ascending=False)
take120.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/20.xlsx")
#print(take118)


  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー120


for i in unq_21 :
  #print(i)
  if i == keyitem[20]:
    del_failes.append(i)  
    
  else:
    sample_21_in = pd.concat(sample_21)
    take121 = sample_21_in[sample_21_in["商品名"] == i]
    take122 = len(take121)
    take122_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take122_2 = take122_1["アイテムCD"].values#追加項目2
    take123 = pd.DataFrame({"アイテムCD":[take122_2],"商品名":[i],"SET数":[take122]})
   
    sample_21x.append(take123)
    
take124 = pd.concat(sample_21x)
take125 = pd.DataFrame(take124)
take126 = take125.sort_values(by="SET数" ,ascending=False)
take126.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/21.xlsx")
#print(take118)


  
  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー126


for i in unq_22 :
  #print(i)
  if i == keyitem[21]:
    del_failes.append(i)  
    
  else:
    sample_22_in = pd.concat(sample_22)
    take127 = sample_22_in[sample_22_in["商品名"] == i]
    take128 = len(take127)
    take128_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take128_2 = take128_1["アイテムCD"].values#追加項目2
    take129 = pd.DataFrame({"アイテムCD":[take128_2],"商品名":[i],"SET数":[take128]})
   
    sample_22x.append(take129)
    
take130 = pd.concat(sample_22x)
take131 = pd.DataFrame(take130)
take132 = take131.sort_values(by="SET数" ,ascending=False)
take132.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/22.xlsx")
#print(take118)


  
  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー132

for i in unq_23 :
  #print(i)
  if i == keyitem[22]:
    del_failes.append(i)  
    
  else:
    sample_23_in = pd.concat(sample_23)
    take133 = sample_23_in[sample_23_in["商品名"] == i]
    take134 = len(take133)
    take134_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take134_2 = take134_1["アイテムCD"].values#追加項目2
    take135 = pd.DataFrame({"アイテムCD":[take134_2],"商品名":[i],"SET数":[take134]})
   
    sample_23x.append(take135)
    
take136 = pd.concat(sample_23x)
take137 = pd.DataFrame(take136)
take138 = take137.sort_values(by="SET数" ,ascending=False)
take138.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/23.xlsx")
#print(take118)


  
  
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー138

for i in unq_24 :
  #print(i)
  if i == keyitem[23]:
    del_failes.append(i)  
    
  else:
    sample_24_in = pd.concat(sample_24)
    take139 = sample_24_in[sample_24_in["商品名"] == i]
    take140 = len(take139)
    take140_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take140_2 = take140_1["アイテムCD"].values#追加項目2
    take141 = pd.DataFrame({"アイテムCD":[take140_2],"商品名":[i],"SET数":[take140]})
   
    sample_24x.append(take141)
    
take142 = pd.concat(sample_24x)
take143 = pd.DataFrame(take142)
take144 = take143.sort_values(by="SET数" ,ascending=False)
take144.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/24.xlsx")
#print(take118)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー144

for i in unq_25 :
  #print(i)
  if i == keyitem[24]:
    del_failes.append(i)  
    
  else:
    sample_25_in = pd.concat(sample_25)
    take145 = sample_25_in[sample_25_in["商品名"] == i]
    take146 = len(take145)
    take146_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take146_2 = take146_1["アイテムCD"].values#追加項目2
    take147 = pd.DataFrame({"アイテムCD":[take146_2],"商品名":[i],"SET数":[take146]})
   
    sample_25x.append(take147)
    
take148 = pd.concat(sample_25x)
take149 = pd.DataFrame(take148)
take150 = take149.sort_values(by="SET数" ,ascending=False)
take150.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/25.xlsx")
#print(take118)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー150

for i in unq_26 :
  #print(i)
  if i == keyitem[25]:
    del_failes.append(i)  
    
  else:
    sample_26_in = pd.concat(sample_26)
    take151 = sample_26_in[sample_26_in["商品名"] == i]
    take152 = len(take151)
    take152_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take152_2 = take152_1["アイテムCD"].values#追加項目2
    take153 = pd.DataFrame({"アイテムCD":[take152_2],"商品名":[i],"SET数":[take152]})
   
    sample_26x.append(take153)
    
take154 = pd.concat(sample_26x)
take155 = pd.DataFrame(take154)
take156 = take155.sort_values(by="SET数" ,ascending=False)
take156.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/26.xlsx")
#print(take118)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー156

for i in unq_27 :
  #print(i)
  if i == keyitem[26]:
    del_failes.append(i)  
    
  else:
    sample_27_in = pd.concat(sample_27)
    take157 = sample_27_in[sample_27_in["商品名"] == i]
    take158 = len(take157)
    take158_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take158_2 = take158_1["アイテムCD"].values#追加項目2
    take159 = pd.DataFrame({"アイテムCD":[take158_2],"商品名":[i],"SET数":[take158]})
   
    sample_27x.append(take159)
    
take160 = pd.concat(sample_27x)
take161 = pd.DataFrame(take160)
take162 = take160.sort_values(by="SET数" ,ascending=False)
take162.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/27.xlsx")
#print(take118)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー162

for i in unq_28 :
  #print(i)
  if i == keyitem[27]:
    del_failes.append(i)  
    
  else:
    sample_28_in = pd.concat(sample_28)
    take163 = sample_28_in[sample_28_in["商品名"] == i]
    take164 = len(take163)
    take164_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take164_2 = take164_1["アイテムCD"].values#追加項目2
    take165 = pd.DataFrame({"アイテムCD":[take164_2],"商品名":[i],"SET数":[take164]})
   
    sample_28x.append(take165)
    
take166 = pd.concat(sample_28x)
take167 = pd.DataFrame(take166)
take168 = take160.sort_values(by="SET数" ,ascending=False)
take168.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/28.xlsx")
#print(take118)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー168 


for i in unq_29 :
  #print(i)
  if i == keyitem[28]:
    del_failes.append(i)  
    
  else:
    sample_29_in = pd.concat(sample_29)
    take169 = sample_29_in[sample_29_in["商品名"] == i]
    take170 = len(take169)
    take170_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take170_2 = take170_1["アイテムCD"].values#追加項目2
    take171 = pd.DataFrame({"アイテムCD":[take170_2],"商品名":[i],"SET数":[take170]})
   
    sample_29x.append(take171)
    
take172 = pd.concat(sample_28x)
take173 = pd.DataFrame(take172)
take174 = take173.sort_values(by="SET数" ,ascending=False)
take174.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/29.xlsx")
#print(take118)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー174



for i in unq_30 :
  #print(i)
  if i == keyitem[29]:
    del_failes.append(i)  
    
  else:
    sample_30_in = pd.concat(sample_30)
    take175 = sample_30_in[sample_30_in["商品名"] == i]
    take176 = len(take175)
    take176_1 = df_data2[df_data2["商品名"] == i]#追加項目1
    
    take176_2 = take176_1["アイテムCD"].values#追加項目2
    take177 = pd.DataFrame({"アイテムCD":[take176_2],"商品名":[i],"SET数":[take176]})
   
    sample_30x.append(take177)
    
take178 = pd.concat(sample_28x)
take179 = pd.DataFrame(take178)
take180 = take179.sort_values(by="SET数" ,ascending=False)
take180.to_excel("C:/Users/fun-f/Desktop/myfile/basket-analysis/30.xlsx")
#print(take118)

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー180
  
 #客数
 #Aの商品が売れた点数
 #Bの商品が売れた点数
 #AとBが一緒に売れたセット数 = X
 #ｘが全体客数のナンパ―セントが購入せれたか
 
 #要素１　支持度(※閾値)
 #要素２　信頼度(※確信度)
 #要素３　LIFT値
 


#print(xname_values)
#print(x_values)
 