import os
import markdown
print('======================')
print('=    MARKSITE        =')
print('======================')
try:
    with open('conf.txt','r') as conf:
        for _1 in conf:
            if 'wspace=' in _1:
                wspace = (_1[7:int(len(_1))])
                os.mkdir(wspace)
except:
    os.chdir(wspace)
    bl = os.listdir()
    build = open(bl[0])
    md = markdown.markdown(build.read())
    build.close()
    os.path.dirname(bl[0])
    os.chdir('..')
    try:
        os.mkdir('build')
    except:
        os.chdir('build')
        write = open(bl[0][:-3] + '.html','w')
        write.write(md)
        write.close()
        print('done,now visit http://127.0.0.1:8000 to view it')
        os.system('python -m http.server')


