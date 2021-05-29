# created by miladmolaee@hotmail.com
from Run.Train.single import Single
from Run.Train.multi import Multi
from Prediction import predict

if __name__ == '__main__':

    from os import path
    import sys

    print('------------------------------------------------------------------')
    print('|                                                                |')
    print('|           # enter 1 for Training                               |')
    print('|           # enter 2 for Test                                   |')
    print('|           # enter 3 for Prediction                             |')
    print('|                                                                |')
    print('------------------------------------------------------------------')

    command = input('>>> ')

    if not (command == '1' or command == '2' or command == '3'):
        print('Yor entered a wrong number !\nPress ENTER to exit')
        input()
        sys.exit()

    if command == '1':  # training

        root_dir = input('please enter the address of the directory of your project:\n>>> ')

        if not path.exists(root_dir):
            print('Yor entered path is not exists !\nPress ENTER to exit')
            input()
            sys.exit()

        file = open(root_dir + '\\script.sptnet', 'r')
        Lines = file.readlines()
        scripts = []
        _type = 0

        for line in Lines:

            if not line[0] == '#':
                string = ''
                for i in line:
                    if not (i == ' ' or i == '\t' or i == '\n'):
                        string = string + i

                scripts.append(string)

                if string.__contains__('multirun'):
                    if string.__contains__('off'):
                        _type = 1
                    elif string.__contains__('on'):
                        _type = 2

        if _type == 1:
            single = Single()
            single.set(script=scripts, root_path=root_dir)
            single.run()

        elif _type == 2:
            multi = Multi()
            multi.set(scripts, root_path=root_dir)
            multi.run()

    elif command == '2':  # test

        print('test is not available now')

    elif command == '3':  # prediction

        main_dir = input('please enter the directory address contain \'my_model_weights.h5\' file:\n>>> ')

        predict.prediction(main_dir)