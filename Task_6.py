start = 'Hey Jude,'
end = 'to make it better.'
t = '\n'
song = {1: "don't make it bad,", 2: "Take a sad song and make it better.", 3: "Remember", 4: "to let her into your heart,",\
        5: "Then you", 6: "can start", 7: "don't be afraid", 8: "You were made to go out and get her.", 9: "The minute", 10: "you let her under your skin,",\
        11: "begin", 12: "don't let me down,", 13: "You have found her, now go and get her."}

print('', start, song.get(1), t, song.get(2), t, song.get(3), song.get(4), t, song.get(5), song.get(6), end, t, t,\
      start, song.get(7), t, song.get(8), t, song.get(9), song.get(10), t, song.get(5), song.get(11), end, \
      t, t, start, song.get(12), t, song.get(13), t, song.get(3), song.get(4), t, song.get(5), song.get(6), end, \
      t, t, start, song.get(1), t, song.get(2), t, song.get(3), song.get(10), t, \
      song.get(5), song.get(12), end)