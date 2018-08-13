import sys
from collections import defaultdict
#Parts of Speech**********************        

class PartOfSpeech:
    def __init__(self, speechType,word):
        self.Type = speechType
        self.word = word
        
#Perform action 
#Tenses
    #(Present: simple, continous, perfect. Past: simple, continous, perfect. Future: future, perfect)
#Agree with subject(Singular 1st-3rd, Plural 1st-3rd)
#omitted -> Fragment 
class Verb:
    def __init__(self, verbType, tense, singPlur, person,regIrreg, word):
        #Action verbs****
            #Transitive, intransitive
        #No Action Verbs***
            #To Be Conjugations
            #Linking Verbs
            #Auxiliary Verbs
        self.Type = verbType
        #Present, Past, Future, present perfect, etc
        self.tense = tense
        #For singular/plural verb conjugation/matching noun/pronoun
        self.singPlur = singPlur
        #1st, 2nd or 3rd person
        self.person = person
        #If the verb is regular or irregular
        self.regIrreg = regIrreg
        #Actual word
        self.word = word

#Answer the question of: How,when,where,why, to what extent, how much, how often
#Modifies verbs, adjectives, adverbs
class Adverb:
    def __init__(self, adverbType, word):
        #Manner(Angrily,Happily...)
        #Place(Near,There,ahead...)
        #Time(Yesterday,now,then,late)
        #Frequency(often,usually,frequently)
        self.Type = adverbType
        self.word = word

#Person, place, thing or idea
class Noun:
    def __init__(self, nounType, ppti, singPlur, person, word):
        #Collective, Mass, Count, Proper, Common, Concrete, Abstract
        self.Type = nounType
        #If it's person place thing or idea
        self.ppti = ppti
        #Singular or plural noun
        self.singPlur = singPlur 
        #1st, 2nd, 3rd person
        self.person = person
        #Actual word
        self.word = word

#Replaces a Noun/Noun Phrase
class Pronoun:
    def __init__(self, pronounType, word):
        #Personal, Demonstrative, Interrogative, Indefinite, Possessive, reciprocal, relative, reflexive, intensive
        self.Type = pronounType
        self.word = word
        self.firstPerson = ["I","We"]
        self.secondPerson = ["You","You all"]
        self.thirdPerson = ["He","She","It","They"]
        self.singular = ["I", "You", "He", "She", "It"]
        self.plural = ["We", "You","You all", "They"]
        
                                
       
class Adjective:
    def __init__(self, adjectiveType, word):
        #Descriptive,Quantitative,Demonstrative,Possessive,Interrogative,Distributive, Articles
        self.Type = adjectiveType
        self.word = word
   

