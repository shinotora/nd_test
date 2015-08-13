import os
import tftpy
import datetime

ip_list = []                            #List storing the IP addresses the user enters

print '***** Welcome to LAB_1 *****'


while True:
    x = raw_input("\nEnter the Router's IP address below to fetch the Config file (or done):\n>>")
	# split devide the name by specific letters
    z = x.split('.')

    #print z

    """Check whether IP address entered is Valid"""

    if x == 'done':
        break
    else:
        for val in range(len(z)):
            if int(z[val]) > 255:
                print 'Invalid IP. Please enter a value between 0 & 255'

            else:
                pass

        ip_list.append(x)

#print ip_list
#print len(ip_list)


def read_info():

    """Function to download file from the router"""

    for i in range(0,len(ip_list)):

        connection = tftpy.TftpClient(ip_list[i], 69)
        connection.download('/startup-config', 'my_local_copy.cfg')
        data1 = open('my_local_copy.cfg')
        content1 = data1.read()

        compare_data(ip_list[i], content1)


def store_file(x, y):

    """Function to store the file"""

    store = open(x + '.cfg', 'w')
    store.write(y)


def output_info(x):

    """Function to print the information requested"""
content3
     = x.split('\n')
    #print content3

    for i, j in enumerate(content3):

        if j.startswith('version'):
            print 'Running IOS {}'.format(content3[i]) + '\n'

        elif j.startswith('hostname'):
            print '\n' + content3[i] + '\n'

        elif j.startswith('service'):
            print content3[i]

        elif j.startswith('interface'):
            print content3[i]
            print content3[i + 1]
            print content3[i + 2]
            print content3[i + 3]
            print content3[i + 4]


def compare_data(x, content1):

    """Function to compare data"""

    dir = '/home/netman/Lab_1/' + x

    if not os.path.exists(dir):
            os.makedirs(dir)
            os.chdir(dir)
            store_file(x, content1)


    if os.path.exists(dir):

        os.chdir(dir)
        a = os.listdir(dir)
        b = sorted(a)
        #print b[-1]
        dt = datetime.datetime.now()

        if os.path.isfile(b[-1]):
            data2 = open(b[-1])
            content2 = data2.read()

            if content2 != content1:
                if len(a) > 1:

                    new_file = open(b[-1], 'w')
                    new_file.write(content1)
                    print '\nPARAMETERS HAVE CHANGED. Saving new config file for Router {} at \nDATE/TIME: {}\n'.format(x, dt)
                    print 'NEW PARAMETERS:\n'
                    output_info(content1)
                    print '\nOLD PARAMETERS:\n'
                    output_info(content2)

                else:

                    new_file = open(x + str(dt) + '.cfg', 'w')
                    new_file.write(content1)
                    print '\nPARAMETERS HAVE CHANGED. Saving new config file for Router {} at \nDATE/TIME: {}\n'.format(x, dt)
                    print 'NEW PARAMETERS:\n'
                    output_info(content1)
                    print '\nOLD PARAMETERS:\n'
                    output_info(content2)


            else:
                #print 'equal'
                print '\nSAVING CONFIG FOR THE ROUTER {}... \n'.format(x)
                output_info(content2)


def main():

    """Main Function"""

    read_info()

main()
