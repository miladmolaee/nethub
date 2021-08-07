line = '---------------------------------------------------------------------------------\n'
_line = '---------------------------------------------------------------------------------'


def write_final_result(net, _print=True):
    file = open(net.working_directory + '\\training_result.txt', 'w')

    file.write(line)
    file.write('|\t\t\t\tRESULT\t\t\t\t\t\t|\n')
    file.write(line)
    file.write('\t\t|\t\tR2\t\t|\t\tmse\t\t|\n')
    file.write(line)
    file.write('training\t|\t' + str(net.final_training_accuracy) + '\t|\t' + str(net.final_training_loss) + '\t|\n')
    file.write(line)
    file.write('validation\t|\t' + str(net.final_val_accuracy) + '\t|\t' + str(net.final_val_loss) + '\t|\n')
    file.write(line)
    file.write('test\t\t|\t' + str(net.final_test_accuracy) + '\t|\t' + str(net.final_test_loss) + '\t|\n')
    file.write(line)
    file.write('all\t\t|\t' + str(net.final_all_accuracy) + '\t|\t' + str(net.final_all_loss) + '\t|\n')
    file.write(line)
    file.close()

    if _print:
        print(_line)
        print('|\t\t\t\tRESULT\t\t\t\t\t\t|')
        print(_line)
        print('\t\t|\t\tR2\t\t|\t\tmse\t\t|')
        print(_line)
        print('training\t|\t' + str(net.final_training_accuracy) + '\t|\t' + str(net.final_training_loss) + '\t|')
        print(_line)
        print('validation\t|\t' + str(net.final_val_accuracy) + '\t|\t' + str(net.final_val_loss) + '\t|')
        print(_line)
        print('test\t\t|\t' + str(net.final_test_accuracy) + '\t|\t' + str(net.final_test_loss) + '\t|')
        print(_line)
        print('all\t\t|\t' + str(net.final_all_accuracy) + '\t|\t' + str(net.final_all_loss) + '\t|')
        print(_line)
