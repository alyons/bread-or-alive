from os import listdir
from os.path import isfile, join

def main():
    my_path = './assets/images/2021-12-11'
    only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    with open('gallery.yml', 'w') as file:
        file.write('gallery:\n')
        for index, item in enumerate(only_files):
            file.write(f'  - url: /assets/images/2021-12-11/{item}\n')
            file.write(f'    image_path: /assets/images/2021-12-11/{item}\n')
            file.write(f'    alt: "Image {index}"\n')
            file.write(f'    title: "Image {index} title caption"\n')
    

if __name__ == '__main__':
    main()