#GRAMMAR****************************************************     
class Grammar:
    def __init__(self):
        #Keep track of current word number in sentence parsing
        self.wordNumber = 0
        #List of parts of speech of each word
        self.POSPattern = []
        #List of Generally Grammatical structure
        self.GrammarPattern = []
        #Subject
        self.Subject = []
        #Predicate
        self.Predicate = []
        #Object
        self.Object = []
        #List of words forming the sentence
        self.sentence = []
        #1st,2nd,3rd person
        self.person = []
        #Present,past,future, etc
        self.tense = ""
        #Singular/plural subject
        self.subjectSingPlur = ""
        
        self.terminals = defaultdict(list)
        
        
    
    def restart(self):
        self.wordNumber = 0
        self.POSPattern = []
        self.GrammarPattern = []
        self.person = []
        self.tense = ""
        self.subjectSingPlur = ""
        self.Subject = []
        self.Predicate = []
        self.Object = []
        self.currentTerminal = ""
                
    def boundsCheck(self):
        if self.sentence[int(self.wordNumber)] is ".":
            self._onExit()
            sys.exit() 
    
    def linkTerminal(self):
        if self.currentTerminal == "Subject":
            self.Subject.append(self.POSPattern[self.wordNumber].Type)      
        
        if self.currentTerminal == "Predicate":
            self.Predicate.append(self.POSPattern[self.wordNumber].Type)  
        
        if self.currentTerminal == "Object":
            self.Object.append(self.POSPattern[self.wordNumber].Type)   
    
    def TerminalToString(self,str):
        pass
        #if str == "<Subject>"
       
    def setContext(self, string):
        self.currentTerminal = string
        self.GrammarPattern.append(string)
        
    def _onExit(self):
        #Grammar Patter
        g1 = ""
        
        for i in self.GrammarPattern:
            g1 = g1 + " " + i
            if i == "<Subject>":
                subject = "Subject: "
                for j in self.Subject:
                    subject = subject + " "  + j
                #g1 = g1 + subject + "\n"
            
            elif i == "<Predicate>":
                predicate = "Predicate: "
                for k in self.Predicate:
                    predicate = predicate + " "  + k
                
        
        
        
        predicate = "Predicate: "
        for i in self.Predicate:
            predicate = predicate + " "  + i
            
        objects = "Object: "
        for i in self.Object:
            objects = objects + " "  + i
        #Part Of Speech pattern
        g = ""
        for i in self.POSPattern:
            g = g + " " + i.Type
        
        #Sentence correctly found
        s1 = ""
        for i in self.POSPattern:
            s1 = s1 + " " +  i.word 
            
        print("\nGrammatical Pattern\n")    
        print(g1)
        #print("\n" + subject + "\n")
        #print("\n" + predicate + "\n")
        #print("\n" + object + "\n")
        print(g)
        print("")
        print(s1)
        sys.exit()
        
    def main(self):  
    
        #Enter a sentence to be parsed
        w = input("Enter a sentence")
        w = w.split(" ")
    
        for i in w:
            self.sentence.append(i)
        self.sentence.append(".")
        self.stmt()
        self._onExit()
    
    
    
    
    
    # RECURSIVE DESCENT PARSER******************************    
    #<STMT>: <SV>|<SVO>
    def stmt(self):
        #SUBJECT VERB
        passFail = self.IndependentClause()
        if passFail is 0 and self.sentence[int(self.wordNumber)] is ".":
            self._onExit()
        
        '''#SUBJECT VERB OBJECT
        self.restart()
        passFail = self.SVO()
        if passFail is -1:
            sys.exit()'''
        
    '''#<SUBJECT><PREDICATE>
    def SV(self):
        #Subject
        self.GrammarPattern.append("<Subject>")
        self.GrammarPattern.append("<Predicate>")
        error = self.subject()
        if error is -1:
            return error
        
        #Predicate
        error = self.predicate()
        if error is -1:
            return error
        success = 0
        return success'''
    
    #<SUBJECT><PREDICATE>(<Object>)
    def IndependentClause(self):
        #Subject
        self.setContext("<Subject>")
        error = self.subject()
        if error is -1:
            return error
        
        #Predicate
        self.setContext("<Predicate>")
        error = self.predicate()
        if error is -1:
            return error
        
        #Object
        self.setContext("<Object>")
        error = self.object()
        if error is -1:
            return error
        
        success = 0
        return success
    
    #<adjectives> (noun | pronoun)
    def subject(self):
        self.subject = []
        #Subject is Adjective
        while self.isAdjective(self.sentence[int(self.wordNumber)], False):
            if not self.isAdjective(self.sentence[int(self.wordNumber)], True):
                print("Adj Expected: Syntax error(word: " + self.sentence[int(self.wordNumber)] + ")")
                return -1
        
            
            
        #Subject is Noun
        if not self.isNoun(self.sentence[int(self.wordNumber)]) and not self.isPronoun(self.sentence[int(self.wordNumber)]):
            print("Noun/pronoun Expected: Syntax error(word: " + self.sentence[int(self.wordNumber)] + ")")
            return -1
       
    
    def predicate(self):
        self.Predicate = []
        #Verb is Helping Verb
        helpingused = False
        while self.isHelpingVerb(self.sentence[int(self.wordNumber)], False):
            helpingused = True
            if not self.isHelpingVerb(self.sentence[int(self.wordNumber)], True):
                print("Helping Verb Expected: Syntax error(word: " + self.sentence[int(self.wordNumber)] + ")")
                return -1
    
           
        #Verb is action verb
        if not self.isVerb(self.sentence[int(self.wordNumber)]) and helpingused is False:
            print("Verb expected: Syntax error(word: " + self.sentence[int(self.wordNumber)] + ")")
            return -1
    
        
    #<adjectives> (noun | pronoun)
    def object(self):
        self.Object = []
        #Subject is Adjective
        while self.isAdjective(self.sentence[int(self.wordNumber)], False):
            if not self.isAdjective(self.sentence[int(self.wordNumber)], True):
                print("Adj Expected: Syntax error(word: " + self.sentence[int(self.wordNumber)] + ")")
                return -1
    
            
        #Subject is Noun
        if not self.isNoun(self.sentence[int(self.wordNumber)]) and not self.isPronoun(self.sentence[int(self.wordNumber)]):
            print("Noun/pronoun Expected: Syntax error(word: " + self.sentence[int(self.wordNumber)] + ")")
            return -1       
    
    
    #HELPER Functions*********************************
    def isNoun(self, i):             
        with open('nouns.txt', 'r', encoding = 'UTF-8') as f1:
            for line in f1:
                if i.upper() == line.strip().upper():
                    #print("\ni: " + i +"\nLine: " + line)
                    self.POSPattern.append(Noun("Noun", None,None,None,i)) 
                    self.linkTerminal()
                    self.wordNumber = self.wordNumber + 1
                    self.boundsCheck()
                    return True
        return False
    
    
    def isAdjective(self, i, bools):   
        with open('adjectives.txt', 'r', encoding = 'UTF-8') as f1:
            for line in f1:
                if i.upper() == line.strip().upper():
                    #print("\ni: " + i +"\nLine: " + line)
                    if bools is True:
                        self.POSPattern.append(Adjective("Adjective", i))
                        self.linkTerminal()
                        self.wordNumber = self.wordNumber + 1
                        self.boundsCheck()
                    return True
        return False
    
    
    def isVerb(self, i):
        with open('verbs.txt', 'r', encoding = 'UTF-8') as f1:
            for line in f1:
                if i.upper() == line.strip().upper():
                    #print("\ni: " + i +"\nLine: " + line)
                    #verbType, tense, singPlur, person,regIrreg, word
                    self.POSPattern.append(Verb("Action-Verb",None,None,None,None,i))
                    self.linkTerminal()
                    self.wordNumber = self.wordNumber + 1
                    self.boundsCheck()
                    return True
        return False
    
    
    def isHelpingVerb(self, i, bools):
        with open('helpingVerbs.txt', 'r', encoding = 'UTF-8') as f1:
            for line in f1:
                if i.upper() == line.strip().upper():
                    #print("\ni: " + i +"\nLine: " + line)
                    if bools is True:
                        self.POSPattern.append(Verb("Helping-Verb",None,None,None,None,i))
                        self.linkTerminal()
                        self.wordNumber = self.wordNumber + 1
                        self.boundsCheck()
                    return True
        return False
    
    
    def isPronoun(self, i):             
        with open('Pronouns.txt', 'r', encoding = 'UTF-8') as f1:
            for line in f1:
                if i.upper() == line.strip().upper():
                    #print("\ni: " + i +"\nLine: " + line)
                    self.POSPattern.append(Pronoun("Pronoun", i))
                    self.linkTerminal()
                    self.wordNumber = self.wordNumber + 1
                    self.boundsCheck() 
                    return True
        return False
    
    
    def isAdverb(self, i):             
        with open('adverbs.txt', 'r', encoding = 'UTF-8') as f1:
            for line in f1:
                if i.upper() == line.strip().upper():
                    #print("\ni: " + i +"\nLine: " + line)
                    self.POSPattern.append(Adverb("Adverb", i)) 
                    self.linkTerminal()
                    self.wordNumber = self.wordNumber + 1
                    self.boundsCheck()
                    return True
        return False

    
#Main*****************************
if __name__ == '__main__':
    g = Grammar()
    g.main()
    
    
    