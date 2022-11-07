# Stwórz listę składającą się z kilku elementów różnego typu np.
# [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć

elements = [13, 'string', 2.45, 0]


for i in elements:
    try:
        x = 10 / i
    except ValueError:
        print('To jest string', i)
    except ZeroDivisionError:
        print(' Zero div error', i)


