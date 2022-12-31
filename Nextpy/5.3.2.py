class MusicNotes:


    def __init__(self):
        self.notes = [55,61.74,65.41 ,73.42 ,82.41 ,87.31 ,98 ,110 ,123.48 ,130.82 ,146.84
,164.82 ,174.62 ,196 ,220 ,246.96 ,261.64 ,293.68 ,329.64 ,349.24 ,392 ,440 ,493.92,523.28
,587.36 ,659.28,698.48,784,880,987.84,1046.56,1174.72,1318.56,1396.96,1568]
        self.current_note = -1
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_note < len(self.notes):
            self.current_note += 1
            curr_note = self.notes[self.current_note]
            return curr_note
        else:
            raise StopIteration

if __name__ == "__main__":
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)

