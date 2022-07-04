import json
import glob


def count_n(s):
    return len(s.splitlines())


all_dir = 'text'
directories = [f'{all_dir}/bach', f'{all_dir}/magi', f'{all_dir}/inter', f'{all_dir}/dpo', f'{all_dir}/mba', f'{all_dir}/startup', f'{all_dir}/dobav', f'{all_dir}/drugoe']


def write(direc):
    """
    Генерация ответов на вопросы с текстовых файлов.
    Берёт файлы с указанных директорий и генерирует их в json файлы
    Пример:
    вход     ---     директория 'text/bach' (внутри m > 0 файлов)
    выход    ---     в директории 'gen' генерируется файл 'bach.json' c m ответами в виде списка

    вход     ---     директория 'text1/text2/text3/text4/bach' (внутри m > 0 файлов)
    выход    ---     в директории 'gen' генерируется файл 'bach.json' c m ответами в виде списка

    :return: нету, только генерация файла
    """
    for i in direc:
        texts = {}
        temp = [i.split('\\')[1] for i in glob.glob(f'{i}/*.txt')]

        for j in temp:
            with open(f'{i}/{j}', 'r', encoding='utf-8') as f:
                data = ''.join([j.replace('\n', '////') for j in f.readlines()])
                texts[j.split('.txt')[0]] = data

        with open(f'{"gen/"+i.split("/")[-1]}.json', 'w', encoding='utf-8') as f:
            f.write('{\n'
                    '\t"asks": {\n')
            for j in texts:
                f.write(f'\t\t\"{j}\": \"{texts[j]}\",\n')
            f.write('\t\t\"null_ask\": \"\"\n'
                    '\t}\n'
                    '}\n')


def read(name):
    """
    Возвращение ответов на вопросы с заданного файла name.json

    :return: dict
    """
    f = open(f'data/gen/{name}.json', encoding='utf-8')

    res = json.load(f)['asks']
    for i in res:
        res[i] = res[i].replace('////', '\n')

    f.close()
    return res


def main():
    write(directories)
    print(read('bach'))
    print(read('magi'))
    print(read('inter'))
    print(read('dpo'))
    print(read('mba'))
    print(read('startup'))
    print(read('kasal'))
    print(read('popas'))
    print(read('dobav'))
    print(read('drugoe'))


if __name__ == '__main__':
    main()
