from random import randint, seed
seed()
TürAuto=randint(1,3)
TürKandidat=int(input('Hallo Kandidat, bitte wähle eine der drei Türen aus: '))
TürZiege=1+2+3-TürAuto-TürKandidat
print("*** es öffnet sich Tür", TürZiege,"***")
print('(...)')
print('***goat noise***')
print('Du hast nun die Möglichkeit deine Entscheidung zu ändern. Möchtest Du zu der anderen Tür wechseln?')
TürKandidatNeu=int(input('Wähle eine der beiden Türen aus: '))
if TürKandidatNeu==TürAuto:
    print('Okay, wir öffnen Tür', TürKandidatNeu)
    print('(...)')
    print('Herzlichen Glückwunsch, Du hast gewonnen!')
else:
    print('(...)')
    print('***goat noise***')
    print('Oh je, das war wohl nichts... vielleicht klappt es ja beim nächsten Mal :)')