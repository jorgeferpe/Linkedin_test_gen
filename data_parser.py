import os

folder =os.getcwd() + os.sep + 'quiz'
subjects=[]
questions=[]
question_doc=[]
answers=[]

def extractSubjects():
    for subject in os.listdir(folder):
        if subject[0]!= '.' and os.path.isdir(folder + os.sep + subject):
            subjects.append(subject)
        else:
            pass

    subjects.sort()

    for subject in subjects:
        print(subject)
    return

def extractQuestions(subject):
    subFolder = folder + os.sep + subject + os.sep + (subject+'-quiz.md')


    with open(subFolder, 'r+') as info:
        number=0
        for line in info.readlines():
            
            if line.startswith('####'):
                number+=1
                question = line.split('. ',1)
                #print(number + '_' +question[1])
                print(number)
                questions.append(str(number) + '_' +question[1])
            elif line.startswith('- [')==False:
                if line in ['\n', '\r\n']:
                    pass
                elif line.startswith('[reference') or line.startswith('[Reference'):
                    pass
                elif line.startswith('Explanation') or line.startswith('**Explanation**'):
                    pass
                elif line.startswith('![image]'):
                    pass
                elif line.startswith('hint'):
                    pass
                else:
                    print(line)
    return
'''
            elif line.startswith('- ['):
                print('answer')
                while line.startswith('####')==False:
                    pass
'''
    
    


def extractAnswers(subject):
    subFolder = folder + os.sep + subject + os.sep + (subject+'-quiz.md')
    with open(subFolder, 'r+') as info:
        for line in info.readlines():

            if line.startswith('####'):
                number = line.split(' Q',-1)[1].split('. ')[0]
                
            if line.startswith('- ['):
                if '[x]' in line:
                    answer = line.split('] ',1)
                    answers.append(number+'_c_'+answer[1])
                    print(number+'_c_'+answer[1])
                else:
                    answer = line.split('] ',1)
                    try:
                        answers.append(number+'_'+answer[1])
                    except:
                        continue
                    print(number+'_'+answer[1])
        return

#extractSubjects()
extractQuestions('git')
#extractAnswers('git')