import cgi

from urllib import quote_plus

header = 'Content-Type:text/html\n\n'
url = '/cgi-bin/friendsC.py'

errhtml = '''<HTML><HEAD><TITLE>
Friends CGi Demo</Title></HEAD>
<body><H3>.....

</body></HTML>'''

def showError(error_str):
    print header + errhtml % error_str

formhtml = '''<HTML>....</html>'''

fadio='<INPUT type=radio name=howmany value="%s" %s>%s\n'

def showForm(who,howmany):
    friends = []
    for i in (0,10,25,50,100):
        checked = ''
        if str(i) == howmany:
            checked ='checked'
            friends.append(fradio %(str(i),checked,str(i)))
    print('%s%s' %(header,formhtml %(who,url,who,''.join(friends))))

    reshtml = '''<html>...</html>'''

def doresults(who,howmant):
    newurl = url +'?action=reedit&person=%s&howmany=%s'% \
    (quote_plus(who),howmany)
    print header + reshtml %(who,who,howmant,newurl)

def process():
    error = ''
    form = cgi.FieldStorage()

    if 'person' in from:
        who = form['person'].value.title()
    else:
        who = 'NEW USER'

    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        if 'action' in form and form['action'].value == 'edit':
            error = 'Please select number of friends.'
        else:
            howmany = o

    if not error:
        if 'action' in form and form['action'].value !='reedit':
            doResults(who,howmay)
        else:
            showForm()
    else:
        showError(error)

if __name__ =='__main__':
    process()
