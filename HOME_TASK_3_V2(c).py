def m_func(n_1, n_2, n_3):
    m_list = [n_1, n_2, n_3]
    try:
        m_list.remove(min(m_list))
        return sum(m_list)
    except TypeError:
        return 'Error'
print(m_func(n_1=15, n_2=5, n_3=10))
