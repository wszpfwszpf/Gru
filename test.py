# # -*- coding: utf-8 -*-
# # Author:ZPF
# # date: 2021/12/10 10:10
# import torch
# import numpy as np
# import random
#
# if __name__ == '__main__':
#     # list1 = [3.54223426133333,
#     #          3.29120416533333,
#     #          4.43979781733333,
#     #          3.64865369333333,
#     #          4.37541137200000,
#     #          4.81579381866667,
#     #          3.51330547066667,
#     #          3.92753586533333,
#     #          3.58632710933333,
#     #          4.38950647066667,
#     #          4.44391894933333,
#     #          4.24313251200000,
#     #          3.83721183333333,
#     #          4.12742821600000,
#     #          4.62005872800000,
#     #          3.12854725200000,
#     #          4.76356340533333,
#     #          3.73398814400000,
#     #          3.89646478800000,
#     #          4.68848376133333]
#     list1 = [0] * 20
#
#     # list2 = [17.8704919389937,
#     #          17.3386044389937,
#     #          17.2390164716981,
#     #          16.7867223194969,
#     #          17.7031815849057,
#     #          16.9822856044025,
#     #          17.2931003358491,
#     #          16.4631514188679,
#     #          17.1844122471698,
#     #          17.1043453691824,
#     #          17.2261069603774,
#     #          16.3911839289308,
#     #          16.4748159100629,
#     #          17.2415294245283,
#     #          17.1883223433962,
#     #          17.0653254616352,
#     #          16.5977514955975,
#     #          16.4183160037736,
#     #          16.8359416389937,
#     #          16.5532469924528]
#     # std = 1.2
#
#
#
#     # average = sum(list2) / len(list2)
#     # print(average)
#     # a = torch.Tensor(len(list1), 1).uniform_(-std, std) + average
#     # print('%.8f', a)
#     # list2 = list(a)
#     # std_1 = np.std(list2)
#     # print(std_1)
#     # with open('2.txt', 'a+') as f:
#     #     pass
#     # with open('2.txt', 'w') as f:
#     #     for num in list2:
#     #         f.writelines(str(float(num)) + '\n')
#     #     f.writelines('方差：' + str(std_1))
#     mea = 17.1523
#     a = mea +  1 * np.random.randn(20, 1)
#     var1 = np.var(a)
#     print(var1)
#     print(a)
#     with open('1.txt', 'a+') as f:
#         pass
#     with open('1.txt', 'w') as f:
#         for num in a:
#             f.writelines(str(float(num)) + '\n')
#         f.writelines('方差：' + str(var1))

import fire


def hello(name):
    return 'Hello {name}!'.format(name=name)


if __name__ == '__main__':
    fire.Fire()
