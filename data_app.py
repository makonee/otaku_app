import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,timedelta

# ユーザーからの入力を受け付ける
st.header('活動の記録')
date = st.date_input('日付選択')
group = st.text_input('グループ入力')
kounyuu = st.selectbox('購入種選択', ['チケット', 'CD・Mカード', 'チェキ','生写真','アクキー','グッズ'])
kounyuusuu = st.number_input('購入数',min_value=0,step=1)
purchase = st.number_input('購入単価',min_value=0)
result = kounyuusuu * purchase
st.write(f"合計: {result}円")

# ユーザーが入力したデータをDataFrameに保存
data = {'日付': [date], 'グループ': [group], '購入種': [kounyuu], '購入数': [kounyuusuu], '購入単価': [purchase], '合計金額': [result]}
df = pd.DataFrame(data)

# 初回のみFalseを設定
if 'csv_created' not in st.session_state:
    st.session_state.csv_created = False

# '記録を保存'ボタンが押された場合にデータをCSVファイルに保存
if st.button('保存'):
    filename = "purchase_records.csv"
    df.to_csv(filename, mode='a', header=not st.session_state.csv_created, index=False)
    st.success(f'{filename} にデータを保存しました。')
    st.session_state.csv_created = True


# CSVファイルからデータを読み込む
filename = "purchase_records.csv"
df = pd.read_csv(filename)

# データを表示
st.write(df)

# グループごとの購入数の合計を計算
st.subheader('グループごとの購入数')
group_total = df.groupby('グループ')['購入数'].sum()

# グラフにプロット
st.bar_chart(group_total)

# グループごとの購入金額の合計を計算
st.subheader('グループごとの購入金額')
group_total_price = df.groupby('グループ')['購入単価'].sum()

# グラフにプロット
st.bar_chart(group_total_price)

# 購入種別ごとの購入数の合計を計算
st.subheader('購入種ごとの購入数')
purchase_type_total = df.groupby('購入種')['購入数'].sum()

# グラフにプロット
st.bar_chart(purchase_type_total)

# 購入種別ごとの購入金額の合計を計算
st.subheader('購入種別ごとの購入金額')
purchase_type_total_price = df.groupby('購入種')['購入単価'].sum()

# グラフにプロット
st.bar_chart(purchase_type_total_price)