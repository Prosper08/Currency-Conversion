import streamlit as st
st.header('Currency Conversion in Black Markets') 
a=st.number_input('Please enter the amount you want to convert')
b=['NGN','GBP','EUR','USD']
c, conv=st.columns(2)
first= c.radio('Input your base currency',b )
second= conv.radio('Input currency you want to convert to',b)
if first=='NGN'and second=='GBP':
    d=round(a/748,1)
    if st.button('Calculate'):
        st.subheader (f'{d}GBP')
elif  first=='GBP' and second=='NGN':
    d=round(a*748,1)
    if st.button('Calculate'):
        st.subheader (f'{d}NGN')
elif first=='NGN' and second=='USD':
    d=round(a/580,1)
    if st.button('Calculate'):
        st.subheader (f'{d}USD')
elif  first=='USD' and second=='NGN':
    d=round(a*580,1)
    if st.button('Calculate'):
        st.subheader (f'{d}NGN')
elif  first=='NGN' and second=='EUR':
    d=round(a/634,1)
    if st.button('Calculate'):
        st.subheader (f'{d}EUR')
elif  first=='EUR' and second=='NGN':
    d=round(a*634,1)
    if st.button('Calculate'):
        st.subheader (f'{d}NGN')
elif  first=='GBP' and second=='USD':
    e=(a*748)
    d=round(e/580,1)
    if st.button('Calculate'):
        st.subheader (f'{d}USD')
elif  first=='USD' and second=='GBP':
    e=a*580
    d=round(e/748,1)
    if st.button('Calculate'):
        st.subheader (f'{d}GBP')
elif  first=='GBP' and second=='EUR':
    e=a*748
    d==round(e/634,1)
    if st.button('Calculate'):
        st.subheader (f'{d}EUR')
elif  first=='EUR' and second=='GBP':
    e=a*634
    d=round(e/748,1)
    if st.button('Calculate'):
        st.subheader (f'{d}GBP')
elif  first=='EUR' and second=='USD':
    e=a*634
    d=round(e/580,1)
    if st.button('Calculate'):
        st.subheader (f'{d}USD')
elif  first=='USD' and second=='EUR':
    e=a*580
    d=round(e/634,1)
    if st.button('Calculate'):
        st.subheader (f'{d}EUR')
elif  first=='NGN' and second=='NGN':
    d=a
    if st.button('Calculate'):
        st.subheader (f'{d}NGN')
elif  first=='USD' and second=='USD':
    d=a
    if st.button('Calculate'):
        st.subheader (f'{d}USD')
elif  c=='GBP' and second=='GBP':
    d=a
    if st.button('Calculate'):
        st.subheader (f'{d}GBP')
elif  first=='EUR' and second=='EUR':
    d=a
    if st.button('Calculate'):
        st.subheader (f'{d}EUR')

else:
     if st.button('Calculate'):
        st.error('This is an Error')
