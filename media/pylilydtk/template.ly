% LilyPond template
\version "2.12.0"
% \header {
% title = "pyLilyDTK Generated Score"
% composer = "Mark Freeman"
% }
\include "english.ly"
verse= \lyricmode {
}
staffTimpani = \new RhythmicStaff {
\time TIME_SIGNATURE
\set Staff.midiInstrument = "timpani"
\repeat volta 1
{
RHYTHM
}
}
\score {
<<
\staffTimpani
>>
}
                        
\paper {
ragged-last-bottom = false
}
                                                            
                                                               
