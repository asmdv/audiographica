import abjad
notes = ["C0", "C#0/Db0", "D0", "D#0/Eb0","E0", "F0", "F#0/Gb0", "G0", "G#0/Ab0", "A0", "A#0/Bb0", "B0", "C1", "C#1/Db1", "D1", "D#1/Eb1", "E1", "F1", "F#1/Gb1", "G1", "G#1/Ab1", "A1", "A#1/Bb1", "B1", "C2", "C#2/Db2", "D2", "D#2/Eb2", "E2", "F2", "F#2/Gb2", "G2", "G#2/Ab2", "A2", "A#2/Bb2", "B2", "C3", "C#3/Db3", "D3", "D#3/Eb3", "E3", "F3", "F#3/Gb3", "G3", "G#3/Ab3", "A3", "A#3/Bb3", "B3", "C4", "C#4/Db4", "D4", "D#4/Eb4", "E4", "F4", "F#4/Gb4", "G4", "G#4/Ab4", "A4", "A#4/Bb4", "B4", "C5", "C#5/Db5", "D5", "D#5/Eb5", "E5", "F5","F#5/Gb5", "G5", "G#5/Ab5", "A5", "A#5/Bb5", "B5", "C6", "C#6/Db6", "D6", "D#6/Eb6", "E6", "F6", "F#6/Gb6", "G6", "G#6/Ab6", "A6", "A#6/Bb6", "B6", "C7", "C#7/Db7", "D7", "D#7/Eb7", "E7", "F7", "F#7/Gb7", "G7", "G#7/Ab7", "A7", "A#7/Bb7", "B7", "C8", "C#8/Db8", "D8", "D#8/Eb8", "E8", "F8", "F#8/Gb8", "G8", "G#8/Ab8", "A8", "A#8/Bb8", "B8"]

def get_note(str):
    note=""
    octave={"0":",,,","1":",,","2":",","3":"","4":"'","5":"''","6":"'''","7":"''''","8":"'''''"}
    note_octave=octave[str[-1]]
    note+=str[0].lower()
    if(len(str)>2):
        note+="f"
    note+=note_octave
    return note

def divide_notes(arr):

    left = " "
    right = " "
    for i in arr:
        if int(i[-1])>4:
            right+=get_note(i)
            right+=" "
        elif int(i[-1])<4:
            left+=get_note(i)   
            left+=" "
        else:
            if i[0].lower() in ['d','e','f','g','a','b']:
                left+=get_note(i)
                left+=" "
            else:
                right+=get_note(i)
                right+=" "   
    return [left,right]



def print_sheet_music(left_hand_notes, right_hand_notes):
    rh_voice = abjad.Voice(name="RH_Voice")
    rh_staff = abjad.Staff([rh_voice], name="RH_Staff")
    lh_voice = abjad.Voice(name="LH_Voice")
    lh_staff = abjad.Staff([lh_voice],name="LH_Staff")

    piano_staff = abjad.StaffGroup(lilypond_type="PianoStaff", name="Piano_Staff")
    piano_staff.extend([rh_staff, lh_staff])
    score = abjad.Score([piano_staff], name="Score")
    rh = right_hand_notes
    lh = left_hand_notes

    rh_voice.extend(rh)
    lh_voice.extend(lh)


    clef = abjad.Clef("bass")
    note = abjad.select(lh_voice).note(0)
    abjad.attach(clef, note)

    note = abjad.select(rh_voice).note(0)
    abjad.override(note).Hairpin.to_barline = False
    abjad.show(score)


#example
left = divide_notes(notes)[0]
right = divide_notes(notes)[1]
print_sheet_music(left,right)