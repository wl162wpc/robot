import os
from aip import AipSpeech


APP_ID = '16574953'
API_KEY = 'jq22QZiLtwp2vAiMM1TQwWZV'
SECRET_KEY = 'yHH2CiaFQkTpGCpCF0t9NRGEkiTS4jP3'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

role_param = {
    'vol': 5,
    'per': '4',
    'pit': '5'
}


def text2audio(worlds, role_param, out_putfile, lang='zh'):
    result = client.synthesis(worlds, lang, 1, role_param)

    if not isinstance(result, dict):
        with open(out_putfile, 'wb') as f:
            f.write(result)
        return 'ok'


def anything2pcm(input_file):
    output_file=input_file.rsplit('.',1)[0]+'.pcm'
    cmd='ffmpeg -y -i {} -acodec pcm_s161e -f s161e -ac 1 -ar 16000 {}'.format(input_file,output_file)
    print(os.popen(cmd).read())
    return output_file


def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

if __name__ == '__main__':
    file_name='hello.mp3'

    # if text2audio('你好百度',role_param,file_name,lang='zh'):
    #     print('合成成功')
    # else:
    #     exit('合成失败')

    output_file=anything2pcm(file_name)
    result=client,asr(get_file_content(output_file),'pcm',16000,{
        'dev_pid':1536,
    })
    print(result)

