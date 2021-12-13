import pandas as pd


def get_result(filename, round_):
    file = pd.read_csv('csv_file/' + filename)
    m_dict = {}

    for budget in range(200, 801, 100):
        m_dict[budget] = []
        for _id in range(0, round_):
            tmp = file[(file['budget'] == budget) & (file['node_id'] == _id)]
            m_dict[budget].append({'node_id': _id, 'average_rate': tmp['rate'].sum() / round_,
                                   'budget_save': tmp['budget_save'].sum() / round_,
                                   'user_num': tmp['user_num'].sum() / round_})
    return m_dict


def get_result3(filename):
    file = pd.read_csv('csv_file/' + filename)
    res = {'average_rate': list(file['rate']), 'budget_save': list(file['budget_save']),
           'user_num': list(file['user_num'])}
    print(res)
    return res
