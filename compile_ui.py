import glob, os, pickle

mtimes_old = []

if os.path.isfile('mtimes.pickle'):
    mtimes_old = pickle.loads(open('mtimes.pickle', 'rb').read())

mtimes_new = []

for f in glob.glob('src\\*.ui'):
    mtimes_new.append([f, os.stat(f).st_mtime])
    
mtimes_new.sort()

if mtimes_new != mtimes_old:
    open('mtimes.pickle', 'wb').write(pickle.dumps(mtimes_new))
    os.chdir('src')
    for fname, mtime in mtimes_new:
        fname = os.path.split(fname.split('.')[0])[-1]
        os.system(f'call pyuic5 {fname}.ui -o {fname}.py')
    print('ui modified... compiling')
    print('-'*80)