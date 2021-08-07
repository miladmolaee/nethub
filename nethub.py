# created by miladmolaee@hotmail.com

from Run.Train.single import Single
from Run.Train.multi import Multi
from Prediction import predict
from Util.info import Info

if __name__ == '__main__':

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
        print(' * Yor entered a wrong number !  -  Press ENTER to exit')
        input()
        sys.exit()

    if command == '1':  # training

        root_dir = input(' # please enter the [ name ] or [ address ] of your project:\n>>> ')

        try:
            file = open(".config")
            file.close()
        except OSError as err:
            print("OS error: {0} - but we creat a default one".format(err))
            file = open(".config", "w+")
            file.write('Net Hub - version : ' + Info.version + '\n')
            file.close()

        file_conf = open(".config", "r")
        _dir = file_conf.readlines()
        file_conf.close()
        _f = False

        for i in _dir:
            if i.__contains__('='):
                _sp = i.split('=')
                if root_dir == _sp[0]:
                    root_dir = _sp[1]
                    _f = True

        if root_dir == 'root':
            file = open('script.sptnet', 'r')

        else:

            if not _f:
                save_ = input('Do you want to save this path as a project directory? \'y\' or \'n\' : ')
                if save_ == 'y' or save_ == 'yes':
                    name_ = input('Enter a name for this project : ')
                    file_config = open(".config", "a")
                    file_config.write(name_ + '=' + root_dir + '\n')
                    file_config.close()

            root_dir = root_dir[:len(root_dir) - 1]
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
