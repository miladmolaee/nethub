line = '---------------------------------------------------------------------------------\n'
l = '---------------------------------------------------------------------------------'


def write_final_result(net):

    file = open(net.working_directory + '\\training_result.txt', 'w')

    file.write(line)
    print(l)
    file.write('|\t\t\t\tRESULT\t\t\t\t\t\t|\n')
    print('|\t\t\t\tRESULT\t\t\t\t\t\t|')
    file.write(line)
    print(l)
    file.write('\t\t|\t\tR2\t\t|\t\tmse\t\t|\n')
    print('\t\t|\t\tR2\t\t|\t\tmse\t\t|')
    file.write(line)
    print(l)

    file.write('training\t|\t' + str(net.final_training_accuracy) + '\t|\t' + str(net.final_training_loss) + '\t|\n')
    print('training\t|\t' + str(net.final_training_accuracy) + '\t|\t' + str(net.final_training_loss) + '\t|')
    file.write(line)
    print(l)

    file.write('validation\t|\t' + str(net.final_val_accuracy) + '\t|\t' + str(net.final_val_loss) + '\t|\n')
    print('validation\t|\t' + str(net.final_val_accuracy) + '\t|\t' + str(net.final_val_loss) + '\t|')
    file.write(line)
    print(l)

    file.write('test\t\t|\t' + str(net.final_test_accuracy) + '\t|\t' + str(net.final_test_loss) + '\t|\n')
    print('test\t\t|\t' + str(net.final_test_accuracy) + '\t|\t' + str(net.final_test_loss) + '\t|')
    file.write(line)
    print(l)

    file.write('all\t\t|\t' + str(net.final_all_accuracy) + '\t|\t' + str(net.final_all_loss) + '\t|\n')
    print('all\t\t|\t' + str(net.final_all_accuracy) + '\t|\t' + str(net.final_all_loss) + '\t|')
    file.write(line)
    print(l)

    file.close()
